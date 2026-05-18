# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.octave import OctavePackage

from spack.package import *


class OctaveStatistics(OctavePackage):
    """Additional statistics functions for Octave."""

    homepage = "https://octave.sourceforge.io/statistics/"
    git = "https://github.com/gnu-octave/statistics/"
    url = "https://github.com/gnu-octave/statistics/releases/download/release-1.7.6/statistics-1.7.6.tar.gz"

    version("1.7.6", sha256="a518c50209e25e59742414c73955060f83c39c07b2d9a20b2fc8d13bd3106af3")
    version(
        "1.4.2",
        sha256="7976814f837508e70367548bfb0a6d30aa9e447d4e3a66914d069efb07876247",
        url="https://sourceforge.net/projects/octave/files/Octave%20Forge%20Packages/Individual%20Package%20Releases/statistics--1.4.2.tar.gz",
    )

    depends_on("octave-io")
    depends_on("cxx", type="build")

    extends("octave@4.0.0:")
