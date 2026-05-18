# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class G4hepem(CMakePackage, CudaPackage):
    """Geant4 EM physics simulation R&D project looking for solutions
    to reduce the computing performance bottleneck experienced by
    HEP detector simulation applications."""

    homepage = "https://github.com/mnovak42/g4hepem"
    url = "https://github.com/mnovak42/g4hepem/archive/refs/tags/20251114.tar.gz"
    git = "https://github.com/mnovak42/g4hepem.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("20251114", sha256="d1bf94fd9403043f0c5f3b8bb6d9b79d6108f07c19d8b7403de0acd66774f8af")

    variant(
        "early_tracking_exit", default=False, description="Enable user-defined early tracking exit"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.17:", type="build")

    depends_on("geant4@10.6:")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", self.run_tests),
            self.define("CMAKE_CXX_STANDARD", self.spec["geant4"].variants["cxxstd"].value),
            self.define("G4HepEm_GEANT4_BUILD", True),
            self.define_from_variant("G4HepEm_CUDA_BUILD", "cuda"),
            self.define_from_variant("G4HepEm_EARLY_TRACKING_EXIT", "early_tracking_exit"),
        ]
        if self.spec.satisfies("+cuda"):
            args.append(CMakeBuilder.define_cuda_architectures(self))
        return args
