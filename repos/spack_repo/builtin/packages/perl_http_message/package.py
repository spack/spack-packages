# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlHttpMessage(PerlPackage):
    """HTTP style message (base class)"""

    homepage = "https://metacpan.org/pod/HTTP::Message"
    url = "http://search.cpan.org/CPAN/authors/id/O/OA/OALDERS/HTTP-Message-6.13.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("7.04", sha256="699f3350dbb7bd8fdc9f3b013b0c91b7c059783708443e39bc395fa33352f006")
    version("6.45", sha256="01cb8406612a3f738842d1e97313ae4d874870d1b8d6d66331f16000943d4cbe")
    version("6.44", sha256="398b647bf45aa972f432ec0111f6617742ba32fc773c6612d21f64ab4eacbca1")
    version("6.13", sha256="f25f38428de851e5661e72f124476494852eb30812358b07f1c3a289f6f5eded")

    depends_on("perl-extutils-makemaker", type="build")

    with default_args(type=("build", "run")):
        depends_on("perl-clone@0.46:", when="@6.44:")
        depends_on("perl-compress-raw-bzip2")
        depends_on("perl-compress-raw-zlib")
        depends_on("perl-encode-locale")
        depends_on("perl-http-date")
        depends_on("perl-io-html")
        depends_on("perl-lwp-mediatypes")
        depends_on("perl-uri")
