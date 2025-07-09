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

    with default_args(deprecated=True):
        # Due to various CVEs
        # https://www.libssh.org/2025/06/24/libssh-0-11-2-security-and-bugfix-release/
        version(
            "0.11.0", sha256="860e814579e7606f3fc3db98c5807bef2ab60f793ec871d81bcd23acdcdd3e91"
        )
        version(
            "0.10.6", sha256="1861d498f5b6f1741b6abc73e608478491edcf9c9d4b6630eef6e74596de9dc1"
        )
        version("0.9.8", sha256="9f834b732341d428d67bbe835b7d10ae97ccf25d6f5bd0288fa51ae683f2e7cd")
        # https://nvd.nist.gov/vuln/detail/CVE-2023-48795
        # https://nvd.nist.gov/vuln/detail/CVE-2023-6918
        # https://nvd.nist.gov/vuln/detail/CVE-2023-6004
        version("0.8.9", sha256="8559e19da0c40b6f93482b6160219ad77a4d9f1dc190bf174757455c6ae26825")
        version("0.8.5", sha256="07d2c431240fc88f6b06bcb36ae267f9afeedce2e32f6c42f8844b205ab5a335")
        version("0.7.5", sha256="54e86dd5dc20e5367e58f3caab337ce37675f863f80df85b6b1614966a337095")

    variant("gssapi", default=True, description="Build with gssapi support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build", when="@0.11:")
    depends_on("cmake@3.3:", type="build", when="@0.8:0.10")
    depends_on("cmake@2.8.5:", type="build", when="@0.7")
    depends_on("openssl@1.1.1:", when="@0.11:")
    depends_on("openssl@:1.0", when="@:0.7")
    depends_on("openssl")
    depends_on("zlib-api")
    depends_on("krb5", when="+gssapi")

    def url_for_version(self, version):
        url = "https://www.libssh.org/files/{0}/libssh-{1}.tar.xz"
        return url.format(version.up_to(2), version)

    def cmake_args(self):
        args = [self.define_from_variant("WITH_GSSAPI", "gssapi")]
        return args
