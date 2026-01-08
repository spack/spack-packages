# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libnl(AutotoolsPackage):
    """libnl - Netlink Protocol Library Suite"""

    homepage = "https://www.infradead.org/~tgr/libnl/"
    url = "https://github.com/thom311/libnl/releases/download/libnl3_3_0/libnl-3.3.0.tar.gz"

    license("LGPL-2.1-or-later")

    version("3.12.0", sha256="fc51ca7196f1a3f5fdf6ffd3864b50f4f9c02333be28be4eeca057e103c0dd18")
    version("3.3.0", sha256="705468b5ae4cd1eb099d2d1c476d6a3abe519bc2810becf12fb1e32de1e074e4")

    depends_on("c", type="build")  # generated

    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("m4", type="build")

    conflicts("platform=darwin", msg="libnl requires FreeBSD or Linux")

    def url_for_version(self, version):
        url = "https://github.com/thom311/libnl/releases/download/libnl{0}/libnl-{1}.tar.gz"
        return url.format(str(version).replace(".", "_"), version)
