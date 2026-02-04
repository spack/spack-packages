# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os.path
import re
import sys
from glob import glob

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class MvapichPlus(Package, CudaPackage, ROCmPackage):
    """Mvapich is a High-Performance MPI Library for clusters with diverse
    networks (InfiniBand, Omni-Path, Ethernet/iWARP, and RoCE) and computing
    platforms (x86 (Intel and AMD), ARM and OpenPOWER)"""

    homepage = "https://mvapich.cse.ohio-state.edu/userguide/userguide_spack/"
    url = "https://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich-3.0.tar.gz"
    list_url = "https://mvapich.cse.ohio-state.edu/downloads/"
    executables = ["^mpiname$", "^mpichversion$"]
    manual_download = True

    maintainers("natshineman", "harisubramoni", "MatthewLieber")

    license("Unlicense")

    # Prefer the latest stable release

    version(
        "4.1",
        sha256="891b98563216222bd12171ec9ace4a831eef73094f3705a4635bb6104cdfb465",
        url="https://mvapich.cse.ohio-state.edu/download/mvapich/plus/4.1/mvapich-plus-installer.sh",
        expand=False,
    )

    provides("mpi")
    provides("mpi@:4.1")

    variant("wrapperrpath", default=True, description="Enable wrapper rpath")
    variant("debug", default=False, description="Enable debug info and error messages at run-time")
    variant("apu", default=False, description="Enable APU enhancements")

    variant("regcache", default=True, description="Enable memory registration cache")

    # Accepted values are:
    #   single      - No threads (MPI_THREAD_SINGLE)
    #   funneled    - Only the main thread calls MPI (MPI_THREAD_FUNNELED)
    #   serialized  - User serializes calls to MPI (MPI_THREAD_SERIALIZED)
    #   multiple    - Fully multi-threaded (MPI_THREAD_MULTIPLE)
    #   runtime     - Alias to "multiple"
    variant(
        "threads",
        default="multiple",
        values=("single", "funneled", "serialized", "multiple"),
        multi=False,
        description="Control the level of thread support",
    )

    variant(
        "process_managers",
        description="List of the process managers to activate",
        values=disjoint_sets(("auto",), ("slurm",), ("hydra", "gforker", "remshell"))
        .with_error("'slurm' or 'auto' cannot be activated along with other process managers")
        .with_default("auto")
        .with_non_feature_values("auto"),
    )

    variant(
        "netmod",
        description="Select the netmod to be enabled for this build."
        "For IB/RoCE systems, use the ucx netmod, for interconnects supported "
        "by libfabrics, use the ofi netmod. For more info, visit the "
        "homepage url.",
        default="ofi",
        values=("ofi", "ucx"),
        multi=False,
    )

    variant(
        "alloca", default=False, description="Use alloca to allocate temporary memory if available"
    )

    variant(
        "file_systems",
        description="List of the ROMIO file systems to activate",
        values=auto_or_any_combination_of("lustre", "gpfs", "nfs", "ufs"),
    )

    depends_on("zlib-api")
    depends_on("rpm")
    depends_on("libpciaccess", when=(sys.platform != "darwin"))
    depends_on("libxml2")
    depends_on("libfabric", when="netmod=ofi")
    depends_on("slurm", when="process_managers=slurm")
    depends_on("ucx", when="netmod=ucx")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    requires("%fortran=gcc", when="%c=gcc")
    requires("%fortran=clang", when="%c=clang")
    requires("%fortran=intel-oneapi-compilers", when="%c=intel-oneapi-compilers")
    requires("%fortran=nvhpc", when="%c=nvhpc")

    filter_compiler_wrappers("mpicc", "mpicxx", "mpif77", "mpif90", "mpifort", relative_root="bin")

    @classmethod
    def determine_version(cls, exe):
        if exe.endswith("mpichversion"):
            output = Executable(exe)(output=str, error=str)
            match = re.search(r"^MVAPICH Version:\s*(\S+)", output)
        elif exe.endswith("mpiname"):
            output = Executable(exe)("-a", output=str, error=str)
            match = re.search(r"^MVAPICH (\S+)", output)
        return match.group(1) if match else None

    @property
    def libs(self):
        query_parameters = self.spec.last_query.extra_parameters
        libraries = ["libmpi"]

        if "cxx" in query_parameters:
            libraries = ["libmpicxx"] + libraries

        return find_libraries(libraries, root=self.prefix, shared=True, recursive=True)

    def install(self, spec, prefix):
        runfile = glob(join_path(self.stage.source_path, "mvapich-plus-installer.sh"))[0]
        mvp_ver = str(spec.version)
        gpu = "nogpu"
        gpu_ver = ""
        apu = ""
        if spec.satisfies("^cuda"):
            gpu = "cuda"
            gpu_ver = str(spec["cuda"].version)[:4]
        elif spec.satisfies("+rocm"):
            gpu = "rocm"
            gpu_ver = spec["hip"].version
            if spec.satisfies("+apu"):
                apu = ".mi300a"

        netmod = "ucx" if spec.satisfies("netmod=ucx") else "ofi"
        comp = spec["c"].format("{name}{version}")
        el = "el9" if spec["glibc"].satisfies("@2.34:") else "el8"
        rhel = "rh" + el
        ofed = "24.10"
        slurm = ""
        if spec.satisfies("process_managers=slurm"):
            slurm = ".slurm"
        rpm = f"mvapich-plus-{mvp_ver}-{gpu}{gpu_ver}.{rhel}.ofed{ofed}.{netmod}.{comp}\
{slurm}{apu}-4.1-1.{el}.x86_64.rpm"

        install_shell = which("bash")
        io = which("rpm2cpio").path
        arguments = [
            runfile,  # the install script
            "--prefix=%s" % prefix,  # Where to install
            "--io=%s" % io,  # rpm2cpio
            "--rpm=%s" % rpm,  # rpm name
        ]

        install_shell(*arguments)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("MPI_ROOT", self.prefix)

        # Because MPI functions as a compiler, we need to treat it as one and
        # add its compiler paths to the run environment.
        self.setup_compiler_environment(env)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        self.setup_compiler_environment(env)

        # use the Spack compiler wrappers under MPI
        env.set("MPICH_CC", spack_cc)
        env.set("MPICH_CXX", spack_cxx)
        env.set("MPICH_F77", spack_f77)
        env.set("MPICH_F90", spack_fc)
        env.set("MPICH_FC", spack_fc)

    def setup_compiler_environment(self, env: EnvironmentModifications):
        # For Cray MPIs, the regular compiler wrappers *are* the MPI wrappers.
        # Cray MPIs always have cray in the module name, e.g. "cray-mvapich"
        if self.spec.satisfies("platform=cray"):
            env.set("MPICC", spack_cc)
            env.set("MPICXX", spack_cxx)
            env.set("MPIF77", spack_fc)
            env.set("MPIF90", spack_fc)
        else:
            env.set("MPICC", join_path(self.prefix.bin, "mpicc"))
            env.set("MPICXX", join_path(self.prefix.bin, "mpicxx"))
            env.set("MPIF77", join_path(self.prefix.bin, "mpif77"))
            env.set("MPIF90", join_path(self.prefix.bin, "mpif90"))

    def setup_dependent_package(self, module, dependent_spec):
        # For Cray MPIs, the regular compiler wrappers *are* the MPI wrappers.
        # Cray MPIs always have cray in the module name, e.g. "cray-mvapich"
        if self.spec.satisfies("platform=cray"):
            self.spec.mpicc = spack_cc
            self.spec.mpicxx = spack_cxx
            self.spec.mpifc = spack_fc
            self.spec.mpif77 = spack_f77
        else:
            self.spec.mpicc = join_path(self.prefix.bin, "mpicc")
            self.spec.mpicxx = join_path(self.prefix.bin, "mpicxx")
            self.spec.mpifc = join_path(self.prefix.bin, "mpif90")
            self.spec.mpif77 = join_path(self.prefix.bin, "mpif77")

        self.spec.mpicxx_shared_libs = [
            os.path.join(self.prefix.lib, f"libmpicxx.{dso_suffix}"),
            os.path.join(self.prefix.lib, f"libmpi.{dso_suffix}"),
        ]
