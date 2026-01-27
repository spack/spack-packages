# SPDX-License-Identifier: (Sana-Proprietary)

import inspect
from typing import List, Optional

from spack.package import (
    BuilderWithDefaults,
    EnvironmentModifications,
    PackageBase,
    Prefix,
    Spec,
    build_system,
    depends_on,
    register_builder,
    when,
    working_dir,
)


class PipxPackage(PackageBase):
    """Specialized class for Python packages via pipx"""

    #: Package name, version, and extension on PyPI
    pypi: Optional[str] = None

    build_system_class = "PipxPackage"

    build_system("pipx")

    with when("build_system=pipx"):
        depends_on("pipx", type="build")
        # Though `pipx` itself has a dependency on `python`, we must explicitly include
        # `python` as a dependency to ensure that, upon installation of the pipx-built
        # package, Spack rewrites any paths to the `python` commands and appropriately
        # sets any symlinks to `python` commands
        depends_on("python")

    @property
    def homepage(cls: "PipxPackage") -> Optional[str]:
        """Get the homepage from PyPI if available."""
        if cls.pypi:
            name = cls.pypi.split("/")[0]
            return f"https://pypi.org/project/{name}/"
        return None

    @property
    def url(cls: "PipxPackage") -> Optional[str]:
        if cls.pypi:
            return f"https://files.pythonhosted.org/packages/source/{cls.pypi[0]}/{cls.pypi}"
        return None

    @property
    def list_url(cls: "PipxPackage") -> Optional[str]:
        if cls.pypi:
            name = cls.pypi.split("/")[0]
            return f"https://pypi.org/simple/{name}/"
        return None


@register_builder("pipx")
class PipxBuilder(BuilderWithDefaults):
    """The pipx builder provides the following methods that can be overridden:

    1. :py:meth:`~.PipxBuilder.setup_build_environment`
    2. :py:meth:`~.PipxBuilder.install`

    For a finer tuning you may override:

        +-----------------------------------------------+----------------------+
        | **Method**                                    | **Purpose**          |
        +===============================================+======================+
        | :py:meth:`~.PipxBuilder.build_directory`      | Specify the build    |
        |                                               | directory            |
        +-----------------------------------------------+----------------------+
        | :py:meth:`~.PipxBuilder.install_args`         | Specify arguments    |
        |                                               | to ``pipx install``  |
        +-----------------------------------------------+----------------------+
    """

    phases = ("install",)

    package_attributes = ("build_directory", "install_args")

    @property
    def build_directory(self) -> str:
        return self.pkg.stage.source_path

    @property
    def install_args(self) -> List[str]:
        """Arguments to pipx install"""
        # We default to being very verbose so that a `spack install -v` will show
        # everything that pipx and pip are doing
        return ["-vv", "--pip-args", "--no-cache-dir -v"]

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        """Set additional environment variables if desired"""
        pass

    def install(self, pkg: PipxPackage, spec: Spec, prefix: Prefix) -> None:
        """Install pkg via 'pipx install'"""
        # We must ensure pipx puts everything in the prefix so that it will all be bundled
        # into the binary package.
        pipx_env = EnvironmentModifications()
        pipx_env.set("PIPX_HOME", self.prefix)
        pipx_env.set("PIPX_BIN_DIR", self.prefix.bin)
        pipx_env.set("PIPX_MAN_DIR", self.prefix.share.man)

        with working_dir(self.build_directory):
            inspect.getmodule(self.pkg).pipx(
                "install",
                *self.install_args,
                pkg.stage.archive_file,
                extra_env=pipx_env,
            )
