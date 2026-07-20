# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class ROrgMmEgDb(RPackage):
    """Genome wide annotation for Mouse.

    Genome wide annotation for Mouse, primarily based on mapping using Entrez
    Gene identifiers."""

    bioc = "org.Mm.eg.db"
    url = "https://bioconductor.org/packages/3.21/data/annotation/src/contrib/org.Mm.eg.db_3.21.0.tar.gz"

    version(
        "3.21.0",
        url="https://bioconductor.org/packages/3.21/data/annotation/src/contrib/org.Mm.eg.db_3.21.0.tar.gz",
        sha256="0b8e75105f37fb84586e4e3875c28bfe09a2889c2b711303c636073399c22e07",
    )
    version(
        "3.20.0",
        url="https://bioconductor.org/packages/3.20/data/annotation/src/contrib/org.Mm.eg.db_3.20.0.tar.gz",
        sha256="87cc0e4314771d1d09a54b67e4595cf138ff8c601204c45b7569438031198cf2",
    )
    version(
        "3.19.1",
        url="https://bioconductor.org/packages/3.19/data/annotation/src/contrib/org.Mm.eg.db_3.19.1.tar.gz",
        sha256="47cee87aff4ccb7879eb33a50839f45578ee99acb8aff6bbfb78f7655ca6a889",
    )

    depends_on("r@2.7.0:", type=("build", "run"))

    depends_on("r-annotationdbi@1.69:", type=("build", "run"), when="@3.21:")
    depends_on("r-annotationdbi@1.67:", type=("build", "run"), when="@3.20:")
    depends_on("r-annotationdbi@1.65.2:", type=("build", "run"))
