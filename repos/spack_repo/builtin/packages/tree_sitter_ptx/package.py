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
#     spack install tree-sitter-ptx
#
# You can edit this file again by typing:
#
#     spack edit tree-sitter-ptx
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class TreeSitterPtx(CMakePackage):
    """tree-sitter-ptx is a highlight-grade formal grammar for NVIDIA PTX, used
    with the tree-sitter parser generator."""

    homepage = "https://github.com/JuliaGPU/tree-sitter-ptx"
    url = "https://github.com/JuliaGPU/tree-sitter-ptx/tarball/a993c54d2c60a943b8c6bcfe0972ea1d9633f314"

    supplier = "Tim Besard at JuliaGPU"

    maintainers("guanyuming-he")

    license("MIT", checked_by="guanyuming-he")

    version("993c54d2c60a943b8c6bcfe0972ea1d9633f314",
         sha256="7f6d7ec802c1342135087d0d0af8a9bfabff7d2e836fc5ed9a2b5de934a0883f",
         extension="tar.gz")

    depends_on("tree-sitter")
    depends_on("c", type="build")
    depends_on("cmake@3.13:", type="build")

