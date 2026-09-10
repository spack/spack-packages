# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEvalTypeBackport(PythonPackage):
    """Like `typing._eval_type`, but lets older Python versions use
    newer typing features."""

    homepage = "https://github.com/alexmojaki/eval_type_backport"
    pypi = "eval_type_backport/eval_type_backport-0.2.2.tar.gz"

    license("MIT")

    version("0.2.2", sha256="f0576b4cf01ebb5bd358d02314d31846af5e07678387486e2c798af0e7d849c1")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-setuptools-scm +toml", type="build")
    depends_on("python@3.8:", type=("build", "run"))
