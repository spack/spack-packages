# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Mlx(CMakePackage, CudaPackage):
    """MLX is an array framework for machine learning on Apple silicon.

    MLX is designed by machine learning researchers for machine learning
    researchers. The framework is intended to be user-friendly, but still
    efficient to train and deploy models. It provides familiar NumPy-like
    APIs and supports composable function transformations for automatic
    differentiation, automatic vectorization, and computation graph optimization.
    """

    homepage = "https://ml-explore.github.io/mlx/"
    git = "https://github.com/ml-explore/mlx.git"

    maintainers("rbberger")

    license("MIT")

    version("main", branch="main")
    version("0.31.2", commit="68cf2fddd8de5edd8ab3d926391772b2e2cedad8", tag="v0.31.2")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    variant("shared", default=False, description="Build shared libraries")
    variant("tests", default=False, description="Build tests")
    variant("examples", default=False, description="Build examples")
    variant("benchmarks", default=False, description="Build benchmarks")
    variant("python", default=False, description="Build Python bindings")
    variant("metal", default=True, description="Build Metal backend (macOS GPU)")
    variant("cpu", default=True, description="Build CPU backend")
    variant("cuda", default=False, description="Build CUDA backend (Linux)")
    variant("gguf", default=True, description="Include support for GGUF format")
    variant("safetensors", default=True, description="Include support for safetensors format")
    variant("metal_jit", default=False, description="Use JIT compilation for Metal kernels")

    depends_on("metal-cpp", type="build", when="+metal")
    depends_on("metal-cpp@26.4", type="build", when="@0.31.2 +metal")

    # Dependencies for Python bindings
    depends_on("python@3.8:", type=("build", "run"), when="+python")
    depends_on("py-numpy", type=("build", "run"), when="+python")
    depends_on("py-pybind11", type="build", when="+python")

    # CUDA dependencies
    depends_on("cuda@11:", type=("build", "run"), when="+cuda")

    # Platform conflicts
    conflicts("~metal~cpu~cuda", msg="At least one backend (metal, cpu, or cuda) must be enabled")
    conflicts("+metal", when="platform=linux", msg="Metal backend is only available on macOS")
    conflicts("+metal", when="platform=windows", msg="Metal backend is only available on macOS")
    conflicts("+cuda", when="platform=darwin", msg="CUDA backend is not available on macOS")

    def cmake_args(self):
        spec = self.spec

        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("MLX_BUILD_TESTS", "tests"),
            self.define_from_variant("MLX_BUILD_EXAMPLES", "examples"),
            self.define_from_variant("MLX_BUILD_BENCHMARKS", "benchmarks"),
            self.define_from_variant("MLX_BUILD_PYTHON_BINDINGS", "python"),
            self.define_from_variant("MLX_BUILD_METAL", "metal"),
            self.define_from_variant("MLX_BUILD_CPU", "cpu"),
            self.define_from_variant("MLX_BUILD_CUDA", "cuda"),
            self.define_from_variant("MLX_BUILD_GGUF", "gguf"),
            self.define_from_variant("MLX_BUILD_SAFETENSORS", "safetensors"),
            self.define_from_variant("MLX_METAL_JIT", "metal_jit"),
        ]

        if spec.satisfies("%c,cxx=apple-clang"):
            args.extend(
                [
                    self.define("CMAKE_C_COMPILER", self.compiler.cc),
                    self.define("CMAKE_CXX_COMPILER", self.compiler.cxx),
                ]
            )

        if spec.satisfies("+metal"):
            args.append(f"-DFETCHCONTENT_SOURCE_DIR_METAL_CPP={spec['metal-cpp'].prefix.include}")

        if spec.satisfies("+python"):
            args.append(self.define("MLX_BUILD_PYTHON_STUBS", True))

        if spec.satisfies("+cuda"):
            cuda_arch = spec.variants["cuda_arch"].value
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", ";".join(cuda_arch)))

        return args
