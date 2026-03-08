# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPbr(PythonPackage):
    """PBR is a library that injects some useful and sensible default
    behaviors into your setuptools run."""

    pypi = "pbr/pbr-5.4.3.tar.gz"

    # Skip 'pbr.tests' imports
    import_modules = ["pbr", "pbr.cmd", "pbr.hooks"]

    version("7.0.3", sha256="b46004ec30a5324672683ec848aed9e8fc500b0d261d40a3229c2d2bbfcedc29")  # FIXME
    version("7.0.2", sha256="2a598b3d930f260576888932969b3b7dbcaa1d86505f9317dbd34b4a83eaf7ad")
    version("7.0.1", sha256="3ecbcb11d2b8551588ec816b3756b1eb4394186c3b689b17e04850dfc20f7e57")
    version("7.0.0", sha256="cf4127298723dafbce3afd13775ccf3885be5d3c8435751b867f9a6a10b71a39")
    version("6.1.1", sha256="93ea72ce6989eb2eed99d0f75721474f69ad88128afdef5ac377eb797c4bf76b")
    version("6.1.0", sha256="788183e382e3d1d7707db08978239965e8b9e4e5ed42669bf4758186734d5f24")
    version("6.0.0", sha256="d1377122a5a00e2f940ee482999518efe16d745d423a670c27773dfbc3c9a7d9")
    version("5.11.1", sha256="aefc51675b0b533d56bb5fd1c8c6c0522fe31896679882e1c4c63d5e4a0fccb3")
    version("5.11.0", sha256="b97bc6695b2aff02144133c2e7399d5885223d42b7912ffaec2ca3898e673bfe")
    version("5.10.0", sha256="cfcc4ff8e698256fc17ea3ff796478b050852585aa5bae79ecd05b2ab7b39b9a")
    version("5.7.0", sha256="4651ca1445e80f2781827305de3d76b3ce53195f2227762684eb08f17bc473b7")
    version("5.4.3", sha256="2c8e420cd4ed4cec4e7999ee47409e876af575d4c35a45840d59e8b5f3155ab8")
    version("5.2.1", sha256="93d2dc6ee0c9af4dbc70bc1251d0e545a9910ca8863774761f92716dece400b6")
    version("3.1.1", sha256="05f61c71aaefc02d8e37c0a3eeb9815ff526ea28b3b76324769e6158d7f95be1")
    version("2.0.0", sha256="0ccd2db529afd070df815b1521f01401d43de03941170f8a800e7531faba265d")
    version("1.10.0", sha256="186428c270309e6fdfe2d5ab0949ab21ae5f7dea831eab96701b86bd666af39c")
    version("1.8.1", sha256="e2127626a91e6c885db89668976db31020f0af2da728924b56480fc7ccf09649")

    depends_on("c", type="build")  # generated

    depends_on("python@2.6:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
