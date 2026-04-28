# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyParse(PythonPackage):
    """parse() is the opposite of format()"""

    pypi = "parse/parse-1.11.1.tar.gz"

    license("MIT")

    version("1.21.0", sha256="937725d51330ffec9c7a26fdb5623baa135d8ba8ed78817ea9523538844e3ce4")
    version("1.20.2", sha256="b41d604d16503c79d81af5165155c0b20f6c8d6c559efa66b4b695c3e5a0a0ce")
    version("1.19.1", sha256="cc3a47236ff05da377617ddefa867b7ba983819c664e1afe46249e5b469be464")
    version("1.18.0", sha256="91666032d6723dc5905248417ef0dc9e4c51df9526aaeef271eacad6491f06a4")
    version("1.12.1", sha256="a5fca7000c6588d77bc65c28f3f21bfce03b5e44daa8f9f07c17fe364990d717")
    version("1.11.1", sha256="870dd675c1ee8951db3e29b81ebe44fd131e3eb8c03a79483a58ea574f3145c2")

    depends_on("py-setuptools@61.2:", type="build", when="@1.19:")
    depends_on("py-setuptools", type="build")
