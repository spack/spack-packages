# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import re

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RocmSmiLib(CMakePackage):
    """It is a C library for Linux that provides a user space interface
    for applications to monitor and control GPU applications."""

    homepage = "https://github.com/ROCm/rocm_smi_lib"
    git = "https://github.com/ROCm/rocm_smi_lib.git"
    url = "https://github.com/ROCm/rocm_smi_lib/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath")
    libraries = ["librocm_smi64"]

    version("7.1.1", sha256="f47550aeeb2827a3ae857c35e16f5a9042de70d911abab80bebe4840c9ecd4fd")
    version("7.1.0", sha256="eab6c7a85deb992b5cf511cdf7d0a6f8a93e46a0bfb6cf66c73d95c26dc4ce5e")
    version("7.0.2", sha256="cdd7951fb46b79f6791340da21fc47dc3e719f82795f2e1f5546bb7d35db954c")
    version("7.0.0", sha256="c41c5e697d53201108608916c6e495514b0695c0fbbac8d524820f7ae2af3fdb")
    version("6.4.3", sha256="74fde0f8cd9362f7073db22ffb98c72f1f7bdb42b6e7a63ae4e0a06607644d4a")
    version("6.4.2", sha256="466f6351c1d94c043195c6b5addd70d21eb1e678d5637b9849dc6b5d0e858cb5")
    version("6.4.1", sha256="c82c8c9de89537b903d82711c531b4b1c6d104098b5370d049527d1f250944b7")
    version("6.4.0", sha256="0c462520b4fa0cf9b49515b207b0ead32a5f96ddba487c5d4fa07a403690c05a")
    version("6.3.3", sha256="679dfd0cbd213d27660e546584ab013afea286eff95928d748d168503305c9c4")
    version("6.3.2", sha256="29a9190143dfcbafeac93d8064b00c9320dbca57a3344adb009ec17d9b09d036")
    version("6.3.1", sha256="0f45e4823e361a1c6ac560eabf6000c3b59e08bcd96e87150149149e861c6a63")
    version("6.3.0", sha256="573cfb759f8c7700fdcb0c28d045aed0f2d950692bb66a10bd589b89b8f48d0f")
    version("6.2.4", sha256="eb8986dd571f5862c2db693398c0dbec28e2754f764f6bd3cfb21be7699e4452")
    version("6.2.1", sha256="28543d099fa44b4b79644533644aba4b67fa48d477628dd5802c3b50cc78583a")
    version("6.2.0", sha256="95010dfc9de9c608b9ce159107585ff4adce82a52a38daab2a37870aca2428bf")
    version("6.1.2", sha256="01f46fb1cb8c7a16a4c4db61871ee710ed37c0f8bd3a2dbe3415d3de2dffb4ef")
    version("6.1.1", sha256="7fd2234b05eb6b9397c5508bb37e81fb16ce2cadc2c97298b2124b46c3687880")
    version("6.1.0", sha256="d1a1b372489b27cb7eb8c91d74a71370ad9668dd5aaf89c0267172534e417e41")
    version("6.0.2", sha256="61e755d710ff38425df3d262d1ad4c510d52d3c64e3fe15140c2575eba316949")
    version("6.0.0", sha256="0053b42402fd007e5ca9b3186c70f2c6f1b3026558f328722adadc2838c51309")
    version("5.7.1", sha256="4d79cb0482b2f801cc7824172743e3dd2b44b9f6784d1ca2e5067f2fbb4ef803")
    version("5.7.0", sha256="a399db3d9fc113ce2dd1ab5608a1cf9129ec4b6a2a79ab7922b1d9f43c454640")

    variant("shared", default=True, description="Build shared or static library")
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3:", type="build")
    depends_on("python@3:", type=("build", "run"))

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
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
    ]:
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    for ver in [
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
    ]:
        depends_on("llvm-amdgpu", when=f"@{ver}+asan")

    depends_on("pkgconfig", when="@6.4:")
    depends_on("libdrm", when="@6.4:")

    patch(
        "https://github.com/ROCm/rocm_smi_lib/commit/11f12b86517d0e9868f4d16d74d4e8504c3ba7da.patch?full_index=1",
        sha256="62be7262f6e1e71bf82a03f500a424a536638f04e913d0f4b477f60e8e1190fd",
        when="@6.1.1:6",
    )

    patch(
        "https://github.com/ROCm/rocm_smi_lib/commit/ce405476cabf66a884a351cb2e3253bd5c29e06b.patch?full_index=1",
        sha256="54094b5dbd05b79341e38e95f785dcbb0ba4a5aef4bad19e075ea77470164138",
        when="@6.4.0",
    )
    patch("0001-add-libdrm-include-dir.patch", when="@6.4")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define("BUILD_TESTS", self.run_tests),
        ]
        if self.spec.satisfies("@5.7.0:"):
            args.append(self.define_from_variant("ADDRESS_SANITIZER", "asan"))
        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@6.1: +asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            return "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        return None

    @run_after("build")
    @on_package_attributes(run_tests=True)
    def check_build(self):
        exe = which(join_path(self.build_directory, "tests", "rocm_smi_test", "rsmitst"))
        exe()
