# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Xbae(AutotoolsPackage):
    """The Xbae widget set consists of the well known XbaeMatrix widget,
    and Caption and XbaeInput widgets."""

    homepage = "https://sourceforge.net/projects/xbae/"
    url = "https://sourceforge.net/projects/xbae/files/xbae/4.60.4/xbae-4.60.4.tar.gz"

    license("MIT", checked_by="wdconinc")  # Old style, Bellcore variant

    version("4.60.4", sha256="eb72702ed0a36d043f2075a9d5a4545556da1b8dab4d67d85fca92f37aeb04a8")

    depends_on("c", type="build")

    depends_on("libxext")
    depends_on("libxmu")
    depends_on("libxpm")
    depends_on("libxt")
    depends_on("motif")

    # Fix build with GCC 14 and newer
    patch("fix_build_with_gcc14.patch", level=0)

    def flag_handler(self, name, flags):
        # The package does not build with C dialects newer than gnu17, so set gnu17
        # for GCC 15 and newer which default to gnu23
        if name == "cflags" and self.spec.satisfies("%gcc@15:"):
            flags.append("-std=gnu17")
        return (flags, None, None)
