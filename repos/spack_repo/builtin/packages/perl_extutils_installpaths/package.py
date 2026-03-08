# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlExtutilsInstallpaths(PerlPackage):
    """ExtUtils::InstallPaths - Build.PL install path logic made easy"""

    homepage = "https://metacpan.org/pod/ExtUtils::InstallPaths"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-InstallPaths-0.012.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.015", sha256="7d64eb2dfa87ead010cdf55c8a1bdfde50b7b5852d7cb8cf2304f55bea2eb007")  # FIXME
    version("0.014", sha256="ae65d20cc3c7e14b3cd790915c84510f82dfb37a4c9b88aa74b2e843af417d01")  # FIXME
    version("0.013", sha256="65969d3ad8a3a2ea8ef5b4213ed5c2c83961bb5bd12f7ad35128f6bd5b684aa0")
    version("0.012", sha256="84735e3037bab1fdffa3c2508567ad412a785c91599db3c12593a50a1dd434ed")

    depends_on("perl-extutils-config", type=("build", "run"))
