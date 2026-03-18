# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re
import shutil
import stat
from typing import Dict, Iterable, List, Mapping, Optional, Tuple

from spack.package import (
    BuilderWithDefaults,
    ClassProperty,
    HeaderList,
    LibraryList,
    PackageBase,
    Prefix,
    Spec,
    build_system,
    classproperty,
    depends_on,
    determine_number_of_jobs,
    execute_install_time_tests,
    extends,
    filter_file,
    find,
    get_effective_jobs,
    has_shebang,
    join_path,
    path_contains_subdirectory,
    register_builder,
    run_after,
    symlink,
    test_part,
    tty,
    when,
    working_dir,
)


def _flatten_dict(dictionary: Mapping[str, object]) -> Iterable[str]:
    """Iterable that yields KEY=VALUE paths through a dictionary.

    Args:
        dictionary: Possibly nested dictionary of arbitrary keys and values.

    Yields:
        A single path through the dictionary.
    """
    for key, item in dictionary.items():
        if isinstance(item, dict):
            # Recursive case
            for value in _flatten_dict(item):
                yield f"{key}={value}"
        else:
            # Base case
            yield f"{key}={item}"


class PythonExtension(PackageBase):
    @property
    def import_modules(self) -> Iterable[str]:
        """Names of modules that the Python package provides.

        These are used to test whether or not the installation succeeded.
        These names generally come from running:

        .. code-block:: python

           >> import setuptools
           >> setuptools.find_packages()

        in the source tarball directory. If the module names are incorrectly
        detected, this property can be overridden by the package.

        Returns:
            List of strings of module names.
        """
        modules = []
        pkg = self.spec["python"].package

        # Packages may be installed in platform-specific or platform-independent
        # site-packages directories
        for directory in {pkg.platlib, pkg.purelib}:
            root = os.path.join(self.prefix, directory)

            # Some Python libraries are packages: collections of modules
            # distributed in directories containing __init__.py files
            for path in find(root, "__init__.py", recursive=True):
                modules.append(
                    path.replace(root + os.sep, "", 1)
                    .replace(os.sep + "__init__.py", "")
                    .replace("/", ".")
                )

            # Some Python libraries are modules: individual *.py files
            # found in the site-packages directory
            for path in find(root, "*.py", recursive=False):
                modules.append(
                    path.replace(root + os.sep, "", 1).replace(".py", "").replace("/", ".")
                )

        modules = [
            mod
            for mod in modules
            if re.match("[a-zA-Z0-9._]+$", mod) and not any(map(mod.startswith, self.skip_modules))
        ]

        tty.debug("Detected the following modules: {0}".format(modules))

        return modules

    @property
    def skip_modules(self) -> Iterable[str]:
        """Names of modules that should be skipped when running tests.

        These are a subset of import_modules. If a module has submodules,
        they are skipped as well (meaning a.b is skipped if a is contained).

        Returns:
            List of strings of module names.
        """
        return []

    @property
    def bindir(self) -> str:
        """Path to Python package's bindir, bin on unix like OS's Scripts on Windows"""
        windows = self.spec.satisfies("platform=windows")
        return join_path(self.spec.prefix, "Scripts" if windows else "bin")

    def add_files_to_view(self, view, merge_map, skip_if_exists=True):
        # Patch up shebangs if the package extends Python and we put a Python interpreter in the
        # view.
        if not self.extendee_spec:
            return super().add_files_to_view(view, merge_map, skip_if_exists)

        python, *_ = self.spec.dependencies("python-venv") or self.spec.dependencies("python")

        if python.external:
            return super().add_files_to_view(view, merge_map, skip_if_exists)

        # We only patch shebangs in the bin directory.
        copied_files: Dict[Tuple[int, int], str] = {}  # File identifier -> source
        delayed_links: List[Tuple[str, str]] = []  # List of symlinks from merge map
        bin_dir = self.spec.prefix.bin

        for src, dst in merge_map.items():
            if skip_if_exists and os.path.lexists(dst):
                continue

            if not path_contains_subdirectory(src, bin_dir):
                view.link(src, dst)
                continue

            s = os.lstat(src)

            # Symlink is delayed because we may need to re-target if its target is copied in view
            if stat.S_ISLNK(s.st_mode):
                delayed_links.append((src, dst))
                continue

            # If it's executable and has a shebang, copy and patch it.
            if (s.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)) and has_shebang(src):
                copied_files[(s.st_dev, s.st_ino)] = dst
                shutil.copy2(src, dst)
                filter_file(
                    python.prefix, os.path.abspath(view.get_projection_for_spec(self.spec)), dst
                )
            else:
                view.link(src, dst)

        # Finally re-target the symlinks that point to copied files.
        for src, dst in delayed_links:
            try:
                s = os.stat(src)
                target = copied_files[(s.st_dev, s.st_ino)]
            except (OSError, KeyError):
                target = None
            if target:
                symlink(os.path.relpath(target, os.path.dirname(dst)), dst)
            else:
                view.link(src, dst, spec=self.spec)

    def test_imports(self) -> None:
        """Attempts to import modules of the installed package."""

        # Make sure we are importing the installed modules,
        # not the ones in the source directory
        python = self.module.python
        for module in self.import_modules:
            with test_part(
                self,
                f"test_imports_{module}",
                purpose=f"checking import of {module}",
                work_dir="spack-test",
            ):
                python("-c", f"import {module}")


def _homepage(cls: "PythonPackage") -> Optional[str]:
    """Get the homepage from PyPI if available."""
    if cls.pypi:
        name = cls.pypi.split("/")[0]
        return f"https://pypi.org/project/{name}/"
    return None


