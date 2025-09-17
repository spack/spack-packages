# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

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
    version("1.9.2", sha256="0430d5898980435e5602b67188264621a27f71969ff886efaa2e6d43a45caac4")
    version(
        "1.9.1-fixed", sha256="13d052a7d5d53271638382f06e9da0d58b01ed9cfdf9c4fa1e82367b9e1732e1"
    )
    version("1.8.3", sha256="df7200289a2a368ec874140039b417abdfe681b57fb1b9f4c52f924952226020")

    variant("benchs", default=False, description="Build benchmarks")
    variant("docs", default=False, description="Build documentation")
    variant("tests", default=False, description="Build tests")
    variant("fortran", default=True, description="Enable Fortran support")
    variant("python", default=True, description="Enable Python support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.16.3:", type=("build"))
    depends_on("doxygen@1.8.17:", type=("build"), when="+docs")
    depends_on("paraconf@1: +shared", type=("link", "run"))
    depends_on("paraconf +fortran", type=("link", "run"), when="+fortran")
    depends_on("pkgconfig", type=("build"))
    depends_on("python@3.8.2:3", type=("build", "link", "run"), when="+python")
    depends_on("py-pybind11@2.4.3:2", type=("link"), when="+python")
    depends_on(
        "py-setuptools", type=("build", "link"), when="+python^python@3.12:"
    )  # Needs distutils.
    depends_on("spdlog@1.5:", type=("link"))

    root_cmakelists_dir = "pdi"

    def patch(self):
        # Run before build so that the standard Spack sbang install hook can fix
        # up the path to the python binary the zpp scripts requires. We dont use
        # filter_shebang("vendor/zpp-1.0.16/bin/zpp.in") because the template is
        # not yet instantiated and PYTHON_EXECUTABLE is not yet large enough to
        # trigger the replacement via filter_shebang.
        filter_file(
            r"#!@PYTHON_EXECUTABLE@ -B",
            sbang_shebang_line() + "\n#!@PYTHON_EXECUTABLE@ -B",
            "vendor/zpp-1.0.16/bin/zpp.in",
        )

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
