# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libbeef(AutotoolsPackage):
    """
    Library for Bayesian error estimation functionals for use in density functional theory codes.
    """

    homepage = "https://github.com/vossjo/libbeef"
    git = "https://github.com/vossjo/libbeef.git"

    maintainers("nolta")

    license("LGPL-3.0-or-later", checked_by="nolta")

    version("0.1.3", commit="535ea67327baa8368ec5c502392a212375b16187")

    depends_on("c", type="build")

    @property
    def libs(self):
        libraries = ["libbeef"]
        return find_libraries(libraries, root=self.prefix, recursive=True, shared=False)
