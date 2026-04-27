# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Hipsparse(CMakePackage, CudaPackage, ROCmPackage):
    """hipSPARSE is a SPARSE marshalling library, with
    multiple supported backends"""

    homepage = "https://github.com/ROCm/hipSPARSE"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("cgmb", "srekolam", "renjithravindrankannath", "haampie", "afzpatel")
    libraries = ["libhipsparse"]
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/hipsparse/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="bc5140deec3b1c93c13796a8a6d2cb7e50aa87fd89f60f87c8d801d66f2fd156")
    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="b001834d8e65c3878d1a69d08803d5b6ce4fe623e78099fe51cb146d0ffa10e7")
    version("7.1.0", sha256="1d399d16a388279f71c8de19e6ccfde35a3dedc5ba49858bca7a377aa08198c0")
    version("7.0.2", sha256="8f2d187ef9a44e58538a7bf3298b245e740066c74e431da01c38ed35fad649fc")
    version("7.0.0", sha256="09102f4a74cfcffb8371428f70a592a004b72f4f08135d35738b34c4d5a5edba")
    version("6.4.3", sha256="0ac06136778a25e7d38c69d831d169b85ad370d0ae1cd45deb5f63a43797244e")
    version("6.4.2", sha256="e6ed9a0dab093f428418c7914f3d2e1612cafc280cd0ee27ab4df8c93284a5ed")
    version("6.4.1", sha256="cae547776076066c0ee19a7f98516ac2e9a0cf3bb3b0809d7a4e474f9ee4cb90")
    version("6.4.0", sha256="aaab3e9a905f5c5f470634ed7a0929ef93e28d2c5fe4f6f89338b39a937f1825")
    version("6.3.3", sha256="61c26eb93e857c942a03ea4350a403e20191be465041e542ad7da00058e89ead")
    version("6.3.2", sha256="9fbc3468632fdc828d7bae386c2737eb371d78811f53da7348b417fb00d62808")
    version("6.3.1", sha256="d64bc48e0aa5ec2f48853272a9c554b37ec98cb0724135e45f21b1340df7bccb")
    version("6.3.0", sha256="550fd5a480490e631507e8c34b2b0cf9cbc2ad2a5bf84e8ea0a8fad96eecb25a")
    version("6.2.4", sha256="0ecc0ff1eeb99e9a9ac419e49e9be9ec4cd23a117d819710114ee2f35aefe88b")
    version("6.2.1", sha256="5a3241c857f705b1e5c64b3f5163575726e64a8d19f3957f7326622fda277710")
    version("6.2.0", sha256="e51b9871d764763519c14be2ec52c1e1ae3959b439afb4be6518b9f9a6f0ebaf")
    version("6.1.2", sha256="dd44f9b6000b3b0ac0fa238037a80f79d6745a689d4a6755f2d595643be1ef6d")
    version("6.1.1", sha256="307cff012f0465942dd6666cb00ae60c35941699677c4b26b08e4832bc499059")
    version("6.1.0", sha256="1d9277a11f71474ea4a9f8419a7a2c37170a86969584e5724e385ec74241e565")
    version("6.0.2", sha256="40c1d2493f87c686d9afd84a00321ad10ca0d0d80d6dcfeee8e51858dd1bd8c1")
    version("6.0.0", sha256="718a5f03b6a579c0542a60d00f5688bec53a181b429b7ee8ce3c8b6c4a78d754")
    version("5.7.1", sha256="16c3818260611226c3576d8d55ad8f51e0890d2473503edf2c9313250ae65ca7")
    version("5.7.0", sha256="729b749b5340034639873a99e6091963374f6f0456c8f36d076c96f03fe43888")

    # default to an 'auto' variant until amdgpu_targets can be given a better default than 'none'
    amdgpu_targets = ROCmPackage.amdgpu_targets
    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=disjoint_sets(("auto",), amdgpu_targets)
        .with_default("auto")
        .with_error(
            "the values 'auto' and 'none' are mutually exclusive with any of the other values"
        )
        .with_non_feature_values("auto", "none"),
        sticky=True,
    )
    variant("rocm", default=True, description="Enable ROCm support")
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")
    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")
    conflicts("~cuda ~rocm", msg="CUDA or ROCm support is required")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("hip +cuda", when="+cuda")

    depends_on("cmake@3.5:", type="build")
    depends_on("git", type="build")
    depends_on("googletest", when="@6.3:")

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
        "7.2.1",
    ]:
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")
        depends_on(f"rocsparse@{ver}", when=f"+rocm @{ver}")

    for tgt in ROCmPackage.amdgpu_targets:
        depends_on(f"rocsparse amdgpu_target={tgt}", when=f"+rocm amdgpu_target={tgt}")

    # Add c++17 to hipsparse to fix error with std::filesystem
    patch(
        "https://github.com/ROCm/hipSPARSE/commit/037b54ecc129edaaff59d3df149a3f071466ba29.patch?full_index=1",
        sha256="02f44a3bac6f9983648afeb606aa43b7329547218e0f13b9d31b685acb8b198e",
        when="@6.3",
    )

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/hipsparse"
        else:
            return "."

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            ver = "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        else:
            ver = None
        return ver

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+asan"):
            self.asan_on(env)

    def cmake_args(self):
        args = [
            self.define("BUILD_CLIENTS_SAMPLES", "OFF"),
            self.define("BUILD_CLIENTS_TESTS", "OFF"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]

        args.append(self.define_from_variant("BUILD_CUDA", "cuda"))

        # FindHIP.cmake is still used for +cuda
        if self.spec.satisfies("+cuda"):
            args.append(self.define("CMAKE_MODULE_PATH", self.spec["hip"].prefix.lib.cmake.hip))
        if self.spec.satisfies("@:6.3.1"):
            args.append(self.define("BUILD_FILE_REORG_BACKWARD_COMPATIBILITY", True))
        if self.spec.satisfies("@:6"):
            args.append(self.define("CMAKE_CXX_STANDARD", "14"))
        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
        return args
