# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class HsakmtRoct(CMakePackage):
    """This is a thunk python recipe to build and install Thunk Interface.
    Thunk Interface is a user-mode API interfaces used to interact
    with the ROCk driver."""

    homepage = "https://github.com/ROCm/ROCT-Thunk-Interface"
    git = "https://github.com/ROCm/ROCT-Thunk-Interface.git"
    url = "https://github.com/ROCm/ROCT-Thunk-Interface/archive/rocm-6.2.4.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath")

    version("6.2.4", sha256="5c71655e3a1b9d1404dc8cb64b9d2fadd27e67606aaa8aec0c325768d8c483c0")
    version("6.2.1", sha256="bba5dd8cce595d94d6a8e467dbd6de9e921f81e665ca8aac1e346e0ade7620f0")
    version("6.2.0", sha256="73df98ca2be8a887cb76554c23f148ef6556bdbccfac99f34111fa1f87fd7c5d")
    version("6.1.2", sha256="097a5b7eb136300667b36bd35bf55e4a283a1ed04e614cf24dddca0a65c86389")
    version("6.1.1", sha256="c586d8a04fbd9a7bc0a15e0a6a161a07f88f654402bb11694bd8aebc343c00f0")
    version("6.1.0", sha256="1085055068420821f7a7adb816692412b5fb38f89d67b9edb9995198f39e2f31")
    version("6.0.2", sha256="5354bda9382f80edad834463f2c684289841770a4f7b13f0f40bd8271cc4c71d")
    version("6.0.0", sha256="9f4e80bd0a714ce45326941b906a62298c62025eff186dc6c48282ce84c787c7")
    version("5.7.1", sha256="38bc3732886a52ca9cd477ec6fcde3ab17a0ba5dc8e2f7ac34c4de597bd00e8b")
    version("5.7.0", sha256="52293e40c4ba0c653d796e2f6109f5fb4c79f5fb82310ecbfd9a5432acf9da43")

    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build")
    depends_on("cmake@3:", type="build")
    depends_on("numactl")
    depends_on("libdrm")

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
    ]:
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", type="test", when=f"@{ver}")

    def cmake_args(self):
        args = [
            self.define("BUILD_SHARED_LIBS", False),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]
        if self.spec.satisfies("@5.7.0:"):
            args.append(self.define_from_variant("ADDRESS_SANITIZER", "asan"))
        return args

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):
        """Check if package is installed correctly"""
        test_dir = join_path("tests", "kfdtest")
        with working_dir(test_dir, create=True):
            prefixes = ";".join(
                [
                    self.spec["libdrm"].prefix,
                    self.prefix,
                    self.spec["numactl"].prefix,
                    self.spec["pkgconfig"].prefix,
                    self.spec["llvm-amdgpu"].prefix,
                    self.spec["zlib-api"].prefix,
                    self.spec["ncurses"].prefix,
                ]
            )
            hsakmt_path = ";".join([self.prefix])
            cc_options = [
                "-DCMAKE_PREFIX_PATH=" + prefixes,
                "-DLIBHSAKMT_PATH=" + hsakmt_path,
                ".",
            ]
            cmake = self.spec["cmake"].command
            cmake(*cc_options)
            make = which("make", required=True)
            make()
            os.environ["LD_LIBRARY_PATH"] = hsakmt_path
            os.environ["BIN_DIR"] = os.getcwd()
            run_kfdtest = which(join_path("scripts", "run_kfdtest.sh"), required=True)
            run_kfdtest()
            make("clean")
