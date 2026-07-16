# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RLintr(RPackage):
    """A 'Linter' for R Code

    Checks adherence to a given style, syntax errors and possible semantic issues."""

    cran = "lintr"

    license("MIT")

    version("3.3.0-1", sha256="b12964c46fcd77d235e98af10586e103e50a4109affa9ede547c9ee75cffca06")

    with default_args(type=("build", "run")):
        depends_on("r@4:")

        depends_on("r-backports@1.5:")
        depends_on("r-cli@3.4:")
        depends_on("r-codetools")
        depends_on("r-digest")
        depends_on("r-glue")
        depends_on("r-knitr")
        depends_on("r-rex")
        depends_on("r-xfun")
        depends_on("r-xml2@1:")
        depends_on("r-xmlparsedata@1.0.5:")
