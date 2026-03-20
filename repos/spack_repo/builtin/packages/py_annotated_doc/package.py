# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAnnotatedDoc(PythonPackage):
    """Document parameters, class attributes, return types,
    and variables inline, with Annotated."""

    homepage = "https://github.com/fastapi/annotated-doc"
    pypi = "annotated_doc/annotated_doc-0.0.4.tar.gz"

    version("0.0.4", sha256="fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")
