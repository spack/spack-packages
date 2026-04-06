# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Xrootd(CMakePackage):
    """The XROOTD project aims at giving high performance, scalable fault
    tolerant access to data repositories of many kinds."""

    homepage = "https://xrootd.web.cern.ch"
    urls = [
        "https://xrootd.web.cern.ch/download/v5.7.0/xrootd-5.7.0.tar.gz",
        "https://github.com/xrootd/xrootd/releases/download/v5.7.0/xrootd-5.7.0.tar.gz",
    ]
    list_url = "https://xrootd.org/dload.html"
    git = "https://github.com/xrootd/xrootd.git"

    maintainers("gartung", "greenc-FNAL", "marcmengel", "vitodb", "wdconinc")

    license("LGPL-3.0-only")

    version("5.9.1", sha256="39946509a50e790ab3fcc77ba0f4c9b66abef221262756aa8bb2494f00a0e321")
    version("5.8.4", sha256="d8716bf764a7e8103aab83fbf4906ea2cc157646b1a633d99f91edbf204ff632")
    version("5.7.3", sha256="3a90fda99a53cb6005ebecf7d6125ce382cedb0a27fb453e44a2c13bade0a90f")
    version("5.7.1", sha256="c28c9dc0a2f5d0134e803981be8b1e8b1c9a6ec13b49f5fa3040889b439f4041")
    version("5.7.0", sha256="214599bba98bc69875b82ac74f2d4b9ac8a554a1024119d8a9802b3d8b9986f8")
    version("5.6.9", sha256="44196167fbcf030d113e3749dfdecab934c43ec15e38e77481e29aac191ca3a8")
    version("5.6.8", sha256="19268fd9f0307d936da3598a5eb8471328e059c58f60d91d1ce7305ca0d57528")
    version("5.6.7", sha256="4089ce3a69fcf6566d320ef1f4a73a1d6332e6835b7566e17548569bdea78a8d")
    version("5.6.6", sha256="b265a75be750472561df9ff321dd0b2102bd64ca19451d312799f501edc597ba")
    version("5.6.5", sha256="600874e7c5cdb11d20d6bd6c549b04a3c5beb230d755829726cd15fab99073b1")
    version("5.6.4", sha256="52f041ab2eaa4bf7c6087a7246c3d5f90fbab0b0622b57c018b65f60bf677fad")
    version("5.6.3", sha256="72000835497f6337c3c6a13c6d39a51fa6a5f3a1ccd34214f2d92f7d47cc6b6c")
    version("5.6.2", sha256="7d7c262714268b92dbe370a9ae72275cc07f0cdbed400afd9989c366fed04c00")
    version("5.6.1", sha256="9afc48ab0fb3ba69611b1edc1b682a185d49b45caf197323eecd1146d705370c")
    version("5.6.0", sha256="cda0d32d29f94220be9b6627a80386eb33fac2dcc25c8104569eaa4ea3563009")
    version("5.5.5", sha256="0710caae527082e73d3bf8f9d1dffe95808afd3fcaaaa15ab0b937b8b226bc1f")
    version("5.5.4", sha256="41a8557ea2d118b1950282b17abea9230b252aa5ee1a5959173e2534b7d611d3")
    version("5.5.3", sha256="703829c2460204bd3c7ba8eaa23911c3c9a310f6d436211ba0af487ef7f6a980")
    version("5.5.2", sha256="ec4e0490b8ee6a3254a4ea4449342aa364bc95b78dc9a8669151be30353863c6")
    version("5.5.1", sha256="3556d5afcae20ed9a12c89229d515492f6c6f94f829a3d537f5880fcd2fa77e4")

    variant("davix", default=True, description="Build with Davix")
    variant(
        "ec",
        default=True,
        description="Build with erasure coding component support",
        when="@5.7.0:",
    )
    variant("http", default=True, description="Build with HTTP support")
    variant("krb5", default=False, description="Build with KRB5 support")
    variant("python", default=False, description="Build pyxroot Python extension")
    variant("readline", default=True, description="Use readline")

    variant(
        "cxxstd",
        default="14",
        values=("11", "14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building",
        when="@:5.6",
    )

    variant(
        "cxxstd",
        default="17",
        values=("11", "14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building",
        when="@5.7:",
    )

    variant("scitokens-cpp", default=False, description="Enable support for SciTokens")

    variant("client_only", default=False, description="Build and install client only")

    # Before 5.7, the C++ standard was not honored.
    # See https://github.com/xrootd/xrootd/pull/1929
    # and https://github.com/xrootd/xrootd/commit/9ef3a2a00b52105883613d2adb6d46a8409b2249
    # Related: C++>14 causes compilation errors with ~client_only.
    # See https://github.com/xrootd/xrootd/pull/1933.
    conflicts("cxxstd=17", when="@5.0:5.5.2")
    conflicts("cxxstd=20", when="@5.0:5.5.2")
    conflicts("cxxstd=17", when="@5:5.6 ~client_only")
    conflicts("cxxstd=20", when="@5:5.6 ~client_only")
    conflicts("^scitokens-cpp", when="@:5.5.2 +client_only")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("bzip2")
    depends_on("cmake@2.6:", type="build", when="@3.1.0:")
    depends_on("cmake@3.16:", type="build", when="@5.6:")
    conflicts("^cmake@:3.0", when="@5.0.0")
    conflicts("^cmake@:3.15.99", when="@5.5.4:5.5")
    depends_on("davix", when="+davix")
    depends_on("isa-l", when="+ec")
    depends_on("pkgconfig", type="build", when="+davix")
    depends_on("libxml2", when="+http")
    depends_on("uuid", when="@4.11.0:")
    depends_on("openssl")
    depends_on("python", when="+python")
    depends_on("py-setuptools", type="build", when="@:5.5 +python")
    depends_on("py-pip", type="build", when="@5.6: +python")
    depends_on("readline", when="+readline")
    depends_on("xz")
    depends_on("zlib-api")
    depends_on("curl")
    depends_on("krb5", when="+krb5")
    depends_on("json-c")
    depends_on("scitokens-cpp", when="+scitokens-cpp")
    depends_on("libxcrypt", type="link")

    extends("python", when="+python")

    # https://github.com/xrootd/xrootd/pull/1805
    patch(
        "https://github.com/xrootd/xrootd/commit/c267103e3093d9fc1370d56eed7481dbc10eba7d.patch?full_index=1",
        sha256="2655e2d609d80bf9c9ab58557f4f6940408a1af9c686e7aa214ac0348c89c8fa",
        when="@5.5.1",
    )
    # https://github.com/xrootd/xrootd/pull/1930
    patch(
        "https://github.com/xrootd/xrootd/commit/984efbc72bdad86b43923569f4dfa707b7a287a2.patch?full_index=1",
        sha256="13a4a3373268b137f8cea8d6e082db421d17175cef36bb53a2b939f697290f0e",
        when="@5.5.3",
    )
    # https://github.com/xrootd/xrootd/pull/2013
    patch(
        "https://patch-diff.githubusercontent.com/raw/xrootd/xrootd/pull/2013.patch?full_index=1",
        sha256="3596f45234c421abb00d0d0539033207596587f00b2d35897da8ba3302811bba",
        when="@5.5.0:5.5.5",
    )

    # do not use systemd
    patch("no-systemd-pre-5.5.2.patch", when="@:5.5.1")
    patch("no-systemd-5.5.2.patch", when="@5.5.2:")

    @when("@5.2.0:5 +client_only")
    def patch(self):
        """Allow CMAKE_CXX_STANDARD to be set in cache"""
        # See https://github.com/xrootd/xrootd/pull/1929
        filter_file(
            r"^(\s+(?i:set)\s*\(\s*CMAKE_CXX_STANDARD\s+\d+)(\s*\).*)$",
            r'\1 CACHE STRING "C++ Standard"\2',
            "cmake/XRootDOSDefs.cmake",
        )

    def cmake_args(self):
        spec = self.spec
        define = self.define
        define_from_variant = self.define_from_variant
        options = []
        if spec.satisfies("+client_only") or spec.satisfies("@6:"):
            options += [
                define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
                define("CMAKE_CXX_STANDARD_REQUIRED", True),
            ]

        options += [
            define_from_variant("ENABLE_HTTP", "http"),
            define_from_variant("ENABLE_XRDCLHTTP", "davix"),
            define_from_variant("ENABLE_PYTHON", "python"),
            define_from_variant("ENABLE_READLINE", "readline"),
            define_from_variant("ENABLE_KRB5", "krb5"),
            define_from_variant("ENABLE_SCITOKENS", "scitokens-cpp"),
            define_from_variant("ENABLE_XRDEC", "ec"),
            define_from_variant("XRDCL_ONLY", "client_only"),
            define("ENABLE_CEPH", False),
            define("ENABLE_CRYPTO", True),
            define("ENABLE_FUSE", False),
            define("ENABLE_MACAROONS", False),
            define("ENABLE_VOMS", False),
            define("FORCE_ENABLED", True),
            define("USE_SYSTEM_ISAL", True),
        ]
        # see https://github.com/spack/spack/pull/11581
        if "+python" in self.spec:
            options.append(define("XRD_PYTHON_REQ_VERSION", spec["python"].version.up_to(2)))

        if "+scitokens-cpp" in self.spec:
            options.append("-DSCITOKENS_CPP_DIR=%s" % spec["scitokens-cpp"].prefix)

        return options
