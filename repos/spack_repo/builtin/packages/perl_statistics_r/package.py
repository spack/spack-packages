# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlStatisticsR(PerlPackage):
    """Perl interface with the R statistical program."""

    homepage = "https://metacpan.org/pod/Statistics::R"
    url = "https://cpan.metacpan.org/authors/id/F/FA/FANGLY/Statistics-R-0.34.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    maintainers("w8jcik")

    version("0.34", sha256="782dd064876ac94680d97899f24fb0e727df42c05ba474ec096a9116438fbed4")

    depends_on("perl-ipc-run")
    depends_on("perl-module-install")
    depends_on("perl-regexp-common")
    depends_on("r")
