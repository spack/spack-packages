# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import cmake, makefile
from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.cuda import CudaPackage, conflicts
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *

from os.path import join as pjoin
import os, glob

class Nvshmem(MakefilePackage, CMakePackage, CudaPackage):
    """NVSHMEM is a parallel programming interface based on OpenSHMEM that
    provides efficient and scalable communication for NVIDIA GPU
    clusters. NVSHMEM creates a global address space for data that spans
    the memory of multiple GPUs and can be accessed with fine-grained
    GPU-initiated operations, CPU-initiated operations, and operations on
    CUDA streams."""

    homepage = "https://developer.nvidia.com/nvshmem"

    maintainers("bvanessen")

    license("BSD-3-Clause-Open-MPI")

    version("3.4.5", sha256="40c1d4c255dd7395e04df41b181c4afdf2e0724c06b6fabde58bf2f8f532b0e5")
    version("3.3.24", sha256="3210e6ed0f010991af3c9f31266b4149a15bc1d560f98951c234f25e2076507e")
    version("3.3.20", sha256="96ec9620e82ec90de92c7d61a7ba03c0eba05075bf10e1fc4a066d45e7f7d21f")
    version("3.3.9", sha256="ba41e9ad6650cf99c1a60a3e47c19d1d97d814add7d35ea72337520ae13eeb59")
    version("3.2.5-1", sha256="eb2c8fb3b7084c2db86bd9fd905387909f1dfd483e7b45f7b3c3d5fcf5374b5a")
    version("2.7.0-6", sha256="23ed9b0187104dc87d5d2bc1394b6f5ff29e8c19138dc019d940b109ede699df")
    version("2.6.0-1", sha256="fc0e8de61b034f3a079dc231b1d0955e665a9f57b5013ee98b6743647bd60417")
    version("2.5.0-19", sha256="dd800b40f1d296e1d3ed2a9885adcfe745c3e57582bc809860e87bd32abcdc60")
    version("2.4.1-3", sha256="8b6c0eab321b6352911e470f9e81a777a49e58148ec3728453b9522446dba178")
    version("2.2.1-0", sha256="c8efc6cd560e0ed66d5fe4c5837c650247bec7b0dc65b5089deb8ab49658e1c3")
    version("2.1.2-0", sha256="367211808df99b4575fb901977d9f4347065c61a26642d65887f24d60342a4ec")
    version("2.0.3-0", sha256="20da93e8508511e21aaab1863cb4c372a3bec02307b932144a7d757ea5a1bad2")

    build_system(
        conditional("cmake", when="@2.9.0:"),
        conditional("makefile", when="@:2.11"),
        default="cmake",
    )

    variant("cuda", default=True, description="Build with CUDA")
    variant("ucx", default=True, description="Build with UCX support")
    variant("nccl", default=True, description="Build with NCCL support")
    variant("gdrcopy", default=True, description="Build with gdrcopy support")
    variant("mpi", default=True, description="Build with MPI support")
    variant("shmem", default=False, description="Build with shmem support")
    variant(
        "gpu_initiated_support",
        default=False,
        when="@2.6:",
        description="Build with support for GPU initiated communication",
    )
    variant("libfabric", default=False, description="Build with Libfabric support")

    variant("python", default=False, description="Build/install nvshmem4py (Python bindings)")
    variant("mpi4py", default=True, when="+python+mpi", description="Install mpi4py runtime dep")
    variant("cupy",   default=True, when="+python",     description="Install CuPy interop dep")
    variant("pytorch", default=True, when="+python",    description="Install PyTorch interop dep")

    generator("ninja")

    conflicts("~cuda", msg="NVSHMEM requires CUDA")
    conflicts("+python", when="@:3.2", msg="Python bindings require NVSHMEM >= 3.3")

    extendable = True
    extends("python", when="+python")

    def url_for_version(self, version):
        ver_str = "{0}".format(version)
        directory = ver_str.split("-")[0]
        if version < Version("3.3.9"):
            url_fmt = "https://developer.download.nvidia.com/compute/redist/nvshmem/{0}/source/nvshmem_src_{1}.txz"
        else:
            url_fmt = "https://developer.download.nvidia.com/compute/redist/nvshmem/{0}/source/nvshmem_src_cuda12-all-all-{0}.tar.gz"
        return url_fmt.format(directory, version)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cuda@11:", when="@3.2.5:")

    with default_args(when="build_system=cmake", type="build"):
        depends_on("cmake@3.19:")
        depends_on("ninja")

    depends_on("mpi", when="+mpi")

    depends_on("ucx", when="+ucx")
    depends_on("ucx@1.10:", when="@3: +ucx")

    depends_on("gdrcopy", when="+gdrcopy")
    conflicts("~gdrcopy", when="~ucx")
    depends_on("gdrcopy@2:", when="@3: +gdrcopy")

    depends_on("nccl", when="+nccl")
    depends_on("nccl@2:", when="@3: +nccl")

    depends_on("libfabric", when="+libfabric")
    depends_on("libfabric@1.15:", when="@3: +libfabric")

    with when("+python"):
        depends_on("python@3.9:", type=("build", "link", "run"))
        depends_on("py-pip",      type="build")
        depends_on("py-wheel",    type="build")
        depends_on("py-setuptools", type="build")
        depends_on("py-cython@0.29.24:", type=("build", "link"))
        depends_on("py-numpy@1.26:",     type=("build", "link", "run"))
        depends_on("py-cuda-bindings",     type="run")
        depends_on("py-mpi4py", when="+mpi4py",  type="run")
        depends_on("py-cupy",   when="+cupy",    type="run")
        depends_on("py-pytorch@2.6:", when="+pytorch", type="run")

    patch("v3.4.5-perftest-mpich.patch", when="@3.4.5 +mpi")


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        config = [
            self.define("CMAKE_CUDA_ARCHITECTURES", self.spec.variants["cuda_arch"].values),
            self.define_from_variant("NVSHMEM_MPI_SUPPORT", "mpi"),
            self.define_from_variant("NVSHMEM_LIBFABRIC_SUPPORT", "libfabric"),
            self.define_from_variant("NVSHMEM_UCX_SUPPORT", "ucx"),
            self.define_from_variant("NVSHMEM_USE_NCCL", "nccl"),
            self.define_from_variant("NVSHMEM_USE_GDRCOPY", "gdrcopy"),
            self.define_from_variant("NVSHMEM_SHMEM_SUPPORT", "shmem"),
            self.define("NVSHMEM_IBRC_SUPPORT", False),
            self.define_from_variant("NVSHMEM_BUILD_PYTHON_LIB", "python"),
            self.define("NVSHMEM_BUILD_EXAMPLES", False),
            self.define("NVSHMEM_BUILD_HYDRA_LAUNCHER", False),
            self.define("NVSHMEM_BUILD_TESTS", True),
            self.define("NVSHMEM_BUILD_TXZ_PACKAGE", False),
        ]

        if "+mpi" in self.spec:
            config.append(self.define("MPI_HOME", self.spec["mpi"].prefix))

        if "+libfabric" in self.spec:
            config.append(self.define("LIBFABRIC_HOME", self.spec["libfabric"].prefix))

        if "+ucx" in self.spec:
            config.append(self.define("UCX_HOME", self.spec["ucx"].prefix))

        if "+nccl" in self.spec:
            config.append(self.define("NCCL_HOME", self.spec["nccl"].prefix))

        if "+gdrcopy" in self.spec:
            config.append(self.define("GDRCOPY_HOME", self.spec["gdrcopy"].prefix))

        if "+shmem" in self.spec:
            config.append(self.define("SHMEM_HOME", self.spec["shmem"].prefix))

        if "+python" in self.spec:
            py = self.spec["python"]
            # Python interpreter for CMake’s FindPython3
            config.append(self.define("Python3_EXECUTABLE", py.command.path))
            # Explicit include dir for Python.h (avoids CMake guessing wrong)
            inc_dirs = py.headers.directories
            if inc_dirs:
                config.append(self.define("Python3_INCLUDE_DIR", inc_dirs[0]))

        config.append(self.define("NVSHMEM_DEBUG","0"))
        config.append(self.define("NVSHMEM_DEVEL","0"))

        config.append(self.define("NVSHMEM_DEFAULT_PMI2", "1"))
        config.append(self.define("NVSHMEM_DEFAULT_PMIX", "0"))
        config.append(self.define("NVSHMEM_PMI2_SUPPORT", "1"))
        config.append(self.define("NVSHMEM_PMIX_SUPPORT", "0"))

        config.append(self.define("NVSHMEM_DISABLE_COLL_POLL", "1"))
        config.append(self.define("NVSHMEM_ENABLE_ALL_DEVICE_INLINING", "0"))
        config.append(self.define("NVSHMEM_GPU_COLL_USE_LDST", "0"))
        config.append(self.define("NVSHMEM_MPI_IS_OMPI", "1" if self.spec.satisfies("^openmpi") else "0"))
        config.append(self.define("NVSHMEM_NVTX", "1"))

        config.append(self.define("NVSHMEM_TEST_STATIC_LIB", "0"))
        config.append(self.define("NVSHMEM_TIMEOUT_DEVICE_POLLING", "0"))
        config.append(self.define("NVSHMEM_TRACE", "0"))
        config.append(self.define("NVSHMEM_USE_DLMALLOC", "0"))

        config.append(self.define("NVSHMEM_VERBOSE", "0"))
        config.append(self.define("NVSHMEM_DEFAULT_UCX", "0"))

        config.append(self.define("NVSHMEM_IBGDA_SUPPORT", "0"))
        config.append(self.define("NVSHMEM_IBGDA_SUPPORT_GPUMEM_ONLY", "0"))
        config.append(self.define("NVSHMEM_IBDEVX_SUPPORT", "0"))
        config.append(self.define("NVSHMEM_IBRC_SUPPORT", "0"))

        return config

    @run_before("cmake")
    def pin_wheel_build_inputs(self):
        if "+python" not in self.pkg.spec:
            return

        src = self.pkg.stage.source_path
        py = self.pkg.spec["python"]
        py_ver = str(py.version.up_to(2))  # e.g. "3.12"
        py_exec = py.command.path

        # Force the python version list to only our interpreter
        script = pjoin(src, "nvshmem4py", "scripts", "find_python_versions.sh")
        with open(script, "w") as f:
            f.write(f'#!/bin/sh\n# Spack override\n'
                    f'echo "{py_ver}|{py_exec}"\n')
        os.chmod(script, 0o755)

        # Restrict CUDA versions to just our major (11 or 12 or 13)
        cuda_major = str(self.pkg.spec["cuda"].version.up_to(1)).split(".")[0]
        cmakelists = pjoin(src, "nvshmem4py", "CMakeLists.txt")
        filter_file(
            r'set\(CUDA_VERSIONS\s+"11"\s+"12"\s+"13"\s*\)',
            f'set(CUDA_VERSIONS "{cuda_major}")',
            cmakelists
        )

    @run_after("install")
    def install_python_wheel(self):
        if "+python" not in self.pkg.spec:
            return

        dist_dir = pjoin(self.pkg.stage.source_path, "build", "dist")
        if not os.path.isdir(dist_dir):
            raise InstallError(f"nvshmem4py dist directory not found: {dist_dir}")

        cuda_major = str(self.pkg.spec["cuda"].version.up_to(1)).split(".")[0]  # e.g. '12'
        base_pat   = f"nvshmem4py_cu{cuda_major}-*.whl"
        many_pat   = f"nvshmem4py_cu{cuda_major}-*manylinux*.whl"

        # Prefer plain linux wheel (system-specific)
        wheels_plain = sorted([p for p in glob.glob(pjoin(dist_dir, base_pat))
                               if "manylinux" not in os.path.basename(p)])
        # Fallback: manylinux wheel (portable)
        wheels_many  = sorted(glob.glob(pjoin(dist_dir, many_pat)))

        artifact = (wheels_plain[-1] if wheels_plain
                    else wheels_many[-1] if wheels_many
                    else None)
        if not artifact:
            raise InstallError(f"No nvshmem4py artifacts found in {dist_dir}")

        # Install exactly that artifact; pip will still validate tags vs current Python
        python("-m", "pip", "install",
               "--no-deps", "--no-build-isolation",
               "--prefix", self.pkg.prefix,
               "--no-index", artifact)


