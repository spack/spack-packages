# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class LibcapNg(AutotoolsPackage):
    """Libcap-ng is a library that makes using posix capabilities easier"""

    homepage = "https://people.redhat.com/sgrubb/libcap-ng/"
    url = "https://people.redhat.com/sgrubb/libcap-ng/libcap-ng-0.8.5.tar.gz"

    license("GPL-2.0-or-later AND LGPL-2.1-or-later")

    version("0.8.5", sha256="3ba5294d1cbdfa98afaacfbc00b6af9ed2b83e8a21817185dfd844cc8c7ac6ff")
    version("0.8.3", sha256="bed6f6848e22bb2f83b5f764b2aef0ed393054e803a8e3a8711cb2a39e6b492d")
    version("0.8", sha256="f14d23b60ae1465b032e4e8cbd4112006572c69a6017d55d5d3c6aad622a9e21")
    version("0.7.11", sha256="85815c711862d01a440db471f12fba462c9949e923966f5859607e652d9c0ae9")
    version("0.7.10", sha256="a84ca7b4e0444283ed269b7a29f5b6187f647c82e2b876636b49b9a744f0ffbf")

    depends_on("c", type="build")

    depends_on("attr", type="build")
    depends_on("swig", type="build")
    depends_on("python@2.7:", type=("build", "link", "run"), when="+python")

    variant("python", default=True, description="Enable python")

    extends("python", when="+python")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+python"):
            env.set("PYTHON", python.path)

    def configure_args(self):
        args = []
        spec = self.spec
        if spec.satisfies("+python"):
            if spec.satisfies("^python@3:"):
                args.extend(["--without-python", "--with-python3"])
            else:
                args.extend(["--with-python", "--without-python3"])
        else:
            args.extend(["--without-python", "--without-python3"])
        return args