def _url(cls: "PythonPackage") -> Optional[str]:
    if cls.pypi:
        return f"https://files.pythonhosted.org/packages/source/{cls.pypi[0]}/{cls.pypi}"
    return None


def _list_url(cls: "PythonPackage") -> Optional[str]:
    if cls.pypi:
        name = cls.pypi.split("/")[0]
        return f"https://pypi.org/simple/{name}/"
    return None


class PythonPackage(PythonExtension):
    """Specialized class for packages that are built using pip."""

    #: Package name, version, and extension on PyPI
    pypi: Optional[str] = None

    # To be used in UI queries that require to know which
    # build-system class we are using
    build_system_class = "PythonPackage"
    #: Legacy buildsystem attribute used to deserialize and install old specs
    default_buildsystem = "python_pip"

    #: Callback names for install-time test
    install_time_test_callbacks = ["test_imports"]

    build_system("python_pip")

    with when("build_system=python_pip"):
        extends("python")
        depends_on("py-pip", type="build")
        # FIXME: technically wheel is only needed when building from source, not when
        # installing a downloaded wheel, but I don't want to add wheel as a dep to every
        # package manually
        depends_on("py-wheel", type="build")

    homepage: ClassProperty[Optional[str]] = classproperty(_homepage)
    url: ClassProperty[Optional[str]] = classproperty(_url)
    list_url: ClassProperty[Optional[str]] = classproperty(_list_url)

    @property
    def python_spec(self) -> Spec:
        """Get python-venv if it exists or python otherwise."""
        python, *_ = self.spec.dependencies("python-venv") or self.spec.dependencies("python")
        return python

    @property
    def headers(self) -> HeaderList:
        return HeaderList([])

    @property
    def libs(self) -> LibraryList:
        return LibraryList([])


@register_builder("python_pip")
class PythonPipBuilder(BuilderWithDefaults):
    phases = ("install",)

    #: Names associated with package methods in the old build-system format
    package_methods = ("test_imports",)

    #: Same as package_methods, but the signature is different
    package_long_methods = ("install_options", "global_options", "config_settings")

    #: Names associated with package attributes in the old build-system format
    package_attributes = ("archive_files", "build_directory", "install_time_test_callbacks")

    #: Callback names for install-time test
    install_time_test_callbacks = ["test_imports"]

    @staticmethod
    def std_args(cls) -> List[str]:
        return [
            # Verbose
            "-vvv",
            # Disable prompting for input
            "--no-input",
            # Disable the cache
            "--no-cache-dir",
            # Don't check to see if pip is up-to-date
            "--disable-pip-version-check",
            # Install packages
            "install",
            # Don't install package dependencies
            "--no-deps",
            # Overwrite existing packages
            "--ignore-installed",
            # Use env vars like PYTHONPATH
            "--no-build-isolation",
            # Don't warn that prefix.bin is not in PATH
            "--no-warn-script-location",
            # Ignore the PyPI package index
            "--no-index",
        ]

    @property
    def build_directory(self) -> str:
        """The root directory of the Python package.

        This is usually the directory containing one of the following files:

        * ``pyproject.toml``
        * ``setup.cfg``
        * ``setup.py``
        """
        return self.pkg.stage.source_path

    def config_settings(self, spec: Spec, prefix: Prefix) -> Dict[str, object]:
        """Configuration settings to be passed to the PEP 517 build backend.

        Requires pip 22.1 or newer for keys that appear only a single time,
        or pip 23.1 or newer if the same key appears multiple times.

        Args:
            spec: Build spec.
            prefix: Installation prefix.

        Returns:
            Possibly nested dictionary of KEY, VALUE settings.
        """
        return {}

    def install_options(self, spec: Spec, prefix: Prefix) -> Iterable[str]:
        """Extra arguments to be supplied to the setup.py install command.

        Requires pip 23.0 or older.

        Args:
            spec: Build spec.
            prefix: Installation prefix.

        Returns:
            List of options.
        """
        return []

    def global_options(self, spec: Spec, prefix: Prefix) -> Iterable[str]:
        """Extra global options to be supplied to the setup.py call before the install
        or bdist_wheel command.

        Deprecated in pip 23.1.

        Args:
            spec: Build spec.
            prefix: Installation prefix.

        Returns:
            List of options.
        """
        return []

    def install(self, pkg: PythonPackage, spec: Spec, prefix: Prefix) -> None:
        """Install everything from build directory."""
        pip = spec["python"].command
        pip.add_default_arg("-m", "pip")

        args = PythonPipBuilder.std_args(pkg) + [f"--prefix={prefix}"]
        config_settings = self.config_settings(spec, prefix)

        # Pass -jN for compile-args if supported and needed
        if spec.satisfies("%py-pip@22.1: %py-meson-python@0.11:"):
            # get_effective_jobs returns None when a jobserver is active, then we don't pass -j.
            jobs = get_effective_jobs(
                jobs=determine_number_of_jobs(parallel=pkg.parallel), supports_jobserver=True
            )
            if jobs is not None:
                config_settings["compile-args"] = f"-j{jobs}"

        for setting in _flatten_dict(config_settings):
            args.append(f"--config-settings={setting}")
        for option in self.install_options(spec, prefix):
            args.append(f"--install-option={option}")
        for option in self.global_options(spec, prefix):
            args.append(f"--global-option={option}")

        if pkg.stage.archive_file and pkg.stage.archive_file.endswith(".whl"):
            args.append(pkg.stage.archive_file)
        else:
            args.append(".")

        with working_dir(self.build_directory):
            pip(*args)

    run_after("install")(execute_install_time_tests)
