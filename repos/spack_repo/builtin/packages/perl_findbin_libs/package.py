# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlFindbinLibs(PerlPackage):
    """FindBin::libs - locate and a 'use lib' or export directories based on $FindBin::Bin."""

    homepage = "https://metacpan.org/pod/FindBin::libs"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEMBARK/FindBin-libs-v4.0.4.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    maintainers("w8jcik")

    version("4.0.4", sha256="2e39c663aa69b9a63f76a05503c1a7db28df266c335d8e4870b4e43f743f1b72")

    depends_on("perl-data-dump")
    depends_on("perl-file-copy-recursive-reduced")
