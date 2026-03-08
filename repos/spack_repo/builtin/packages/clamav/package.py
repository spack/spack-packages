# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Clamav(AutotoolsPackage):
    """Open source antivirus engine for detecting trojans,
    viruses, malware & other malicious threats."""

    homepage = "https://www.clamav.net/"
    url = "https://www.clamav.net/downloads/production/clamav-0.101.2.tar.gz"

    license("GPL-2.0-only")

    # clamav 0.101.2 is affected by multiple HIGH CVEs:
    # - CVE-2019-12625 (CVSS 7.5 HIGH): Zip bomb causes unauthenticated remote DoS
    # - CVE-2020-3341 (CVSS 7.5 HIGH): PDF parser flaw causes unauthenticated DoS
    # - CVE-2022-20770 (CVSS 8.6 HIGH): CHM file parsing allows unauthenticated DoS
    # Fixed in 0.103.x+. Note: clamav 0.103.x and later use CMake; this package
    # needs a build system update to support versions beyond 0.101.x.
    with default_args(deprecated=True):
        version("0.101.2", sha256="0a12ebdf6ff7a74c0bde2bdc2b55cae33449e6dd953ec90824a9e01291277634")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build")
    depends_on("json-c")
    depends_on("openssl")
    depends_on("pcre")
    depends_on("yara")
    depends_on("zlib-api")
    depends_on("bzip2")
    depends_on("curl", type="link")

    def configure_args(self):
        spec = self.spec
        args = [
            "--enable-llvm=no",
            "--with-libjson=%s" % spec["json-c"].prefix,
            "--with-openssl=%s" % spec["openssl"].prefix,
            "--with-pcre=%s" % spec["pcre"].prefix,
            "--with-zlib=%s" % spec["zlib-api"].prefix,
            "--with-bzip2=%s" % spec["bzip2"].prefix,
        ]
        return args
