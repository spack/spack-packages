# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlFileCopyRecursiveReduced(PerlPackage):
    """Recursive copying of files and directories."""

    homepage = "https://metacpan.org/pod/File::Copy::Recursive::Reduced"
    url = "https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/File-Copy-Recursive-Reduced-0.008.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    maintainers("w8jcik")

    version("0.008", sha256="462bd66bf55e74b78f29ebdc9626af622d4f0115b5191b03167e82164db98f5a")

    depends_on("perl-capture-tiny", type="build")
    depends_on("perl-path-tiny", type="build")
