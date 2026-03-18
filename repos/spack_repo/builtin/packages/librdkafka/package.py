# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Librdkafka(AutotoolsPackage):
    """librdkafka is a C library implementation of the Apache Kafka
    protocol."""

    homepage = "https://github.com/edenhill/librdkafka"
    url = "https://github.com/edenhill/librdkafka/archive/v1.5.0.tar.gz"

    license("BSD-2-Clause")

    version("2.13.2", sha256="14972092e4115f6e99f798a7cb420cbf6daa0c73502b3c52ae42fb5b418eea8f")
    version("2.13.0", sha256="3bd351601d8ebcbc99b9a1316cae1b83b00edbcf9411c34287edf1791c507600")
    version("2.12.1", sha256="ec103fa05cb0f251e375f6ea0b6112cfc9d0acd977dc5b69fdc54242ba38a16f")
    version("2.12.0", sha256="1355d81091d13643aed140ba0fe62437c02d9434b44e90975aaefab84c2bf237")
    version("2.11.1", sha256="a2c87186b081e2705bb7d5338d5a01bc88d43273619b372ccb7bb0d264d0ca9f")
    version("2.8.0", sha256="5bd1c46f63265f31c6bfcedcde78703f77d28238eadf23821c2b43fc30be3e25")
    version("2.6.1", sha256="0ddf205ad8d36af0bc72a2fec20639ea02e1d583e353163bf7f4683d949e901b")
    version("2.6.0", sha256="abe0212ecd3e7ed3c4818a4f2baf7bf916e845e902bb15ae48834ca2d36ac745")
    version("2.5.3", sha256="eaa1213fdddf9c43e28834d9a832d9dd732377d35121e42f875966305f52b8ff")
    version("2.2.0", sha256="af9a820cbecbc64115629471df7c7cecd40403b6c34bfdbb9223152677a47226")
    version("2.1.1", sha256="7be1fc37ab10ebdc037d5c5a9b35b48931edafffae054b488faaff99e60e0108")
    version("2.1.0", sha256="d8e76c4b1cde99e283a19868feaaff5778aa5c6f35790036c5ef44bc5b5187aa")
    version("2.0.2", sha256="f321bcb1e015a34114c83cf1aa7b99ee260236aab096b85c003170c90a47ca9d")
    version("1.9.2", sha256="3fba157a9f80a0889c982acdd44608be8a46142270a389008b22d921be1198ad")
    version("1.5.0", sha256="f7fee59fdbf1286ec23ef0b35b2dfb41031c8727c90ced6435b8cf576f23a656")
    version("1.4.4", sha256="0984ffbe17b9e04599fb9eceb16cfa189f525a042bef02474cd1bbfe1ea68416")
    version("1.4.2", sha256="3b99a36c082a67ef6295eabd4fb3e32ab0bff7c6b0d397d6352697335f4e57eb")

    variant("sasl", default=True, description="Enable SASL")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("pkgconfig", type="build")
    depends_on("zstd")
    depends_on("lz4")
    depends_on("curl")
    depends_on("openssl")
    depends_on("zlib")
    depends_on("cyrus-sasl", when="+sasl")
