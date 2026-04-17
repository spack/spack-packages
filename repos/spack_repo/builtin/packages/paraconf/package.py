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

    license("MIT", when="@1.0.2:")
    license("BSD-3-Clause", when="@:1.0.1")

    maintainers("jbigot")

    version("develop", branch="main", no_cache=True)
    version("1.0.4", sha256="aa27493f7a256fe13a72d0ce85a2e6118a34dba67d96c0c74bd4fe68a82bdfba")
    version("1.0.3", sha256="462c487b1c9681ad0fd04cde611a9b9d969c3ab2504e2573c5ca88d1b7afa203")
    version("1.0.2", sha256="063c7e180c91f06543c4e05de39380882c05d1bd64881177b3b11ee831018a6f")
    version(
        "1.0.1",
        sha256="93884d40c1b195ad71c64f4b5301040b8b6ea4a0cae8b21e89232290d781b1eb",
        deprecated=True,
    )
    version(
        "1.0.0",
        sha256="9336492c292088a7d97192f2b1fa306e11f6f32373ac75f29b9af7eecd5c0c11",
        deprecated=True,
    )
    version(
        "0.4.16",
        sha256="d896cb5bbf1c6b311f6bed44263548c799265e1f22d50475aecbddc80b0db982",
        deprecated=True,
    )
    version(
        "0.4.15",
        sha256="914befa7a8d6fbf2de3466e434a9ea20363900af5519859663a24c7a51bd26a6",
        deprecated=True,
    )
    version(
        "0.4.14",
        sha256="8a07bdf972ce137932b0d5e08036cf90db23b69f7eaabf52eb7d495d1da01d99",
        deprecated=True,
    )
    version(
        "0.4.13",
        sha256="28da96ba45bcb826a387488f283baa0c88bc0b00fa74f4c110d444c0b9a8030c",
        deprecated=True,
    )
    version(
        "0.4.12",
        sha256="bbbaf462ed23e9a64a4d521ee469ab723fcd86a6dda9a9d9b4dddfd1a58eef93",
        deprecated=True,
    )
    version(
        "0.4.11",
        sha256="35f4ba41eaf675ff16ad4f0722a9e2050ee63b073c7e3e67eb74439978599499",
        deprecated=True,
    )
    version(
        "0.4.10",
        sha256="0a0028354b131436e70af06c9e029f738ed771088e53633b2b5d1c8ee1276e83",
        deprecated=True,
    )
    version(
        "0.4.9",
        sha256="e99a01584e07e4d09b026fcd9a39500fbdbc3074a2598a4bc89f400825094c5a",
        deprecated=True,
    )

    variant("example", default=False, description="Build example")
    variant("fortran", default=True, description="Enable Fortran support")
    variant("tests", default=False, description="Build tests")
    variant("shared", default=True, description="Build shared libraries rather than static ones")

    depends_on("c", type="build")
    depends_on("cxx", type="build", when="@1.0.3 +example")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.5:", type=("build"))
    depends_on("cmake@3.10:", type=("build"), when="@1.0.1:")
    depends_on("cmake@3.22:", type=("build"), when="@1.0.2:")
    depends_on("pkgconfig", type=("build", "link"))
    depends_on("libyaml@0.1.7:", type=("link", "run"))
    depends_on("libyaml@0.2.2:", type=("link", "run"), when="@1.0.2:")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:1.0.2"):
            return "paraconf"
        else:
            return ""

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("PARACONF_BUILD_EXAMPLE", "example"),
            self.define_from_variant("PARACONF_BUILD_FORTRAN", "fortran"),
            self.define_from_variant("PARACONF_BUILD_TESTING", "tests"),
        ]
