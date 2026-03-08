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

    version("6.81", sha256="ab30552f194e8b5ae3ac0885132fd1d4ea04c4c7fe6555765b98f01af70c1736")
    version("6.80", sha256="5ba3fc5a00836e61cb428bcd91bf69d8d74eaee6d78e44c3a414f78076af0a98")
    version("6.79", sha256="f2526e9a33ac96715cc47fbf5b4bec1a8c51720330b24e3974c2c5ae07a9c5e7")
    version("6.78", sha256="b738bdcf54e2c6bb81fd2b83ec47bc83347f97b371ea80f0dc10360f817a9a44")
    version("6.77", sha256="94a907d6b3ea8d966ef43deffd4fa31f5500142b4c00489bfd403860a5f060e4")
    version("6.76", sha256="75c2e57d6102eea540f3611b56fd86268a59b022dd00ea6562ac36412fcdf8e1")
    version("6.75", sha256="b3df1420af48301ca9e5a6c1f241802b0ac32fabd57ee5253e0cfd97d0f43462")
    version("6.74", sha256="2a49d361e79b3509d8150290901a4e3bea3603291887306a88cc93fbbfa5b19a")
    version("6.73", sha256="41afb949b5ab95251bed45defcbd3811b75fc41d1b6ba48003fcd7704f86db3c")
    version("6.72", sha256="e9b8354fd5e20be207afe23ddd584fcd59bf82998dc077decf684ba1dae5a05d")
    version("6.71", sha256="9d852d92c1f087d838adcb4107c4ff69887e7e5bdb742f984639c4c18dddb6e7")
    version("6.68", sha256="42784a5869855ee08522dfb1d30fccf98ca4ddefa8c6c1bcb0d68a0adceb7f01")
    version("6.33", sha256="97417386f11f007ae129fe155b82fd8969473ce396a971a664c8ae6850c69b99")
    version("6.29", sha256="4c6f2697999d2d0e6436b584116b12b30dc39990ec0622751c1a6cec2c0e6662")

    depends_on("perl-clone", type=("build", "run"))
    depends_on("perl-encode-locale", type=("build", "run"))
    depends_on("perl-file-listing", type=("build", "run"))
    depends_on("perl-html-parser", type=("build", "run"))
    depends_on("perl-http-cookies", type=("build", "run"))
    depends_on("perl-http-daemon", type=("build", "run"))
    depends_on("perl-http-date", type=("build", "run"))
    depends_on("perl-http-message", type=("build", "run"))
    depends_on("perl-http-negotiate", type=("build", "run"))
    depends_on("perl-lwp-mediatypes", type=("build", "run"))
    depends_on("perl-net-http", type=("build", "run"))
    depends_on("perl-try-tiny", type=("build", "run"))
    depends_on("perl-uri", type=("build", "run"))
    depends_on("perl-www-robotrules", type=("build", "run"))
