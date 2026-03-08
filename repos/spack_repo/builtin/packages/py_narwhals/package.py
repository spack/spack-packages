# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNarwhals(PythonPackage):
    """Extremely lightweight compatibility layer between dataframe libraries"""

    homepage = "https://github.com/narwhals-dev/narwhals"
    pypi = "narwhals/narwhals-1.8.1.tar.gz"

    version("2.16.0", sha256="155bb45132b370941ba0396d123cf9ed192bf25f39c4cea726f2da422ca4e145")
    version("2.15.0", sha256="a9585975b99d95084268445a1fdd881311fa26ef1caa18020d959d5b2ff9a965")
    version("2.14.0", sha256="98be155c3599db4d5c211e565c3190c398c87e7bf5b3cdb157dece67641946e0")
    version("2.13.0", sha256="ee94c97f4cf7cfeebbeca8d274784df8b3d7fd3f955ce418af998d405576fdd9")
    version("2.12.0", sha256="075b6d56f3a222613793e025744b129439ecdff9292ea6615dd983af7ba6ea44")
    version("2.11.0", sha256="d23f3ea7efc6b4d0355444a72de6b8fa3011175585246c3400c894a7583964af")
    version("2.10.2", sha256="ff738a08bc993cbb792266bec15346c1d85cc68fdfe82a23283c3713f78bd354")
    version("2.9.0", sha256="d8cde40a6a8a7049d8e66608b7115ab19464acc6f305d136a8dc8ba396c4acfe")
    version("2.8.0", sha256="52e0b22d54718264ae703bd9293af53b04abc995a1414908c3b807ba8c913858")
    version("2.7.0", sha256="e3fff7f1610fd3318ede78c969bc5954ce710d585eefdb689586fb69da3da43c")
    version("2.6.0", sha256="5c9e2ba923e6a0051017e146184e49fb793548936f978ce130c9f55a9a81240e")
    version("2.5.0", sha256="8ae0b6f39597f14c0dc52afc98949d6f8be89b5af402d2d98101d2f7d3561418")
    version("2.4.0", sha256="a71931f7fb3c8e082cbe18ef0740644d87d60eba841ddfa9ba9394de1d43062f")
    version("2.3.0", sha256="b66bc4ab7b6746354f60c4b3941e3ce60c066588c35360e2dc6c063489000a16")
    version("1.38.0", sha256="0a356a21ad00de0db0e631332a823a6a6755544bd10b8e68a02d75029c71392e")
    version("1.8.1", sha256="97527778e11f39a1e5e2113b8fbb9ead788be41c0337f21852e684e378f583e8")

    depends_on("python@3.9:", type=("build", "run"), when="@1.43:")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type=("build"))
