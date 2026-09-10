# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Apfelxx(CMakePackage):
    """APFEL++ is a C++ rewriting of the Fortran 77 code APFEL
    originally conceived to evolve collinear parton
    distribution functions (PDFs)."""

    homepage = "https://github.com/vbertone/apfelxx"
    url = "https://github.com/vbertone/apfelxx/archive/refs/tags/4.8.0.tar.gz"
    git = "https://github.com/vbertone/apfelxx.git"

    tags = ["hep"]

    maintainers("wdconinc")

    license("GPL-3.0", checked_by="wdconinc")

    version("4.10.0", sha256="bff51f56f36c9fa8a2e9b35a87847e7f061d532ba15c8e7f151ad344e4aa2f3f")

    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.10:", type="build")

    depends_on("lhapdf")
    depends_on("yaml-cpp")
    depends_on("py-pybind11")
