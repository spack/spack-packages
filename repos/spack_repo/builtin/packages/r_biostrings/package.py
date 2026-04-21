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

    license("Artistic-2.0")

    with default_args(get_full_repo=True):
        version("2.78.0", commit="eda5d667ad05a73336d8c83a71f670198433232f")
        version("2.76.0", commit="2e04124cda03d509d857df228153a45c89840284")
        version("2.68.0", commit="f28b7838fb8321a9956506b3d2f4af2740bca124")
        version("2.66.0", commit="3470ca7da798971e2c3a595d8dc8d0d86f14dc53")
        version("2.64.1", commit="ffe263e958463bd1edb5d5d9316cfd89905be53c")
        version("2.64.0", commit="c7ad3c7af607bc8fe4a5e1c37f09e6c9bf70b4f6")

    depends_on("c", type="build")  # generated

    with default_args(type=("build", "run")):
        depends_on("r@4.0.0:")
        depends_on("r@4.1.0:", when="@2.78:")
        depends_on("r-biocgenerics@0.37.0:")
        depends_on("r-s4vectors@0.27.12:")
        depends_on("r-iranges@2.23.9:")
        depends_on("r-iranges@2.30.1:", when="@2.64.1:")
        depends_on("r-iranges@2.31.2:", when="@2.66.0:")
        depends_on("r-xvector@0.29.2:")
        depends_on("r-xvector@0.37.1:", when="@2.66.0:")
        depends_on("r-seqinfo", when="@2.78:")
        depends_on("r-crayon")

        # Historical
        depends_on("r-genomeinfodb", when="@:2.76.0")

    conflicts("r@4.5.0:", when="@:2.75")
