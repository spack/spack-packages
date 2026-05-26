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

    homepage = "https://gitlab.desy.de/millepede/millepede-ii"
    url = "https://gitlab.desy.de/millepede/millepede-ii/-/archive/V05-00-00/millepede-ii-V05-00-00.tar.gz"
    git = "https://gitlab.desy.de/millepede/millepede-ii.git"

    license("LGPL-2.0-only")

    version("main", branch="main")
    version("05-01-03", sha256="18f707a1b372f07420e26969f503518b6dd067642f5eab45f05728aa7ff742ec")
    version("05-01-02", sha256="fd7991487682e8b28cac6a036b905fedc19ec0ac9e26fd85e2514b22a75e3343")
    version("05-01-01", sha256="b6a316e4b1ebf93cbf72ddd57a157e09f4446e4677352ef288748731ac2c0297")
    version("05-01-00", sha256="fec88805d33004f9ca03733dc14f7b30f888cd3a48e3cdf4333d74b42242d3d3")
    version("05-00-00", sha256="df8ffb2ffae3c4f32177824026f79ed3b824536f5ef581643aaae09da308aca6")
    version(
        "04-13-03",
        sha256="669a6e46a6f02ba3c78b2760e2ffb2c90d25b582ccd1a5c0770eef81c7bcbbe9",
        deprecated=True,
    )
    version(
        "04-11-01",
        sha256="9869eb84d8d07cecfab15c396f3faa36aef10906e39f8641c48b58e0325b3205",
        deprecated=True,
    )

    # Fix LAPACK handling
    patch(
        "https://gitlab.desy.de/millepede/millepede-ii/-/merge_requests/48.diff",
        sha256="4b151e220012b53bf3ae2c82cd5f736df870b2332e7cfdec60ce13e6788af86a",
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
    requires("%gcc", msg="Millepede hardcodes gcc/g++/gfortran")

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

        if "~mkl" in self.spec:  # ← only for OpenBLAS
            libs = self.spec["openblas"].libs.joined()
            args += [self.define("BLAS_LIBRARIES", libs), self.define("LAPACK_LIBRARIES", libs)]

        return args
