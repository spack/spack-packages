# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Etcd(GoPackage):
    """etcd is a distributed reliable key-value store for the most
    critical data of a distributed system"""

    homepage = "https://etcd.io/"
    url = "https://github.com/etcd-io/etcd/archive/v3.4.7.tar.gz"

    maintainers("alecbcs")

    license("Apache-2.0")

    version("3.6.12", sha256="43b78c492dd5dd5f012d14af85adf1ea15b25384cd2f8de04d7d68e418e4907a")
    version("3.6.5", sha256="96b2eabaf6da7dd21797152e7d1c1ce27da75926ae10e08a90b7ed0458287a4b")
    version("3.5.9", sha256="ab24d74b66ba1ed7d2bc391839d961e7215f0f3d674c3a9592dad6dc67a7b223")
    version("3.4.23", sha256="055c608c4898d25f23aefbc845ff074bf5e8a07e61ed41dbd5cc4d4f59c93093")

    depends_on("go@1.25:", type="build", when="@3.6.9:")
    depends_on("go@1.24:", type="build", when="@3.6.5:")
    depends_on("go@1.19:", type="build")
    depends_on("gmake", type="build")
