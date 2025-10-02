# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.packages.mpich.package import MpichEnvironmentModifications

from spack.package import *


class CrayMvapich2(MpichEnvironmentModifications, Package):
    """Cray/HPE packaging of MVAPICH2 for HPE Apollo systems"""

    homepage = "https://docs.nersc.gov/development/compilers/wrappers/"

    maintainers("hppritcha")

    version("8.1.0")
    version("8.0.16")
    version("8.0.14")
    version("8.0.11")
    version("8.0.9")
    version("7.7.16")
    version("7.7.15")
    version("7.7.14")
    version("7.7.13")

    provides("mpi@3")

    has_code = False  # Skip attempts to fetch a source that is not available

    # Allows attaching compilers to externals in packages.yaml
    depends_on("c", type="build")

    requires("platform=linux", msg="Cray software is only available on linux")

    def install(self, spec, prefix):
        raise InstallError(
            self.spec.format(
                "{name} is not installable, you need to specify "
                "it as an external package in packages.yaml"
            )
        )

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.has_virtual_dependency("c"):
            env.set("MPICC", self["c"].cc)

        if self.spec.has_virtual_dependency("cxx"):
            env.set("MPICXX", self["cxx"].cxx)

        if self.spec.has_virtual_dependency("fortran"):
            env.set("MPIFC", self["fortran"].fortran)
            env.set("MPIF77", self["fortran"].fortran)
