# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlStatisticsRegression(PerlPackage):
    """Weighted linear regression (line+plane fitting)"""

    homepage = "https://metacpan.org/pod/Statistics::Regression"
    url = "https://cpan.metacpan.org/authors/id/I/IA/IAWELCH/Statistics-Regression-0.53.tar.gz"

    license("GPL-1.0-or-later")

    maintainers("w8jcik")

    version("0.53", sha256="2cc53e3996dda4dceb5d7a794ba15107adb7a6614e19b485c0b8e47a5ab8b69a")

    depends_on("perl-module-install", type="build")

    depends_on("perl-test-pod", type="test")
