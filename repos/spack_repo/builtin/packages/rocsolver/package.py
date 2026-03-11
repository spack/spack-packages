# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import itertools
import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Rocsolver(CMakePackage):
    """rocSOLVER is a work-in-progress implementation of a
    subset of LAPACK functionality on the ROCm platform."""

    homepage = "https://github.com/ROCm/rocSOLVER"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("cgmb", "srekolam", "renjithravindrankannath", "haampie", "afzpatel")
    libraries = ["librocsolver"]
    license("BSD-2-Clause")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/rocSOLVER/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )
    variant(
        "optimal",
        default=True,
        description="This option improves performance at the cost of increased binary "
        "size and compile time by adding specialized kernels "
        "for small matrix sizes",
    )
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    conflicts("+asan", when="os=rhel9")
    conflicts("+asan", when="os=centos7")
    conflicts("+asan", when="os=centos8")

    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="15a29454239dbbac34219d484247f5721d4af08ca1b1f3973ebcbd7895184ae6")
    version("7.1.0", sha256="643100d6e225eb0d6d26cdc485df79ddd6e7938519e4d74d6f3e8c26d22c5cf2")
    version("7.0.2", sha256="675c7cdc0e582f93d81d2dcd953ea567f040cbeb300ccd2db61cad4a07ca1d5b")
    version("7.0.0", sha256="635bbf625d81e11afc70f6c0e23212ed13ea20ea50cf995d3dfa0e4636c19558")
    version("6.4.3", sha256="6c2c6019eaf49abb30fc54f09b3d755ebcfbbd30d9b71052aa13bb0cbc26d2bb")
    version("6.4.2", sha256="fe78538ead2ce9a95abbec74bc2c85408d5224f80b4816520e2d55d6b0188935")
    version("6.4.1", sha256="d27d3e0a59fbe1fb82172f545e38857643bb86fa1cd69ba51e9e292440a785c6")
    version("6.4.0", sha256="48930842ac441a6a5d7e25d6c5c6ac6b5fe26549a1add49a102b374e02f5b60e")
    version("6.3.3", sha256="0e8bb906513555d349b6a20cb17976402f5ea6702668efcdda595a2e2d516b46")
    version("6.3.2", sha256="834f532c54bdf0e4900e73ffb0544068071976175559c8bf3c50d7a3b7230a3a")
    version("6.3.1", sha256="ffa70c4dedeb20a33cf79d4ae3e95ade2ae5202f819459b19a0ebf62c380bba0")
    version("6.3.0", sha256="48861f7b86379f2b825c0496d1d9318c6e29426d083b361c10f685b0ddd66274")
    version("6.2.4", sha256="022863df6a9d51bd216e56dd4dc7d437584e48304cfdbc9c5751be1abfd7c73f")
    version("6.2.1", sha256="e1c19cd25f7119c116d1c63e2384e9c47a4ff7ae14bb42dfcef766a4d3a011d5")
    version("6.2.0", sha256="74cb799dcddfcbd6ee05398003416dbccd3d06d7f4b23e4324baac3f15440162")
    version("6.1.2", sha256="8cb45b6a4ed819b8e952c0bfdd8bf7dd941478ac656bea42a6d6751f459e66ea")
    version("6.1.1", sha256="3bbba30fa7f187676caf858f66c2345e4dcc81b9546eca4a726c0b159dad22bd")
    version("6.1.0", sha256="f1d7a4edf14ed0b2e2f74aa5cbc9db0c3b0dd31e50bbada1586cb353a28fe015")
    version("6.0.2", sha256="781d5df2886ab0d5087a215a33ac390dd27653b2a9b4a620c7d51b0ae56f63d2")
    version("6.0.0", sha256="5fcaba96f3efafc2ecc3f4ec104095d96545c16e1b9f95410bd571cb0fc643ae")
    version("5.7.1", sha256="83e0c137b8690dbeb2e85d9e25415d96bd06979f09f2b10b2aff8e4c9f833fa4")
    version("5.7.0", sha256="bb16d360f14b34fe6e8a6b8ddc6e631672a5ffccbdcb25f0ce319edddd7f9682")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.8:", type="build")
    depends_on("fmt@7:8.0.1", type="test")
    depends_on("fortran", type="build")

    depends_on("googletest@1.10.0:", type="test")
    depends_on("netlib-lapack@3.7.1:", type="test")

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
        "7.2.0",
    ]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rocblas@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")
        depends_on(f"rocsparse@{ver}", when=f"@{ver}")

    for tgt in itertools.chain(["auto"], amdgpu_targets):
        depends_on(f"rocblas amdgpu_target={tgt}", when=f"amdgpu_target={tgt}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/rocsolver"
        else:
            return "."

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            return "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        return None

    def cmake_args(self):
        args = [
            self.define("BUILD_CLIENTS_SAMPLES", "OFF"),
            self.define("BUILD_CLIENTS_TESTS", self.run_tests),
            self.define("BUILD_CLIENTS_BENCHMARKS", "OFF"),
            self.define_from_variant("OPTIMAL", "optimal"),
            self.define("ROCSOLVER_EMBED_FMT", "ON"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]

        tgt = self.spec.variants["amdgpu_target"]
        if "auto" not in tgt:
            if self.spec.satisfies("@7.1:"):
                args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
            else:
                args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))

        if self.spec.satisfies("^cmake@3.21.0:3.21.2"):
            args.append(self.define("__skip_rocmclang", "ON"))

        if self.spec.satisfies("@:6.3.1"):
            args.append(self.define("BUILD_FILE_REORG_BACKWARD_COMPATIBILITY", True))

        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CXX", self.spec["hip"].hipcc)
        if self.spec.satisfies("+asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    @run_after("build")
    @on_package_attributes(run_tests=True)
    def check_build(self):
        exe = Executable(join_path(self.build_directory, "clients", "staging", "rocsolver-test"))
        exe("--gtest_filter=checkin*-*known_bug*")
