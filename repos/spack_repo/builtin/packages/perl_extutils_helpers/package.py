# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlExtutilsHelpers(PerlPackage):
    """ExtUtils::Helpers - Various portability utilities for module builders"""

    homepage = "https://metacpan.org/pod/ExtUtils::Helpers"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-Helpers-0.026.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.028", sha256="c8574875cce073e7dc5345a7b06d502e52044d68894f9160203fcaab379514fe")
    version("0.027", sha256="9d592131dc5845a86dc28be9143f764e73cb62db06fedf50a895be1324b6cec5")
    version("0.026", sha256="de901b6790a4557cf4ec908149e035783b125bf115eb9640feb1bc1c24c33416")