class MakeBuilder(makefile.MakefileBuilder):
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CUDA_HOME", self.spec["cuda"].prefix)
        env.set("NVSHMEM_PREFIX", self.prefix)

        if "+ucx" in self.spec:
            env.set("NVSHMEM_UCX_SUPPORT", "1")
            env.set("UCX_HOME", self.spec["ucx"].prefix)

        if "+gdrcopy" in self.spec:
            env.set("NVSHMEM_USE_GDRCOPY", "1")
            env.set("GDRCOPY_HOME", self.spec["gdrcopy"].prefix)

        if "+nccl" in self.spec:
            env.set("NVSHMEM_USE_NCCL", "1")
            env.set("NCCL_HOME", self.spec["nccl"].prefix)

        if "+mpi" in self.spec:
            env.set("NVSHMEM_MPI_SUPPORT", "1")
            env.set("MPI_HOME", self.spec["mpi"].prefix)

            if self.spec.satisfies("^spectrum-mpi") or self.spec.satisfies("^openmpi"):
                env.set("NVSHMEM_MPI_IS_OMPI", "1")
            else:
                env.set("NVSHMEM_MPI_IS_OMPI", "0")

        if "+shmem" in self.spec:
            env.set("NVSHMEM_SHMEM_SUPPORT", "1")
            env.set("SHMEM_HOME", self.spec["mpi"].prefix)

        if "+gpu_initiated_support" in self.spec:
            env.set("NVSHMEM_GPUINITIATED_SUPPORT", "1")
