# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install dolfinx-mpc
#
# You can edit this file again by typing:
#
#     spack edit dolfinx-mpc
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class DolfinxMpc(CMakePackage):
    """Extension of fenics-dolfinx for multipoint constraints."""

    homepage = "https://www.jsdokken.com/dolfinx_mpc"
    url = "https://github.com/jorgensd/dolfinx_mpc/archive/v0.9.3.tar.gz"

    maintainers("jorgensd")

    license("MIT", checked_by="jorgensd")

    version(
        "0.9.3",
        sha256="efa312cc498e428aab44acccc9bb0c74c200eda005742de7778c8e68fa84e8df",
    )
    version(
        "0.9.2",
        sha256="8681def964aef0101b7e35aa377cfbcc4b220a20cfc540ec9058b324031b58c2",
    )
    version(
        "0.9.1",
        sha256="2d0c3583b8d69ad4374b0938cd157c9ca48acf50d6969e51ccce8ab14625040e",
    )
    version(
        "0.9.0",
        sha256="9b87cd75e3b26b3f92b600e935c45677624c8e169782bf6646265d1e03a0e043",
    )
    version(
        "0.8.1",
        sha256="e0254b4a1c9c1456583c1415821946b11b0b2e48dbfee6558da2bbedfe78b461",
    )
    version(
        "0.8.0.post1",
        sha256="bb4803af8bfe53366237dc27dc06085699d5e68e2ffd8098e54614ff207683a8",
    )
    version(
        "0.8.0.post0",
        sha256="c413c866ba27e02233af4954c819583615d53394ef336c78f137284a63f850b1",
    )
    version(
        "0.8.0",
        sha256="4c77ce49b28b04974205f62dc04d5324168f8d2275f6ee4d7fa24aa4e0ac2eaa",
    )
    version(
        "0.7.2",
        sha256="decf73dac8688ed235b8ee357b763d80a0d477110f35757117c1de649930c71a",
    )
    version(
        "0.7.1",
        sha256="eb9595adac26213c731fac53be361f8f4b9e22bd4ba611101b326958949ac9b9",
    )

    # HDF5 dependency requires C in CMake
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("fenics-dolfinx@main+petsc", when="@main")
    depends_on("fenics-dolfinx@0.9+petsc", when="@0.9")
    depends_on("fenics-dolfinx@0.8+petsc", when="@0.8")
    depends_on("fenics-dolfinx@0.7+petsc", when="@0.7")

    depends_on("cmake@3.21:", when="@0.9:", type="build")
    depends_on("cmake@3.19:", when="@:0.8", type="build")

    conflicts(
        "%gcc@:9.10", msg="fenics-dolfinx requires GCC-10 or newer for C++20 support"
    )
    conflicts(
        "%clang@:9.10",
        msg="fenics-dolfinx requires Clang-10 or newer for C++20 support",
    )

    root_cmakelists_dir = "cpp"
