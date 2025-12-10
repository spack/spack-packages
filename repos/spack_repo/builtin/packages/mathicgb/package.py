# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Mathicgb(AutotoolsPackage):
    """Mathicgb is a program and library for computing Gröbner bases
    and signature Gröbner bases.  It builds on the efficient data
    structures provided by Mathic to achieve high performance in
    computational algebra tasks."""

    homepage = "https://github.com/Macaulay2/mathicgb"
    git = "https://github.com/Macaulay2/mathicgb"

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    version("1.0.2025.05.13", commit="de139564927563afef383174fd3cf8c93ee18ab3")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("mathic")
    depends_on("memtailor")

    def configure_args(self):
        return ["--enable-shared"]
