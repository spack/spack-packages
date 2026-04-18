# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Cubelib(AutotoolsPackage):
    """Component of CubeBundle: General purpose C++ library and tools"""

    homepage = "https://www.scalasca.org/software/cube-4.x/download.html"
    url = "https://apps.fz-juelich.de/scalasca/releases/cube/4.4/dist/cubelib-4.4.tar.gz"

    maintainers("swat-jsc", "wrwilliams")
    version("4.9", sha256="a0658f5bf3f74bf7dcf465ab6e30476751ad07eb93618801bdcf190ba3029443")
    version("4.8.2", sha256="d6fdef57b1bc9594f1450ba46cf08f431dd0d4ae595c47e2f3454e17e4ae74f4")
    version("4.8.1", sha256="e4d974248963edab48c5d0fc5831146d391b0ae4632cccafe840bf5f12cd80a9")
    version("4.8", sha256="171c93ac5afd6bc74c50a9a58efdaf8589ff5cc1e5bd773ebdfb2347b77e2f68")
    version("4.7.1", sha256="62cf33a51acd9a723fff9a4a5411cd74203e24e0c4ffc5b9e82e011778ed4f2f")
    version("4.7", sha256="e44352c80a25a49b0fa0748792ccc9f1be31300a96c32de982b92477a8740938")
    version("4.6", sha256="36eaffa7688db8b9304c9e48ca5dc4edc2cb66538aaf48657b9b5ccd7979385b")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build")
    depends_on("zlib-api")

    def url_for_version(self, version):
        url = "https://apps.fz-juelich.de/scalasca/releases/cube/{0}/dist/cubelib-{1}.tar.gz"

        return url.format(version.up_to(2), version)

    def configure_args(self):
        configure_args = ["--enable-shared"]
        configure_args.append("--with-frontend-zlib=%s" % self.spec["zlib-api"].prefix.lib)
        return configure_args

    def install(self, spec, prefix):
        make("install", parallel=False)
