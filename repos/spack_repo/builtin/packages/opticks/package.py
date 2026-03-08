# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Opticks(CMakePackage, CudaPackage):
    """GPU Optical Photon Simulation using NVIDIA OptiX ray tracing
    and integrated with Geant4 simulation."""

    homepage = "https://simoncblyth.github.io/opticks/"
    url = "https://github.com/simoncblyth/opticks/archive/refs/tags/v0.5.6.tar.gz"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("0.5.6", sha256="caa269d1876e5e0be1ea879ce3d200d9a2910ebc8a3b01eda46840d924227691")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.5:", type="build")

    depends_on("assimp")
    depends_on("geant4")
    depends_on("glm")
    depends_on("glew")
    depends_on("glfw")
    depends_on("imgui")
    depends_on("nlohmann-json")
    depends_on("plog")
    depends_on("xerces-c")
    depends_on("optix-dev")

    conflicts("~cuda", msg="Opticks requires CUDA")
    conflicts("cuda_arch=none", when="+cuda", msg="Opticks requires a cuda_arch value")

    def setup_build_environment(self, env):
        cuda_arch = self.spec.variants["cuda_arch"].value
        env.set("OPTICKS_PREFIX", self.prefix)
        env.set("OPTICKS_CUDA_PREFIX", self.spec["cuda"].prefix)
        env.set("OPTICKS_OPTIX_PREFIX", self.spec["optix-dev"].prefix)
        env.set("OPTICKS_COMPUTE_CAPABILITY", cuda_arch)

    def cmake_args(self):
        args = []
        return args
