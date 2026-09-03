# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class PyTorch(PythonPackage, CudaPackage, ROCmPackage):
    """Tensors and Dynamic neural networks in Python with strong GPU acceleration."""

    homepage = "https://pytorch.org/"
    git = "https://github.com/pytorch/pytorch.git"
    submodules = True

    # Exact set of modules is version- and variant-specific, just attempt to import the
    # core libraries to ensure that the package was successfully installed.
    import_modules = ["torch", "torch.autograd", "torch.nn", "torch.utils"]

    license("Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT")
    maintainers("adamjstewart")

    tags = ["e4s"]

    version("main", branch="main")
    version("2.14.0", tag="v2.14.0", commit="2b3ec34829036a65cd9d1398ea72a0167dc37470")
    version("2.13.0", tag="v2.13.0", commit="cf30153c4c131c8164ee7798e5022d810682e2cb")
    version("2.12.1", tag="v2.12.1", commit="7269437d655783a26cba32aa88195b741ff496aa")
    version("2.12.0", tag="v2.12.0", commit="0d62256a2b23365f8e1604297eb23a6545102aa8")
    version("2.11.0", tag="v2.11.0", commit="70d99e998b4955e0049d13a98d77ae1b14db1f45")
    version("2.10.0", tag="v2.10.0", commit="449b1768410104d3ed79d3bcfe4ba1d65c7f22c0")

    is_darwin = sys.platform == "darwin"

    # All options are defined in CMakeLists.txt.
    variant("debug", default=False, description="Build with debugging support")
    variant("caffe2", default=False, description="Build Caffe2")
    variant("test", default=False, description="Build C++ test binaries")
    variant("cuda", default=not is_darwin, description="Use CUDA")
    variant("rocm", default=False, description="Use ROCm")
    variant("cudnn", default=not is_darwin, description="Use cuDNN", when="+cuda")
    variant("fbgemm", default=True, description="Use FBGEMM (quantized 8-bit server operators)")
    variant("kineto", default=True, description="Use Kineto profiling library", when="@:2.10")
    variant(
        "kineto", default=True, description="Use Kineto profiling library", when="@2.11: ~rocm"
    )
    variant(
        "kineto",
        default=False,
        description="Disable Kineto from 2.11 on ROCm",
        when="@2.11: +rocm",
    )
    variant("magma", default=not is_darwin, description="Use MAGMA", when="+cuda")
    variant("metal", default=is_darwin, description="Use Metal for Caffe2 iOS build")
    variant(
        "mps",
        default=is_darwin and macos_version() >= Version("12.3"),
        description="Use MPS for macOS build (requires full Xcode suite)",
        when="platform=darwin",
    )
    variant("nccl", default=True, description="Use NCCL", when="+cuda platform=linux")
    variant("nccl", default=True, description="Use NCCL", when="@:2.10 +rocm platform=linux")
    variant(
        "nccl",
        default=False,
        description="Disable NCCL from 2.11 on rocm",
        when="@2.11: +rocm platform=linux",
    )
    # Requires AVX2: https://discuss.pytorch.org/t/107518
    variant("nnpack", default=True, description="Use NNPACK", when="target=x86_64_v3:")
    variant("numa", default=True, description="Use NUMA", when="platform=linux")
    variant("numpy", default=True, description="Use NumPy")
    variant("openmp", default=True, description="Use OpenMP for parallel code")
    variant("qnnpack", default=True, description="Use QNNPACK (quantized 8-bit operators)")
    variant("valgrind", default=True, description="Use Valgrind", when="platform=linux")
    variant("xnnpack", default=True, description="Use XNNPACK")
    variant("mkldnn", default=True, description="Use MKLDNN")
    variant("distributed", default=True, description="Use distributed")
    variant("mpi", default=True, description="Use MPI for Caffe2", when="+distributed")
    variant("ucc", default=False, description="Use UCC", when="+distributed")
    variant("gloo", default=False, description="Use Gloo", when="+distributed")
    variant("tensorpipe", default=True, description="Use TensorPipe", when="+distributed")
    # Flash attention has very high memory requirements that may cause the build to fail
    # https://github.com/pytorch/pytorch/issues/111526
    # https://github.com/pytorch/pytorch/issues/124018
    _desc = "Build the flash_attention kernel for scaled dot product attention"
    variant("flash_attention", default=True, description=_desc, when="+cuda")
    variant("flash_attention", default=True, description=_desc, when="+rocm")
    variant("cusparselt", default=True, description="Use NVIDIA cuSPARSELt", when="+cuda")
    # py-torch has strict dependencies on old protobuf/py-protobuf versions that
    # cause problems with other packages that require newer versions of protobuf
    # and py-protobuf --> provide an option to use the internal/vendored protobuf.
    variant("custom-protobuf", default=False, description="Use vendored protobuf")

    conflicts("+cuda+rocm")
    conflicts("+gloo+rocm")
    conflicts("+rocm", when="@2.12", msg="Rocm doesn't support py-torch 2.12 release")
    conflicts("+rocm", when="@2.13", msg="Rocm doesn't support py-torch 2.13 release")
    conflicts("+tensorpipe", when="+rocm ^hip@:5.1", msg="TensorPipe not supported until ROCm 5.2")

    # https://github.com/pytorch/pytorch/issues/77811
    conflicts("+qnnpack", when="platform=darwin target=aarch64:")

    # https://github.com/pytorch/pytorch/issues/97397
    conflicts(
        "~tensorpipe",
        when="+distributed",
        msg="TensorPipe must be enabled with +distributed",
    )

    conflicts(
        "cuda_arch=none",
        when="+cuda",
        msg="Must specify CUDA compute capabilities of your GPU, see "
        "https://developer.nvidia.com/cuda-gpus",
    )

    # Required dependencies
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("binutils@2.36:", when="platform=linux", type="build")

    # Based on PyPI wheel availability
    with default_args(type=("build", "link", "run")):
        depends_on("python@3.10:3.15", when="@2.13:")
        depends_on("python@3.10:3.14", when="@:2.12")

    # pyproject.toml
    with default_args(type="build"):
        depends_on("py-numpy")
        depends_on("py-packaging@24.2:", when="@2.13:")
        depends_on("py-packaging")
        depends_on("py-pyyaml")
        depends_on("py-scikit-build-core@1:", when="@2.14:")
        depends_on("py-typing-extensions@4.10:")
        depends_on("py-six")

        # Historical dependencies
        depends_on("py-setuptools@77.0:81", when="@2.13")
        depends_on("py-setuptools@70.1:81", when="@:2.12")
        depends_on("cmake@3.27:", when="@:2.13")
        depends_on("ninja", when="@:2.13")
        depends_on("py-requests", when="@:2.13")

    # METADATA Requires-Dist in wheel files
    with default_args(type="run"):
        depends_on("py-filelock")
        depends_on("py-typing-extensions@4.10:")
        depends_on("py-setuptools@77.0.3:", when="@2.13:")
        depends_on("py-setuptools@:81", when="@:2.12")
        depends_on("py-sympy@1.13.3:")
        depends_on("py-networkx@2.5.1:")
        depends_on("py-jinja2")
        depends_on("py-fsspec@0.8.5:")

    # third_party
    depends_on("fp16@2020-05-14")
    depends_on("fxdiv@2020-04-17")
    depends_on("nvtx@3.5.0", when="@2.14:")
    depends_on("nvtx@3.3.0")
    # https://github.com/pytorch/pytorch/issues/60332
    # depends_on("xnnpack@2024-12-03", when="+xnnpack")
    depends_on("benchmark", when="@1.6:+test")
    depends_on("cpuinfo@2026-04-13", when="@2.13:")
    depends_on("cpuinfo@2025-11-14", when="@:2.12")
    with when("+gloo"):
        depends_on("gloo@2026-06-10", when="@2.14:")
        depends_on("gloo@2026-02-12", when="@2.13")
        depends_on("gloo@2025-12-02", when="@2.11:2.12")
        depends_on("gloo@2025-08-21", when="@:2.10")
        depends_on("gloo+cuda", when="+gloo+cuda")
        depends_on("gloo+libuv", when="platform=darwin")
    # https://github.com/pytorch/pytorch/issues/60331
    # depends_on("onnx@1.18.0")
    with when("~custom-protobuf"):
        depends_on("protobuf@21.12:", when="@2.14:")
        depends_on("protobuf@3.13.0", when="@:2.13")
        with default_args(type=("build", "run")):
            depends_on("py-protobuf@4.21.12:", when="@2.14:")
            depends_on("py-protobuf@3.13", when="@:2.13")
    depends_on("psimd@2020-05-17")
    depends_on("pthreadpool@2026-05-01", when="@2.13:")
    depends_on("pthreadpool@2023-08-29", when="@:2.12")
    with default_args(type=("build", "link", "run")):
        depends_on("py-pybind11@3.1.0:", when="@2.14:")
        depends_on("py-pybind11@3.0.4:", when="@2.13:")
        depends_on("py-pybind11@3.0.1:")
        # https://github.com/spack/spack-packages/pull/3708#issuecomment-4077800794
        depends_on("py-pybind11@:3.0.1", when="@:2.11")
    depends_on("sleef@3.8")
    depends_on("eigen")

    # Optional dependencies
    with default_args(type=("build", "link", "run")):
        # cmake/public/cuda.cmake
        depends_on("cuda@12.6:", when="@2.14:+cuda")
        depends_on("cuda@12.1:", when="@2.12:+cuda")
        depends_on("cuda@12:", when="+cuda")
    # https://github.com/pytorch/pytorch#prerequisites
    with when("+cudnn"):
        depends_on("cudnn@9:", when="@2.12:")
        depends_on("cudnn@8.5:9", when="@:2.11")
    # torch/csrc/distributed/c10d/NCCLUtils.hpp
    with when("+nccl+cuda"):
        depends_on("nccl@2.23:", when="@2.13:")
        depends_on("nccl@2.7:")
    # https://github.com/pytorch/pytorch/pull/178065
    depends_on("magma@:2.9+cuda", when="+magma+cuda")
    depends_on("magma@:2.9+rocm", when="+magma+rocm")
    depends_on("numactl", when="+numa")
    depends_on("llvm-openmp@19:", when="+openmp %apple-clang")
    depends_on("valgrind", when="+valgrind")
    with when("+rocm"):
        depends_on("hsa-rocr-dev")
        depends_on("hip@7.0:")
        depends_on("rccl", when="+nccl")
        depends_on("rocprim")
        depends_on("hipcub")
        depends_on("rocthrust")
        depends_on("roctracer-dev")
        depends_on("rocrand")
        depends_on("hipsparse")
        depends_on("hipfft")
        depends_on("hiprand")
        depends_on("hipsolver")
        depends_on("rocm-core")
        depends_on("amdsmi", when="@2.12")
        depends_on("rocfft")
        depends_on("rocblas")
        depends_on("miopen-hip")
        depends_on("composable-kernel")
        depends_on("hipblaslt")
        depends_on("rocm-smi-lib")
        depends_on("hipblaslt@7.0:")
        depends_on("rocminfo")
        depends_on("hipsparselt@7.0:")
        depends_on("aotriton@0.11b", when="@2.11:")
        depends_on("aotriton@0.10b", when="@:2.10")

    depends_on("mpi", when="+mpi")
    depends_on("ucc", when="+ucc")
    depends_on("ucx", when="+ucc")
    depends_on("mkl", when="+mkldnn")
    depends_on("cusparselt", when="+cusparselt")

    # Test dependencies
    with default_args(type="test"):
        depends_on("py-hypothesis")
        depends_on("py-six")
        depends_on("py-psutil")

    conflicts("%gcc@:9.3", msg="C++17 support required")

    # https://github.com/pytorch/pytorch/issues/172630 (GCC-14.2 ICE for aarch64)
    patch(
        "https://github.com/pytorch/pytorch/commit/8fd509399e25cb4b265dff663d3f777406001f2e.patch?full_index=1",
        sha256="91d0470cc05f5f0f775f32b70f174af74f5607162852ba1bcdd81381cd735f24",
        when="@:2.10.0",
    )

    # https://github.com/pytorch/pytorch/issues/151592
    patch("macos_rpath.patch", when="@:2.12")

    # to detect openmp settings used by Fujitsu compiler.
    patch("detect_omp_of_fujitsu_compiler.patch", when="%fj")

    # Fixes to build with fujitsu-ssl2
    patch("fj-ssl2_1.11.patch", when="^fujitsu-ssl2")

    # Make Pytorch build work in air gapped environments (without internet access)
    # This forwards six source folder path to NNPACK which forwards it to PeachPy
    # for versions @2.5:2.11
    patch("air_gapped_nnpack_cmake_older.patch", when="@:2.11")
    # for version @2.12: (env forwarding mechanism changed)
    # This error has been raised upstream https://github.com/pytorch/pytorch/pull/188263
    patch("air_gapped_nnpack_cmake.patch", when="@2.12:")

    # Backport the generic environment forwarding fix from PyTorch PR 188242.
    # PyTorch 2.12--2.13 parse the entire environment as a CMake list, which
    # can lose USE_* selections when unrelated values contain semicolons.
    patch("envvar-forwarding-188242.patch", when="@2.12:2.13")

    def patch(self):
        # https://github.com/pytorch/pytorch/issues/52208
        filter_file(
            "torch_global_deps PROPERTIES LINKER_LANGUAGE C",
            "torch_global_deps PROPERTIES LINKER_LANGUAGE CXX",
            "caffe2/CMakeLists.txt",
        )
        if self.spec.satisfies("+rocm"):
            filter_file(
                "find_library(ROCM_ROCTX_LIB roctx64 HINTS ${ROCM_PATH}/lib)",
                "find_library(ROCM_ROCTX_LIB roctx64 HINTS ${ROCM_PATH}/lib)\n"
                "if(DEFINED ENV{ROCTRACER_INCLUDE_DIR})\n"
                "  set(ROCTRACER_INCLUDE_DIR $ENV{ROCTRACER_INCLUDE_DIR} CACHE PATH "
                '"Roctracer include directory" FORCE)\n'
                "endif()",
                "cmake/public/LoadHIP.cmake",
                string=True,
            )

    def torch_cuda_arch_list(self, env):
        if "+cuda" in self.spec:
            torch_cuda_arch = CudaPackage.compute_capabilities(
                self.spec.variants["cuda_arch"].value
            )
            env.set("TORCH_CUDA_ARCH_LIST", ";".join(torch_cuda_arch))

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        """Set environment variables used to control the build.

        PyTorch's ``setup.py`` is a thin wrapper around ``cmake``.
        In ``tools/setup_helpers/cmake.py``, you can see that all
        environment variables that start with ``BUILD_``, ``USE_``,
        or ``CMAKE_``, plus a few more explicitly specified variable
        names, are passed directly to the ``cmake`` call. Therefore,
        most flags defined in ``CMakeLists.txt`` can be specified as
        environment variables.
        """

        def enable_or_disable(variant, keyword="USE", var=None):
            """Set environment variable to enable or disable support for a
            particular variant.

            Parameters:
                variant (str): the variant to check
                keyword (str): the prefix to use for enabling/disabling
                var (str): CMake variable to set. Defaults to variant.upper()
            """
            if var is None:
                var = variant.upper()

            if "+" + variant in self.spec:
                env.set(keyword + "_" + var, "ON")
            elif "~" + variant in self.spec:
                env.set(keyword + "_" + var, "OFF")

        # Build in parallel to speed up build times
        env.set("MAX_JOBS", str(make_jobs))

        # Spack logs have trouble handling colored output
        env.set("COLORIZE_OUTPUT", "OFF")

        # Currently there are no variants/dependencies for Intel GPU support
        env.set("USE_XPU", "OFF")

        enable_or_disable("test", keyword="BUILD")
        enable_or_disable("caffe2", keyword="BUILD")

        enable_or_disable("cuda")
        if "+cuda" in self.spec:
            env.set("CUDA_TOOLKIT_ROOT_DIR", self.spec["cuda"].prefix)  # Linux/macOS
            env.set("CUDA_HOME", self.spec["cuda"].prefix)  # Linux/macOS
            env.set("CUDA_PATH", self.spec["cuda"].prefix)  # Windows
            self.torch_cuda_arch_list(env)

            if self.spec.satisfies("%clang"):
                for flag in self.spec.compiler_flags["cxxflags"]:
                    if "gcc-toolchain" in flag:
                        env.set("CMAKE_CUDA_FLAGS", "=-Xcompiler={0}".format(flag))

        enable_or_disable("rocm")
        if "+rocm" in self.spec:
            # So libtorch_hip.so and dependents find ROCm/runtime libs at runtime and
            # during binary cache relocation (avoids "=> not found" for e.g.
            # libamdhip64.so.6, libhsa-runtime64.so.1).
            for lib_dir in [
                self.spec["hip"].prefix.lib,
                self.spec["hsa-rocr-dev"].prefix.lib,
                self.spec["rocm-smi-lib"].prefix.lib,
            ]:
                env.append_flags("LDFLAGS", "-Wl,-rpath," + lib_dir)
            # Link to rocm-smi-lib which provides rsmi_* symbols used by libtorch_hip.so
            env.append_flags(
                "LDFLAGS", "-L{} -lrocm_smi64".format(self.spec["rocm-smi-lib"].prefix.lib)
            )
            env.set("PYTORCH_ROCM_ARCH", ";".join(self.spec.variants["amdgpu_target"].value))
            env.set("HSA_PATH", self.spec["hsa-rocr-dev"].prefix)
            env.set("ROCBLAS_PATH", self.spec["rocblas"].prefix)
            env.set("ROCFFT_PATH", self.spec["rocfft"].prefix)
            env.set("HIPFFT_PATH", self.spec["hipfft"].prefix)
            env.set("HIPSPARSE_PATH", self.spec["hipsparse"].prefix)
            env.set("HIP_PATH", self.spec["hip"].prefix)
            env.set("HIPRAND_PATH", self.spec["hiprand"].prefix)
            env.set("ROCRAND_PATH", self.spec["rocrand"].prefix)
            env.set("MIOPEN_PATH", self.spec["miopen-hip"].prefix)
            if "+nccl" in self.spec:
                env.set("RCCL_PATH", self.spec["rccl"].prefix)
            env.set("ROCPRIM_PATH", self.spec["rocprim"].prefix)
            env.set("HIPCUB_PATH", self.spec["hipcub"].prefix)
            env.set("THRUST_PATH", self.spec["rocthrust"].prefix)
            env.set("ROCTRACER_PATH", self.spec["roctracer-dev"].prefix)
            env.set("ROCTRACER_INCLUDE_DIR", self.spec["roctracer-dev"].prefix.include.roctracer)
            env.set("TORCHINDUCTOR_CK_DIR", self.spec["composable-kernel"].prefix)
            env.set("AOTRITON_INSTALLED_PREFIX", self.spec["aotriton"].prefix)
            env.prepend_path("CPATH", self.spec["aotriton"].prefix.include)
            if self.spec.satisfies("^hip@5.2.0:"):
                env.set("CMAKE_MODULE_PATH", self.spec["hip"].prefix.lib.cmake.hip)

        enable_or_disable("cudnn")
        if "+cudnn" in self.spec:
            # cmake/Modules_CUDA_fix/FindCUDNN.cmake
            env.set("CUDNN_INCLUDE_DIR", self.spec["cudnn"].prefix.include)
            env.set("CUDNN_LIBRARY", self.spec["cudnn"].libs[0])

        enable_or_disable("cusparselt")
        enable_or_disable("fbgemm")
        enable_or_disable("kineto")
        enable_or_disable("magma")
        enable_or_disable("metal")
        enable_or_disable("mps")
        enable_or_disable("flash_attention")

        enable_or_disable("nccl")
        if "+cuda+nccl" in self.spec:
            env.set("NCCL_LIB_DIR", self.spec["nccl"].libs.directories[0])
            env.set("NCCL_INCLUDE_DIR", self.spec["nccl"].prefix.include)

        # cmake/External/nnpack.cmake
        enable_or_disable("nnpack")
        if "+nnpack" in self.spec and "py-six" in self.spec:
            # NNPACK/PeachPy wires this path into PYTHONPATH for codegen.
            # Point it at Spack's installed py-six to avoid network fetches.
            env.set(
                "PYTHON_SIX_SOURCE_DIR",
                self["py-six"].module.python_purelib,
            )

        enable_or_disable("numa")
        if "+numa" in self.spec:
            # cmake/Modules/FindNuma.cmake
            env.set("NUMA_ROOT_DIR", self.spec["numactl"].prefix)

        # cmake/Modules/FindNumPy.cmake
        enable_or_disable("numpy")
        # cmake/Modules/FindOpenMP.cmake
        enable_or_disable("openmp")
        enable_or_disable("qnnpack")
        enable_or_disable("qnnpack", var="PYTORCH_QNNPACK")
        enable_or_disable("valgrind")
        enable_or_disable("xnnpack")
        enable_or_disable("mkldnn")
        enable_or_disable("distributed")
        enable_or_disable("mpi")
        enable_or_disable("ucc")
        # cmake/Modules/FindGloo.cmake
        enable_or_disable("gloo")
        enable_or_disable("tensorpipe")

        if "+debug" in self.spec:
            env.set("DEBUG", "ON")
        else:
            env.set("DEBUG", "OFF")

        if not self.spec.satisfies("@main"):
            env.set("PYTORCH_BUILD_VERSION", str(self.version))
            env.set("PYTORCH_BUILD_NUMBER", str(0))

        # BLAS to be used by Caffe2
        # Options defined in cmake/Dependencies.cmake and cmake/Modules/FindBLAS.cmake
        if self.spec["blas"].name == "atlas":
            env.set("BLAS", "ATLAS")
            env.set("WITH_BLAS", "atlas")
            env.set("Atlas_ROOT_DIR", self.spec["atlas"].prefix)
        elif self.spec["blas"].name in ["blis", "amdblis"]:
            env.set("BLAS", "BLIS")
            env.set("WITH_BLAS", "blis")
            env.set("BLIS_HOME", self.spec["blas"].prefix)
        elif self.spec["blas"].name == "eigen":
            env.set("BLAS", "Eigen")
        elif self.spec["lapack"].name in ["libflame", "amdlibflame"]:
            env.set("BLAS", "FLAME")
            env.set("WITH_BLAS", "FLAME")
        elif self.spec["blas"].name == "intel-oneapi-mkl":
            env.set("BLAS", "MKL")
            env.set("WITH_BLAS", "mkl")
            env.set("INTEL_MKL_DIR", self.spec["intel-oneapi-mkl"].prefix.mkl.latest)
        elif self.spec["blas"].name == "openblas":
            env.set("BLAS", "OpenBLAS")
            env.set("WITH_BLAS", "open")
            env.set("OpenBLAS_HOME", self.spec["openblas"].prefix)
        elif self.spec["blas"].name == "veclibfort":
            env.set("BLAS", "vecLib")
            env.set("WITH_BLAS", "veclib")
        elif self.spec["blas"].name == "fujitsu-ssl2":
            env.set("BLAS", "SSL2")
            env.set("WITH_BLAS", "ssl2")
        else:
            env.set("BLAS", "Generic")
            env.set("WITH_BLAS", "generic")

        # Don't use vendored third-party libraries when possible
        # env.set("USE_SYSTEM_LIBS", "ON")
        env.set("USE_SYSTEM_BENCHMARK", "ON")
        env.set("USE_SYSTEM_CPUINFO", "ON")
        env.set("USE_SYSTEM_EIGEN_INSTALL", "ON")
        env.set("USE_SYSTEM_FP16", "ON")
        env.set("USE_SYSTEM_FXDIV", "ON")
        env.set("USE_SYSTEM_GLOO", "ON")
        env.set("USE_SYSTEM_NCCL", "ON")
        env.set("USE_SYSTEM_NVTX", "ON")
        # https://github.com/pytorch/pytorch/issues/60331
        # env.set("USE_SYSTEM_ONNX", "ON")
        env.set("USE_SYSTEM_PSIMD", "ON")
        env.set("USE_SYSTEM_PTHREADPOOL", "ON")
        env.set("USE_SYSTEM_PYBIND11", "ON")
        env.set("USE_SYSTEM_SLEEF", "ON")
        env.set("USE_SYSTEM_UCC", "ON")
        # https://github.com/pytorch/pytorch/issues/60332
        # env.set("USE_SYSTEM_XNNPACK", "ON")

        if self.spec.satisfies("+custom-protobuf"):
            env.set("BUILD_CUSTOM_PROTOBUF", "ON")
        else:
            env.set("BUILD_CUSTOM_PROTOBUF", "OFF")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        self.torch_cuda_arch_list(env)
        if "+rocm" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["hip"].prefix.lib)

    def setup_dependent_build_environment(self, env, dependent_spec):
        if "+rocm" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["hip"].prefix.lib)
            # PyTorch headers (e.g. c10/util/complex.h) include <thrust/complex.h>;
            # dependents need rocthrust include so HIP device builds can find it.
            env.set("THRUST_PATH", self.spec["rocthrust"].prefix)
            env.prepend_path("CPATH", self.spec["rocthrust"].prefix.include)

    def setup_dependent_run_environment(self, env, dependent_spec):
        """So dependents (e.g. py-torch-nvidia-apex, py-torchaudio) can find
        libamdhip64.so when importing torch or running code that uses ROCm."""
        if "+rocm" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["hip"].prefix.lib)

    @run_before("install")
    def build_amd(self):
        if "+rocm" in self.spec:
            python(os.path.join("tools", "amd_build", "build_amd.py"))

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def install_test(self):
        with working_dir("test"):
            python("run_test.py")

    @property
    def cmake_prefix_paths(self):
        cmake_prefix_paths = [join_path(python_platlib, "torch", "share", "cmake")]
        return cmake_prefix_paths

    @property
    def libs(self):
        return find_libraries(
            "libtorch*", root=python_platlib, recursive=True, shared=True
        ) + find_libraries("libc10*", root=python_platlib, recursive=True, shared=True)
