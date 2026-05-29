# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLupa(PythonPackage):
    """Python wrapper around Lua and LuaJIT."""

    homepage = "https://github.com/scoder/lupa"
    pypi = "lupa/lupa-2.6.tar.gz"

    version("2.6", sha256="9a770a6e89576be3447668d7ced312cd6fd41d3c13c2462c9dc2c2ab570e45d9")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython@3.1.6:", type="build")

    depends_on("lua-luajit", type=("build", "run"))
