# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.octave import OctavePackage
from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *


class OctaveControl(OctavePackage, SourceforgePackage):
    """Computer-Aided Control System Design (CACSD) Tools for GNU Octave,
    based on the proven SLICOT Library"""

    homepage = "https://octave.sourceforge.io/control/"
    sourceforge_mirror_path = "octave/control-3.2.0.tar.gz"
    git = "https://github.com/gnu-octave/pkg-control/"
    # url = "https://github.com/gnu-octave/pkg-control/releases/download/control-4.1.3/control-4.1.3.tar.gz"

    license("GPL-3.0-or-later")

    version("4.1.3", sha256="07ce19c121778333e409b4fd67d8946ff6fa9d0eb93b00312b331b86ea6954b4")
    version("3.2.0", sha256="faf1d510d16ab46e4fa91a1288f4a7839ee05469c33e4698b7a007a0bb965e3e")

    depends_on("cxx", type="build")  # generated

    def url_for_version(self, version):
        if version <= Version("3.2.0"):
            return f"https://sourceforge.net/projects/octave/files/Octave%20Forge%20Packages/Individual%20Package%20Releases/control--{version}.tar.gz"
        else:
            url = "https://github.com/gnu-octave/pkg-control/releases/download/control-{0}/control-{1}.tar.gz"
            return url.format(version, version)

    extends("octave@4.0.0:")
