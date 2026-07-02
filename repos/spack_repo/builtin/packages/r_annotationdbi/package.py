# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RAnnotationdbi(RPackage):
    """Manipulation of SQLite-based annotations in Bioconductor.

    Implements a user-friendly interface for querying SQLite-based
    annotation data packages."""

    bioc = "AnnotationDbi"

    with default_args(get_full_repo=True):
        version("1.74.0", commit="c7dbd19487bbf100ad1a6ab58b475c5ec001cc4b")  # bioc 3.23
        version("1.72.0", commit="ffdaf5d5dda16995f1afb7276be8f96cf738e16b")  # bioc 3.22
        version("1.70.0", commit="a8184e6a1b0bc175040118c73fd22062ddcd3392")  # bioc 3.21
        version("1.68.0", commit="6a2aa3361bb114fbfe7a25b51bcaed36450a57e0")  # bioc 3.20
        version("1.66.0", commit="989c1dcf56db17646e79bd7caa70484e4cda73d1")  # bioc 3.19
        version("1.64.1", commit="e5b997eac9f538d6ad5418fbe90716848d8c5f2e")  # bioc 3.18
        version("1.62.2", commit="baefc543c43b039c6ebf28acb4f82be3e491b8c5")  # bioc 3.17
        version("1.62.0", commit="7ca03a0332d0a284ea27d16edb7b386c86cf99ea")
        version("1.60.2", commit="eebebb2401fc57a7a9a103e77bf18ff06dd7b2a8")  # bioc 3.16
        version("1.60.0", commit="cd61bd1b1538e2f1f411fd7087820749ecf39da8")
        version("1.58.0", commit="05fcf7a28a6b15b195da23474d7ba89bd0cfd891")
        version("1.56.2", commit="13fdc4a93852199ca6ec120a2fe1078f9f445f67")
        version("1.52.0", commit="c4e0ca9bd65362ae9cad6a98d90f54267b0ae838")
        version("1.46.1", commit="ff260913741d0fcf9487eeb1f44a6c6968ced5b9")
        version("1.44.0", commit="ce191b08cfd612d014431325c26c91b11c5f13ac")
        version("1.42.1", commit="71085b47ea2e1ef929bebe8b17eb8e8a573f98e3")
        version("1.40.0", commit="e34dff07e10402eecbf95604a512bc1fc4edb127")
        version("1.38.2", commit="67d46facba8c15fa5f0eb47c4e39b53dbdc67c36")

    depends_on("r@2.7.0:", type=("build", "run"))

    depends_on("r-biobase@1.17.0:", type=("build", "run"))

    depends_on("r-biocgenerics@0.29.2:", type=("build", "run"), when="@1.46.1:")
    depends_on("r-biocgenerics@0.23.1:", type=("build", "run"), when="@1.40.0:")
    depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))

    depends_on("r-dbi", type=("build", "run"))

    depends_on("r-iranges", type=("build", "run"))

    depends_on("r-keggrest", type=("build", "run"), when="@1.56.2:")

    depends_on("r-rsqlite", type=("build", "run"))

    depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
