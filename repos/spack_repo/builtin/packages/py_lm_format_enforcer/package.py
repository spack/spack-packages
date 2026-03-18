# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLmFormatEnforcer(PythonPackage):
    """Enforce the output format (JSON Schema, Regex etc) of a language model."""

    homepage = "https://github.com/noamgat/lm-format-enforcer"
    pypi = "lm_format_enforcer/lm_format_enforcer-0.11.3.tar.gz"

    version("0.11.3", sha256="e68081c108719cce284a9bcc889709b26ffb085a1945b5eba3a12cfa96d528da")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pydantic@1.10.8:", type=("build", "run"))
    depends_on("py-interegular@0.3.2:", type=("build", "run"))
    depends_on("py-packaging", type="build")
    depends_on("py-pyyaml", type=("build", "run"))
