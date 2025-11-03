# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class FastFloat(CMakePackage):
    """Fast and exact implementation of the C++ from_chars functions for number
    types."""

    homepage = "https://github.com/fastfloat/fast_float"
    url = "https://github.com/fastfloat/fast_float/archive/refs/tags/v6.1.4.tar.gz"

    license("Apache-2.0 OR BSL-1.0 OR MIT", checked_by="pranav-sivararamn")

    version("8.1.0", sha256="4bfabb5979716995090ce68dce83f88f99629bc17ae280eae79311c5340143e1")
    version("8.0.2", sha256="e14a33089712b681d74d94e2a11362643bd7d769ae8f7e7caefe955f57f7eacd")
    version("8.0.1", sha256="18f868f0117b359351f2886be669ce9cda9ea281e6bf0bcc020226c981cc3280")
    version("8.0.0", sha256="f312f2dc34c61e665f4b132c0307d6f70ad9420185fa831911bc24408acf625d")
    version("7.0.0", sha256="d2a08e722f461fe699ba61392cd29e6b23be013d0f56e50c7786d0954bffcb17")
    version("6.1.6", sha256="4458aae4b0eb55717968edda42987cabf5f7fc737aee8fede87a70035dba9ab0")
    version("6.1.5", sha256="597126ff5edc3ee59d502c210ded229401a30dafecb96a513135e9719fcad55f")
    version("6.1.4", sha256="12cb6d250824160ca16bcb9d51f0ca7693d0d10cb444f34f1093bc02acfce704")

    depends_on("cxx", type="build")
    depends_on("cmake@3.9:", type="build")

    depends_on("doctest", type="test")

    patch(
        "https://github.com/fastfloat/fast_float/commit/a7ed4e89c7444b5c8585453fc6d015c0efdf8654.patch?full_index=1",
        sha256="25561aa7db452da458fb0ae3075ef8e63ccab174ca8f5a6c79fb15cb342b3683",
        when="@:6.1.5",
    )

    def cmake_args(self):
        args = [self.define("FASTFLOAT_TEST", self.run_tests), self.define("SYSTEM_DOCTEST", True)]

        return args
