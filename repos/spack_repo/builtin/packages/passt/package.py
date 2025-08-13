# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Passt(MakefilePackage):
    """Passt provides full, quasi-native network connectivity to
    virtual machines in user-mode without requiring any capabilities or privileges."""

    homepage = "https://passt.top"

    license("GPL-2.0-or-later", checked_by="cmelone")

    version(
        "2025_01_21.4f2c8e7",
        sha256="1f3dc31502b4fa7c997c9f029e2472b7055bdee956f49551f4187fc75b7cbe13",
        url="https://passt.top/passt/snapshot/passt-2025_01_21.4f2c8e7.tar.gz",
    )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make()
        install("passt", prefix.bin)
        install("pasta", prefix.bin)
