# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Abinit(AutotoolsPackage, CudaPackage, ROCmPackage):
    """ABINIT is a package whose main program allows one to find the total
    energy, charge density and electronic structure of systems made of
    electrons and nuclei (molecules and periodic solids) within
    Density Functional Theory (DFT), using pseudopotentials and a planewave
    or wavelet basis.

    ABINIT also includes options to optimize the geometry according to the
    DFT forces and stresses, or to perform molecular dynamics
    simulations using these forces, or to generate dynamical matrices,
    Born effective charges, and dielectric tensors, based on Density-Functional
    Perturbation Theory, and many more properties. Excited states can be
    computed within the Many-Body Perturbation Theory (the GW approximation and
    the Bethe-Salpeter equation), and Time-Dependent Density Functional Theory
    (for molecules). In addition to the main ABINIT code, different utility
    programs are provided.
    """

    homepage = "https://abinit.github.io/abinit_web/"
    url = "https://forge.abinit.org/abinit-10.0.9.tar.gz"
    license("Apache-2.0")

    maintainers("downloadico")
    version("10.6.5", sha256="9ae9b563137e08302d830a58a8bc3df2d8d0f78afeca2029b451636651d18f74")
    version("10.6.3", sha256="aceefc4289873097bb6b9dc4ec05efd897b9c052eb860746f6d778f4cd14317d")
    version("10.4.7", sha256="161c60ef90686c19e0718363eb5a17bfa29494e5fbdc59be45a7342e20349768")
    version("10.4.3", sha256="2150ac8472ad570f3cd3fa34c8bc6ac496c6715b319b69e3aa011a555d72d7d7")
    version("10.2.7", sha256="e0e1049b01b4ebaec29be632cd554caeccb4b2a8acf2e148c8ac505e6b226dc1")
    version("10.0.9", sha256="17650580295e07895f6c3c4b1f3f0fe0e0f3fea9bab5fd8ce7035b16a62f8e5e")
    version("10.0.7", sha256="a9fc044b33861b7defd50fafd19a73eb6f225e18ae30b23bc731d9c8009c881c")
    version("9.10.5", sha256="a9e0f0e058baa6088ea93d26ada369ccf0fe52dc9d4a865b1c38c20620148cd5")
    version("9.10.3", sha256="3f2a9aebbf1fee9855a09dd687f88d2317b8b8e04f97b2628ab96fb898dce49b")
    version("9.8.4", sha256="a086d5045f0093b432e6a044d5f71f7edf5a41a62d67b3677cb0751d330c564a")
    version("9.8.3", sha256="de823878aea2c20098f177524fbb4b60de9b1b5971b2e835ec244dfa3724589b")
    version("9.6.1", sha256="b6a12760fd728eb4aacca431ae12150609565bedbaa89763f219fcd869f79ac6")
    version("9.4.2", sha256="d40886f5c8b138bb4aa1ca05da23388eb70a682790cfe5020ecce4db1b1a76bc")
    version("8.10.3", sha256="ed626424b4472b93256622fbb9c7645fa3ffb693d4b444b07d488771ea7eaa75")
    version("8.10.2", sha256="4ee2e0329497bf16a9b2719fe0536cc50c5d5a07c65e18edaf15ba02251cbb73")
    version("8.8.2", sha256="15216703bd56a799a249a112b336d07d733627d3756487a4b1cb48ebb625c3e7")
    version("8.6.3", sha256="82e8d071088ab8dc1b3a24380e30b68c544685678314df1213180b449c84ca65")
    version("8.2.2", sha256="e43544a178d758b0deff3011c51ef7c957d7f2df2ce8543366d68016af9f3ea1")

    variant("mpi", default=True, description="Builds with MPI support. Requires MPI2+")
    variant("openmp", default=False, description="Enables OpenMP threads. Use threaded FFTW3")
    variant("scalapack", default=False, description="Enables scalapack support. Requires MPI")

    variant("wannier90", default=False, description="Enables the Wannier90 library")
    variant("libxml2", default=False, description="Enable libxml2 support, used by multibinit")
    variant(
        "gpu_openmp_offload",
        when="@10.4: +openmp",
        default=False,
        description="Enable OpenMP offload support. Requires CUDA & NVHPC or ROCM & Cray CE",
    )
    variant(
        "gpu_aware_mpi",
        when="@10.4: +mpi+gpu_openmp_offload",
        default=True,
        description="Enable optimizations for GPU-aware MPI",
    )
    variant(
        "gpu_markers",
        when="@10.4: +gpu_openmp_offload",
        default=False,
        description="Enable GPU markers, either NVTX for CUDA or rocTX for ROCM",
    )

    variant(
        "optimization-flavor",
        default="standard",
        multi=False,
        values=("safe", "standard", "aggressive"),
        description="Select the optimization flavor to use.",
    )

    variant("install-tests", default=False, description="Install test cases")

    # Add dependencies
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("atompaw", when="@:8")
    depends_on("blas")
    depends_on("lapack")

    # Require MPI2+
    depends_on("mpi@2:", when="+mpi")

    depends_on("scalapack", when="+scalapack+mpi")

    depends_on("fftw-api")

    depends_on("netcdf-fortran")

    # Need OpenMP threaded FFTW and BLAS libraries when configured
    # with OpenMP support
    with when("+openmp"):
        requires("^fftw+openmp", when="^[virtuals=fftw-api] fftw")
        requires("^amdfftw+openmp", when="^[virtuals=fftw-api] amdfftw")
        requires("^openblas threads=openmp", when="^[virtuals=blas] openblas")
        requires("^amdblis threads=openmp", when="^[virtuals=blas] amdblis")
        requires("^intel-oneapi-mkl threads=openmp", when="^[virtuals=blas] intel-oneapi-mkl")
        requires("^armpl-gcc threads=openmp", when="^[virtuals=blas] armpl-gcc")
        requires("^acfl threads=openmp", when="^[virtuals=blas] acfl")

    with when("+mpi"):
        depends_on("netcdf-c+mpi")
        depends_on("hdf5+mpi")
        depends_on("wannier90+shared", when="+wannier90")

    with when("~mpi"):
        depends_on("netcdf-c~mpi")
        depends_on("hdf5~mpi")
        # Cannot ask for +scalapack if it does not depend on MPI
        conflicts("+scalapack")
        # Cannot ask for +wannier90 if it does not depend on MPI
        conflicts("+wannier90")

    with when("+rocm"):
        depends_on("hipblas+rocm")
        depends_on("hipfft+rocm")
        depends_on("hipsolver+rocm")

    # Need a MPI provider built with either CUDA or ROCM when configured
    # with GPU-aware optimizations
    requires(
        "^cray-mpich +cuda",
        "^mpich +cuda",
        "^openmpi+cuda",
        when="+gpu_aware_mpi+cuda",
        policy="one_of",
        msg="'+gpu_aware_mpi +cuda' requires an MPI implementation with CUDA awareness enabled.",
    )

    requires(
        "^cray-mpich +rocm",
        "^mpich +rocm",
        "^openmpi +rocm",
        when="+gpu_aware_mpi+rocm",
        policy="one_of",
        msg="'+gpu_aware_mpi +rocm' requires an MPI implementation with ROCm awareness enabled.",
    )

    # constrain version of hdf5
    depends_on("hdf5@:1.8", when="@9:9.8")
    depends_on("hdf5@:1.14", when="@10:")

    # constrain libxc version
    depends_on("libxc")
    depends_on("libxc@:2", when="@:8")
    depends_on("libxc+kxc@5:", when="@9.4:")

    # libxml2
    depends_on("libxml2", when="@9:+libxml2")

    # If the Intel suite is used for Lapack, it must be used for fftw and vice-versa
    requires("^[virtuals=fftw-api] intel-oneapi-mkl", when="^[virtuals=lapack]   intel-oneapi-mkl")
    requires("^[virtuals=lapack]   intel-oneapi-mkl", when="^[virtuals=fftw-api] intel-oneapi-mkl")

    # libxml2 needs version 9 and above
    conflicts("+libxml2", when="@:8")

    conflicts("%gcc@7:", when="@:8.8")
    conflicts("%gcc@9:", when="@:8.10")

    conflicts("%nvhpc", when="@:9.8")
    conflicts("%cce", when="@:9.8")

    conflicts(
        "+gpu_openmp_offload",
        when="~mpi",
        msg="ABINIT builds with GPU support require MPI support enabled as well",
    )
    conflicts(
        "+cuda",
        when="~gpu_openmp_offload",
        msg="ABINIT builds with GPU support require OpenMP offload support enabled as well",
    )
    conflicts(
        "+rocm",
        when="~gpu_openmp_offload",
        msg="ABINIT builds with GPU support require OpenMP offload support enabled as well",
    )
    conflicts(
        "+cuda",
        when="~openmp",
        msg="ABINIT builds with GPU support require OpenMP support enabled as well",
    )
    conflicts(
        "+rocm",
        when="~openmp",
        msg="ABINIT builds with GPU support require OpenMP support enabled as well",
    )
    conflicts("cuda_arch=none", when="+cuda", msg="CUDA architecture is required")
    conflicts("amdgpu_target=none", when="+rocm", msg="ROCM architecture is required")

    requires(
        "%nvhpc",
        "%cce",
        when="+gpu_openmp_offload",
        policy="one_of",
        msg="ABINIT with OpenMP offload builds only with NVHPC or Cray CE",
    )
    requires(
        "+cuda",
        "+rocm",
        when="+gpu_openmp_offload",
        policy="one_of",
        msg="ABINIT with OpenMP offload builds only with CUDA or ROCM",
    )

    # propagate ROCm architecture when +rocm
    for arch in ROCmPackage.amdgpu_targets:
        depends_on("hipblas+rocm amdgpu_target=%s" % arch, when="+rocm amdgpu_target=%s" % arch)
        depends_on("hipfft+rocm amdgpu_target=%s" % arch, when="+rocm amdgpu_target=%s" % arch)
        depends_on("hipsolver+rocm amdgpu_target=%s" % arch, when="+rocm amdgpu_target=%s" % arch)

    # need openmp threading for abinit+openmp
    # TODO: The logic here can be reversed with the new concretizer. Instead of
    # using `conflicts`, `depends_on` could be used instead.
    for fftw in ["amdfftw", "cray-fftw", "fujitsu-fftw", "fftw"]:
        conflicts("+openmp", when=f"^{fftw}~openmp", msg=f"Need to request {fftw} +openmp")

    with when("+openmp"):
        requires("^intel-oneapi-mkl threads=openmp", when="^[virtuals=lapack] intel-oneapi-mkl")

    conflicts(
        "+openmp", when="^fujitsu-ssl2 ~parallel", msg="Need to request fujitsu-ssl2 +parallel"
    )

    conflicts(
        "~openmp", when="^fujitsu-ssl2 +parallel", msg="Need to request fujitsu-ssl2 ~parallel"
    )

    patch("rm_march_settings.patch", when="@:8")
    patch("rm_march_settings_v9.patch", when="@9")

    # Fix detection of Fujitsu compiler
    # Fix configure not to collect the option that causes an error
    # Fix intent(out) and unnecessary rewind to avoid compile error
    patch("fix_for_fujitsu.patch", when="@:8 %fj")
    patch("fix_for_fujitsu.v9.patch", when="@9: %fj")

    # Fix obsolete bool typedef (breaks in gcc@15)
    # Fixed since 10.4
    patch("fix_for_gcc15_stdbool.patch", when="@9:10.2.7 %gcc@15:")

    def configure_args(self):
        spec = self.spec
        options = self.with_or_without("libxml2")

        oapp = options.append
        if spec.satisfies("@:8"):
            oapp(f"--enable-optim={self.spec.variants['optimization-flavor'].value}")
        else:
            oapp(f"--with-optim-flavor={self.spec.variants['optimization-flavor'].value}")

        if spec.satisfies("+wannier90"):
            if spec.satisfies("@:8"):
                oapp(f"--with-wannier90-libs=-L{spec['wannier90'].prefix.lib} -lwannier -lm")
                oapp(f"--with-wannier90-incs=-I{spec['wannier90'].prefix.modules}")
                oapp(f"--with-wannier90-bins={spec['wannier90'].prefix.bin}")
                oapp("--enable-connectors")
                oapp("--with-dft-flavor=atompaw+libxc+wannier90")
            elif spec.satisfies("@:9.8"):
                options.extend(
                    [
                        f"WANNIER90_CPPFLAGS=-I{spec['wannier90'].prefix.modules}",
                        f"WANNIER90_LIBS=-L{spec['wannier90'].prefix.lib} -lwannier",
                    ]
                )
            else:
                options.extend(
                    [
                        f"WANNIER90_CPPFLAGS=-I{spec['wannier90'].prefix.modules}",
                        f"WANNIER90_LIBS=-L{spec['wannier90'].prefix.lib}",
                        "WANNIER90_LDFLAGS=-lwannier",
                    ]
                )
        else:
            if spec.satisfies("@:9.8"):
                oapp(f"--with-fftw={spec['fftw-api'].prefix}")
                oapp(f"--with-hdf5={spec['hdf5'].prefix}")

            if spec.satisfies("@:8"):
                oapp("--with-dft-flavor=atompaw+libxc")
            else:
                oapp("--without-wannier90")

        if spec.satisfies("+mpi"):
            oapp(f"CC={spec['mpi'].mpicc}")
            oapp(f"CXX={spec['mpi'].mpicxx}")
            oapp(f"FC={spec['mpi'].mpifc}")
            if spec.satisfies("@9.8:"):
                oapp(f"F90={spec['mpi'].mpifc}")

            # MPI version:
            # let the configure script auto-detect MPI support from mpi_prefix
            if spec.satisfies("@:8"):
                oapp("--enable-mpi=yes")
            else:
                oapp("--with-mpi")
        else:
            if spec.satisfies("@:8"):
                oapp("--enable-mpi=no")
            else:
                oapp("--without-mpi")

        # Activate OpenMP in Abinit Fortran code.
        if spec.satisfies("+openmp"):
            oapp("--enable-openmp=yes")
            if spec.satisfies("+gpu_openmp_offload"):
                oapp("--enable-openmp-offload=yes")
            else:
                oapp("--enable-openmp-offload=no")
        else:
            oapp("--enable-openmp=no")
            oapp("--enable-openmp-offload=no")

        if spec.satisfies("+cuda"):
            oapp(f"--with-cuda={spec['cuda'].prefix}")
            oapp(f"GPU_ARCH={self.spec.variants['cuda_arch'].value[0]}")

        if spec.satisfies("+rocm"):
            oapp(f"--with-rocm={spec['hip'].prefix}")
            oapp(f"GPU_ARCH={self.spec.variants['amdgpu_target'].value[0]}")

        if spec.satisfies("+gpu_aware_mpi"):
            oapp("--enable-mpi-gpu-aware=yes")

        if spec.satisfies("+gpu_markers"):
            oapp("--with-gpu-markers=yes")

        # BLAS/LAPACK/SCALAPACK-ELPA
        linalg = spec["lapack"].libs + spec["blas"].libs

        # linalg_flavor is selected using the virtual lapack provider
        is_using_intel_libraries = spec["lapack"].name == "intel-oneapi-mkl"

        # These *must* be elifs, otherwise spack's lapack provider is ignored
        # linalg_flavor ends up as "custom", which is not supported by abinit@9.10.3:
        if is_using_intel_libraries:
            linalg_flavor = "mkl"
        # Else, if spack's virtual "lapack" provider is openblas, use it:
        elif spec.satisfies("@9:") and (
            spec["lapack"].name == "openblas" or spec.satisfies("^fujitsu-ssl2")
        ):
            linalg_flavor = "openblas"
        # Cray wrapper will set flags for cray-libsci itself so "netlib" is alright here
        elif spec["lapack"].name == "cray-libsci":
            linalg_flavor = "netlib"
        else:
            # If you need to force custom (and not have it as fallback, like now)
            # you should likely implement a variant to force it, but it seems that
            # newer versions do not have it, so it should likely be a fallback:
            linalg_flavor = "custom"

        if spec.satisfies("+scalapack"):
            linalg = spec["scalapack"].libs + linalg
            if spec.satisfies("@:8"):
                linalg_flavor = f"scalapack+{linalg_flavor}"

        if spec.satisfies("@:8"):
            oapp(f"--with-linalg-libs={linalg.ld_flags}")
        else:
            oapp(f"LINALG_LIBS={linalg.ld_flags}")

        oapp(f"--with-linalg-flavor={linalg_flavor}")

        if is_using_intel_libraries:
            fftflavor = "dfti"
        else:
            if spec.satisfies("+openmp"):
                fftflavor, fftlibs = "fftw3-threads", "-lfftw3_omp -lfftw3 -lfftw3f"
            else:
                fftflavor, fftlibs = "fftw3", "-lfftw3 -lfftw3f"

        oapp(f"--with-fft-flavor={fftflavor}")

        if spec.satisfies("@:8"):
            if is_using_intel_libraries:
                oapp(f"--with-fft-incs={spec['fftw-api'].headers.cpp_flags}")
                oapp(f"--with-fft-libs={spec['fftw-api'].libs.ld_flags}")
            else:
                options.extend(
                    [
                        f"--with-fft-incs={spec['fftw-api'].headers.cpp_flags}",
                        f"--with-fft-libs=-L{spec['fftw-api'].prefix.lib} {fftlibs}",
                    ]
                )
        else:
            if is_using_intel_libraries:
                options.extend(
                    [
                        f"FFT_CPPFLAGS={spec['fftw-api'].headers.cpp_flags}",
                        f"FFT_LIBs={spec['fftw-api'].libs.ld_flags}",
                    ]
                )
            else:
                options.extend(
                    [
                        f"FFTW3_CPPFLAGS={spec['fftw-api'].headers.cpp_flags}",
                        f"FFTW3_LIBS=-L{spec['fftw-api'].prefix.lib} {fftlibs}",
                    ]
                )

        # LibXC library
        libxc = spec["libxc:fortran"]
        if spec.satisfies("@:8"):
            options.extend(
                [
                    f"--with-libxc-incs={libxc.headers.cpp_flags}",
                    f"--with-libxc-libs={libxc.libs.ld_flags + ' -lm'}",
                ]
            )
        else:
            oapp(f"--with-libxc={libxc.prefix}")

        # Netcdf4/HDF5
        hdf5 = spec["hdf5:hl"]
        netcdfc = spec["netcdf-c"]
        netcdff = spec["netcdf-fortran:shared"]
        if spec.satisfies("@:8"):
            oapp("--with-trio-flavor=netcdf")
            # Since version 8, Abinit started to use netcdf4 + hdf5 and we have
            # to link with the high level HDF5 library
            options.extend(
                [
                    "--with-netcdf-incs={}".format(
                        netcdfc.headers.cpp_flags + " " + netcdff.headers.cpp_flags
                    ),
                    "--with-netcdf-libs={}".format(
                        netcdff.libs.ld_flags + " " + hdf5.libs.ld_flags
                    ),
                ]
            )
        else:
            options.extend(
                [f"--with-netcdf={netcdfc.prefix}", f"--with-netcdf-fortran={netcdff.prefix}"]
            )

        if self.spec.satisfies("%fj"):
            oapp(f"FCFLAGS_MODDIR=-M{join_path(self.stage.source_path, 'src/mods')}")

        return options

    def check(self):
        """This method is called after the build phase if tests have been
        explicitly activated by user.
        """
        make("check")

        # the tests directly execute abinit. thus failing with MPI
        # TODO: run tests in tests/ via the builtin runtests.py
        #       requires Python with numpy, pyyaml, pandas
        if self.spec.satisfies("~mpi"):
            make("tests_in")

    # Abinit assumes the *old* behavior of HDF5 where the library flags to link
    # to the library were stored in the lib/libhdf5.settings file.
    # Spack already knows how to link to HDF5, disable this check in configure
    def patch(self):
        filter_file(
            r"sd_hdf5_libs_extra=.*",
            "sd_hdf5_libs_extra=%s" % self.spec["hdf5"].libs.ld_flags,
            "configure",
        )

    def install(self, spec, prefix):
        make("install")
        if spec.satisfies("+install-tests"):
            install_tree("tests", spec.prefix.tests)
