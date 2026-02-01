# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Mojitos(Package):
    """MojitO/S is an Open Source System, Energy and
    Network Monitoring Tools at the O/S level.
    MojitO/S runs on GNU/Linux"""

    homepage = "https://gitlab.irit.fr/sepia-pub/mojitos"
    git = "https://gitlab.irit.fr/sepia-pub/mojitos"
    version("2.0.1", branch="guix")
    maintainers("georges-da-costa")
    license("GPL-3.0-or-later", checked_by="georges-da-costa")

    depends_on("gcc")
    depends_on("gmake")
    depends_on("libmicrohttpd")

    def install(self, spec, prefix):
        configure = Executable("./configure")
        configure(f"--prefix={prefix}")

        make()

        make("install")
