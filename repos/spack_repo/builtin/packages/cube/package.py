# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Cube(AutotoolsPackage):
    """Cube the profile viewer for Score-P and Scalasca profiles. It displays a
    multi-dimensional performance space consisting of the dimensions:
    - performance metric
    - call path
    - system resource
    """

    homepage = "https://www.scalasca.org/software/cube-4.x/download.html"
    url = "https://apps.fz-juelich.de/scalasca/releases/cube/4.4/dist/cubegui-4.4.2.tar.gz"
    maintainers("swat-jsc")

    version("4.9", sha256="10c76d6e3d44df64066d087a0ee9195b4e8121798a84a4d8bdc1da0e80837e11")
    version("4.8.2", sha256="bf2e02002bb2e5c4f61832ce37b62a440675c6453463014b33b2474aac78f86d")
    version("4.8.1", sha256="a8a2a62b4e587c012d3d32385bed7c500db14232419795e0f4272d1dcefc55bc")
    version("4.8", sha256="1df8fcaea95323e7eaf0cc010784a41243532c2123a27ce93cb7e3241557ff76")
    version("4.7.1", sha256="7c96bf9ffb8cc132945f706657756fe6f88b7f7a5243ecd3741f599c2006d428")
    version("4.7", sha256="103fe00fa9846685746ce56231f64d850764a87737dc0407c9d0a24037590f68")
    version("4.6", sha256="1871c6736121d94a22314cb5daa8f3cbb978b58bfe54f677c4c9c9693757d0c5")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cubelib@4.9", when="@4.9")
    depends_on("cubelib@4.8", when="@4.8")
    depends_on("cubelib@4.7", when="@4.7")
    depends_on("cubelib@4.6", when="@4.6")

    depends_on("pkgconfig", type="build")
    depends_on("dbus")
    depends_on("zlib-api")

    depends_on("qt@5:")

    def url_for_version(self, version):
        url = "https://apps.fz-juelich.de/scalasca/releases/cube/{0}/dist/cubegui-{1}.tar.gz"

        return url.format(version.up_to(2), version)

    def configure_args(self):
        return ["--enable-shared"]

    def install(self, spec, prefix):
        make("install", parallel=False)
