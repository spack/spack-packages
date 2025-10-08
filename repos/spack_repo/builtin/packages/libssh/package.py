# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libssh(CMakePackage):
    """libssh: the SSH library"""

    homepage = "https://www.libssh.org"
    url = "https://www.libssh.org/files/0.11/libssh-0.11.2.tar.xz"
    list_url = "https://www.libssh.org/files"
    list_depth = 1

    version("0.11.2", sha256="69529fc18f5b601f0baf0e5a4501a2bc26df5e2f116f5f8f07f19fafaa6d04e7")

    variant("gssapi", default=True, description="Build with gssapi support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")
    depends_on("openssl@1.1.1:")
    depends_on("openssl")
    depends_on("zlib-api")
    depends_on("krb5", when="+gssapi")

    def url_for_version(self, version):
        url = "https://www.libssh.org/files/{0}/libssh-{1}.tar.xz"
        return url.format(version.up_to(2), version)

    def cmake_args(self):
        args = [self.define_from_variant("WITH_GSSAPI", "gssapi")]
        return args
