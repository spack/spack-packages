# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.install_test import SkipTest
from spack.package import *


class Quest(CMakePackage, CudaPackage, ROCmPackage):
    """A multithreaded, distributed, GPU-accelerated simulator of quantum computers."""

    homepage = "https://quest.qtechtheory.org"
    url = "https://github.com/QuEST-Kit/QuEST/archive/refs/tags/v4.0.0.tar.gz"

    maintainers("AcerP-py")

    license("MIT", checked_by="AcerP-py")

    version("4.1.0", sha256="85aa95bba6457c4f4e93221f4c417d988588891a1f7cb211c307dfe81a10cadd")
    version("4.0.0", sha256="e6a922a9dc1d6ee7c4d2591a277646dca2ce2fd90eecf36fd66970cb24bbfb67")

    variant("examples", default=False, description="Build examples")
    variant("mpi", default=True, description="Enable MPI support")
    variant("openmp", default=True, description="Build with OpenMP")
    variant(
        "precision",
        default="2",
        description="Set floating-point precision",
        values=("1", "2", "4"),
        multi=False,
    )
    variant("tests", default=False, description="Build tests")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with when("+mpi"):
        depends_on("mpi")

    with when("+tests"):
        depends_on("catch2")

    def check(self):
        if self.spec.satisfies("~tests"):
            raise SkipTest("To run tests for QuEST you must enable the 'tests' variant!")
        super().check()

    def cmake_args(self):
        args = [
            # from variants
            self.define_from_variant("BUILD_EXAMPLES", "examples"),
            self.define_from_variant("ENABLE_DISTRIBUTION", "mpi"),
            self.define_from_variant("ENABLE_MULTITHREADING", "openmp"),
            self.define_from_variant("FLOAT_PRECISION", "precision"),
            self.define_from_variant("ENABLE_TESTING", "tests"),
            # others
            self.define("DOWNLOAD_CATCH2", False),  # don't use internal catch2
        ]

        if self.spec.satisfies("+cuda"):
            args.append(self.define("ENABLE_CUDA", True))

            targets = ";".join(self.spec.variants["cuda_arch"].value)
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", targets))

        if self.spec.satisfies("+rocm"):
            args.append(self.define("ENABLE_HIP", True))

            targets = ";".join(self.spec.variants["amdgpu_target"].value)
            args.append(self.define("CMAKE_HIP_ARCHITECTURES", targets))

        return args

    def patch(self):
        # remove extra 'quest' that is added to the install path
        filter_file(r'^cmake_path\(APPEND CMAKE_INSTALL_PREFIX "quest"\)$', "", "CMakeLists.txt")
