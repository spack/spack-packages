# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libssh(CMakePackage):
    """libssh: the SSH library"""

    homepage = "https://www.libssh.org"
    url = "https://www.libssh.org/files/0.12/libssh-0.12.0.tar.xz"
    list_url = "https://www.libssh.org/files"
    list_depth = 1

    version("0.12.0", sha256="1a6af424d8327e5eedef4e5fe7f5b924226dd617ac9f3de80f217d82a36a7121")
    version("0.11.4", sha256="002ac320e3d66c9e100ec6576e3e84aa0c48949efde3bf5b40a2802992297701")
    # Previous versions deprecated because of CVEs
    version(
        "0.11.3",
        sha256="7d8a1361bb094ec3f511964e78a5a4dba689b5986e112afabe4f4d0d6c6125c3",
        deprecated=True,
    )
    # Previous versions removed because of CVEs

    variant("gssapi", default=True, description="Build with gssapi support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")
    depends_on("openssl@1.1.1:")
    depends_on("zlib-api")
    depends_on("krb5", when="+gssapi")

    def url_for_version(self, version):
        url = "https://www.libssh.org/files/{0}/libssh-{1}.tar.xz"
        return url.format(version.up_to(2), version)

    def cmake_args(self):
        args = [self.define_from_variant("WITH_GSSAPI", "gssapi")]
        return args
