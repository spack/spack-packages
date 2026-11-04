# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlSocket(PerlPackage):
    """Networking constants and support functions."""

    homepage = "https://metacpan.org/dist/Socket"
    url = "https://www.cpan.org/authors/id/P/PE/PEVANS/Socket-2.043.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("2.043", sha256="236aab8262e928d05be0bb0a68fae9e829913f9d3fa4bb6aebba9e30edb189ad")
