# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import itertools

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Rocwmma(CMakePackage):
    """AMD's C++ library for accelerating mixed precision matrix multiplication
    and accumulation (MFMA) operations leveraging specialized GPU matrix cores.
    rocWMMA provides a C++ API to facilitate breaking down matrix multiply-accumulate
    problems into fragments and using them in block-wise operations that are
    distributed in parallel across GPU wavefronts. The API is a header library
    of GPU device code meaning that matrix core acceleration may be compiled directly
    into your kernel device code. This can benefit from compiler optimization in the
    generation of kernel assembly, and does not incur additional overhead costs of
    linking to external runtime libraries or having to launch separate kernels."""

    homepage = "https://github.com/ROCm/rocWMMA"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/rocWMMA/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="5a3c22ba75bf8473dc4a008fbff365d0666fc5a49c54e742f7ed4444a2b2d431")
    version("7.1.0", sha256="96bed5cd6f2d3334cfbd4a9e6dab132cc2ec60150409712661dc69e774427707")
    version("7.0.2", sha256="359604712e6802fbb66ebddf4c337916c5a851bd4302d8c3ab5c31f0d8b7ec7e")
    version("7.0.0", sha256="14e0cec245c7c4827dc5421c9878fab5e1734112933351f8bef3a0d1ed68f6b6")
    version("6.4.3", sha256="34797c458603688748a046b611e14693221843de96740ed3ba5c606d41ab0cdf")
    version("6.4.2", sha256="63bbac42242ea3bf5f5dd160739a0bd8a2d01c0f6456c187a2e6c29fecdcc93a")
    version("6.4.1", sha256="888e9794adff06ca1be811d80018e761b9a9cf84cb88dec9e51bc3a6db7a359a")
    version("6.4.0", sha256="d95d53f70b4a2adc565bf4490515626cb7109f1d2e8a9978626610d3f178cf42")
    version("6.3.3", sha256="5bfd2909cc9b4601bb83ddd79da6cfa4075afa6d6e9396d9bbe1df844163fbd2")
    version("6.3.2", sha256="f9dc5e837ac30efe4600775fb309e46ed8ef112a673435663d2ef7fdf28f8f12")
    version("6.3.1", sha256="9afd06c58b405dd86535ea1ca479fd6f9d717fa8665710bb64fc8027a26e6ac7")
    version("6.3.0", sha256="8dcd06599083dc3a67958a1b6f7c29c1880758eb6ff579143e0fb162985b0612")
    version("6.2.4", sha256="eaa2f313a1bfe455d9641df44d7b890ea7334b58a643c75f0b7f108cae5f777c")
    version("6.2.1", sha256="f05fcb3612827502d2a15b30f0e46228625027145013652b8f591ad403fa9ddc")
    version("6.2.0", sha256="08c5d19f0417ee9ba0e37055152b22f64ed0eab1d9ab9a7d13d46bf8d3b255dc")
    version("6.1.2", sha256="7f6171bea5c8b7cdaf5c64dbfb76eecf606f2d34e8409153a74b56027c5e92a7")
    version("6.1.1", sha256="6e0c15c78feb8fb475ed028ed9b0337feeb45bfce1e206fe5f236a55e33f6135")
    version("6.1.0", sha256="ca29f33cfe6894909159ad68d786eacd469febab33883886a202f13ae061f691")
    version("6.0.2", sha256="61c6cc095b4ac555f4be4b55f6a7e3194c8c54bffc57bfeb0c02191119ac5dc8")
    version("6.0.0", sha256="f9e97e7c6c552d43ef8c7348e4402bead2cd978d0f81a9657d6a0f6c83a6139b")
    version("5.7.1", sha256="a998a1385e6ad7062707ddb9ff82bef727ca48c39a10b4d861667024e3ffd2a3")
    version("5.7.0", sha256="a8f1b090e9e504a149a924c80cfb6aca817359b43833a6512ba32e178245526f")

    amdgpu_targets = ROCmPackage.amdgpu_targets
    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )
    variant(
        "build_type",
        default="Release",
        values=("Release", "Debug", "RelWithDebInfo"),
        description="CMake build type",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.16:", type="build")

    depends_on("googletest@1.10.0:", type="test")

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
        depends_on("rocm-cmake@%s:" % ver, type="build", when="@" + ver)
        depends_on("llvm-amdgpu@" + ver, type="build", when="@" + ver)
        depends_on("hip@" + ver, when="@" + ver)
        depends_on("rocblas@" + ver, type="build", when="@" + ver)
        depends_on("rocm-smi-lib@" + ver, when="@" + ver)

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
        depends_on("rocm-openmp-extras@" + ver, type="build", when="@" + ver)

    for tgt in itertools.chain(["auto"], amdgpu_targets):
        depends_on("rocblas amdgpu_target={0}".format(tgt), when="amdgpu_target={0}".format(tgt))

    patch("0001-add-rocm-smi-lib-path-for-building-tests.patch", when="@:6.3")
    patch("0002-use-find-package-rocm-smi.patch", when="@6.4")
    patch("0004-add-rocm-smi-link-dir.patch", when="@7.2")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/rocwmma"
        else:
            return "."

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CXX", self.spec["hip"].hipcc)

    def cmake_args(self):
        args = [
            self.define("ROCWMMA_BUILD_TESTS", "ON"),
            self.define("ROCWMMA_BUILD_VALIDATION_TESTS", "ON"),
            self.define("ROCWMMA_BUILD_BENCHMARK_TESTS", "ON"),
            self.define("ROCWMMA_BUILD_SAMPLES", "ON"),
            self.define("ROCWMMA_BUILD_DOCS", "OFF"),
            self.define("ROCWMMA_BUILD_ASSEMBLY", "OFF"),
            self.define("ROCM_SMI_DIR", self.spec["rocm-smi-lib"].prefix),
        ]
        args.extend(["-DOpenMP_CXX_FLAGS=-fopenmp=libomp", "-DOpenMP_CXX_LIB_NAMES=libomp"])
        if self.spec.satisfies("@:7.1"):
            args.append(
                f"-DOpenMP_libomp_LIBRARY={self.spec['rocm-openmp-extras'].prefix}/lib/libomp.so"
            )
        else:
            args.append(f"-DOpenMP_libomp_LIBRARY={self.spec['llvm-amdgpu'].prefix}/lib/libomp.so")
        tgt = self.spec.variants["amdgpu_target"]
        if "auto" not in tgt:
            if self.spec.satisfies("@7.1:"):
                args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
            else:
                args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))
        return args
