# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage


class Aretomo3(MakefilePackage, CudaPackage):
    """AreTomo3 is a multi-GPU accelerated software package that enables
    real-time fully automated reconstruction of cryoET tomograms in parallel
    with cryoET data collection. Integrating MotionCor3, AreTomo2, and GCtfFind
    in a single application."""

    homepage = "https://github.com/czimaginginstitute/AreTomo3"
    url = "https://github.com/czimaginginstitute/AreTomo3/archive/refs/tags/v2.2.2.tar.gz"

    license("BSD-3-Clause")

    version("2.2.2", sha256="ee0a6bae8b541e1a1dd3465cf1e7d0bf4ee70b030662c55f2b583d678bb33fa9")
    version("2.1.3", sha256="1a57a861e2598e56a98b9c2c8dde326b72a58cfa83eb5f542366982acd6acf4d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    depends_on("cuda@11:", type=("build", "link"))
    depends_on("libtiff", type=("build", "link"))

    conflicts("~cuda")
    conflicts("cuda_arch=none", when="+cuda", msg="A value for cuda_arch must be specified.")

    build_targets = ["exe"]

    @property
    def build_directory(self):
        return self.stage.source_path

    def edit(self, spec, prefix):
        cuda = spec["cuda"]
        cuda_arch = spec.variants["cuda_arch"].value
        cuda_gencode = " ".join(self.cuda_flags(cuda_arch))
        stubs = cuda.prefix.lib64.stubs

        # Use makefile11 (for compute capability >= 6.x)
        makefile = FileFilter("makefile11")

        # Set CUDA paths
        makefile.filter(r"CUDAHOME = .*", f"CUDAHOME = {cuda.prefix}")

        # Use Spack's compiler wrappers
        makefile.filter(r"^CC = g\+\+ -std=c\+\+11", "CC = c++ -std=c++11")

        # Use nvcc directly
        makefile.filter(
            r"NVCC = \$\(CUDAHOME\)/bin/nvcc -std=c\+\+11",
            f"NVCC = {cuda.prefix}/bin/nvcc -std=c++11",
        )

        # Replace CUFLAG gencode block
        makefile.filter(
            r"CUFLAG = -Xptxas -dlcm=ca -O2 \\", f"CUFLAG = -Xptxas -dlcm=ca -O2 {cuda_gencode}"
        )
        # Remove all old gencode continuation lines
        makefile.filter(r"\s*-gencode arch=compute_\d+,code=sm_\d+.*", "")

        # Add libtiff and nvtx include/lib paths
        tiff = spec["libtiff"]
        makefile.filter(
            r"^CFLAG = -c -g -pthread -m64",
            f"CFLAG = -c -g -pthread -m64 -I{tiff.prefix.include} -I{cuda.prefix.include}",
        )
        makefile.filter(r"^CUFLAG = (.*)", f"CUFLAG = \\1 -I{tiff.prefix.include}")

        # Add stubs path for -lcuda (driver lib not in build container)
        makefile.filter("-lcuda", f"-L{stubs} -lcuda")

        # Fix hardcoded g++ in link line
        makefile.filter(r"\t@g\+\+ -g -pthread -m64 \$\(OBJS\)", "\t@c++ -g -pthread -m64 $(OBJS)")

    def build(self, spec, prefix):
        make("-f", "makefile11", "exe")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("AreTomo3", prefix.bin)
