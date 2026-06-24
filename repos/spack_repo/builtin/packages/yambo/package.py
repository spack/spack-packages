# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Yambo(AutotoolsPackage, CudaPackage):
    """YAMBO is an open-source code released within the GPL licence.

    YAMBO implements Many-Body Perturbation Theory (MBPT) methods
    such as GW and BSE, and Time-Dependent Density Functional Theory
    (TDDFT), allowing accurate predictions of fundamental properties
    such as band gaps, band alignments, defect quasi-particle energies,
    optical properties, and out-of-equilibrium properties of materials.
    """

    homepage = "http://www.yambo-code.eu"
    url = "https://github.com/yambo-code/yambo/archive/5.3.0.tar.gz"
    git = "https://github.com/yambo-code/yambo.git"

    maintainers("nicspalla", "LydDeb")

    license("GPL-2.0-or-later")

    version("5.3.0", sha256="97b6867c28af6ea690bb02446745e817adcedf95bcd568f132ef3510abbb1cfe")
    version("5.2.4", sha256="7c3f2602389fc29a0d8570c2fe85fe3768d390cfcbb2d371e83e75c6c951d5fc")
    version("5.1.4", sha256="f2dfa1b4cb6a28bd54efb56a9333f51e6da9bd248d92ca3f6e945cb9ac9fe82c")

    with default_args(deprecated=True):
        version("5.2.3", sha256="a6168d1fa820af857ac51217bd6ad26dda4cc89c07e035bd7dc230038ae1ab9c")
        version("5.2.2", sha256="2ddd6356830ce9302e304b7627cff3aa973846cf893f91742b4390d0b53d63d4")
        version("5.2.1", sha256="0ac362854313927d75bbf87be98ff58447f3805f79724c38dc79df07f03a7046")
        version("5.2.0", sha256="88fd6de5c9be49b8af89a2634b3c2da6db5a614eff8e19a7ec5c48ef12bafc8b")
        version("5.1.3", sha256="eb12297990030e785a58db6b9c9f0e34809eb2f095082e0aeca89eeaaf14ff37")
        version("5.1.2", sha256="9625d8a96bd9a3ff3713ebe53228d5ac9be0a98adecbe2a2bad67234c0e26a2e")
        version("5.1.1", sha256="c85036ca60507e627c47b6c6aee8241830349e88110e1ce9132ef03ab2c4e9f6")
        version("5.0.4", sha256="1841ded51cc31a4293fa79252d7ce893d998acea7ccc836e321c3edba19eae8a")
        version("5.0.3", sha256="7a5a5f3939bdb6438a3f41a3d26fff0ea6f77339e4daf6a5d850cf2a51da4414")
        version("5.0.2", sha256="a2cc0f880dd915b47efa0d5dd88cb94edffbebaff37a252183efb9e23dbd3fab")
        version("5.0.1", sha256="bbdbd08f7219d575a0f479ff05dac1f1a7b25f7e20f2165abf1b2cf28aedae92")
        version("5.0.0", sha256="b1cbc0b3805538f892b2b8691901c4cc794e75e056a4bd9ad9cf585899cf0aa9")
        version("4.5.3", sha256="04f89b5445d35443325c071784376c7b5c25cc900d1fdcc92971a441f8c05985")
        version("4.5.2", sha256="0b4f8b82c1d37fce472228bdffb6f6f44b86104d170677a5d55e77a2db832cf0")
        version("4.5.1", sha256="6ef202535e38f334a69bd75bd24ff8403b0a4c6b8c60a28b69d4b1c5808aeff5")
        version("4.5.0", sha256="c68b2c79acc31b3d48e7edb46e4049c1108d60feee80bf4fcdc4afe4b12b6928")
        version("4.4.1", sha256="2daf80f394a861301a9bbad559aaf58de283ce60395c9875e9f7d7fa57fcf16d")
        version("4.3.3", sha256="790fa1147044c7f33f0e8d336ccb48089b48d5b894c956779f543e0c7e77de19")

    patch(
        "s_psi.patch",
        sha256="44e6a2850143976fccb6a79f68d77267473f26ddd4846a1c5b92a58c02d92b39",
        when="@:5.1.99 %gcc@12.0.0:",
    )
    patch(
        "cuda_runtime.patch",
        sha256="2f4d07a02929d9d866e5c5bf537e18ff3605089147035929e029fcdc3a933b0c",
        when="@5.3.0+cuda",
    )
    patch(
        "yambo-5-petsc-slepc-3.23.patch",
        sha256="5361808d4aef593c9728a1ae172978a17c3546d94cd837f2beffa32e8da460b4",
        when="@5.3.0",
    )

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("tar", type="build")

    variant("mpi", default=True, description="Enable MPI support")
    variant("openmp", default=True, description="Enable OpenMP support")
    variant("slepc", default=False, description="Activate support for SLEPc and PETSc")
    variant("dp", default=False, description="Enable double precision")
    variant("time", default=False, description="Activate time profiling of specific sections")
    variant("memory", default=False, description="Activate memory profiling of specific sections")
    variant("ph", default=False, description="Compile Electron-phonon coupling executables")
    variant("rt", default=False, description="Compile Real-time dynamics executables")
    variant("sc", default=False, description="Compile Self-consistent project executables")
    variant("nl", default=False, description="Compile Non-linear optics executables")

    conflicts(
        "%oneapi", when="@:5.2.4", msg="oneapi compilation supported only from version 5.3.0"
    )

    with when("+mpi"):
        variant(
            "scalapack",
            default=False,
            description="Activate parallel linear algebra with ScaLAPACK",
        )
        variant(
            "parallel_io",
            default=True,
            when="@4.4.0:",
            description="Activate HDF5 parallel I/O",
        )
        depends_on("mpi")

    depends_on("blas")
    depends_on("lapack")

    with when("+scalapack"):
        depends_on("scalapack")

    conflicts("+scalapack", when="~mpi", msg="Parallel linear algebra available only with +mpi")

    with when("+slepc"):
        depends_on("petsc+complex~superlu-dist~hypre~metis")
        depends_on("petsc+mpi", when="+mpi")
        depends_on("petsc~mpi", when="~mpi")
        depends_on("petsc+double", when="+dp")
        depends_on("petsc~double", when="~dp")
        depends_on("petsc~cuda", when="@:5.2.0")
        depends_on("petsc@:3.20", when="@:5.2.4")
        depends_on("petsc@:3.24", when="@5.3.0")
        depends_on("slepc~arpack")
        depends_on("slepc~cuda", when="@:5.2.0")
    conflicts(
        "+slepc",
        when="@:5.1.4 %nvhpc",
        msg="SLEPc support not available with this version of Yambo and nvhpc compiler.",
    )

    depends_on("fftw-api@3")
    depends_on("fftw+mpi", when="+mpi ^[virtuals=fftw-api] fftw")
    depends_on("fftw~mpi", when="~mpi ^[virtuals=fftw-api] fftw")

    with when("+parallel_io"):
        depends_on("hdf5+fortran+hl+mpi")
        depends_on("netcdf-c+mpi")

    with when("~parallel_io"):
        depends_on("hdf5+fortran+hl~mpi")
        depends_on("netcdf-c~mpi")

    depends_on("netcdf-fortran")

    conflicts("hdf5+mpi", when="@:4.4.0", msg="Parallel I/O available from version 4.4.1")

    depends_on("libxc@2.0.3:3.0.0~cuda", when="@:5.0")
    depends_on("libxc@5.0.0:6.2.2~cuda", when="@5.1.0:")

    with when("+cuda"):
        conflicts("@:4.5.3", msg="CUDA Fortran available only from version 5.0.0")
        requires("%nvhpc", msg="CUDA-Fortran support available only with NVIDIA compilers")

    with when("@5.3.0:"):
        depends_on("devicexlib ~cuda-fortran~openacc~openmp5~openmp", when="~cuda~openmp")
        depends_on("devicexlib ~cuda-fortran~openacc~openmp5+openmp", when="~cuda+openmp")
        depends_on("devicexlib +cuda-fortran+cuda", when="+cuda")

    with when("+openmp"):
        depends_on("openblas threads=openmp", when="^[virtuals=lapack] openblas")
        depends_on("intel-oneapi-mkl threads=openmp", when="^[virtuals=lapack] intel-oneapi-mkl")
        depends_on("fftw+openmp", when="^[virtuals=fftw-api] fftw")
        depends_on("petsc+openmp", when="^[virtuals=petsc] petsc")

    resource(
        name="iotk",
        url="https://github.com/yambo-code/yambo-libraries/raw/master/external/iotk-y1.2.2.tar.gz",
        sha256="64af6a4b98f3b62fcec603e4e1b00ef994f95a0efa53ab6593ebcfe6de1739ef",
        placement={"iotk-y1.2.2.tar.gz": "lib/archive/iotk-y1.2.2.tar.gz"},
        expand=False,
    )

    resource(
        name="Ydriver",
        url="https://github.com/yambo-code/yambo-libraries/archive/0.0.1.tar.gz",
        sha256="5cfaacde4716e5eb7729a6032adc82d403f377ac4b501ed9d64a7c20644e3375",
        placement={"0.0.1.tar.gz": "lib/archive/0.0.1.tar.gz"},
        when="@5.0",
        expand=False,
    )
    resource(
        name="Ydriver",
        url="https://github.com/yambo-code/yambo-libraries/raw/master/external/Ydriver-1.1.0.tar.gz",
        sha256="6c316d613f5a41ddd15efad7ba97e4712f87d7e56c073ba5458caf424afcb97a",
        placement={"Ydriver-1.1.0.tar.gz": "lib/archive/Ydriver-1.1.0.tar.gz"},
        when="@5.1",
        expand=False,
    )
    resource(
        name="Ydriver",
        url="https://github.com/yambo-code/Ydriver/archive/refs/tags/1.2.0.tar.gz",
        sha256="0f29a44e9c4b49d3f6be3f159a7ef415932b2ae2f2fdba163af60a0673befe6e",
        placement={"1.2.0.tar.gz": "lib/archive/Ydriver-1.2.0.tar.gz"},
        when="@5.2.0:5.2.3",
        expand=False,
    )
    resource(
        name="Ydriver",
        url="https://github.com/yambo-code/Ydriver/archive/refs/tags/1.4.2.tar.gz",
        sha256="c242f0700a224325ff59326767614a561b02ce16ddb2ce6c13ddd2d5901cc3e4",
        placement={"1.4.2.tar.gz": "lib/archive/Ydriver-1.4.2.tar.gz"},
        when="@5.2.4",
        expand=False,
    )

    sanity_check_is_file = ["bin/yambo", "bin/ypp", "bin/a2y", "bin/c2y", "bin/p2y"]

    @property
    def build_targets(self):
        spec = self.spec

        if spec.satisfies("+ph", "+rt", "+sc", "+nl"):
            return ["all"]

        targets = ["core"]

        if spec.satisfies("+ph"):
            targets.append("ph-project")
        if spec.satisfies("+rt"):
            targets.append("rt-project")
        if spec.satisfies("+sc"):
            targets.append("sc-project")
        if spec.satisfies("+nl"):
            targets.append("nl-project")

        return targets

    @run_before("configure")
    def filter_configure(self):
        report_abspath = join_path(self.build_directory, "config", "report")
        filter_file("cat config/report", f"cat {report_abspath}", "configure")

        filter_file(
            "#include <petsc/finclude/petscvec.h90>",
            "#include <petsc/finclude/petscvec.h>",
            "configure",
        )

        filter_file(".+try_HDF5_LIBS=..h5pfc -show .+", "#", "configure")
        filter_file(".+try_hdf5_incdir=..h5pfc -show .+", "#", "configure")
        filter_file(".+try_HDF5_LIBS=..h5fc -show .+", "#", "configure")
        filter_file(".+try_hdf5_incdir=..h5fc -show .+", "#", "configure")

    @run_before("configure")
    def filter_linking_issue(self):
        spec = self.spec

        if "@5.1.2:" in spec and "%intel-oneapi-compilers" in spec:
            filter_file(
                'libs="-lint_modules $libs $llocal $lPLA $lIO $lextlibs -lm"',
                r'libs="-lint_modules $libs $llocal $lSL $lPLA $lIO $lextlibs -lm"',
                "sbin/compilation/libraries.sh",
                string=True,
            )
            filter_file(
                "$libs $llocal",
                r"-Wl,--start-group $libs $llocal",
                "sbin/compilation/libraries.sh",
                string=True,
            )
            filter_file(
                "$lextlibs",
                r"$lextlibs -Wl,--end-group",
                "sbin/compilation/libraries.sh",
                string=True,
            )
            filter_file(
                'libs=" "',
                'libs=" -l_Y_tddft "',
                "sbin/compilation/libraries.sh",
                string=True,
            )

    @run_before("configure")
    def filter_time(self):
        spec = self.spec

        if "+time" in spec and "@5.0.0:" in spec:
            filter_file(
                "total_time(i_c)<600.",
                "total_time(i_c)<604800.",
                "src/timing/TIMING_clock_write.F",
                string=True,
            )
            filter_file(
                "ch='            [Time-Profile]: '//trim(time_string(total_time))",
                "write (ch,'(a,f11.4,a)') '            [Time-Profile]: ',total_time,'s'",
                "src/modules/mod_timing.F",
                string=True,
            )

    @run_before("configure")
    def filter_makev1(self):
        spec = self.spec
        if "@:5.1.4" in spec:
            filter_file(
                "$(MAKE) $(MAKEFLAGS) -f Makefile.loc all ;",
                "$(MAKE) -f Makefile.loc $(MAKEFLAGS) all ;",
                "config/mk/global/functions/get_libraries.mk",
                string=True,
            )
            filter_file(
                "$(MAKE) $(MAKEFLAGS) -f Makefile.loc $$LIB2DO ;",
                "$(MAKE) -f Makefile.loc $(MAKEFLAGS) $$LIB2DO ;",
                "config/mk/global/functions/get_libraries.mk",
                string=True,
            )

    def enable_or_disable_time(self, activated):
        return "--enable-time-profile" if activated else "--disable-time-profile"

    def enable_or_disable_memory(self, activated):
        return "--enable-memory-profile" if activated else "--disable-memory-profile"

    def enable_or_disable_openmp(self, activated):
        return "--enable-open-mp" if activated else "--disable-open-mp"

    def enable_or_disable_parallel_io(self, activated):
        return "--enable-hdf5-par-io" if activated else "--disable-hdf5-par-io"

    def setup_build_environment(self, env):
        spec = self.spec

        if "%c=nvhpc" in spec:
            env.set("CPP", "cpp -E -P")
        if "%fortran=nvhpc" in spec:
            env.set("FPP", "nvfortran -Mpreprocess -E")
            env.set("F90SUFFIX", ".f90")
        if "%c=intel" in spec:
            env.set("CPP", "icc -E -ansi")
        if "%fortran=intel" in spec:
            env.set("FPP", "ifort -E -free -P")
        if "%c=oneapi" in spec:
            env.set("CPP", "icx -E -ansi")
        if "%fortran=oneapi" in spec:
            env.set("FPP", "ifx -E -free -P")

    def flag_handler(self, name, flags):
        if name == "cflags":
            if self.spec.satisfies("%gcc") and self.spec.satisfies("@:5.1.4"):
                flags.extend(
                    [
                        "-Wno-error=implicit-function-declaration",
                        "-Wno-error=deprecated-declarations",
                    ]
                )
        if name == "fcflags":
            if self.spec.satisfies("%gcc@9:") and self.spec.satisfies("@:4.5.3"):
                flags.extend(
                    [
                        "-fallow-argument-mismatch",
                    ]
                )

        return (flags, None, None)

    def configure_args(self):
        spec = self.spec

        args = [
            "--enable-msgs-comps",
            "--disable-keep-objects",
            "--with-editor=none",
            "--enable-keep-src",
            f"--prefix={self.stage.source_path}",
        ]

        args.extend(self.enable_or_disable("dp"))
        args.extend(self.enable_or_disable("time"))
        args.extend(self.enable_or_disable("memory"))
        args.extend(self.enable_or_disable("mpi"))
        args.extend(self.enable_or_disable("openmp"))

        mkl_lines = {
            "intel": "-lmkl_intel_lp64 -lmkl_sequential -lmkl_core",
            "intel_thr": "-lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -liomp5",
            "gcc": "-Wl,--no-as-needed -lmkl_gf_lp64 -lmkl_sequential -lmkl_core",
            "gcc_thr": "-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -lgomp",
            "nvhpc": "-lmkl_intel_lp64 -lmkl_sequential -lmkl_core",
            "nvhpc_thr": "-lmkl_intel_lp64 -lmkl_pgi_thread -lmkl_core -pgf90libs -mp",
        }

        if "mkl" in spec or "intel-oneapi-mkl" in spec:
            mkl_line = f"-L{env['MKLROOT']}/lib/intel64 "

            if "%oneapi" in spec or "%intel" in spec:
                comp = "intel"
            elif "%gcc" in spec:
                comp = "gcc"
            elif "%nvhpc" in spec:
                comp = "nvhpc"

            if "+openmp" in spec:
                comp += "_thr"

            mkl_line += mkl_lines[comp]
            mkl_line += " -lpthread -lm -ldl"

            args.append(f"--with-blas-libs={mkl_line}")
            args.append(f"--with-lapack-libs={mkl_line}")
            args.extend(
                [
                    f"--with-fft-libs={mkl_line}",
                    f"--with-fft-includedir={env['MKLROOT']}/include/fftw",
                ]
            )
        else:
            args.extend(
                [
                    f"--with-blas-libs={spec['blas'].libs}",
                    f"--with-lapack-libs={spec['lapack'].libs}",
                    f"--with-fft-path={spec['fftw-api'].prefix}",
                ]
            )

        if "+scalapack" in spec:
            args.append("--enable-par-linalg")

            if ("mkl" in spec or "intel-oneapi-mkl" in spec) and "netlib-scalapack" not in spec:
                args.extend(
                    [
                        f"--with-blacs-libs=-L{env['MKLROOT']}/lib/intel64 "
                        "-lmkl_blacs_intelmpi_lp64",
                        f"--with-scalapack-libs=-L{env['MKLROOT']}/lib/intel64 "
                        "-lmkl_scalapack_lp64",
                    ]
                )
            else:
                args.extend(
                    [
                        f"--with-blacs-libs={spec['scalapack'].libs}",
                        f"--with-scalapack-libs={spec['scalapack'].libs}",
                    ]
                )

        if "+slepc" in spec:
            args.extend(
                [
                    "--enable-slepc-linalg",
                    f"--with-petsc-path={spec['petsc'].prefix}",
                    f"--with-slepc-path={spec['slepc'].prefix}",
                ]
            )

        args.extend(
            [
                f"--with-netcdf-path={spec['netcdf-c'].prefix}",
                f"--with-netcdff-path={spec['netcdf-fortran'].prefix}",
                f"--with-hdf5-path={spec['hdf5'].prefix}",
            ]
        )

        if "@4.4.0:" in spec:
            args.extend(self.enable_or_disable("parallel_io"))

        args.append(f"--with-libxc-path={spec['libxc'].prefix}")

        if "@5.3.0:" in spec:
            args.append(f"--with-devxlib-path={spec['devicexlib'].home}")

        if "+cuda" in spec:
            cuda_arch = spec.variants["cuda_arch"].value[0]
            if "@5.3.0:" in spec:
                args.append("--enable-cuda-fortran")
                args.append(f"--with-cuda-cc={cuda_arch}")
            else:
                args.append(f"--enable-cuda=cc{cuda_arch}")

        return args

    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)

    def build(self, spec, prefix):
        if spec.satisfies("%nvhpc") and spec.compiler.version >= Version("24.11"):
            config_file = join_path(self.stage.source_path, "config", "setup")

            filter_file(r"-Mcuda=([^,\s]+),([^,\s]+)", r"-cuda -gpu=\1,\2", config_file)
            filter_file(
                r"-Mcudalib=([^,\s][^,\s]*(?:,[^,\s]+)*)",
                r"-cudalib=\1",
                config_file,
            )
            filter_file(r"-Mcuda=([^,\s]+)", r"-cuda -gpu=\1", config_file)
            filter_file(
                r"-Mcudalib=([^,\s][^,\s]*(?:,[^,\s]+)*)",
                r"-cudalib=\1",
                config_file,
            )

        super().build(spec, prefix)
