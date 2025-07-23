# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDargs(PythonPackage):
    """Argument checking for python programs"""

    homepage = "https://github.com/deepmodeling/dargs"
    url = "https://github.com/deepmodeling/dargs/archive/refs/tags/v0.4.10.tar.gz"
    git = "https://github.com/deepmodeling/dargs.git"
    pypi = "dargs/dargs-0.4.10.tar.gz"

    license("LGPL-3.0-or-later")
    maintainers("mtaillefumier")

    version("master", branch="master")
    version("0.4.10", sha256="7dc9a0b213bed71a281997dbf2be6612e988caadc566b4aec1bf253243a22ea0")
    version("0.4.9", sha256="cbd68ed97fd49ba7b5701ea980ad495c64e41db2785357f2666490531995c407")
    version("0.4.8", sha256="95f3085dc912af4bcefbd38ced60717f023b7b59ff9ce6aadabfaceca2f11243")
    version("0.4.7", sha256="3132ea3f39dc1aaa342b3f045d262ed81c1d52fa2e817bae60839cf67c0d152b")
    version("0.4.6", sha256="864dfa7a61f483d9a025f1f843afd6e9eefe728fdc9a06f991bcef92f0018bed")
    version("0.4.5", sha256="46ddd9aba01be1c185b693cabee481c8a3d95b2d5f2a4f31d190f12c95fa23f3")
    version("0.4.4", sha256="9cc8e9e36bfb401de19ca6e0de5cc5ab76871dacb9071c3f6ff078ca9aec38c0")
    version("0.4.3", sha256="2c0b2f7ea2eef932f2a4d0a3a5801f00854bf2b2b69cb3c415ace0bd224afd7f")
    version("0.4.2", sha256="285684743feec7d28cad31a090949c97a549fa94c9eea1c1d65fd8138f2458df")
    version("0.4.1", sha256="6f04fa6a67b2a7dcb27b36896cd8062ee19f95cc74ab3ca2a08c3985da68a495")

    depends_on("py-typeguard", type="build")
    depends_on("py-typing-extensions", when="^python@:3.8")
