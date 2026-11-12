# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFakeredis(PythonPackage):
    """Python implementation of redis API, can be used for testing purposes."""

    homepage = "https://github.com/cunla/fakeredis-py"
    pypi = "fakeredis/fakeredis-2.35.0.tar.gz"

    license("BSD-3-Clause")

    version("2.35.1", sha256="5bae5eba7b9d93cb968944ac40936373cf2397ff71667d4b595df65c3d2e413f")

    variant("lua", default=False, description="Enable Lua scripting support")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-redis@:7.1", type=("build", "run"), when="^python@:3.9")
    depends_on("py-redis@4.3:", type=("build", "run"), when="^python@3.9:")
    depends_on("py-redis@4:", type=("build", "run"), when="^python@:3.7")
    depends_on("py-sortedcontainers@2:", type=("build", "run"))
    depends_on("py-typing-extensions@4.7:", type=("build", "run"), when="^python@:3.10")

    depends_on("py-lupa@2.1:", type=("build", "run"), when="+lua")
