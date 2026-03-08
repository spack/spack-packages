# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlTryTiny(PerlPackage):
    """Minimal try/catch with proper preservation of $@"""

    homepage = "https://metacpan.org/pod/Try::Tiny"
    url = "http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Try-Tiny-0.28.tar.gz"

    license("MIT")

    version(
        "0.32", sha256="ef2d6cab0bad18e3ab1c4e6125cc5f695c7e459899f512451c8fa3ef83fa7fc0"
    )  # FIXME
    version("0.31", sha256="3300d31d8a4075b26d8f46ce864a1d913e0e8467ceeba6655d5d2b2e206c11be")
    version("0.28", sha256="f1d166be8aa19942c4504c9111dade7aacb981bc5b3a2a5c5f6019646db8c146")
