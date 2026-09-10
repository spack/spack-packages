# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySetuptoolsReproducible(PythonPackage):
    """Extension of setuptools to support reproducible dists."""

    homepage = "https://github.com/wimglenn/setuptools-reproducible"
    pypi = "setuptools_reproducible/setuptools_reproducible-0.1.tar.gz"

    license("MIT")

    version("0.1", sha256="1ae3c0dcca3f125e0fdfb7ce749c872f63d9fe6a0fd8b36954f639ee677f2f73")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
