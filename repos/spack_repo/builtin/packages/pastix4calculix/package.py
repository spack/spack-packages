# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Pastix4calculix(CMakePackage, CudaPackage):
    """CUDA-enabled ILP64 PaStiX fork for CalculiX."""

    homepage = "https://github.com/Dhondtguido/PaStiX4CalculiX"
    git = "https://github.com/Dhondtguido/PaStiX4CalculiX.git"

    license("CECILL-2.0")
    maintainers("failed33")

    # Upstream tag: ccx_2.18.
    version("2021.09.22", commit="d6b493bc431ecf860b3578a2ee6a25f392eb44be")

    variant("cuda", default=True, description="GPU acceleration (required)")
    for arch in CudaPackage.cuda_arch_values:
        if arch not in ("70", "72", "75", "80", "86", "89", "90"):
            conflicts(f"cuda_arch={arch}", when="+cuda", msg="Unsupported by this PaRSEC fork")
    conflicts("~cuda", msg="PaStiX4CalculiX requires CUDA")
    conflicts(
        "cuda_arch=none",
        when="+cuda",
        msg="Select a CUDA architecture",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.16:3", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("cuda@11:12")
    depends_on("python", type="build")

    # Match the integer ABI of the CalculiX adapter.
    depends_on("scotch +int64 ~mpi")
    depends_on("hwloc@2:")
    depends_on("openblas +ilp64 threads=openmp")

    depends_on("parsec-pastix +cuda")
    for arch in CudaPackage.cuda_arch_values:
        depends_on(
            f"parsec-pastix+cuda cuda_arch={arch}",
            when=f"+cuda cuda_arch={arch}",
        )

    patch("pastix4calculix-cuda12.patch", when="@=2021.09.22")
    # A failed precision generation leaves undefined bvec_* symbols at link time.
    patch("pastix4calculix-py3.patch", when="@=2021.09.22")

    @run_before("cmake")
    def disable_examples_and_tests(self):
        # example/ and test/ are added unconditionally and fail to link; we only
        # need the libraries, so neutralise their add_subdirectory() calls.
        cml = join_path(self.stage.source_path, "CMakeLists.txt")
        if os.path.exists(cml):
            filter_file(r"^add_subdirectory\(example\)", "# add_subdirectory(example)", cml)
            filter_file(r"^add_subdirectory\(test\)", "# add_subdirectory(test)", cml)

    @property
    def libs(self):
        return find_libraries("libpastix", root=self.prefix, shared=True, recursive=True)

    def cmake_args(self):
        spec = self.spec
        cuda = spec["cuda"].prefix
        flags = self.cuda_flags(spec.variants["cuda_arch"].value)
        # FindCUDA's separate device-link command also generates host code.
        nvcc_flags = ";".join(" ".join(flags).split() + ["-Xcompiler=-fPIC"])

        return [
            # Restore the OLD FindCUDA / FindPythonInterp modules the vendored
            # 2020 morse_cmake relies on (removed in CMake 3.27 -> CMP0146/0148).
            "-DCMAKE_POLICY_DEFAULT_CMP0146=OLD",
            "-DCMAKE_POLICY_DEFAULT_CMP0148=OLD",
            self.define("BLAS_DIR", spec["openblas"].prefix),
            self.define("LAPACKE_DIR", spec["openblas"].prefix),
            self.define("HWLOC_DIR", spec["hwloc"].prefix),
            self.define("SCOTCH_DIR", spec["scotch"].prefix),
            self.define("PASTIX_INT64", True),
            self.define("PASTIX_ORDERING_SCOTCH", True),
            self.define("BUILD_SHARED_LIBS", True),
            self.define("PASTIX_WITH_PARSEC", True),
            self.define("PARSEC_DIR", spec["parsec-pastix"].prefix),
            self.define("PASTIX_WITH_CUDA", True),
            self.define("CUDA_TOOLKIT_ROOT_DIR", cuda),
            # bare `g++` resolves relative to the build dir under nvcc; use abspath
            self.define("CUDA_HOST_COMPILER", spack_cxx),
            self.define("CUDA_NVCC_FLAGS", nvcc_flags),
            self.define("CMAKE_C_FLAGS", "-fopenmp -fcommon -I{0}/include".format(cuda)),
            self.define("CMAKE_CXX_FLAGS", "-fopenmp -fcommon -I{0}/include".format(cuda)),
            self.define("CMAKE_EXE_LINKER_FLAGS", "-fopenmp"),
        ]
