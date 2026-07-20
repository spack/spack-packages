# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class ROrgDrEgDb(RPackage):
    """Genome wide annotation for Zebrafish.

    Genome wide annotation for Zebrafish, primarily based on mapping using Entrez
    Gene identifiers."""

    bioc = "org.Dr.eg.db"
    url = "https://bioconductor.org/packages/3.21/data/annotation/src/contrib/org.Dr.eg.db_3.21.0.tar.gz"

    version(
        "3.21.0",
        url="https://bioconductor.org/packages/3.21/data/annotation/src/contrib/org.Dr.eg.db_3.21.0.tar.gz",
        sha256="4c033d4e14a6f36ac339cb5ca2d9bdfb3c7963deeacf5327bffcf94aabb37fa3",
    )
    version(
        "3.20.0",
        url="https://bioconductor.org/packages/3.20/data/annotation/src/contrib/org.Dr.eg.db_3.20.0.tar.gz",
        sha256="3aeff5e6041437c1381d9cc75c68a69e50fe51c4fdd96d8936612b2cae51db2b",
    )
    version(
        "3.19.1",
        url="https://bioconductor.org/packages/3.19/data/annotation/src/contrib/org.Dr.eg.db_3.19.1.tar.gz",
        sha256="863ac02795bf28e07190ea9998295617ddaaf3e6b3e04fd64690c709fbb83010",
    )

    depends_on("r@2.7.0:", type=("build", "run"))

    depends_on("r-annotationdbi@1.69:", type=("build", "run"), when="@3.21:")
    depends_on("r-annotationdbi@1.67:", type=("build", "run"), when="@3.20:")
    depends_on("r-annotationdbi@1.65.2:", type=("build", "run"))
