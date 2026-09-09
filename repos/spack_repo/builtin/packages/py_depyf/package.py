# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDepyf(PythonPackage):
    """Decompile python functions, from bytecode to source code."""

    homepage = "https://depyf.readthedocs.io/en/latest/"
    pypi = "depyf/depyf-0.20.0.tar.gz"

    version("0.20.0", sha256="fb7683bd72c44f67b56029df2c47721e9a02ffa4d7b19095f1c54c4ebf797a98")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-astor", type=("build", "run"))
    depends_on("py-dill", type=("build", "run"))
