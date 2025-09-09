# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEvaluate(PythonPackage):
    """Evaluate is a library that makes evaluating and comparing models and
    reporting their performance easier and more standardized."""

    homepage = "https://github.com/huggingface/evaluate"
    pypi = "evaluate/evaluate-0.4.0.tar.gz"

    license("apache-2.0")

    version("0.4.6", sha256="e07036ca12b3c24331f83ab787f21cc2dbf3631813a1631e63e40897c69a3f21")
    version("0.4.0", sha256="bd6a59879be9ae13b681684e56ae3e6ea657073c4413b30335e9efa9856e4f44")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"), when="@0.4.6:")
    depends_on("py-datasets@2.0.0:", type=("build", "run"))
    depends_on("py-numpy@1.17:", type=("build", "run"))
    depends_on("py-dill", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-requests@2.19.0:", type=("build", "run"))
    depends_on("py-tqdm@4.62.1:", type=("build", "run"))
    depends_on("py-xxhash", type=("build", "run"))
    depends_on("py-multiprocess", type=("build", "run"))
    depends_on("py-importlib-metadata", when="^python@:3.7", type=("build", "run"))
    depends_on("py-fsspec@2021.05.0:+http", type=("build", "run"))
    depends_on("py-huggingface-hub@0.7.0:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-responses@:0.18", type=("build", "run"), when="@0.4.0")
