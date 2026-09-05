# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class MpiAbiWrapper(CMakePackage):
    """Implement the MPI ABI on top of an existing MPI implementation.

    mpi_abi_wrapper provides the C bindings of the MPI ABI defined by the MPI 5.0
    standard, forwarding every call to another MPI library which need not
    implement that ABI itself. It is thus a stop-gap for MPI implementations, or
    system-wide MPI installations, that predate MPI 5.0.

    The wrapped MPI is deliberately not a Spack dependency: the point of this
    package is to wrap an MPI that Spack does not manage, such as a vendor MPI
    tuned for a particular interconnect. Name it with ``mpi_prefix=<path>``;
    that path is part of the spec, so wrappers around different MPIs can be
    installed side by side. Without it, CMake's FindMPI searches ``MPI_HOME``
    and ``PATH``.

    This package deliberately provides no virtual. It supplies the C half of an
    MPI, while Spack's ``mpi`` virtual covers the Fortran bindings as well; the
    ``mpif`` package depends on this one, adds those bindings, and is what
    provides ``mpi`` for the pair.
    """

    homepage = "https://github.com/eschnett/mpi_abi_wrapper"
    url = "https://github.com/eschnett/mpi_abi_wrapper/archive/refs/tags/v1.0.0.tar.gz"
    git = "https://github.com/eschnett/mpi_abi_wrapper.git"

    maintainers("eschnett")

    license("MIT", checked_by="eschnett")

    version("main", branch="main")
    version("1.0.0", sha256="56ae86ffed7dd2cf9cafd87ff67ba6360ec152a783cf0823df3c21440adc1fea")

    variant(
        "mpi_prefix",
        values=str,
        default="auto",
        description="Prefix of the MPI implementation to wrap; 'auto' searches MPI_HOME and PATH",
    )
    variant(
        "fortran",
        default=True,
        description="Probe the wrapped MPI's Fortran LOGICAL representation, "
        "which MPI_Abi_get_fortran_booleans reports",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    # The Fortran compiler answers one question -- what the wrapped MPI's
    # LOGICAL looks like -- in a single translation unit that links against
    # nothing. Without ~fortran the build is a hard error rather than a silent
    # "not set", which is why this dependency is not optional when +fortran.
    depends_on("fortran", type="build", when="+fortran")
    depends_on("cmake@3.20:", type="build")
    # find_package(Python3 COMPONENTS Interpreter REQUIRED), unconditionally at
    # configure time: the header and entry-point generators are Python.
    depends_on("python@3:", type="build")

    # bin/mpicc and friends bake in the compiler they were configured with,
    # which under Spack is a wrapper that only works inside a build environment.
    # (bin/mpi_abi_wrapper_info records the same path, but it is a binary and
    # only prints it, so it is deliberately left alone.)
    filter_compiler_wrappers("mpicc", "mpicxx", "mpic++", relative_root="bin")

    def cmake_args(self):
        args = [
            self.define("MPI_ABI_BUILD_WRAPPER", True),
            self.define_from_variant("MPI_ABI_FORTRAN", "fortran"),
        ]
        mpi_prefix = self.spec.variants["mpi_prefix"].value
        if mpi_prefix != "auto":
            args.append(self.define("MPI_HOME", mpi_prefix))
        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # The Fortran compiler this build wants is the wrapped MPI's own, so
        # that the LOGICAL it reports is the one that MPI's Fortran bindings
        # use. Upstream finds it as the mpifort sitting beside the wrapped
        # MPI's mpicc -- but only when FC is unset, since an explicit FC wins
        # outright and is not second-guessed. Spack's Fortran dependency above
        # stays as the fallback that upstream's plain PATH search then finds.
        if self.spec.satisfies("+fortran"):
            env.unset("FC")
            env.unset("F77")

    @property
    def headers(self):
        return HeaderList(find(self.prefix.include, "mpi.h"))

    @property
    def libs(self):
        # MPI-5.0 20.2.1 requires that an application need name no library
        # other than mpi_abi; libmpiwrapper is reached through it, by dlopen.
        return find_libraries("libmpi_abi", root=self.prefix.lib, shared=True)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Like any MPI, this package provides compiler wrappers, and they need
        # to know which compiler to drive.
        env.set("MPI_ABI_CC", self.compiler.cc)
        env.set("MPI_ABI_CXX", self.compiler.cxx)
        env.set("MPICC", join_path(self.prefix.bin, "mpicc"))
        env.set("MPICXX", join_path(self.prefix.bin, "mpicxx"))

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        # Drive the Spack compiler wrappers from under bin/mpicc and bin/mpicxx.
        dependent_module = dependent_spec.package.module
        for var_name, attr_name in (
            ("MPI_ABI_CC", "spack_cc"),
            ("MPI_ABI_CXX", "spack_cxx"),
        ):
            if hasattr(dependent_module, attr_name):
                env.set(var_name, getattr(dependent_module, attr_name))

    def setup_dependent_package(self, module, dependent_spec):
        self.spec.mpicc = join_path(self.prefix.bin, "mpicc")
        self.spec.mpicxx = join_path(self.prefix.bin, "mpicxx")
        # No mpifc/mpif77 on purpose: this package has no Fortran bindings.
        # The mpif package supplies them, and provides the mpi virtual.

    def test_mpi_hello(self):
        """compile and run an MPI program against the installed ABI library"""
        mpiexec = join_path(self.prefix.bin, "mpiexec")
        if not os.path.exists(mpiexec):
            raise SkipTest("this version installs no launcher for the wrapped MPI")

        source = "mpi_hello.c"
        with open(source, "w") as handle:
            handle.write(
                "#include <mpi.h>\n"
                "#include <stdio.h>\n"
                "int main(int argc, char **argv) {\n"
                "  int rank, size;\n"
                "  MPI_Init(&argc, &argv);\n"
                "  MPI_Comm_rank(MPI_COMM_WORLD, &rank);\n"
                "  MPI_Comm_size(MPI_COMM_WORLD, &size);\n"
                '  printf("Hello world! From rank %d of %d\\n", rank, size);\n'
                "  MPI_Finalize();\n"
                "  return 0;\n"
                "}\n"
            )

        with test_part(self, "test_mpi_hello_compile", purpose="compile with bin/mpicc"):
            mpicc = which(join_path(self.prefix.bin, "mpicc"), required=True)
            mpicc("-o", "mpi_hello", source)

        with test_part(self, "test_mpi_hello_run", purpose="run two ranks under bin/mpiexec"):
            launcher = which(mpiexec, required=True)
            out = launcher("-n", "2", "./mpi_hello", output=str.split, error=str.split)
            check_outputs(
                [r"Hello world! From rank 0 of 2", r"Hello world! From rank 1 of 2"], out
            )

    @run_after("install")
    def record_wrapped_mpi(self):
        """Record which MPI this install actually wrapped.

        ``mpi_prefix=`` keeps two wrappers around two MPIs apart in the spec,
        but says nothing when it is left at 'auto', and never names the
        implementation and version that answered. bin/mpi_abi_wrapper_info
        reports both, along with the launcher and the Fortran probe, so run it
        once here and leave the answer beside the installation: a wrapper whose
        wrapped MPI is unknown is not one anybody can reason about later.
        """
        report = join_path(self.prefix.share, "mpi-abi-wrapper", "wrapped-mpi.txt")
        lines = [
            "# " + self.spec.format("{name}@{version} /{hash:7}"),
            f"# mpi_prefix = {self.spec.variants['mpi_prefix'].value}",
            "",
        ]

        info = join_path(self.prefix.bin, "mpi_abi_wrapper_info")
        if os.path.exists(info):
            describe = which(info, required=True)
            output = describe(output=str, error=str, fail_on_error=False)
            lines.append((output or "").strip())
        else:
            lines.append("This version installs no mpi_abi_wrapper_info to ask.")

        mkdirp(os.path.dirname(report))
        with open(report, "w") as handle:
            handle.write("\n".join(lines) + "\n")
        tty.msg(f"Wrapped MPI recorded in {report}", *lines)
