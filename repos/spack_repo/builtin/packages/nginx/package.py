# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Nginx(AutotoolsPackage):
    """nginx [engine x] is an HTTP and reverse proxy server, a mail proxy
    server, and a generic TCP/UDP proxy server, originally written by Igor
    Sysoev."""

    homepage = "https://nginx.org/en/"
    url = "https://nginx.org/download/nginx-1.12.0.tar.gz"

    license("BSD-2-Clause")

    version("1.26.0", sha256="d2e6c8439d6c6db5015d8eaab2470ab52aef85a7bf363182879977e084370497")
    version("1.24.0", sha256="77a2541637b92a621e3ee76776c8b7b40cf6d707e69ba53a940283e30ff2f55d")
    version("1.23.4", sha256="d43300e36bb249a7e6edc60bca1b0fc372a0bafce2f346d76acfb677a8790fc0")
    version("1.23.3", sha256="75cb5787dbb9fae18b14810f91cc4343f64ce4c24e27302136fb52498042ba54")
    version("1.21.3", sha256="14774aae0d151da350417efc4afda5cce5035056e71894836797e1f6e2d1175a")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("openssl")
    depends_on("pcre")
    depends_on("zlib-api")

    def configure_args(self):
        args = ["--with-http_ssl_module"]
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        """Prepend the sbin directory to PATH."""
        env.prepend_path("PATH", self.prefix.sbin)
