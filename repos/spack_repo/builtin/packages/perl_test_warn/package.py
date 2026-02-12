# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlTestWarn(PerlPackage):
    """Perl extension to test methods for warnings"""

    homepage = "https://metacpan.org/pod/Test::Warn"
    url = "https://cpan.metacpan.org/authors/id/B/BI/BIGJ/Test-Warn-0.37.tar.gz"

    maintainers("EbiArnie")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.37", sha256="98ca32e7f2f5ea89b8bfb9a0609977f3d153e242e2e51705126cb954f1a06b57")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))
    depends_on("perl-sub-uplevel@0.12:", type=("build", "run", "test"))
