# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Aom(CMakePackage):
    """Alliance for Open Media AOM AV1 Codec Library"""

    homepage = "https://aomedia.googlesource.com/aom"
    git = "https://aomedia.googlesource.com/aom"

    license("BSD-2-Clause AND AOM-Patent-License-1.0", checked_by="tgamblin")

    version("3.12.1", tag="v3.12.1", commit="10aece4157eb79315da205f39e19bf6ab3ee30d0")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("nasm", type="build")

    def cmake_args(self):
        args = []
        args.append("-DBUILD_SHARED_LIBS=ON")
        return args
