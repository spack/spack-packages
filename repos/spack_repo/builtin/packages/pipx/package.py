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

    version("1.16.6", sha256="1a2ace67be16262a3bc8d1d6eedc5d6b63119b2b9e4eadc1b280d8e9c25fd722")
    version("1.15.0", sha256="193aab4983b787903e389d623e6347f697026c0d7a2ba0b4fbd5189bed22f19d")
    version("1.14.1", sha256="d11023138ac223d79e6d711ec738772c896d00366c46515a4948c3ede3389a24")
    version("1.13.0", sha256="d754c19d070893aab5d1ddb3d622ef57ec082b79f53c2664183165dbd2868c0e")
    version("1.12.0", sha256="a25ae54944c116b7dc53440aab71975f29f4f9fe4bc478cf9ddb123bed3e00f5")
    version("1.11.2", sha256="f6e445c7bfceee9566c4dfc78e4d91b9b97e511681cdd61da5bd4cc181b20997")
    version("1.10.1", sha256="3c05159c1d861a9b5ef182dcb15a60acb07b3b4c16162099ec1c84a8011a48a8")
    version("1.9.0", sha256="b7a82e09ea61fadcdbdea1f9bb49a22aa8a327d1986c97e06123a42961319c4c")
    version("1.8.0", sha256="61a653ef2046de67c3201306b9d07428e93c80e6bebdcbbcb8177ecf3328b403")
    version("1.7.1", sha256="762de134e16a462be92645166d225ecef446afaef534917f5f70008d63584360")
    version("1.6.0", sha256="840610e00103e3d49ae24b6b51804b60988851a5dd65468adb71e5a97e2699b2")
    version("1.5.0", sha256="2371af2b772954cdb5c1dbfa0170219e3d2c09d9ff9b18e975f65562eeb7ab0a")
    version("1.4.3", sha256="d214512bccc601b575de096ee84fde8797323717a20752c48f7a55cc1bf062fe")
    version("1.3.3", sha256="6d5474e71e78c28d83570443e5418c56599aa8319a950ccf5984c5cb0a35f0a7")
    version("1.2.1", sha256="698777c05a97cca81df4dc6a71d9ca4ece2184c6f91dc7a0e4802ac51d86d32a")
    version("1.2.0", sha256="d1908041d24d525cafebeb177efb686133d719499cb55c54f596c95add579286")

    # pipx >= 1.12 will use uv by default, if it finds it, so it makes sense to enable
    # it as the default backend. If the user does not want to use the uv backend, they
    # can specify pip, and pipx will use pip instead.
    variant(
        "backend",
        default="uv",
        description="Support pip or uv backend for installing packages",
        values=("pip", "uv"),
        when="@1.12:",
    )

    depends_on("python@3.10:", when="@1.11.2:", type=("build", "run"))
    depends_on("python@3.9:", when="@1.8:", type=("build", "run"))
    depends_on("python@3.8:", when="@1.3:1.7", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-argcomplete@1.9.4:", type=("build", "run"))

    depends_on("py-colorama@0.4.4:", when="platform=windows", type=("build", "run"))

    depends_on("py-docutils@0.21:", when="@1.15.1:", type="build")

    depends_on("py-filelock@3.16:", when="@1.15.1:", type="run")

    depends_on("py-hatch-vcs@0.4:", when="@1.3.2:", type="build")

    depends_on("py-hatchling@1.27:", when="@1.9:", type="build")
    depends_on("py-hatchling@1.18:", when="@1.3.2:", type="build")
    depends_on("py-hatchling@0.15:", when="@:1.3.1", type="build")

    depends_on("py-importlib-metadata@3.3:", when="^python@:3.7", type=("build", "run"))

    depends_on("py-packaging@20:", type=("build", "run"))

    # When using uv backend, py-pip is needed for building, else it is needed for building and
    # running
    depends_on("py-pip", when="backend=uv", type="build")
    depends_on("py-pip", when="backend=pip", type=("build", "run"))
    depends_on("py-pip", when="@:1.11", type=("build", "run"))

    depends_on("py-platformdirs@2.1:", when="@1.3:", type=("build", "run"))

    depends_on("py-tomli@2:", when="@1.3: ^python@:3.10", type=("build", "run"))

    # Avoid broken py-userpath 1.9.0
    depends_on("py-userpath@1.6.0:1.8.0,1.9.1:", type=("build", "run"))

    depends_on("py-uv@0.9.17:", when="@1.15.1: backend=uv", type="run")
    depends_on("py-uv@0.4:", when="@1.12: backend=uv", type="run")

    def setup_run_environment(self, env):
        if self.spec.satisfies("@1.12:"):
            backend = self.spec.variants["backend"].value

            env.set("PIPX_DEFAULT_BACKEND", backend)

            if backend == "uv":
                # Ensure Spack-installed uv is used
                env.set("PIPX_UV_BINARY", self.spec["py-uv"].prefix.bin.uv)
