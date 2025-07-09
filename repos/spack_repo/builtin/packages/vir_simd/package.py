# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class VirSimd(CMakePackage):
    """A fallback std::experimental::simd (Parallelism TS 2) implementation with additional
    features."""

    homepage = "https://mattkretz.github.io/vir-simd/master/"
    url = "https://github.com/mattkretz/vir-simd/archive/refs/tags/v0.4.4.tar.gz"

    maintainers("ax3l", "mattkretz")

    license("LGPL-3.0-or-later", checked_by="ax3l")

    version("0.4.4", sha256="0d2953e1219798967b156aa392de6430099d85887770e5c81aefe8fb63e9464c")

    depends_on("cxx", type="build")
