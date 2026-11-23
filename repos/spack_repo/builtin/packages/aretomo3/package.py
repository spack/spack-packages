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
    # Upstream stopped tagging after v2.2.2, so newer versions are pinned by commit.
    version("2.3.3", commit="6b4d6b38e0f1bec7ca2344badeaa795665a38b7f")
    version(
        "2.2.2",
        sha256="ee0a6bae8b541e1a1dd3465cf1e7d0bf4ee70b030662c55f2b583d678bb33fa9",
    )
    version(
        "2.1.3",
        sha256="1a57a861e2598e56a98b9c2c8dde326b72a58cfa83eb5f542366982acd6acf4d",
    )

    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    depends_on("cuda@12:", type=("build", "link"))
    depends_on("libtiff", type=("build", "link"))

    conflicts("~cuda")
    conflicts("cuda_arch=none", when="+cuda", msg="A value for cuda_arch must be specified.")
    conflicts(
        "^cuda@13:",
        when="@:2.2",
        msg="CUDA 13+ requires @2.3: (makefile13 not in older releases)",
    )
    # LibSrc/Lib ships prebuilt x86-64 static libraries
    requires("target=x86_64:", msg="AreTomo3 links prebuilt x86-64 libraries")

    @property
    def _makefile_name(self):
        """Select makefile based on version and CUDA version.

        Tagged releases only ship makefile11. From 2.3 on, makefile11 is stale
        (it omits sources that are needed), so use makefile12 or makefile13.
        """
        if self.spec.satisfies("@:2.2"):
            return "makefile11"
        if self.spec.satisfies("^cuda@13:"):
            return "makefile13"
        return "makefile12"

    @property
    def build_directory(self):
        return self.stage.source_path

    def edit(self, spec, prefix):
        cuda = spec["cuda"]
        tiff = spec["libtiff"]
        cuda_arch = spec.variants["cuda_arch"].value
        cuda_gencode = " ".join(self.cuda_flags(cuda_arch))
        stubs = cuda.prefix.lib64.stubs
        makefile = FileFilter(self._makefile_name)

        # makefile12 at 2.3.3 still lists this source, deleted in that version.
        # Only the path is removed so the line continuation stays intact.
        if spec.satisfies("@2.3.3:"):
            makefile.filter(r"\./AreTomo/PatchAlign/GRandom2D\.cu", "")

        # Set CUDA paths
        makefile.filter(r"^CUDAHOME = .*", f"CUDAHOME = {cuda.prefix}")

        # Use Spack's compiler wrappers
        makefile.filter(r"^CC = g\+\+", "CC = c++")

        # nvcc also does the final link, so its host compiler must be Spack's wrapper:
        # the real compiler adds no RPATHs to cuda and libtiff.
        makefile.filter(
            r"^NVCC = \$\(CUDAHOME\)/bin/nvcc",
            f"NVCC = {cuda.prefix}/bin/nvcc -ccbin {spack_cxx}",
        )

        # Replace CUFLAG gencode block
        makefile.filter(
            r"^CUFLAG = -Xptxas -dlcm=ca -O2 \\",
            f"CUFLAG = -Xptxas -dlcm=ca -O2 -I{tiff.prefix.include} {cuda_gencode}",
        )
        # Remove all old gencode continuation lines
        makefile.filter(r"^\s+-gencode arch=compute_\d+,code=sm_\d+.*", "")

        # Add libtiff include to CFLAG
        makefile.filter(
            r"^CFLAG = -c -g -pthread -m64",
            f"CFLAG = -c -g -pthread -m64 -I{tiff.prefix.include}",
        )

        # Add stubs path for -lcuda (driver lib not in build container)
        makefile.filter(
            r"-L\$\(CUDALIB\)/stubs",
            f"-L{stubs}",
        )

        # Add libtiff link flags
        makefile.filter(
            r"-ltiff",
            f"{tiff.libs.search_flags} -ltiff",
        )

    def build(self, spec, prefix):
        make("-f", self._makefile_name, "exe")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("AreTomo3", prefix.bin)
