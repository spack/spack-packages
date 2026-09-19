# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mpif(CMakePackage):
    """Fortran bindings for MPI, given any C implementation of MPI.

    mpif implements the Fortran bindings of MPI 5.0 -- mpif.h, use mpi and
    use mpi_f08 -- on top of the C MPI ABI, which the MPI 5.0 standard defines
    for C only. One mpif build therefore works with any MPI implementing that
    ABI, and which implementation runs is decided by the dynamic loader rather
    than at compile time.

    This package provides the mpi virtual: mpif supplies the Fortran half and
    mpi-abi-wrapper, which it depends on, the C half. Spack does not let one
    package both provide and consume the mpi virtual, so the two halves are
    separate packages and this one, holding the Fortran bindings, is the
    provider a dependent sees.
    """

    test_requires_compiler = True

    homepage = "https://github.com/eschnett/mpif"
    url = "https://github.com/eschnett/mpif/archive/refs/tags/v1.0.1.tar.gz"
    git = "https://github.com/eschnett/mpif.git"

    maintainers("eschnett")

    license("MIT", checked_by="eschnett")

    version("main", branch="main")
    version("1.0.1", sha256="ef99da4f566ce531042653b97ce4e2cb9feeecd1639fcf973c24f2e7f669e6a3")
    version("1.0.0", sha256="b83bc74b3ca857d542f684e1c048aa8bcc2abed7f4bb34d815926f0c4bd4db0a")

    variant("shared", default=True, description="Build a shared version of the library")
    variant(
        "cfi",
        default=True,
        description="Use TS 29113 assumed-rank choice buffers in mpi_f08 where "
        "the toolchain supports them",
    )

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.13:", type="build")

    # Named concretely rather than through a virtual for "any MPI providing the
    # standard ABI". Such a virtual would have to be given a default provider
    # in Spack core's etc/spack/defaults/packages.yaml, which a package
    # repository cannot do, and `spack audit configs` rejects a virtual without
    # one. This is the line to widen once an MPI implements the ABI natively.
    depends_on("mpi-abi-wrapper")

    provides("mpi@5.0")

    # Nothing in mpif is declared bind(C): the generated entry points rely on
    # the compiler lowercasing names, appending one underscore, and passing
    # hidden character lengths as size_t, which gfortran did as int before 8.
    # Earlier versions compile mpif without complaint and are wrong at run
    # time, so this floor cannot be checked by compiling.
    conflicts("%gcc@:7", msg="mpif requires gfortran 8 or later")

    # bin/mpifort bakes in the Fortran compiler it was configured with, which
    # under Spack is a wrapper that only works inside a build environment.
    filter_compiler_wrappers("mpifort", relative_root="bin")

    def cmake_args(self):
        # mpif is built against the ABI mpi.h and libmpi_abi and nothing
        # implementation-specific; its configure stage refuses outright if
        # MPI_C_LIBRARIES names no libmpi_abi. Naming the C compiler wrapper
        # explicitly is what keeps FindMPI from wandering off to a system MPI.
        mpi_abi = self.spec["mpi-abi-wrapper"]
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("MPIF_ENABLE_CFI", "cfi"),
            self.define("MPI_HOME", mpi_abi.prefix),
            self.define("MPI_C_COMPILER", join_path(mpi_abi.prefix.bin, "mpicc")),
        ]

    @property
    def headers(self):
        # Both halves: mpif.h and the Fortran modules here, the ABI mpi.h from
        # the C provider.
        return (
            HeaderList(find(self.prefix.include, "mpif.h", recursive=False))
            + self.spec["mpi-abi-wrapper"].headers
        )

    @property
    def libs(self):
        return (
            find_libraries("libmpif", root=self.prefix.lib, shared=self.spec.satisfies("+shared"))
            + self.spec["mpi-abi-wrapper"].libs
        )

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        mpi_abi = self.spec["mpi-abi-wrapper"]
        env.set("MPIF_FC", self.compiler.fc)
        env.set("MPICC", join_path(mpi_abi.prefix.bin, "mpicc"))
        env.set("MPICXX", join_path(mpi_abi.prefix.bin, "mpicxx"))
        env.set("MPIFORT", join_path(self.prefix.bin, "mpifort"))
        env.set("MPIF77", join_path(self.prefix.bin, "mpifort"))
        env.set("MPIF90", join_path(self.prefix.bin, "mpifort"))

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        # Drive the Spack compiler wrappers from under bin/mpifort, the same way
        # the C half does from under bin/mpicc.
        dependent_module = dependent_spec.package.module
        if hasattr(dependent_module, "spack_fc"):
            env.set("MPIF_FC", dependent_module.spack_fc)
        # find_package(mpif) warns when the consumer uses a different Fortran
        # compiler than mpif was built with. Under Spack it is the same one by
        # construction, and the warning only ever fires on the wrapper path
        # spelling, so silence it.
        env.set("MPIF_SKIP_COMPILER_CHECK", "1")

    def setup_dependent_package(self, module, dependent_spec):
        mpi_abi = self.spec["mpi-abi-wrapper"]
        self.spec.mpicc = join_path(mpi_abi.prefix.bin, "mpicc")
        self.spec.mpicxx = join_path(mpi_abi.prefix.bin, "mpicxx")
        self.spec.mpifc = join_path(self.prefix.bin, "mpifort")
        self.spec.mpif77 = join_path(self.prefix.bin, "mpifort")

    @run_after("install")
    def complete_mpi_prefix(self):
        """Make this prefix answer as a whole MPI installation.

        A dependent that reads ``spec["mpi"].mpicc`` and ``.mpifc`` is served by
        ``setup_dependent_package`` above, but many recipes instead hand
        ``spec["mpi"].prefix`` to a configure script or look for
        ``prefix.bin.mpiexec`` in a stand-alone test, and this prefix holds only
        the Fortran half. Link the C half's entry points in beside ours.

        The launcher linked here is the one belonging to the MPI that the C half
        was built against. That is the right default and not a constraint: the
        ABI's whole point is that MPI_ABI_WRAPPER_LIB and the loader's search
        path can send the same binary to another implementation at run time,
        with that implementation's own mpiexec.
        """
        mpi_abi = self.spec["mpi-abi-wrapper"]
        for subdir, names in (
            ("bin", ["mpicc", "mpicxx", "mpiexec", "mpirun"]),
            ("include", ["mpi.h", "mpiabi.h"]),
        ):
            target_dir = join_path(self.prefix, subdir)
            mkdirp(target_dir)
            for name in names:
                source = join_path(mpi_abi.prefix, subdir, name)
                target = join_path(target_dir, name)
                if os.path.exists(source) and not os.path.lexists(target):
                    symlink(source, target)

        # libmpi_abi and its versioned variants: MPI-5.0 20.2.1 lets an
        # application name either. Which of lib/ and lib64/ either prefix used
        # is GNUInstallDirs' business, so look in both and link into whichever
        # this installation has.
        our_libdir = next(
            (d for d in (self.prefix.lib, self.prefix.lib64) if os.path.isdir(d)), None
        )
        if our_libdir:
            for libdir in (mpi_abi.prefix.lib, mpi_abi.prefix.lib64):
                for source in glob.glob(join_path(libdir, "libmpi_abi*")):
                    target = join_path(our_libdir, os.path.basename(source))
                    if not os.path.lexists(target):
                        symlink(source, target)

    @run_after("install")
    def setup_build_tests(self):
        """Copy the test project, which needs mpif installed to build at all.

        cmake/ comes along because the test project reaches into it: it re-runs
        the parent build's TS 29113 probe (cmake/cfi-probe) so that mpi_f08's
        constants cannot pass vacuously.
        """
        cache_extra_test_sources(self, ["test", "cmake"])

    def test_test_suite(self):
        """build and run the upstream test project against the installation"""
        cmake_bin = self.spec["cmake"].prefix.bin
        cmake_exe = which(cmake_bin.cmake, required=True)
        ctest = which(cmake_bin.ctest, required=True)
        work_dir = join_path(self.test_suite.current_test_cache_dir, "test")

        # The test project is a separate CMake project on purpose: it finds and
        # uses the *installation*, so it tests the install procedure as much as
        # the library. Both halves of the MPI it looks for are in this prefix,
        # the Fortran one built here and the C one linked in after install.
        prefix_path = ";".join([str(self.prefix)] + get_cmake_prefix_path(self))
        args = [
            ".",
            "-DCMAKE_PREFIX_PATH=" + prefix_path,
            "-DMPI_HOME=" + str(self.prefix),
            "-DMPI_C_COMPILER=" + join_path(self.prefix.bin, "mpicc"),
            "-DMPI_Fortran_COMPILER=" + join_path(self.prefix.bin, "mpifort"),
            # The consuming project is configured by Spack, not by whoever
            # built mpif, so the wrapper-path comparison has nothing to say.
            "-DMPIF_SKIP_COMPILER_CHECK=ON",
        ]

        with working_dir(work_dir):
            with test_part(self, "test_configure", purpose="configure the test project"):
                cmake_exe(*args)
            with test_part(self, "test_build", purpose="build the test project"):
                cmake_exe("--build", ".")
            with test_part(self, "test_ctest", purpose="run the test project's ctest suite"):
                ctest("--output-on-failure")

    def test_mpif_info(self):
        """run mpif_info under the wrapped MPI's launcher"""
        mpiexec = self.spec["mpi-abi-wrapper"].prefix.bin.mpiexec
        if not os.path.exists(mpiexec):
            raise SkipTest("this mpi-abi-wrapper version installs no launcher")
        launcher = which(mpiexec, required=True)
        out = launcher(
            "-n", "2", join_path(self.prefix.bin, "mpif_info"), output=str.split, error=str.split
        )
        check_outputs([r"libmpi_abi"], out)
