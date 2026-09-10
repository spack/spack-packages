# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libksba(AutotoolsPackage):
    """Libksba is a library to make the tasks of working with X.509
    certificates, CMS data and related objects easier.
    """

    homepage = "https://gnupg.org/software/libksba/index.html"
    url = "https://gnupg.org/ftp/gcrypt/libksba/libksba-1.3.5.tar.bz2"

    maintainers("alalazo")

    license("LGPL-3.0-only AND GPL-2.0-only AND GPL-3.0-only")

    version("1.8.0", sha256="296b9db9095749f2aa104202d7ab7fd09ad10710e00780a709c9754b1a1d9292")
    version("1.7.0", sha256="e1d3a5745911f5a663fddecf526541c4241052a9e4cafbc92dc7f4096c7efdac")
    version("1.6.8", sha256="0f4510f1c7a679c3545990a31479f391ad45d84e039176309d42f80cf41743f5")
    version("1.6.7", sha256="cf72510b8ebb4eb6693eef765749d83677a03c79291a311040a5bfd79baab763")
    version("1.6.6", sha256="5dec033d211559338838c0c4957c73dfdc3ee86f73977d6279640c9cd08ce6a4")
    version("1.6.5", sha256="a564628c574c99287998753f98d750babd91a4e9db451f46ad140466ef2a6d16")
    version("1.6.4", sha256="bbb43f032b9164d86c781ffe42213a83bf4f2fee91455edfa4654521b8b03b6b")
    version("1.6.3", sha256="3f72c68db30971ebbf14367527719423f0a4d5f8103fc9f4a1c01a9fa440de5c")

    depends_on("c", type="build")  # generated

    # Versions before 1.6.3 were deprecated over CVE-2022-3515
    # (https://gnupg.org/blog/20221017-pepe-left-the-ksba.html)

    depends_on("libgpg-error@1.8:")

    def configure_args(self):
        return [
            "--enable-static",
            "--enable-shared",
            f"--with-libgpg-error-prefix={self.spec['libgpg-error'].prefix}",
        ]
