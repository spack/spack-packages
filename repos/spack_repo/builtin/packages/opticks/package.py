# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Opticks(CMakePackage, CudaPackage):
    """GPU-Accelerated Optical Photon Simulation using NVIDIA OptiX"""

    homepage = "https://github.com/bnlnpps/eic-opticks"
    git = "https://github.com/bnlnpps/eic-opticks.git"

    license("Apache-2.0")

    maintainers("plexoos")

    version("main", branch="main")

    depends_on("cxx", type="build")
    depends_on("cmake@3.10:", type="build")

    depends_on("geant4@11.1.2")
    depends_on("glew")
    depends_on("glfw")
    depends_on("glm")
    depends_on("glu")
    depends_on("nlohmann-json")
    depends_on("mesa")
    depends_on("optix-dev@7.7")
    depends_on("openssl")
    depends_on("plog")
    depends_on("python")
