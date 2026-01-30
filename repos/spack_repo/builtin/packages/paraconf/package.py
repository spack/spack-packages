# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Paraconf(CMakePackage):
    """Paraconf is a library that provides a simple query language to access a
    Yaml tree on top of libyaml."""

    homepage = "https://github.com/pdidev/paraconf"
    git = "https://github.com/pdidev/paraconf.git"
    url = "https://github.com/pdidev/paraconf/archive/1.0.3.tar.gz"

    license("MIT")

    maintainers("jbigot")

    version("develop", branch="main", no_cache=True)
    version("1.0.4", sha256="aa27493f7a256fe13a72d0ce85a2e6118a34dba67d96c0c74bd4fe68a82bdfba")
    version("1.0.3", sha256="462c487b1c9681ad0fd04cde611a9b9d969c3ab2504e2573c5ca88d1b7afa203")

    variant("example", default=False, description="Build example")
    variant("fortran", default=True, description="Enable Fortran support")
    variant("tests", default=False, description="Build tests")
    variant("shared", default=True, description="Build shared libraries rather than static ones")

    depends_on("c", type="build")
    depends_on("cxx", type="build", when="@1.0.3 +example")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.22:", type=("build"))
    depends_on("pkgconfig", type=("build"))
    depends_on("libyaml@0.2.2:", type=("link", "run"))

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("PARACONF_BUILD_EXAMPLE", "example"),
            self.define_from_variant("PARACONF_BUILD_FORTRAN", "fortran"),
            self.define_from_variant("PARACONF_BUILD_TESTING", "tests"),
        ]
