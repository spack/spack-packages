# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlLibwwwPerl(PerlPackage):
    """The libwww-perl collection is a set of Perl modules which provides
    a simple and consistent application programming interface to the
    World-Wide Web. The main focus of the library is to provide classes and
    functions that allow you to write WWW clients."""

    homepage = "https://github.com/libwww-perl/libwww-perl"
    url = "http://search.cpan.org/CPAN/authors/id/O/OA/OALDERS/libwww-perl-6.33.tar.gz"

    license("Artistic-1.0")

    version("6.83", sha256="e75f0fa9d3c6f0daf5a5a72fa9f8b1c9c0d23e3a84a8522ccb4f835232b95505")
    version("6.68", sha256="42784a5869855ee08522dfb1d30fccf98ca4ddefa8c6c1bcb0d68a0adceb7f01")
    version("6.33", sha256="97417386f11f007ae129fe155b82fd8969473ce396a971a664c8ae6850c69b99")
    version("6.29", sha256="4c6f2697999d2d0e6436b584116b12b30dc39990ec0622751c1a6cec2c0e6662")

    with default_args(type=("build", "run")):
        depends_on("perl-encode-locale")
        depends_on("perl-file-listing")
        # provides HTML::Entities and HTML::HeadParser
        depends_on("perl-html-parser")
        depends_on("perl-http-cookies")
        depends_on("perl-http-date")
        # provides HTTP::Request, HTTP::Request::Common, HTTP::Response and HTTP::Status
        depends_on("perl-http-message@7.01:", when="@6.81:")
        depends_on("perl-http-message")
        depends_on("perl-http-negotiate")
        depends_on("perl-lwp-mediatypes")
        depends_on("perl-net-http@6.18:")
        depends_on("perl-try-tiny")
        depends_on("perl-uri")
        depends_on("perl-www-robotrules")

        # dependencies ignored because in core:
        # Digest::MD5, File::Copy, File::Temp, Getopt::Long, IO::Select,
        # IO::Socket, MIME::Base64, Module::Load, Net::FTP, Scalar::Util,
        # parent, strict, warnings

        # Historical dependencies
        depends_on("perl-http-daemon", when="@:6.52")
