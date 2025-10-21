# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyStringzilla(PythonPackage):
    """Search, hash, sort, and process strings faster via SWAR and SIMD"""

    homepage = "https://github.com/ashvardanian/StringZilla"
    pypi = "stringzilla/stringzilla-4.2.1.tar.gz"

    license("Apache-2.0")

    version("4.2.1", sha256="fd15835ab3b78b09dba678c66b36715bcf7f9e550994ea09abcc8eb7a5e1c9f7")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
