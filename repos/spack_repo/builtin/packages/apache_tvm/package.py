# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class ApacheTvm(CMakePackage, CudaPackage):
    """Apache TVM is an open source machine learning compiler framework for
    CPUs, GPUs, and machine learning accelerators. It aims to enable machine
    learning engineers to optimize and run computations efficiently on any
    hardware backend."""

    homepage = "https://tvm.apache.org/"

    license("Apache-2.0", checked_by="alex391")
    url = "https://github.com/apache/tvm/releases/download/v0.19.0/apache-tvm-src-v0.19.0.tar.gz"

    version("0.19.0", sha256="13fd707eae37b9b2b77bccd39668764f61ae6824d50cd1ab8164df1c75565be1")

    variant("llvm", default=True, description="Build with llvm for CPU codegen")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.18:", type="build")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("zlib-api", type=("link", "run"))
    depends_on("ncurses", type=("link", "run"))

    depends_on("llvm@4:", type="build", when="+llvm")

    depends_on("cuda@8:", when="+cuda")

    def cmake_args(self):
        return [
            self.define_from_variant("USE_CUDA", "cuda"),
            self.define_from_variant("USE_LLVM", "llvm"),
        ]
