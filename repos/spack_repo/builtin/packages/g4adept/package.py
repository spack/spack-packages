# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class G4adept(CMakePackage, CudaPackage):
    """Accelerated demonstrator of electromagnetic Particle Transport"""

    homepage = "https://adept-project.readthedocs.io/"
    url = "https://github.com/apt-sim/AdePT/archive/refs/tags/v0.2.0.tar.gz"
    git = "https://github.com/apt-sim/AdePT.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("0.2.0", sha256="4075ebb652b17d6cf94b341fdc64df088ce9538b0aba433e413606d5cb51c618")

    variant("covfie", default=False, description="Use external B field from file via the covfie library")
    variant("examples", default=False, description="Build examples")
    variant("split_kernels", default=False, description="Run split version of the transport kernels")
    variant("surf", default=False, description="Enable surface model navigation on GPU")
    variant("mixed_precision", default=False, description="Use B-field integration and surface model in mixed precision")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.25.2:", type="build")

    depends_on("veccore@0.5.2: +cuda")
    depends_on("vecgeom +gdml")
    depends_on("xerces-c")
    depends_on("geant4")
    depends_on("g4vg@1.0.3:")
    depends_on("g4hepem +cuda")
    depends_on("hepmc3", type="test")

    depends_on("covfie", when="+covfie")

    conflicts("~cuda", msg="G4adept requires CUDA support")

    def cmake_args(self):
        args = [
            self.define("ADEPT_BUILD_TESTING", self.run_tests),
            self.define_from_variants("ADEPT_BUILD_EXAMPLES", "examples"),
            self.define_from_variant("ADEPT_USE_EXT_BFIELD", "covfie"),
            self.define_from_variant("ADEPT_USE_SPLIT_KERNELS", "split_kernels"),
            self.define_from_variant("ADEPT_USE_SURF", "surf"),
            self.define("ADEPT_USE_BUILTIN_G4VG", False),
        ]
        return args
