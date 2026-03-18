# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Aretomo2(MakefilePackage, CudaPackage):
    """AreTomo2 is a multi-GPU accelerated software package that fully automates
    motion-corrected marker-free tomographic alignment and reconstruction, now
    includes robust GPU-accelerated CTF (Contrast Transfer Function) estimation
    in a single package."""

    homepage = "https://github.com/czimaginginstitute/AreTomo2"
    url = "https://github.com/czimaginginstitute/AreTomo2/archive/refs/tags/v1.1.2.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("1.1.2", sha256="4cbb4d25d28778041d80ef2c598519b17b9a40aa84e1e99daf48ad5a90d946b4")

    depends_on("c", type="build")  # Not really, but CUDA does
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")

    conflicts("~cuda")
    conflicts("cuda_arch=none", when="+cuda", msg="A value for cuda_arch must be specified.")

    build_targets = ["exe"]

    patch("cuda_arch_makefile.patch")

    def edit(self, spec, prefix):
        cuda_arch = self.spec.variants["cuda_arch"].value
        cuda_gencode = " ".join(self.cuda_flags(cuda_arch))

        makefile = FileFilter("makefile")
        makefile.filter("NVCC = .*", "NVCC = nvcc -std=c++11")  # Let Spack handle the path
        makefile.filter("CUDAHOME = .*", f"CC = {self.spec['cuda'].prefix}")
        makefile.filter("CUDA_GENCODE =.*", f"CUDA_GENCODE = {cuda_gencode}")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("AreTomo2", prefix.bin)
