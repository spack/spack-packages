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

    version("5.1.2", sha256="7c2a952d6305df23bd4e592c28c27786e0d77982949233df20029370cd0096ad")
    version("5.0.3", sha256="804806a1ffc10b87c558d007aa68443f3b5eba78adbcd4acdcff97c18ff6cb5f")
    version("4.2.1", sha256="fd15835ab3b78b09dba678c66b36715bcf7f9e550994ea09abcc8eb7a5e1c9f7")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@5.0.3:")
    depends_on("py-setuptools@61:", type="build")
