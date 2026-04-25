# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Dineof(MakefilePackage):
    """DINEOF (Data Interpolating Empirical Orthogonal Functions) is an
    EOF-based method to fill in missing data from geophysical fields, such as
    clouds in sea surface temperature.

    For more information on how DINEOF works, please refer to Alvera-Azcarate
    et al (2005) and Beckers and Rixen (2003). The multivariate application of
    DINEOF is explained in Alvera-Azcarate et al (2007), and in Beckers et al
    (2006) the error calculation using an optimal interpolation approach is
    explained. If you need a copy of any of these papers, don't hesitate to
    contact us! For more information about the Lanczos solver, see Toumazou and
    Cretaux (2001).

    References:
        Alvera-Azcarate et al (2005) - https://doi.org/10.1016/j.ocemod.2004.08.001
        Beckers and Rixen (2003) - https://doi.org/10.1175/1520-0426(2003)020%3C1839:ECADFF%3E2.0.CO;2
        Alvera-Azcarate et al (2007) - https://doi.org/10.1029/2006JC003660
        Beckers et al (2006) - https://doi.org/10.5194/os-2-183-2006
        Toumazou and Cretaux (2001) - https://doi.org/10.1175/1520-0493(2001)129%3C1243:UALEIT%3E2.0.CO;2
    """

    homepage = "https://github.com/aida-alvera/DINEOF"
    url = "https://github.com/aida-alvera/DINEOF/archive/refs/tags/v2.0.0.tar.gz"

    maintainers("aida-alvera", "insalt-glitch")
    license("GPL-2.0-only", checked_by="insalt-glitch")
    version("2.0.0", sha256="7a729c27599f3887d2f40e8ddbbdcb29046ae0e225d099739f0adea30b5eb2c0")

    depends_on("gmake", type="build")
    depends_on("fortran", type="build")

    depends_on("blas", type=("build", "link", "run"))
    depends_on("lapack", type=("build", "link", "run"))
    depends_on("netcdf-c", type=("build", "link", "run"))
    depends_on("netcdf-fortran", type=("build", "link", "run"))
    depends_on("arpack-ng", type=("build", "link", "run"))

    def edit(self, spec, prefix):
        copy("config.mk.template", "config.mk")

    def build(self, spec, prefix):
        make(
            f"FC={self.compiler.fc}",
            f"BLAS_LIB={spec['blas'].libs.joined()}",
            f"LAPACK_LIB={spec['lapack'].libs.joined()}",
            parallel=False,
        )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("dineof", prefix.bin)
