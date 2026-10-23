# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Ldak(Package):
    """LDAK is a software package for analyzing GWAS data"""

    homepage = "https://dougspeed.com/ldak/"
    url = "https://dougspeed.com/wp-content/uploads/source.zip"
    git = "https://github.com/dougspeed/LDAK.git"

    maintainers("snehring")

    license("GPL-3.0-only")

    version("7.01", commit="6572adccc93e85a66bb7648e46af21a5638467bf")
    version("5.2", sha256="ba3de4eb4f2d664b3c2a54bef2eb66d1a498ac423179e97a5795d010161b1805")

    variant("glpk", default=False, description="Use glpk instead of vendored qsopt")
    variant("glpk", default=True, description="Use glpk instead of vendored qsopt", when="@7.01:")

    depends_on("c", type="build")

    depends_on("zlib-api")
    depends_on("blas")
    depends_on("lapack")
    depends_on("openblas threads=openmp", when="^[virtuals=blas] openblas")
    depends_on("intel-oneapi-mkl threads=openmp", when="^[virtuals=blas] intel-oneapi-mkl")
    depends_on("glpk", when="+glpk")
    depends_on("zstd", when="@7.01:")
    depends_on("suite-sparse", when="@7.01:")

    requires("target=x86_64:", when="~glpk", msg="bundled qsopt is only for x86_64")
    requires(
        "^[virtuals=lapack] openblas",
        "^[virtuals=lapack] intel-oneapi-mkl",
        policy="one_of",
        msg="Only mkl or openblas are supported for blas/lapack with ldak",
    )

    phases = ["build", "install"]

    def build(self, spec, prefix):
        libs = [
            "-lm",
            (self.spec["lapack"].libs + self.spec["blas"].libs).link_flags,
            self.spec["zlib-api"].libs.link_flags,
        ]
        includes = [
            (self.spec["lapack"].headers + self.spec["blas"].headers).include_flags,
            self.spec["zlib-api"].headers.include_flags,
        ]
        defines = []

        source_path = self.stage.source_path
        if self.spec.satisfies("@7.01:"):
            source_path = join_path(source_path, "Source_Code")

        if self.spec.satisfies("~glpk"):
            if self.spec.satisfies("platform=darwin"):
                libs.append("libqsopt.mac.a")
            else:
                # bundled qsopt is not position independent
                libs.append(["libqsopt.linux.a", "-no-pie"])
            defines.append("-DMET=0")
        else:
            includes.append(self.spec["glpk"].headers.include_flags)
            libs.append(self.spec["glpk"].libs.link_flags)
            defines.append("-DMET=1")

        if self.spec.satisfies("@7.01:"):
            defines.append("-DVQTL=1")
            includes.append(self.spec["suite-sparse"].headers.include_flags)
            libs.extend(self.spec["suite-sparse"].libs.link_flags.split())

        with working_dir(source_path):
            if self.spec.satisfies("^mkl"):
                if self.spec.satisfies("@5.2"):
                    filter_file("#define MKL.*", "#define MKL 1", "ldak.c")
                defines.append("-DMKL=1")
            if self.spec.satisfies("^openblas"):
                if self.spec.satisfies("@5.2"):
                    filter_file("#define MKL.*", "#define MKL 2", "ldak.c")
                filter_file("#if MKL==2", "#if MKL==2\n#include <cblas.h>\n", "ldak.c")
                filter_file("#include <blis.h>", "", "ldak.c", string=True)
                filter_file(
                    "bli_thread_set_num_threads(maxthreads);", "", "defaults.c", string=True
                )
                defines.append("-DMKL=2")
            if self.spec.satisfies("+glpk"):
                if self.spec.satisfies("@5.2"):
                    filter_file("#define MET.*", "#define MET 1", "ldak.c")
                    filter_file(r"weights\[", "tally3[", "weightfuns.c")
                filter_file('#include"glpk.h"', "#include<glpk.h>", "ldak.c")
            if self.spec.satisfies("@7.01:"):
                libs.append(self.spec["zstd"].libs.link_flags)
                includes.append(self.spec["zstd"].headers.include_flags)
            cc = Executable(spack_cc)
            args = ["ldak.c", "-std=gnu17", self.compiler.openmp_flag, "-O3", "-o", "ldak"]
            args += defines + includes + libs
            cc(*args)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        source_path = self.stage.source_path
        if self.spec.satisfies("@7.01:"):
            source_path = join_path(source_path, "Source_Code")
        with working_dir(source_path):
            install("ldak", prefix.bin.ldak)
