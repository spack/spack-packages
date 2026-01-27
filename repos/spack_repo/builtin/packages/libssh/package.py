# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libssh(CMakePackage):
    """libssh: the SSH library"""

    homepage = "https://www.libssh.org"
    url = "https://www.libssh.org/files/0.11/libssh-0.11.3.tar.xz"
    list_url = "https://www.libssh.org/files"
    list_depth = 1

    version("0.11.3", sha256="7d8a1361bb094ec3f511964e78a5a4dba689b5986e112afabe4f4d0d6c6125c3")
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
