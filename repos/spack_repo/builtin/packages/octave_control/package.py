# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.octave import OctavePackage

from spack.package import *


class OctaveControl(OctavePackage):
    """Computer-Aided Control System Design (CACSD) Tools for GNU Octave,
    based on the proven SLICOT Library"""

    homepage = "https://octave.sourceforge.io/control/"
    git = "https://github.com/gnu-octave/pkg-control/"
    url = "https://github.com/gnu-octave/pkg-control/releases/download/control-4.1.3/control-4.1.3.tar.gz"

    license("GPL-3.0-or-later")

    version("4.1.3", sha256="07ce19c121778333e409b4fd67d8946ff6fa9d0eb93b00312b331b86ea6954b4")
    version(
        "3.2.0",
        sha256="faf1d510d16ab46e4fa91a1288f4a7839ee05469c33e4698b7a007a0bb965e3e",
        url="https://sourceforge.net/projects/octave/files/Octave%20Forge%20Packages/Individual%20Package%20Releases/control--3.2.0.tar.gz",
    )

    depends_on("cxx", type="build")

    extends("octave@4.0.0:")
