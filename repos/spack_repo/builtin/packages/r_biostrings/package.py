# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RBiostrings(RPackage):
    """Efficient manipulation of biological strings.

    Memory efficient string containers, string matching algorithms, and
    other utilities, for fast manipulation of large biological sequences or
    sets of sequences."""

    bioc = "Biostrings"

    with default_args(get_full_repo=True):
        version("2.76.0", commit="2e04124cda03d509d857df228153a45c89840284")
        version("2.68.0", commit="f28b7838fb8321a9956506b3d2f4af2740bca124")
        version("2.66.0", commit="3470ca7da798971e2c3a595d8dc8d0d86f14dc53")
        version("2.64.1", commit="ffe263e958463bd1edb5d5d9316cfd89905be53c")
        version("2.64.0", commit="c7ad3c7af607bc8fe4a5e1c37f09e6c9bf70b4f6")

    depends_on("c", type="build")  # generated

    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-biocgenerics@0.37.0:", type=("build", "run"))
    depends_on("r-s4vectors@0.27.12:", type=("build", "run"))
    depends_on("r-iranges@2.23.9:", type=("build", "run"))
    depends_on("r-iranges@2.30.1:", type=("build", "run"), when="@2.64.1:")
    depends_on("r-iranges@2.31.2:", type=("build", "run"), when="@2.66.0:")
    depends_on("r-xvector@0.29.2:", type=("build", "run"))
    depends_on("r-xvector@0.37.1:", type=("build", "run"), when="@2.66.0:")
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))

    conflicts("r@4.5.0:", when="@:2.75")
