# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Apr(AutotoolsPackage):
    """Apache portable runtime."""

    homepage = "https://apr.apache.org/"
    url = "https://archive.apache.org/dist/apr/apr-1.7.0.tar.gz"

    license("Apache-2.0", checked_by="wdconinc")

    version("1.7.5", sha256="3375fa365d67bcf945e52b52cba07abea57ef530f40b281ffbe977a9251361db")

    depends_on("c", type="build")

    depends_on("uuid", type="link")

    @property
    def libs(self):
        return find_libraries(
            [f"libapr-{self.version.up_to(1)}"], root=self.prefix, recursive=True
        )
