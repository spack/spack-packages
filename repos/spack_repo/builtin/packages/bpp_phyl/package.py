# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class BppPhyl(CMakePackage):
    """Bio++ phylogeny library."""

    homepage = "http://biopp.univ-montp2.fr/wiki/index.php/Installation"
    url = "https://github.com/BioPP/bpp-phyl/archive/refs/tags/v2.4.1.tar.gz"

    maintainers("snehring")

    license("CECILL-2.0")

    version("2.4.1", sha256="e7bf7d4570f756b7773904ffa600ffcd77c965553ddb5cbc252092d1da962ff2")

    depends_on("cxx", type="build")  # generated

    depends_on("cmake@2.6:", type="build")
    depends_on("bpp-core")
    depends_on("bpp-seq")

    # Clarify isnan's namespace, because Fujitsu compiler can't
    # resolve ambiguous of 'isnan' function.
    patch("clarify_isnan.patch", when="%fj")

    def cmake_args(self):
        return ["-DBUILD_TESTING=FALSE"]
