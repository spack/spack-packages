# Copyright Spack Project Developers.
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems import python as pybs
from spack.package import *

import os
from contextlib import contextmanager


class PyCutlass(PythonPackage):
    """Python helpers shipped in NVIDIA CUTLASS: `cutlass_library` and `pycute`."""

    homepage = "https://github.com/NVIDIA/cutlass"
    git      = "https://github.com/NVIDIA/cutlass.git"
    url      = "https://github.com/NVIDIA/cutlass/archive/refs/tags/v3.3.0.tar.gz"

    version("main", branch="main")
    version("4.1.0", sha256="8d4675b11e9e5207e3940eaac0f46db934ada371cbb3627c9fda642d912b6230")
    version("4.0.0", sha256="44a121c5878827875856c175ebe82e955062e37cd61fcdf31ebe2e8874f2fc5c")
    version("3.9.2", sha256="4b97bd6cece9701664eec3a634a1f2f2061d85bf76d843fa5799e1a692b4db0d")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")

    # Keep the C++ CUTLASS in lockstep
    depends_on("cutlass@main",   when="@main")
    depends_on("cutlass@4.1.0",  when="@4.1.0")
    depends_on("cutlass@4.0.0",  when="@4.0.0")
    depends_on("cutlass@3.9.2",  when="@3.9.2")

    @property
    def build_directory(self):
        return "python"


class PythonPipBuilder(pybs.PythonPipBuilder):
    @contextmanager
    def _shim_setup(self, path, contents):
        """Create a temporary setup.py shim and remove it afterwards."""
        setup_py = os.path.join(path, "setup.py")
        with open(setup_py, "w") as f:
            f.write(contents)
        try:
            yield setup_py
        finally:
            try:
                os.remove(setup_py)
            except OSError:
                pass

    def _pip_install_here(self, pkg: PythonPackage, spec: Spec, prefix: Prefix, env=None):
        pip = spec["python"].command
        pip.add_default_arg("-m", "pip")

        args = type(self).std_args(pkg) + [f"--prefix={prefix}"]

        # Respect any config/global options from the base implementation
        from spack_repo.builtin.build_systems import python as pybs
        for setting in pybs._flatten_dict(self.config_settings(spec, prefix)):
            args.append(f"--config-settings={setting}")
        for option in self.install_options(spec, prefix):
            args.append(f"--install-option={option}")
        for option in self.global_options(spec, prefix):
            args.append(f"--global-option={option}")

        args.append(".")
        pip(*args, env=env)

    def install(self, pkg: PythonPackage, spec: Spec, prefix: Prefix) -> None:
        """
        Perform two pip installs in CUTLASS's `python/` dir:
          - cutlass_library   via setup_library.perform_setup()
          - pycute            via setup_pycute.perform_setup()
        """
        repo_python_dir = pkg.stage.source_path + "/python"
        env_map = os.environ.copy()

        # Install cutlass_library
        lib_shim = (
            "from setup_library import perform_setup\n"
            "if __name__ == '__main__':\n"
            "    perform_setup()\n"
        )
        with working_dir(repo_python_dir):
            with self._shim_setup(repo_python_dir, lib_shim):
                self._pip_install_here(pkg, spec, prefix, env=env_map)

        # Install pycute
        cute_shim = (
            "from setup_pycute import perform_setup\n"
            "if __name__ == '__main__':\n"
            "    perform_setup()\n"
        )
        with working_dir(repo_python_dir):
            with self._shim_setup(repo_python_dir, cute_shim):
                self._pip_install_here(pkg, spec, prefix, env=env_map)
