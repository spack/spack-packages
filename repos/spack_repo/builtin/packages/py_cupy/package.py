# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class PyCupy(PythonPackage, CudaPackage, ROCmPackage):
    """CuPy is an open-source array library accelerated with
    NVIDIA CUDA. CuPy provides GPU accelerated computing with
    Python. CuPy uses CUDA-related libraries including cuBLAS,
    cuDNN, cuRand, cuSolver, cuSPARSE, cuFFT and NCCL to make
    full use of the GPU architecture."""

    # TODO: CuPy bundles some dependencies in `third_party` (cccl, dlpack, jitify, xsf). These
    #  should be modeled as explicit dependencies.

    homepage = "https://cupy.dev/"
    pypi = "cupy/cupy-8.0.0.tar.gz"
    git = "https://github.com/cupy/cupy.git"
    submodules = True

    version("main", branch="main")
    version("14.0.1", sha256="4b673ab2d8b2329abe7ae0a7ae6159656044a8eecca56cf0b834b7c907063205")
    version("14.0.0", sha256="615a7dfbe699729785fa9ef0789de05ec1c278b8c3b675460ad19c8808802995")
    version("13.6.0", sha256="3cba30ae3dd32b5d5c6536e710cb98015227cd4ba83c46b3f1825a7ae55b6667")
    version("13.5.1", sha256="3dba2f30258463482d52deb420862fbbbaf2c446165a5e8d67377ac6cb5c0870")
    version("13.5.0", sha256="e24be7837c857f95cf484b4eff91a627a5e622aaece559060b138d9d64e6161d")
    version("13.4.1", sha256="9654730da3f7122ba3fe99ce951247e299f3f9c23449a884ba9914444845f0cd")
    version("13.4.0", sha256="d4b60e5a1d3b89be40fad0845bb9fc467a653abe8660f752416fd38d24ab7fdb")
    version("13.3.0", sha256="9a2a17af2b99cce91dd1366939c3805e3f51f9de5046df64f29ccbad3bdf78ed")
    version("13.2.0", sha256="e4dbd2b2ed4159a5cc0c0f98a710a014950eb2c16eeb455e956128f3b3bd0d51")
    version("13.1.0", sha256="5caf62288481a27713384523623045380ff42e618be4245f478238ed1786f32d")
    version("13.0.0", sha256="2f04e7857f692a713360dc9c3b06709806ab8404fca39b5af9721c04a2979aae")
    version("12.3.0", sha256="47db32114e6fdd48d0510cbf0b08b0935522d7dfa3e39416b0c0da3914323524")
    version("12.2.0", sha256="f95ffd0afeacb617b048fe028ede07b97dc9e95aca1610a022b1f3d20a9a027e")
    version("12.1.0", sha256="f6d31989cdb2d96581da12822e28b102f29e254427195c2017eac327869b7320")
    version("12.0.0", sha256="61ddbbef73d50d606bd5087570645f3c91ec9176c2566784c1d486d6a3404545")
    version("11.6.0", sha256="53dbb840072bb32d4bfbaa6bfa072365a30c98b1fcd1f43e48969071ad98f1a7")
    version("11.5.0", sha256="4bc8565bded22cc89b210fd9fb48a5d5316f30701e12bb23852a60314e1f9f6e")
    version("11.4.0", sha256="03d52b2626e02a3a2b46d714c1cd03e702c8fe33915fcca6ed8de5c539964f49")
    version("11.3.0", sha256="d057cc2f73ecca06fae8b9c270d9e14116203abfd211a704810cc50a453b4c9e")
    version("11.2.0", sha256="c33361f117a347a63f6996ea97446d17f1c038f1a1f533e502464235076923e2")

    variant("all", default=False, description="Enable optional py-scipy, optuna, and cython")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("python@3.7:", when="@:11", type=("build", "run"))
    depends_on("python@3.8:3.11", when="@12", type=("build", "run"))
    depends_on("python@3.9:3.13", when="@13", type=("build", "run"))
    depends_on("python@3.10:", when="@14", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@:73", when="@:13.3", type="build")
    depends_on("py-cython@0.29.22:0.29", type="build", when="@:13.3")
    depends_on(
        "py-cython@3:3.0.10,3.0.12:", type="build", when="@13.4:13"
    )  # 3.0.11 broken likely because of cython#6335, fixed in 3.0.12
    depends_on("py-cython@3.1", type="build", when="@14:")
    depends_on("py-fastrlock@0.5:", type=("build", "run"))
    depends_on("py-numpy@1.20:1.25", when="@:11", type=("build", "run"))
    depends_on("py-numpy@1.20:1.26", when="@12", type=("build", "run"))
    depends_on("py-numpy@1.22:1", when="@13.1", type=("build", "run"))
    depends_on("py-numpy@1.22:2.0", when="@13.2", type=("build", "run"))
    depends_on("py-numpy@1.22:2.2", when="@13.4", type=("build", "run"))
    depends_on("py-numpy@1.22:2.3", when="@13.5", type=("build", "run"))
    depends_on("py-numpy@2:", when="@14", type=("build", "run"))
    depends_on("py-scipy@1.6:1.11", when="@:12+all", type=("build", "run"))
    depends_on("py-scipy@1.7:1.16", when="@13+all", type=("build", "run"))
    depends_on("py-scipy@1.10:1.16", when="@14+all", type=("build", "run"))
    depends_on("py-optuna@2:", when="+all", type=("build", "run"))
    depends_on("py-optuna@3:", when="@12:+all", type=("build", "run"))

    # Based on https://github.com/cupy/cupy/releases
    depends_on("cuda@:11.9", when="@:11 +cuda")
    depends_on("cuda@:12.1", when="@12:12.1.0 +cuda")
    depends_on("cuda@:12.1", when="@13.0 +cuda")
    depends_on("cuda@:12.4", when="@13.1:13.2 +cuda")
    depends_on("cuda@:12.6", when="@13.3 +cuda")
    depends_on("cuda@:12.8", when="@13.4 +cuda")
    depends_on("cuda@:12.9", when="@13.5 +cuda")
    depends_on("py-cuda-pathfinder", when="@14: +cuda")

    for a in CudaPackage.cuda_arch_values:
        depends_on("nccl +cuda cuda_arch={0}".format(a), when="+cuda cuda_arch={0}".format(a))
        depends_on(
            "nccl@2.16:2.26 +cuda cuda_arch={0}".format(a), when="@13+cuda cuda_arch={0}".format(a)
        )

    depends_on("cudnn@8.8", when="@12.0.0:13 +cuda")
    depends_on("cudnn@8.5", when="@11.2.0:11.6.0 +cuda")
    depends_on("cutensor", when="@:12.1.0 +cuda")
    depends_on("cutensor@2.0", when="@13.1: +cuda")

    depends_on("hip@4:5", when="@:13.3 +rocm")
    depends_on("hip@4:6", when="@13.4:13 +rocm")
    for _arch in ROCmPackage.amdgpu_targets:
        arch_str = "amdgpu_target={0}".format(_arch)
        rocm_str = "+rocm {0}".format(arch_str)
        depends_on("rocprim {0}".format(arch_str), when=rocm_str, type=("link"))
        depends_on("rocsolver {0}".format(arch_str), when=rocm_str, type=("link"))
        depends_on("rocthrust {0}".format(arch_str), when=rocm_str, type=("link"))
        depends_on("rocrand {0}".format(arch_str), when=rocm_str, type=("link"))
        depends_on("hipcub {0}".format(rocm_str), when=rocm_str, type=("link"))
        depends_on("hipblas {0}".format(rocm_str), when=rocm_str, type=("link"))
        depends_on("hiprand {0}".format(rocm_str), when=rocm_str, type=("link"))
        depends_on("hipsparse {0}".format(rocm_str), when=rocm_str, type=("link"))
        depends_on("hipfft {0}".format(rocm_str), when=rocm_str, type=("link"))

    depends_on("rccl", when="+rocm", type=("link"))
    depends_on("roctracer-dev", when="+rocm", type=("link"))
    depends_on("rocprofiler-dev", when="+rocm", type=("link"))

    conflicts("~cuda ~rocm")
    conflicts("+cuda +rocm")
    conflicts("+cuda cuda_arch=none")

    patch(
        "https://patch-diff.githubusercontent.com/raw/cupy/cupy/pull/9022.patch?full_index=1",
        sha256="bc96ea317748e42f7651d9f3b97f8db224081f627bcfcb6cc48c2ca139143441",
        when="@13.4 ^rocm-core@6.3",
    )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CUPY_NUM_BUILD_JOBS", str(make_jobs))
        if self.spec.satisfies("+cuda"):
            cuda_arch = self.spec.variants["cuda_arch"].value
            arch_str = ";".join("arch=compute_{0},code=sm_{0}".format(i) for i in cuda_arch)
            env.set("CUPY_NVCC_GENERATE_CODE", arch_str)
        elif self.spec.satisfies("+rocm"):
            spec = self.spec

            incs = {
                "hipblas": ["include", "include/hipblas"],
                "hipsparse": ["include", "include/hipsparse"],
                "hipfft": ["include", "include/hipfft"],
                "rocsolver": ["include", "include/rocsolver"],
                "rccl": ["include", "include/rccl"],
                "roctracer-dev": ["include/roctracer"],
                "hiprand": ["include", "include/hiprand"],
                "rocrand": ["include"],
                "rocthrust": ["include"],
                "rocprim": ["include"],
                "hip": ["include", "include/hip"],
            }

            inc_dirs = []
            for pkg, ds in incs.items():
                for d in ds:
                    p = os.path.join(spec[pkg].prefix, d)
                    if os.path.exists(p):
                        inc_dirs.append(p)

            env.set("CUPY_INCLUDE_PATH", ":".join(inc_dirs))

            env.set("HIPCC", self.spec["hip"].hipcc)
            env.set("ROCM_HOME", self.spec["hipcub"].prefix)
            env.set("CUPY_INSTALL_USE_HIP", "1")
