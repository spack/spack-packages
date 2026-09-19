# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxAutoapi(PythonPackage):
    """Sphinx extension for generating API documentation from source code."""

    homepage = "https://github.com/readthedocs/sphinx-autoapi"
    pypi = "sphinx-autoapi/sphinx_autoapi-3.6.0.tar.gz"

    license("MIT")

    version("3.6.0", sha256="c685f274e41d0842ae7e199460c322c4bd7fec816ccc2da8d806094b4f64af06")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-flit-core@3.2:3", type="build")

    depends_on("py-astroid@2.7:", type=("build", "run"), when="^python@:3.11")
    depends_on("py-astroid@3:", type=("build", "run"), when="^python@3.12:")
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-sphinx@7.4.0:", type=("build", "run"))
    depends_on("py-stdlib-list", type=("build", "run"), when="^python@:3.9")
