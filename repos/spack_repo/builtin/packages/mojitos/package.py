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
    git = "https://gitlab.irit.fr/sepia-pub/mojitos.git"
    url = "https://gitlab.irit.fr/sepia-pub/mojitos/-/archive/v2.0.2/mojitos-v2.0.2.tar.gz?ref_type=tags"
    maintainers("georges-da-costa")
    license("GPL-3.0-or-later", checked_by="georges-da-costa")

    version("2.0.2", sha256="3213353199a7d42f0e75a5c2d8680782f6e646147d10d0c7a10f700707b87d82")

    depends_on("c", type="build")
    depends_on("gmake", type="build")
    depends_on("libmicrohttpd")

    def install(self, spec, prefix):
        configure = Executable("./configure")
        configure(f"--prefix={prefix}")

        make()

        make("install")
