# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFakeredis(PythonPackage):
    """Python implementation of redis API, can be used for testing purposes."""

    homepage = "https://github.com/cunla/fakeredis-py"
    pypi = "fakeredis/fakeredis-2.33.0.tar.gz"

    version("2.33.0", sha256="d7bc9a69d21df108a6451bbffee23b3eba432c21a654afc7ff2d295428ec5770")

    variant("lua", default=False, description="Enable Lua scripting support")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-redis@:7.0", when="^python@:3.9", type=("build", "run"))
    depends_on("py-redis@4.3:", when="^python@3.8:", type=("build", "run"))
    depends_on("py-redis@4:", when="^python@:3.7", type=("build", "run"))
    depends_on("py-sortedcontainers@2:", type=("build", "run"))
    depends_on(
        "py-typing-extensions@4.7", when="^python@:3.10", type=("build", "run")
    )  # exact versions

    depends_on("py-lupa@2.1:", when="+lua", type=("build", "run"))
