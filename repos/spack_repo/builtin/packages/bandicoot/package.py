# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Bandicoot(CMakePackage, CudaPackage):
    """Bandicoot is a user-friendly C++ library for GPU accelerated
    linear algebra, integrating with CUDA and OpenCL."""

    homepage = "https://coot.sourceforge.io"
    url = "https://gitlab.com/bandicoot-lib/bandicoot-code/-/archive/3.1.0/bandicoot-code-3.1.0.tar.bz2"
    git = "https://gitlab.com/bandicoot-lib/bandicoot-code.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("3.1.0", sha256="27c8c6d36e6bbc64f4de0cfde89221f6d80a7d59de08c47666afeeacc806d1a5")

    variant("clblast", default=False, description="Enable CLBlast support")

    conflicts("~cuda ~clblast", msg="At least one backend must be enabled")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.6:", type="build")

    depends_on("opencl", when="+clblast")
    depends_on("clblast", when="+clblast")

    def cmake_args(self):
        args = [
            self.define_from_variant("FIND_OPENCL", "clblast"),
            self.define_from_variant("FIND_CLBLAST", "clblast"),
            self.define_from_variant("FIND_CUDA", "cuda"),
            self.define("FIND_CLBLAS", False),  # CLBlast is preferred over clBLAS
            self.define("BUILD_TESTS", self.run_tests),
        ]
        return args
