# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAlePy(PythonPackage):
    """The Arcade Learning Environment: a platform for AI research."""

    homepage = "https://github.com/Farama-Foundation/Arcade-Learning-Environment"
    pypi = "ale_py/ale_py-0.12.0.tar.gz"

    license("GPL-2.0-only")

    version("0.12.0", sha256="6030416b6a049d399bf95420ad2fdbf0ea8f83051b502774d27b477a06000dbc")

    depends_on("cxx", type="build")
    depends_on("cmake@3.14:", type="build")
    depends_on("sdl2", type=("build", "link"))
    depends_on("opencv", type=("build", "link"))

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-scikit-build-core@0.10:", type="build")
    depends_on("py-nanobind@2.5.0:", type="build")
    depends_on("py-jax@0.4.31:", type="build", when="platform=linux")

    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"), when="^python@:3.10")
