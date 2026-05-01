# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Hpckit(Package):
    """Kunpeng HPCKit base installation - Complete HPC toolkit."""

    homepage = "https://www.hikunpeng.com/developer/hpc/hpckit-download"
    url = "https://mirrors.huaweicloud.com/kunpeng/archive/HPC/HPCKit/HPCKit_25.1.0_Linux-aarch64.tar.gz"

    license("UNKNOWN", checked_by="wjunLu")

    version(
        "25.2.1",
        url="https://mirrors.huaweicloud.com/kunpeng/archive/HPC/HPCKit/HPCKit_25.2.1_Linux-aarch64.tar.gz",
        sha256="be9e6b07a0e768570387ab62fed19d59d72af3ae7d01bc240edd9b9dc80dd539",
    )
    version(
        "25.1.0",
        url="https://mirrors.huaweicloud.com/kunpeng/archive/HPC/HPCKit/HPCKit_25.1.0_Linux-aarch64.tar.gz",
        sha256="e58a43cebf0cea071ee69c0106a7edaaec9a6fb7022f13d091a0bd43bf85e2d5",
        preferred=True,
    )

    def install(self, spec, prefix):
        sh = which("sh")
        sh("./install.sh", "-y", "--prefix=" + prefix)
