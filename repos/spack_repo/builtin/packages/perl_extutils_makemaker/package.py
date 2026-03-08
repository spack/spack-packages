# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlExtutilsMakemaker(PerlPackage):
    """ExtUtils::MakeMaker - Create a module Makefile. This utility is designed
    to write a Makefile for an extension module from a Makefile.PL. It is based
    on the Makefile.SH model provided by Andy Dougherty and the perl5-porters.
    """

    homepage = "https://github.com/Perl-Toolchain-Gang/ExtUtils-MakeMaker"
    url = "http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/ExtUtils-MakeMaker-7.24.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("7.76", sha256="30bcfd75fec4d512e9081c792f7cb590009d9de2fe285ffa8eec1be35a5ae7ca")
    version("7.75_01", sha256="530bdf61bbb1253f793bbfcaed2d5f6bc3e97f0bfb170b4101f94f220ac6116d")
    version("7.74", sha256="8ad2be00713b49dcfd386286e0a64ff9297b771a485f2425fbc144794f5a3e8c")
    version("7.73_01", sha256="3ecdf30f345ae318f5ebf6543e01f6456ae9f454f782fd556969ce298698b086")
    version("7.72", sha256="38c892019a3bc4e7b78c1c58356eb39aa1dd32a035981c4e7b487d01091a45d2")
    version("7.71_08", sha256="edbeb9e58cc3fa0c79faee3f13f33c483b06e76ab922ae078f7ed1a3481656b5")
    version("7.71_07", sha256="05e950b3c8d6ea594f2abff1072ffb79f0b53d87be2517f1739793e4c742b19c")
    version("7.71_06", sha256="c5a5efc24488cb8d8e1202318996e266a3287bb8c17be8236f605ee63102e563")
    version("7.71_05", sha256="bfbb6fb6bb661b60903bc5304028ad0ed557c408f1f5026f62523865a8fa1aec")
    version("7.71_04", sha256="776bb4d483cbbdc46c74db3ecddd51f17d2576a7647e772d50c35aef690953a0")
    version("7.71_03", sha256="b1081d1d0f42493c6b157e6e76117f6f37085dddd03bd31898ba7f5fbb2c9c23")
    version("7.71_02", sha256="57a1074f39821cd962a472b59a09d4664ce082ce76ea20663e2aef02e12de285")
    version("7.71_01", sha256="45962f4000347cd03a983791bd37d57778647751d75c353a2cf51c186da86d9d")
    version("7.70", sha256="f108bd46420d2f00d242825f865b0f68851084924924f92261d684c49e3e7a74")
    version("7.68", sha256="270238d253343b833daa005fb57a3a5d8916b59da197698a632b141e7acad779")
    version("7.24", sha256="416abc97c3bb2cc72bef28852522f2859de53e37bf3d0ae8b292067d78755e69")

    depends_on("perl@5.6.0:", type=("build", "run"))
