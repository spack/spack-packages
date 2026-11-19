# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefileBuilder, MakefilePackage

from spack.package import *


class Millepede(MakefilePackage, CMakePackage):
    """Millepede II is a package for linear least squares fits
    with a large number of parameters. Developed for the
    alignment and calibration of tracking detectors."""

    build_system(
        conditional("cmake", when="@5:"), conditional("makefile", when="@:4"), default="cmake"
    )

    homepage = "https://github.com/millepede-project/millepede-ii"
    url = "https://github.com/millepede-project/millepede-ii/archive/refs/tags/V05-00-00.tar.gz"
    git = "https://github.com/millepede-project/millepede-ii.git"

    license("LGPL-2.0-only")

    version("main", branch="main")
    version("05-01-08", sha256="8b409e7f45fbe1dc7aa6ce574983919f813d25aac5dd1129cac07fbec9d6a9ff")
    version("05-01-07", sha256="25ad3d9a7f951e58668189cd063f5e3c5b3099af7697c8a58c0427c1c19769d1")
    version("05-01-06", sha256="d9570fbdb0fce44a12c6bf5db41e8c734777acf2019f7d8381fb9ad55e2da1de")
    version("05-01-05", sha256="037bbfcd3aca2d6497a5609f35bc4a96258d285290996468241dcedd9aa9d172")
    version("05-01-04", sha256="035fd1eefb1c564c63e362efb288688e41db367add1f2be240c3c3119d273690")
    version("05-01-03", sha256="edc32b7ab9001471819e359789b378787c79c605a54d00d986078f5b7efb9491")
    version("05-01-02", sha256="bef40f38840cd8b3139e5631fc7f21705279abb0c913ff2fa345f73f55b3ebca")
    version("05-01-01", sha256="cb1dbb11170688365fcdfcf44da8602cadc9268c11936930b26cf6b75fbae02f")
    version("05-01-00", sha256="21aed50c06dffa2ced705c4012f4c7ac7851b144154470153500aef48e083e36")
    version("05-00-00", sha256="1d78bfcc40fe4b87001e3445c90f62c1b70959e2582ef1b20cac9f0947b81add")
    version(
        "04-13-03",
        sha256="4b2c38a1bbfba2cbc40073eb9bdc9430e0ac5f6b0801b3efafdf1a0b1d4670a8",
        deprecated=True,
    )
    version(
        "04-11-01",
        sha256="fa98a6616b35ead7b838b7db412ed6be82b733320396f0e511c767c91030e195",
        deprecated=True,
    )

    # Fix LAPACK handling
    patch(
        "https://github.com/millepede-project/millepede-ii/compare/"
        "2726f54142c6c3bd0911250e14fceb7174a0deff...8088a7d373e01c224da018f06203da27e22cae32.diff",
        sha256="bc8547ff70c27884648ebe7b2a6819ccbdf3a7f7707691220c561a246ec9933b",
        when="@5.0.0",
    )

    variant("zlib", default=True, description="Enable zlib support")
    variant("root", default=False, description="Enable ROOT support")
    variant("openmp", default=True, description="Enable OpenMP support")
    variant("mkl", default=False, description="Use MKL as LAPACK backend instead of OpenBLAS")
    variant("pardiso", default=False, description="Enable Intel oneMKL PARDISO sparse solver")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    requires("%gcc", msg="Millepede hardcodes gcc/g++/gfortran", when="@:05-01-03")

    depends_on("zlib-api", when="+zlib")

    depends_on("mille")
    depends_on("mille +root", when="+root")
    depends_on("mille +zlib", when="+zlib")

    depends_on("openblas +ilp64", when="~mkl")
    depends_on("intel-oneapi-mkl", when="+mkl")

    conflicts("+pardiso ~mkl", msg="PARDISO requires the MKL backend (+mkl)")

    _cxxstd_values = ["17", "20", "23"]
    variant(
        "cxxstd",
        default="20",
        values=_cxxstd_values,
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    for cxxstd in _cxxstd_values:
        depends_on(f"root cxxstd={cxxstd}", when=f"+root cxxstd={cxxstd}")


class MakefileBuilder(MakefileBuilder):
    def install(self, spec, prefix):
        make("install", "PREFIX=" + prefix)


class CMakeBuilder(CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define("LAPACK_OPENBLAS", self.spec.satisfies("~mkl")),
            self.define("LAPACK_MKL", self.spec.satisfies("+mkl")),
            self.define_from_variant("SUPPORT_ZLIB", "zlib"),
            self.define_from_variant("SUPPORT_ROOT", "root"),
            self.define_from_variant("SUPPORT_OPENMP", "openmp"),
            self.define_from_variant("PARDISO", "pardiso"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ]

        if "~mkl" in self.spec:  # only for OpenBLAS
            libs = self.spec["openblas"].libs.joined()
            args += [self.define("BLAS_LIBRARIES", libs), self.define("LAPACK_LIBRARIES", libs)]

        return args
