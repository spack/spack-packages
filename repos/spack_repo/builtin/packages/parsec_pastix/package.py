# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class ParsecPastix(CMakePackage, CudaPackage):
    """PaRSEC fork with the ABI required by PaStiX4CalculiX."""

    homepage = "https://bitbucket.org/mfaverge/parsec"
    git = "https://bitbucket.org/mfaverge/parsec.git"

    license("BSD-3-Clause-Open-MPI")
    maintainers("failed33")

    version("6.0.2", commit="b580d208094e6cb4106e41d5eeec84f304a090b8")

    variant(
        "cuda",
        default=True,
        description="GPU acceleration (required by PaStiX4CalculiX)",
    )
    for arch in CudaPackage.cuda_arch_values:
        if arch not in ("70", "72", "75", "80", "86", "89", "90"):
            conflicts(f"cuda_arch={arch}", when="+cuda", msg="Unsupported by this PaRSEC fork")
    conflicts("~cuda", msg="PaStiX4CalculiX needs the CUDA-enabled PaRSEC; build +cuda")
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
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("hwloc@2:")

    # PaRSEC will not schedule GPU tasks on devices absent from its capability table.
    patch("parsec-ampere-hopper.patch", when="@=6.0.2")

    @property
    def libs(self):
        return find_libraries("libparsec", root=self.prefix, shared=True, recursive=True)

    def cmake_args(self):
        spec = self.spec
        cuda = spec["cuda"].prefix
        flags = self.cuda_flags(spec.variants["cuda_arch"].value)
        nvcc_flags = ";".join(" ".join(flags).split())
        return [
            "-DCMAKE_POLICY_DEFAULT_CMP0146=OLD",
            "-DCMAKE_POLICY_DEFAULT_CMP0148=OLD",
            self.define("BUILD_TESTING", False),
            self.define("BUILD_SHARED_LIBS", True),
            self.define("PARSEC_GPU_WITH_CUDA", True),
            self.define("PARSEC_DIST_WITH_MPI", False),
            self.define("CUDA_TOOLKIT_ROOT_DIR", cuda),
            self.define("CUDA_HOST_COMPILER", spack_cc),
            self.define("CUDA_NVCC_FLAGS", nvcc_flags),
            self.define("HWLOC_DIR", spec["hwloc"].prefix),
            self.define("CMAKE_C_FLAGS", "-fcommon -I{0}/include".format(cuda)),
        ]

    @run_after("install")
    def strip_threads_target(self):
        # The vendored PaStiX CMake modules cannot resolve this imported target.
        # PaStiX links pthread separately.
        pc = join_path(self.prefix.lib, "pkgconfig", "parsec.pc")
        cfg = join_path(self.prefix.lib, "cmake", "ParsecConfig.cmake")
        if os.path.exists(pc):
            filter_file(" -lThreads::Threads", "", pc, string=True)
        if os.path.exists(cfg):
            filter_file("Threads::Threads;", "", cfg, string=True)
