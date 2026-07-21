# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Yambo(AutotoolsPackage):
    """Yambo is a FORTRAN/C code for Many-Body calculations in solid
    state and molecular physics.
    """

    homepage = "https://www.yambo-code.org/index.php"
    url = "https://github.com/yambo-code/yambo/archive/4.2.2.tar.gz"

    maintainers("LydDeb")

    license("GPL-2.0-or-later")

    version("5.3.0", sha256="97b6867c28af6ea690bb02446745e817adcedf95bcd568f132ef3510abbb1cfe")
    version("5.2.4", sha256="7c3f2602389fc29a0d8570c2fe85fe3768d390cfcbb2d371e83e75c6c951d5fc")
    version("5.1.1", sha256="c85036ca60507e627c47b6c6aee8241830349e88110e1ce9132ef03ab2c4e9f6")

    with default_args(deprecated=True):
        version("5.2.3", sha256="a6168d1fa820af857ac51217bd6ad26dda4cc89c07e035bd7dc230038ae1ab9c")
        version("5.2.1", sha256="0ac362854313927d75bbf87be98ff58447f3805f79724c38dc79df07f03a7046")
        version("4.2.2", sha256="86b4ebe679387233266aba49948246c85a32b1e6840d024f162962bd0112448c")
        version("4.2.1", sha256="8ccd0ca75cc32d9266d4a37edd2a7396cf5038f3a68be07c0f0f77d1afc72bdc")
        version("4.2.0", sha256="9f78c4237ff363ff4e9ea5eeea671b6fff783d9a6078cc31b0b1abeb1f040f4d")

    variant("dp", default=False, description="Enable double precision")
    variant(
        "profile",
        values=any_combination_of("time", "memory"),
        description="Activate profiling of specific sections",
    )
    variant(
        "io",
        default="iotk",
        values=("iotk", "etsf-io"),
        multi=True,
        description="Activate support for different io formats",
    )
    # MPI + OpenMP parallelism
    variant("mpi", default=True, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("blas")
    depends_on("lapack")

    # MPI dependencies are forced, until we have proper forwarding of variants
    #
    # Note that yambo is used as an application, and not linked as a library,
    # thus there will be no case where another package pulls-in e.g.
    # netcdf-c+mpi and wants to depend on yambo~mpi.
    with when("+mpi"):
        depends_on("mpi")
        depends_on("scalapack")
        depends_on("netcdf-c+mpi")
        depends_on("hdf5+mpi")
        depends_on("fftw+mpi")

    with when("~mpi"):
        depends_on("netcdf-c~mpi")
        depends_on("hdf5~mpi")
        depends_on("fftw~mpi")

    depends_on("hdf5+fortran")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("libxc@2.0.3:5")

    depends_on("etsf-io", when="io=etsf-io")

    build_targets = ["all"]

    parallel = False

    sanity_check_is_file = ["bin/yambo"]

    resource(
        when="@5.2.4",
        name="ydriver",
        url="https://github.com/yambo-code/Ydriver/archive/refs/tags/1.4.2.tar.gz",
        sha256="c242f0700a224325ff59326767614a561b02ce16ddb2ce6c13ddd2d5901cc3e4",
        destination="lib/archive",
        placement={"1.4.2.tar.gz": "Ydriver-1.4.2.tar.gz"},
        expand=False,
    )
    resource(
        when="@5.2.1:5.2.3",
        name="ydriver",
        url="https://github.com/yambo-code/Ydriver/archive/refs/tags/1.2.0.tar.gz",
        sha256="0f29a44e9c4b49d3f6be3f159a7ef415932b2ae2f2fdba163af60a0673befe6e",
        destination="lib/archive",
        placement={"1.2.0.tar.gz": "Ydriver-1.2.0.tar.gz"},
        expand=False,
    )
    resource(
        when="@5.2:5.3",
        name="iotk",
        url="https://github.com/yambo-code/yambo-libraries/raw/0bb3a9c5d57fbad5a22ea2bb2e9c9e2fc04a7381/external/iotk-y1.2.2.tar.gz",
        sha256="64af6a4b98f3b62fcec603e4e1b00ef994f95a0efa53ab6593ebcfe6de1739ef",
        destination="lib/archive",
        placement={"iotk-y1.2.2.tar.gz": "iotk-y1.2.2.tar.gz"},
        expand=False,
    )

    def enable_or_disable_time(self, activated):
        return "--enable-time-profile" if activated else "--disable-time-profile"

    def enable_or_disable_memory(self, activated):
        return "--enable-memory-profile" if activated else "--disable-memory-profile"

    def enable_or_disable_openmp(self, activated):
        return "--enable-open-mp" if activated else "--disable-open-mp"

    def configure_args(self):
        spec = self.spec
        args = [
            f"--with-hdf5-path={spec['hdf5'].prefix}",
            f"--prefix={self.stage.source_path}",
            f"--exec-prefix={self.stage.source_path}",
            f"--with-blas-libs={spec['blas'].libs}",
            f"--with-lapack-libs={spec['lapack'].libs}",
            f"--with-netcdf-path={spec['netcdf-c'].prefix}",
            f"--with-netcdff-path={spec['netcdf-fortran'].prefix}",
            f"--with-fft-path={spec['fftw'].prefix}",
            f"--with-libxc-path={spec['libxc'].prefix}",
            "--enable-hdf5-p2y-support",
        ]
        # Double precision
        args.extend(self.enable_or_disable("dp"))

        # Application profiling
        args.extend(self.enable_or_disable("profile"))

        # MPI + threading
        args.extend(self.enable_or_disable("mpi"))
        args.extend(self.enable_or_disable("openmp"))

        if spec.satisfies("+mpi"):
            args.append(f"--with-scalapack-libs={spec['scalapack'].libs}")

        # iotk is always needed (lib/qe_pseudo uses it regardless of io variant)
        # io=iotk controls whether p2y is built / io=etsf-io adds etsf-io support
        args.extend(self.enable_or_disable("io"))

        if spec.satisfies("io=etsf-io"):
            args.append(f"--with-etsf-io-path={spec['etsf-io'].prefix}")

        return args

    # The configure in the package has the string 'cat config/report'
    # hard-coded, which causes a failure at configure time due to the
    # current working directory in Spack. Fix this by using the absolute
    # path to the file.
    @run_before("configure", when="@4.2.1")
    def filter_configure(self):
        report_abspath = join_path(self.build_directory, "config", "report")
        filter_file("config/report", report_abspath, "configure")

    @when("@4.2.1")
    def configure_args(self):
        args = [
            # As of version 4.2.1 there are hard-coded paths that make
            # the build process fail if the target prefix is not the
            # configure directory
            f"--prefix={self.stage.source_path}",
            "--disable-keep-objects",
            "--with-editor=none",
        ]
        spec = self.spec

        # Double precision
        args.extend(self.enable_or_disable("dp"))

        # Application profiling
        args.extend(self.enable_or_disable("profile"))

        # MPI + threading
        args.extend(self.enable_or_disable("mpi"))
        args.extend(self.enable_or_disable("openmp"))

        # LAPACK
        if spec.satisfies("+mpi"):
            args.append(
                "--with-scalapack-libs={0}".format(
                    spec["scalapack"].libs + spec["lapack"].libs + spec["blas"].libs
                )
            )

        args.extend(
            [f"--with-blas-libs={spec['blas'].libs}", f"--with-lapack-libs={spec['lapack'].libs}"]
        )

        # Netcdf
        args.extend(
            [
                "--enable-netcdf-hdf5",
                "--enable-hdf5-compression",
                f"--with-hdf5-libs={spec['hdf5'].libs}",
                f"--with-netcdf-path={spec['netcdf-c'].prefix}",
                f"--with-netcdff-path={spec['netcdf-fortran'].prefix}",
            ]
        )

        args.extend(self.enable_or_disable("io"))

        # Other dependencies
        args.append(f"--with-fft-path={spec['fftw'].prefix}")
        args.append(f"--with-libxc-path={spec['libxc'].prefix}")

        return args

    def install(self, spec, prefix):
        # yambo has no "make install"
        install_tree("bin", prefix.bin)
        install_tree("lib", prefix.lib)
        install_tree("include", prefix.include)
        install_tree("driver", prefix.driver)
