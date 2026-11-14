# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class CnsSysjitter(MakefilePackage):
    """cns-sysjitter measures interruptions to running threads caused by the system
    (kernel and hardware).
    """

    homepage = "https://github.com/Xilinx-CNS/cns-sysjitter"
    git = "https://github.com/Xilinx-CNS/cns-sysjitter.git"

    maintainers("rfbgo")

    license("GPL-3.0-or-later")

    version("master", branch="master")
    version("1.4", tag="sysjitter-1.4", commit="8f390d57d5855a83456ca68d97f35559272ef859")

    depends_on("c", type="build")

    # upstream package is missing `make install`
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("sysjitter", prefix.bin)
