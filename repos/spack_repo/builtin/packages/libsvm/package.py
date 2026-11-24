# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from glob import glob

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Libsvm(MakefilePackage):
    """Libsvm is a simple, easy-to-use, and efficient software for SVM
    classification and regression."""

    homepage = "https://www.csie.ntu.edu.tw/~cjlin/libsvm/"
    url = "https://github.com/cjlin1/libsvm/archive/v322.tar.gz"

    license("BSD-3-Clause")

    version("3.23", sha256="7a466f90f327a98f8ed1cb217570547bcb00077933d1619f3cb9e73518f38196")
    version("3.22", sha256="a3469436f795bb3f8b1e65ea761e14e5599ec7ee941c001d771c07b7da318ac6")

    version(
        "323",
        sha256="7a466f90f327a98f8ed1cb217570547bcb00077933d1619f3cb9e73518f38196",
        deprecated=True,
    )
    version(
        "322",
        sha256="a3469436f795bb3f8b1e65ea761e14e5599ec7ee941c001d771c07b7da318ac6",
        deprecated=True,
    )

    def url_for_version(self, version):
        return f"https://github.com/cjlin1/libsvm/archive/v{str(version).replace('.', '')}.tar.gz"

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def build(self, spec, prefix):
        make()
        make("lib")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.lib)
        mkdirp(prefix.include)
        mkdirp(prefix.lib.pkgconfig)

        install("svm-predict", prefix.bin)
        install("svm-scale", prefix.bin)
        install("svm-train", prefix.bin)
        install("svm.o", prefix.lib)
        install("svm.h", prefix.include)

        for libfile in glob("libsvm.so.*"):
            install(libfile, prefix.lib)

        ar = which("ar")
        ar("rcs", "libsvm.a", "svm.o")
        install("libsvm.a", prefix.lib)

        pc = join_path(prefix.lib.pkgconfig, "libsvm.pc")

        with open(pc, "w") as f:
            f.write(
                f"""\
    prefix={prefix}
    exec_prefix=${{prefix}}
    libdir=${{prefix}}/lib
    includedir=${{prefix}}/include

    Name: libsvm
    Description: LibSVM Support Vector Machines Library
    Version: {self.version}
    Libs: -L${{libdir}} -lsvm
    Cflags: -I${{includedir}}
    """
            )
