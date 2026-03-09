# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyjwt(PythonPackage):
    """JSON Web Token implementation in Python"""

    homepage = "https://github.com/jpadilla/pyjwt"
    pypi = "pyjwt/pyjwt-1.7.1.tar.gz"
    git = "https://github.com/jpadilla/pyjwt.git"

    license("MIT")

    version("2.11.0", sha256="35f95c1f0fbe5d5ba6e43f00271c275f7a1a4db1dab27bf708073b75318ea623")
    version("2.4.0", sha256="d42908208c699b3b973cbeb01a969ba6a96c821eefb1c5bfe4c390c01d67abba")
    version("2.1.0", sha256="fba44e7898bbca160a2b2b501f492824fc8382485d3a6f11ba5d0c1937ce6130")
    version("1.7.1", sha256="8d59a976fb773f3e6a39c85636357c4f0e242707394cadadd9814f5cbaa20e96")

    variant(
        "crypto", default=False, description="Build with cryptography support", when="@:2.0,2.4:"
    )

    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))
    depends_on("python@3.6:", when="@2.1.0:", type=("build", "run"))
    depends_on("python@3.9:", when="@2.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cryptography@1.4:", when="+crypto", type=("build", "run"))
    depends_on("py-cryptography@3.3.1:", when="@2.4: +crypto", type=("build", "run"))
    depends_on("py-cryptography@3.4.0:", when="@2.10: +crypto", type=("build", "run"))

    # With PyJWT 2.5.0, the tarfile changed from PyJWT-2.4.0.tar.gz to pyjwt-2.5.0.tar.gz
    def url_for_version(self, version):
        if version >= Version("2.5.0"):
            url = "https://pypi.io/packages/source/p/pyjwt/pyjwt-{0}.tar.gz"
        else:
            url = "https://pypi.io/packages/source/P/PyJWT/PyJWT-{0}.tar.gz"
        return url.format(version.dotted)

