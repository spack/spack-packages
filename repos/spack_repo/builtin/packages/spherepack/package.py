# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Spherepack(Package):
    """SPHEREPACK - A Package for Modeling Geophysical Processes"""

    homepage = "https://github.com/NCAR/NCAR-Classic-Libraries-for-Geophysics"
    url = "https://github.com/NCAR/NCAR-Classic-Libraries-for-Geophysics/raw/refs/heads/main/SpherePack/spherepack3.2.tar.gz"

    version("3.2", sha256="7f5497e77101a4423cee887294f873048f6ff6bc8d0e908c8a89ece677ee19ea")

    depends_on("fortran", type="build")
    depends_on("gmake", type="build")

    def flag_handler(self, name, flags):
        spec = self.spec

        if name == "fflags":
            if spec.satisfies("%fortran=gcc@10:"):
                flags.append("-fallow-argument-mismatch")

        return (flags, None, None)

    def install(self, spec, prefix):
        make("MAKE=make", "F90=f90", "AR=ar", "libspherepack")
        make("MAKE=make", "F90=f90", "AR=ar", "testspherepack")
        install_tree("lib", prefix.lib)
