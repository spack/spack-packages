# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mamba(CMakePackage):
    """Mamba is a fast, robust, and cross-platform package manager (Miniconda alternative).
    Micromamba is an (almost) statically linked version of mamba.
    """

    homepage = "https://mamba.readthedocs.io/"
    url = "https://github.com/mamba-org/mamba/archive/refs/tags/2.3.0.tar.gz"

    maintainers("charmoniumQ", "Chrismarsh")

    license("BSD-3-Clause")

    version("2.3.0", sha256="671432a2b64719baba54c9efda3662d321a1cc9ff3eba49047b83ffda9acf661")

    # micromamba is mamba but statically linked
    # however there is some nuance in that statement
    # https://github.com/mamba-org/mamba/issues/3295
    # and it needs work in this package
    # variant("micromamba",
    #         default="False",
    #         description="A statically linked version of mamba")

    patch("fix-threads.patch")

    # missing <cassert> header
    # https://github.com/mamba-org/mamba/pull/4021
    patch(
        "https://github.com/mamba-org/mamba/commit/efeac7bac7aae3e3256ea60c6dea07e3a0101344.patch?full_index=1",
        sha256="530a04ca8b476db5670c7aef6295684feeda4e031c6e100181179e29f3f7b921",
        when="@2.3.0",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.16:", type="build")

    depends_on("pkgconfig", type="build")

    # deps taken from
    # https://github.com/mamba-org/mamba/blob/main/libmamba/CMakeLists.txt#L423

    depends_on("libsolv@0.7.34:+conda")

    depends_on("curl@7.66.0: libs=shared")
    depends_on("libarchive crypto=mbedtls xar=libxml2")
    depends_on("openssl")
    depends_on("yaml-cpp")
    depends_on("libreproc +cxx +shared")
    depends_on("tl-expected")

    # spdlog will determine the exact version of fmt used,
    depends_on("spdlog")
    depends_on("fmt@11:")

    depends_on("nlohmann-json")
    depends_on("cpp-termcolor")
    depends_on("cli11@2.2:")

    depends_on("zstd build_system=cmake")
    depends_on("simdjson +shared")

    # 1.4.2 made the static build the old "full_static" build and it needs some work.
    # Only shared or full static exist now https://github.com/mamba-org/mamba/pull/2342
    # this is all broken, keep to work on as needed

    # with when("+micromamba"):
    #     # When linkage is static, BUILD_STATIC=ON
    #     # and then
    #     # https://github.com/mamba-org/mamba/blob/micromamba-1.0.0/libmamba/CMakeLists.txt#L523
    #     # calls libmamba_create_target(libmamba-static STATIC SHARED libmamba)
    #     # where the third argument, SHARED, is the deps_linkage
    #     # as defined here,
    #     # https://github.com/mamba-org/mamba/blob/micromamba-1.0.0/libmamba/CMakeLists.txt#L256
    #     # which would use dynamic linkage here,
    #     # https://github.com/mamba-org/mamba/blob/micromamba-1.0.0/libmamba/CMakeLists.txt#L420
    #     # See linkage=dynamic for what that entails.
    #     depends_on("libsolv+conda", type="link")
    #     depends_on("curl libs=shared", type="link")
    #     depends_on("libarchive crypto=mbedtls xar=libxml2", type="link")
    #     depends_on("openssl", type="link")
    #     depends_on("yaml-cpp", type="link")
    #     depends_on("libreproc+cxx", type="link")
    #     depends_on("tl-expected", type="link")
    #     depends_on("fmt@9.1.0", type="link")
    #     depends_on("spdlog@1.11.0", type="link")
    #     depends_on("nlohmann-json", type="link")
    #     depends_on("cpp-termcolor", type="link")
    #     depends_on("cli11@2.2:", type="link")

    def cmake_args(self):
        args = [
            self.define("BUILD_LIBMAMBA", True),
            self.define("BUILD_MAMBA", True),
            self.define("BUILD_SHARED", True),
            # self.define("BUILD_MICROMAMBA", True), #implies  BUILD_STATIC
            # self.define("BUILD_STATIC", True )
            # self.define("MICROMAMBA_LINKAGE", "STATIC"),
        ]

        return args

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):
        Executable("mamba")("--version")
