# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from glob import glob

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Pdi(CMakePackage):
    """PDI is a library that aims to decouple high-performance simulation codes
    from Input/Output concerns. It offers a declarative application programming
    interface that enables codes to expose the buffers in which they store data
    and to notify PDI of significant steps of the simulation. It supports a
    plugin system to make existing libraries such as HDF5, SIONlib or FTI
    available to codes, potentially mixed in a single execution."""

    homepage = "https://pdi.dev"
    git = "https://github.com/pdidev/pdi.git"
    url = "https://github.com/pdidev/pdi/archive/refs/tags/1.8.0.tar.gz"

    license("BSD-3-Clause")

    maintainers("jbigot")

    # only the latest version is supported upstream
    # we also offer the last 2 patch versions of the current minor
    # and the last patch version of the previous 2 minors
    # all the rest is marked as deprecated
    version("develop", branch="main", no_cache=True)
    version("1.11.0", sha256="a3e5ed6f890a8599d67e1666a14a6c5b1084a0cbb8a748bf40fc53df47d39410")
    version("1.10.1", sha256="f2409611310255360867e3c74d44e055f45c87071ef8881665ff30a7940e1449")
    version(
        "1.10.0",
        sha256="8bda1ed83bdb152a047a45a48f896466e7ebf5163030405c15dbfa4e2e788143",
        deprecated=True,
    )
    version("1.9.3", sha256="ab390e51e3b7298d6b09484a443dc267651aed5978c711f8804848b19ab1527e")
    version(
        "1.9.2",
        sha256="0430d5898980435e5602b67188264621a27f71969ff886efaa2e6d43a45caac4",
        deprecated=True,
    )
    version(
        "1.9.1-fixed",
        sha256="13d052a7d5d53271638382f06e9da0d58b01ed9cfdf9c4fa1e82367b9e1732e1",
        deprecated=True,
    )
    version(
        "1.9.0",
        sha256="04fee7851c4f2a156daddf7eb2c3c3b0132d80d3f0e448cdeebda0b7c4595639",
        deprecated=True,
    )
    version(
        "1.8.3",
        sha256="df7200289a2a368ec874140039b417abdfe681b57fb1b9f4c52f924952226020",
        deprecated=True,
    )
    version(
        "1.8.2",
        sha256="bb4d1654c97f7ff379067adbff339f8b4117c0cf9432f41f1a5cb20a747cac1a",
        deprecated=True,
    )
    version(
        "1.8.1",
        sha256="43f0c0b2bda5515ecf99da7be1600af2c1f669d6c73e3f309275b14940c7e35c",
        deprecated=True,
    )
    version(
        "1.8.0",
        sha256="5d353bfa64f45ee4715b88bd30330030f79f2020cd6bede0ad9b8f9beddadea9",
        deprecated=True,
    )

    variant("benchs", default=False, description="Build benchmarks")
    variant("docs", default=False, description="Build documentation")
    variant("tests", default=False, description="Build tests")
    variant("fortran", default=True, description="Enable Fortran support")
    variant("python", default=True, description="Enable Python support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.22.1:", type=("build"), when="@1.10.0:")
    depends_on("cmake@3.16.3:", type=("build"))
    depends_on("doxygen@1.9.1:", type=("build"), when="@1.10.0: +docs")
    depends_on("doxygen@1.8.17:", type=("build"), when="+docs")
    depends_on("paraconf@1: +shared", type=("link", "run"))
    depends_on("paraconf +fortran", type=("link", "run"), when="+fortran")
    depends_on("pkgconfig", type=("build"))
    depends_on("python@3.10.6:3", type=("build", "link", "run"), when="@1.10.0: +python")
    depends_on("python@3.8.2:3", type=("build", "link", "run"), when="+python")
    depends_on(
        "python@3:3.11.9", type=("build", "link", "run"), when="@:1.8.2 +python"
    )  # Needs distutils.
    extends("python", when="+python")
    depends_on("py-pybind11@2.9.1:2", type=("link"), when="@1.10.0: +python")
    depends_on("py-pybind11@2.4.3:2", type=("link"), when="+python")
    depends_on("py-numpy@1.21.5:2", type=("run"), when="@1.10.0: +python")
    depends_on("py-numpy@1.17.4:2", type=("run"), when="+python")
    depends_on(
        "py-setuptools", type=("build", "link"), when="@1.8.3: +python^python@3.12:"
    )  # Needs distutils.
    depends_on("spdlog@1.9.2:1", type=("link"), when="@1.10.0:")
    depends_on("spdlog@1.5:1", type=("link"))

    root_cmakelists_dir = "pdi"

    def patch(self):
        # Run before build so that the standard Spack sbang install hook can fix
        # up the path to the python binary the zpp scripts requires. We dont use
        # filter_shebang("vendor/zpp-*/bin/zpp.in") because the template is
        # not yet instantiated and PYTHON_EXECUTABLE is not yet large enough to
        # trigger the replacement via filter_shebang.
        zpp_in = glob("vendor/zpp-*/bin/zpp.in")[0]
        with open(zpp_in, "r+", encoding="utf-8") as f:
            content = f.read()
            f.seek(0)
            f.write(f"{sbang_shebang_line()}\n{content}")

    @staticmethod
    def version_url(version):
        return f"https://github.com/pdidev/pdi/archive/refs/tags/{version}.tar.gz"

    def url_for_version(self, version):
        return Pdi.version_url(version)

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_BENCHMARKING", "benchs"),
            self.define_from_variant("BUILD_DOCUMENTATION", "docs"),
            self.define_from_variant("BUILD_FORTRAN", "fortran"),
            self.define_from_variant("BUILD_PYTHON", "python"),
            self.define_from_variant("BUILD_TESTING", "tests"),
        ]
