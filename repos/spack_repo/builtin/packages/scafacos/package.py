# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Scafacos(AutotoolsPackage):
    """ScaFaCoS is a library of scalable fast coulomb solvers."""

    homepage = "http://www.scafacos.de/"
    url = "https://github.com/scafacos/scafacos/releases/download/v1.0.4/scafacos-1.0.4.tar.gz"

    maintainers("hmenke")

    license("GPL-3.0-or-later OR LGPL-3.0-or-later")

    version("1.0.4", sha256="6634c4202e825e771d1dd75bbe9cac5cee41136c87653fde98fbd634681c1be6")
    version("1.0.3", sha256="d3579f4cddb10a562722c190c2452ebc455592d44f6dbde8f155849ba6e2b3d0")
    version("1.0.2", sha256="158078665e48e28fd12b7895063db056cee5d135423fc36802e39c9160102b97")
    version("1.0.1", sha256="2b125f313795c81b0e87eb920082e91addf94c17444f9486d979e691aaded99b")
    version("1.0.0", sha256="cc5762edbecfec0323126b6a6a535dcc3e134fcfef4b00f63eb05fae15244a96")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("fftw")
    depends_on("file")
    depends_on("gmp")
    depends_on("gsl")
    depends_on("mpi")
    depends_on("pfft")
    depends_on("pnfft")

    def patch(self):
        # configure (generated from package/configure.ac -- release
        # tarballs ship the generated script, and this recipe does not
        # run autoreconf) can populate SCAFACOS_PC_LIBS with a stray
        # colon glued onto a linker flag (e.g. "-lmpi:"), picked up from
        # a compiler wrapper's verbose link output when probing for
        # extra Fortran/C++ runtime libs. That corrupts the "Libs:" line
        # of the generated scafacos.pc -- either a dangling trailing
        # colon, or (depending on exactly where it lands) the template's
        # following "Libs.private:" line glued directly onto the same
        # output line with no separator. Consumers resolving scafacos
        # via pkg-config/CMake's FindPkgConfig then pass the malformed
        # token to the linker literally, producing spurious
        # "cannot find -l<garbage>" errors downstream (observed with
        # lammps+scafacos). Colons never appear legitimately inside a
        # well-formed -l/-L linker flag, so strip them from
        # SCAFACOS_PC_LIBS specifically, right before configure's own
        # whitespace-normalization pass. Root-caused and fixed upstream
        # at the configure.ac level: https://github.com/scafacos/scafacos/pull/44
        anchor = 'z= ; for x in ${SCAFACOS_PC_LIBS} ; do'
        strip_colons = (
            'SCAFACOS_PC_LIBS=`echo " ${SCAFACOS_PC_LIBS} " '
            '| sed "s/:/ /g"`\n'
        )
        filter_file(anchor, strip_colons + anchor, "package/configure", string=True)

    def configure_args(self):
        args = [
            "--disable-doc",
            "--enable-fcs-solvers=direct,ewald,fmm,p3m",
            "FC={0}".format(self.spec["mpi"].mpifc),
            "F77={0}".format(self.spec["mpi"].mpif77),
        ]
        return args
