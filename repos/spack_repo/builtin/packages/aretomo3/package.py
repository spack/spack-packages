# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Aretomo3(MakefilePackage, CudaPackage):
    """AreTomo3 is a multi-GPU accelerated software package that enables
    real-time fully automated reconstruction of cryoET tomograms in parallel
    with cryoET data collection. Integrating MotionCor3, AreTomo2, and GCtfFind
    in a single application."""

    homepage = "https://github.com/czimaginginstitute/AreTomo3"
    url = "https://github.com/czimaginginstitute/AreTomo3/archive/refs/tags/v2.2.2.tar.gz"
    git = "https://github.com/czimaginginstitute/AreTomo3.git"

    license("BSD-3-Clause")

    version("main", branch="main")
    version("2.2.2", sha256="ee0a6bae8b541e1a1dd3465cf1e7d0bf4ee70b030662c55f2b583d678bb33fa9")
    version("2.1.3", sha256="1a57a861e2598e56a98b9c2c8dde326b72a58cfa83eb5f542366982acd6acf4d")

    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    depends_on("cuda@12:", type=("build", "link"))
    depends_on("libtiff", type=("build", "link"))

    conflicts("~cuda")
    conflicts("cuda_arch=none", when="+cuda", msg="A value for cuda_arch must be specified.")
    conflicts("^cuda@13:", when="@:2", msg="CUDA 13+ requires @main (makefile13 not in releases)")

    @property
    def _makefile_name(self):
        """Select makefile based on CUDA version."""
        if self.spec.satisfies("^cuda@13:"):
            return "makefile13"
        return "makefile11"

    @property
    def build_directory(self):
        return self.stage.source_path

    def edit(self, spec, prefix):
        cuda = spec["cuda"]
        cuda_arch = spec.variants["cuda_arch"].value
        cuda_gencode = " ".join(self.cuda_flags(cuda_arch))
        stubs = cuda.prefix.lib64.stubs
        tiff = spec["libtiff"]
        makefile = FileFilter(self._makefile_name)

        # Set CUDA paths
        makefile.filter(r"^CUDAHOME = .*", f"CUDAHOME = {cuda.prefix}")

        # Use Spack's compiler wrappers
        makefile.filter(r"^CC = g\+\+", "CC = c++")

        # Use nvcc directly
        makefile.filter(r"^NVCC = \$\(CUDAHOME\)/bin/nvcc", f"NVCC = {cuda.prefix}/bin/nvcc")

        # Replace CUFLAG gencode block
        makefile.filter(
            r"^CUFLAG = -Xptxas -dlcm=ca -O2 \\", f"CUFLAG = -Xptxas -dlcm=ca -O2 {cuda_gencode}"
        )
        # Remove all old gencode continuation lines
        makefile.filter(r"^\s+-gencode arch=compute_\d+,code=sm_\d+.*", "")

        # Add libtiff include to CFLAG
        makefile.filter(
            r"^CFLAG = -c -g -pthread -m64", f"CFLAG = -c -g -pthread -m64 -I{tiff.prefix.include}"
        )

        # Add stubs path for -lcuda (driver lib not in build container)
        makefile.filter(r"-L\$\(CUDALIB\)/stubs", f"-L{stubs}")

        # Fix hardcoded g++ in link line
        makefile.filter(r"@g\+\+ ", "@c++ ")

        # Add libtiff link flags
        makefile.filter(r"-ltiff", f"-L{tiff.prefix.lib} -ltiff")

    def build(self, spec, prefix):
        make("-f", self._makefile_name, "exe")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("AreTomo3", prefix.bin)
