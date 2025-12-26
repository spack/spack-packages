# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.octave import OctavePackage

from spack.package import *


class OctaveArduino(OctavePackage):
    """Provides an Octave look-alike implementation of the
    Arduino extension for Matlab."""

    homepage = "https://octave.sourceforge.io/arduino/"
    git = "https://github.com/gnu-octave/octave-arduino/"
    url = "https://github.com/gnu-octave/octave-arduino/releases/download/release-0.12.2/arduino-0.12.2.tar.gz"

    license("GPL-3.0-or-later")

    version("0.12.2", sha256="37c00bbc9a2615852afbc01250f865b1125f5c5532d88e772313d293feab52b8")
    version(
        "0.2.0",
        sha256="0562ff48ea4b2cef28e2e03ccc4678dafa16f91d1580245bb7f9f488c4f56238",
        url="https://sourceforge.net/projects/octave/files/Octave%20Forge%20Packages/Individual%20Package%20Releases/arduino--0.2.0.tar.gz",
    )

    depends_on("cxx", type="build")

    depends_on("octave-instrctl@0.5.0:", when="@0.12.2:")
    depends_on("octave-instrctl")
    extends("octave@3.6.0:")
