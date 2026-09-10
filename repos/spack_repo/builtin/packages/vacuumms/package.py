# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Vacuumms(CMakePackage):
    """VACUUMMS: (Void Analysis Codes and Unix-like Utilities for Molecular Modeling and
    Simulation) is a collection of research codes for the compuational analysis of
    free volume in molecular structures, including the generation of code for the
    production of high quality ray-traced images and videos. Note that production of the
    images from the generated code is considered post-processing and requires POVRay
    and feh (on X11 systems) as post-processing dependencies. VACUUMMS has been tested
    under Linux on x86_64 and ARM64. Python and JuPyter support are available from 1.3.0
    via the C++ API and library and are now the recommended way to use VACUUMMS. Command
    Line Utilities are still available. Please submit questions, pull requests, and bug
    reports via github. Cite: https://dl.acm.org/doi/abs/10.1145/2335755.2335826"""

    homepage = "https://github.com/VACUUMMS/VACUUMMS"
    url = "https://github.com/VACUUMMS/VACUUMMS/archive/refs/tags/v1.0.0.tar.gz"
    git = "https://github.com/VACUUMMS/VACUUMMS.git"

    maintainers("frankwillmore")

    license("MIT")

    # This is the main branch, for the latest functionality
    version("develop", branch="develop")
    version("1.3.0", tag="1.3.0")
    variant("test", default=True, description="enable CMake testing")
    variant("tiff", default=True, description="Build TIFF utilities")
    variant("cuda", default=False, description="Build CUDA applications and utilities")
    variant("python", default=True, description="Build python bindings")
    variant("variational", default=False, description="Build VARIATIONAL module")
    variant("voronoi", default=False, description="Build VORONOI applications and utilities")
    variant(
        "VOROPP_HOME",
        default="/opt/voropp",
        description="voro++ location",
        multi=False,
        when="+voronoi",
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("voropp", type=("link", "run"), when="+voronoi")
    depends_on("libtiff", type=("link", "run"), when="+tiff")
    depends_on("cuda", type=("link", "run"), when="+cuda")
    depends_on("python", type=("link", "run"), when="+python")
    depends_on("py-pybind11", type=("link", "run"), when="+python")
    depends_on("libx11", type=("link", "run"))
    depends_on("libxext", type=("link", "run"))
    depends_on("libsm", type=("link", "run"))
    depends_on("libice", type=("link", "run"))

    def cmake_args(self):
        return [
            self.define_from_variant("ENABLE_TESTING", "test"),
            self.define_from_variant("BUILD_CUDA_COMPONENTS", "cuda"),
            self.define_from_variant("BUILD_TIFF_UTILS", "tiff"),
            self.define_from_variant("BUILD_VARIATIONAL_MODULE", "variational"),
            self.define_from_variant("BUILD_VORONOI_UTILS", "voronoi"),
            self.define_from_variant("VOROPP_HOME", "VOROPP_HOME"),
        ]

    def setup_run_environment(self, env):
        if "+python" in self.spec:
            env.prepend_path("PYTHONPATH", self.prefix.lib)
