# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RAdsplit(RPackage):
    """Annotation-Driven Clustering.

    This package implements clustering of microarray gene expression
    profiles according to functional annotations. For each term genes are
    annotated to, splits into two subclasses are computed and a significance
    of the supporting gene set is determined."""

    bioc = "adSplit"

    version("1.76.0", commit="3bfef6d1d8a4e11632aeeadf25a00801564d5949")
    version("1.74.0", commit="3df3361641cc343e106525e33bfcea675ec05e3a")
    version("1.72.0", commit="194ddb23b683bc8633c9522456acc49c85b369b5")
    version("1.70.0", commit="a08a994215a459b856eae051c778e2b9144f52d9")
    version("1.68.0", commit="705977b5e1cb7dd69793cc673fa215baaba42af5")
    version("1.66.0", commit="64580a6f7a9bc6b16334267c90df48fbb839cc16")
    version("1.64.0", commit="32f150eb51c66b867301dceeb527de5b97f9f490")

    depends_on("cxx", type="build")  # generated

    depends_on("r@2.1.0:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biobase@1.5.12:", type=("build", "run"))
    depends_on("r-cluster@1.9.1:", type=("build", "run"))
    depends_on("r-go-db@1.8.1:", type=("build", "run"))
    depends_on("r-keggrest@1.30.1:", type=("build", "run"), when="@1.62.0:")
    depends_on("r-multtest@1.6.0:", type=("build", "run"))
