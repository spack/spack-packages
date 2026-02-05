# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SalmonTddft(CMakePackage):
    """SALMON is an open-source computer program for ab-initio
    quantum-mechanical calculations of electron dynamics at the nanoscale
    that takes place in various situations of light-matter interactions.
    It is based on time-dependent density functional theory, solving
    time-dependent Kohn-Sham equation in real time and real space
    with norm-conserving pseudopotentials."""

    homepage = "https://salmon-tddft.jp"
    git = "https://github.com/SALMON-TDDFT/SALMON2.git"

    maintainers("syamada0", "freifrauvonbleifrei")
    license("Apache-2.0")

    version("develop", branch="develop-2.0.0")
    version(
        "2.2.2",
        url="http://salmon-tddft.jp/download/SALMON-v.2.2.2.tar.gz",
        sha256="4ca2afe2f03a455b86bede014004765b3c2f494459dea8d66925f3b3743adde3",
    )
    version(
        "2.2.1",
        url="http://salmon-tddft.jp/download/SALMON-v.2.2.1.tar.gz",
        sha256="f665fc2541b2e664a82b39286ecc9a9ddaa9eb77640f31bcecf131bbb0efe2ba",
    )
    version(
        "2.2.0",
        url="http://salmon-tddft.jp/download/SALMON-v.2.2.0.tar.gz",
        sha256="b0b6eabad48f4547ae2a97f53771047ccb759b8c126ab0f1653b0e0f0d02a28b",
    )
    version(
        "2.1.0",
        url="http://salmon-tddft.jp/download/SALMON-v.2.1.0.tar.gz",
        sha256="18267818cdfa82ea762441e2d751abeff7b553c8ce92cabf5fb010248d2cfcbe",
    )
    version(
        "2.0.2",
        url="http://salmon-tddft.jp/download/SALMON-v.2.0.2.tar.gz",
        sha256="742007d3684a478199ba959ce135ad0020b70676a49f52a5e1dc25438123d50e",
    )
    version(
        "2.0.1",
        url="http://salmon-tddft.jp/download/SALMON-v.2.0.1.tar.gz",
        sha256="6fcd72ddd484a1d2b4700bbe5c1717fabb1e449288da3253d74b4a8ab24e7255",
    )
    version("2.0.0", sha256="c3bb80bc5d338cba21cd8f345acbf2f2d81ef75af069a0a0ddbdc0acf358456c")
    version("1.2.1", sha256="a5045149e49abe9dd9edefe00cd1508a1323081bc3d034632176b728effdbaeb")

    variant("cuda", default=False, description="Enable CUDA-based optimizations")
    variant("mpi", default=False, description="Enable MPI")
    variant("libxc", default=False, description="Enable libxc")
    variant("openacc", default=False, description="Enable OpenACC")
    variant("scalapack", default=False, description="Enable scalapack")
    variant("eigenexa", default=False, description="Enable eigenexa")
    variant(
        "manycore",
        default=False,
        description="Enable optimization of reduction for many-core processor",
    )
    variant(
        "current_processing",
        default=False,
        description="Enable preprocessing of the current computation in RT",
    )

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.14:", type="build")
    depends_on("mpi", type="link", when="+mpi")
    depends_on("scalapack", type="link", when="+scalapack")
    depends_on("eigenexa", type="link", when="+eigenexa")
    depends_on("lapack", type="link")
    depends_on("libxc", type="link", when="+libxc")
    depends_on("libxc@:4.9", type="link", when="@:1.9.9 +libxc")

    conflicts("+scalapack", when="~mpi")
    conflicts("+eigenexa", when="@:1.9.9")
    conflicts("+eigenexa", when="~scalapack")
    conflicts("+manycore", when="@2.0.0:")
    conflicts("+current_processing", when="@2.0.0:")
    conflicts("+cuda", when="~openacc")

    requires("%nvhpc", when="+cuda")

    patch("fjmpi.patch", when="@2.0.0 %fj")
    patch("v2.0.libxc-5.0.patch", when="@2.0.0 +libxc")
    patch("cmakefix.patch", when="+scalapack")

    def cmake_args(self):
        define_from_variant = self.define_from_variant
        spec = self.spec
        define = self.define
        args = [
            define_from_variant("USE_SCALAPACK", "scalapack"),
            define_from_variant("USE_EIGENEXA", "eigenexa"),
            define_from_variant("USE_MPI", "mpi"),
            define_from_variant("USE_LIBXC", "libxc"),
            define_from_variant("REDUCE_FOR_MANYCORE", "manycore"),
            define_from_variant("CURRENT_PREPROCESSING", "current_processing"),
        ]
        if spec.satisfies("+mpi"):
            args.extend(
                [
                    define("CMAKE_C_COMPILER", spec["mpi"].mpicc),
                    define("CMAKE_Fortran_COMPILER", spec["mpi"].mpifc),
                ]
            )
        if spec.satisfies("+scalapack"):
            math_libs = spec["scalapack"].libs + spec["lapack"].libs + spec["blas"].libs
            if spec.satisfies("@2.0:"):
                args.append(define("ScaLAPACK_VENDOR_FLAGS", math_libs.ld_flags))
            else:
                args.extend(
                    [
                        define("BLACS_LINKER_FLAGS", math_libs.ld_flags),
                        define("BLACS_LIBRARIES", math_libs.libraries),
                        define("ScaLAPACK_LINKER_FLAGS", math_libs.ld_flags),
                        define("ScaLAPACK_LIBRARIES", math_libs.libraries),
                    ]
                )
        if "%nvhpc" in spec:
            if "+openacc" in spec:
                if "+cuda" in spec:
                    args.append(define("CMAKE_TOOLCHAIN_FILE", "nvhpc-openacc-cuda"))
                else:
                    args.append(define("CMAKE_TOOLCHAIN_FILE", "nvhpc-openacc"))
            else:
                args.append(define("CMAKE_TOOLCHAIN_FILE", "nvhpc-openmp"))
        elif "%fj" in spec:  # TODO add toolchain files if necessary
            args.append(self.define("CMAKE_Fortran_MODDIR_FLAG", "-M"))

        if spec.satisfies("^fujitsu-mpi"):
            args.append(define("USE_FJMPI", True))
        else:
            args.append(define("USE_FJMPI", False))
        return args

    def flag_handler(self, name, flags):
        flags = list(flags)
        if name == "fflags":
            if self.spec.satisfies("%gcc"):
                flags.append("-ffree-line-length-none")
            if self.spec.satisfies("%gcc@10:"):
                flags.append("-fallow-argument-mismatch")
        return (None, None, flags)
