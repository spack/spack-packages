# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlIoSocketIp(PerlPackage):
    """Family-neutral IP socket supporting both IPv4 and IPv6."""

    homepage = "https://metacpan.org/dist/IO-Socket-IP"
    url = "https://www.cpan.org/authors/id/P/PE/PEVANS/IO-Socket-IP-0.44.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.44", sha256="dc39242154baf276a9b4802a2a56b9e769a8ec67b4c2fb7e089b68e3666cf289")

    depends_on("perl-module-build", type="build")

    depends_on("perl-socket", type=("build", "run"))
