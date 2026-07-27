# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class Mysql(CMakePackage):
    """MySQL is an open source relational database management system."""

    homepage = "https://www.mysql.com/"
    url = "https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.15.tar.gz"

    version("8.0.35", sha256="917c5ed38704e99211185ce4be24e33a8c19c91241ed73af4181a6f38d1574c2")

    variant("client_only", default=False, description="Build and install client only.")
    variant(
        "cxxstd",
        default="17",
        values=("17",),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    # Server code has a macro 'byte', which conflicts with C++17's
    # std::byte.
    conflicts("cxxstd=17", when="~client_only")

    provides("mysql-client")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # https://dev.mysql.com/doc/refman/8.0/en/source-installation.html
    # https://dev.mysql.com/doc/refman/8.0/en/source-configuration-options.html

    # See CMAKE_MINIMUM_REQUIRED in CMakeLists.txt
    depends_on("cmake@3.8.0:", type="build", when="platform=win32")
    depends_on("cmake@3.9.2:", type="build", when="platform=darwin")
    depends_on("cmake@3.4.0:", type="build", when="platform=solaris")
    depends_on("cmake@2.8.12:", type="build")

    depends_on("gmake@3.75:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("doxygen", type="build")

    # Each version of MySQL requires a specific version of boost
    # See BOOST_PACKAGE_NAME in cmake/boost.cmake
    # 8.0.35
    depends_on("boost@1.77.0 cxxstd=17", type="build", when="@8.0.35 cxxstd=17")

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants)

    depends_on("openssl@3:")
    requires("cxxstd=17")

    depends_on("zstd")

    depends_on("patchelf", type="build")
    depends_on("curl")
    depends_on("zlib-api")
    depends_on("libevent")
    depends_on("lz4")

    depends_on("rpcsvc-proto")
    depends_on("ncurses")
    depends_on("libtirpc", when="platform=linux")
    depends_on("libedit", type=("build", "run"))
    depends_on("bison@2.1:", type="build")
    depends_on("m4", type="build", when="@develop platform=solaris")

    @property
    def command(self):
        return Executable(self.prefix.bin.mysql_config)

    @property
    def libs(self):
        return find_libraries("libmysqlclient", root=self.prefix, recursive=True)

    def url_for_version(self, version):
        url = "https://dev.mysql.com/get/Downloads/MySQL-{0}/mysql-{1}.tar.gz"
        return url.format(version.up_to(2), version)

    def cmake_args(self):
        spec = self.spec
        return [
            self.define("REPRODUCIBLE_BUILD", True),
            self.define("WITH_CURL", spec["curl"].prefix),
            self.define("WITH_EDITLINE", "system"),
            self.define("WITH_LIBEVENT", "system"),
            self.define("WITH_LZ4", "system"),
            self.define("WITH_SSL", spec["openssl"].prefix),
            self.define("WITH_ZLIB", "system"),
            self.define_from_variant("WITHOUT_SERVER", "client_only"),
            self.define("WITH_BOOST", spec["boost"].prefix),
            self.define("LOCAL_BOOST_DIR", spec["boost"].prefix),
            self.define("WITH_ZSTD", "system"),
        ]

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        cxxstd = self.spec.variants["cxxstd"].value
        flag = getattr(self.compiler, "cxx{0}_flag".format(cxxstd))
        if flag:
            env.append_flags("CXXFLAGS", flag)
        if cxxstd != "98":
            if int(cxxstd) > 11:
                env.append_flags("CXXFLAGS", "-Wno-deprecated-declarations")
            if int(cxxstd) > 14:
                env.append_flags("CXXFLAGS", "-Wno-error=register")

    @run_before("install")
    def fixup_mysqlconfig(self):
        if not self.spec.satisfies("platform=windows"):
            # mysql uses spack libz but exports -lzlib to its dependencies. Fix that:
            with working_dir(self.build_directory):
                for config in ("scripts/mysql_config", "scripts/mysqlclient.pc"):
                    if os.path.exists(config):
                        filter_file(" -lzlib ", " -lz ", config)
