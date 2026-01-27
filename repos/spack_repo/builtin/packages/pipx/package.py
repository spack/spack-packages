# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Pipx(PythonPackage):
    """pipx is a tool to install and run Python applications in isolated environments"""

    homepage = "https://pypa.github.io/pipx/"
    pypi = "pipx/pipx-1.2.0.tar.gz"

    license("MIT")

    maintainers("ebagrenrut")

    version("1.8.0", sha256="61a653ef2046de67c3201306b9d07428e93c80e6bebdcbbcb8177ecf3328b403")
    version("1.7.1", sha256="762de134e16a462be92645166d225ecef446afaef534917f5f70008d63584360")
    version("1.6.0", sha256="840610e00103e3d49ae24b6b51804b60988851a5dd65468adb71e5a97e2699b2")
    version("1.4.3", sha256="d214512bccc601b575de096ee84fde8797323717a20752c48f7a55cc1bf062fe")
    version("1.2.0", sha256="d1908041d24d525cafebeb177efb686133d719499cb55c54f596c95add579286")

    depends_on("python@3.8:3.12", when="@1.3:1.7", type=("build", "run"))
    depends_on("python@3.9:3.13", when="@1.8:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-argcomplete@1.9.4:", type=("build", "run"))
    depends_on("py-colorama@0.4.4:", type=("build", "run"), when="platform=windows")
    depends_on("py-hatch-vcs@0.4:", when="@1.3.2:", type="build")
    depends_on("py-hatchling@1.18:", when="@1.3.2:", type="build")
    depends_on("py-hatchling@0.15.0:", type="build")
    depends_on("py-importlib-metadata@3.3.0:", type=("build", "run"), when="^python@3.7")
    depends_on("py-packaging@20.0:", type=("build", "run"))
    depends_on("py-platformdirs@2.1:", when="@1.3.0:", type=("build", "run"))
    depends_on("py-tomli@2.0:", when="@1.3.0: ^python@:3.10", type=("build", "run"))
    depends_on("py-userpath@1.6.0:1.8.0,1.9.1:", type=("build", "run"))

    # ========================================================================
    # Set up environment to make install easier for pipx-installed packages
    # ========================================================================
    def setup_dependent_package(self, module, dependent_spec):
        """Called before Pipx modules' install() method."""
        # Pipx builds can have a global `pipx` executable function
        module.pipx = Executable(join_path(self.spec.prefix.bin, "pipx"))
