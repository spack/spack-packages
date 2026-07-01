# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RS4vectors(RPackage):
    """Foundation of vector-like and list-like containers in Bioconductor.

    The S4Vectors package defines the Vector and List virtual classes and a
    set of generic functions that extend the semantic of ordinary vectors
    and lists in R. Package developers can easily implement vector-like or
    list-like objects as concrete subclasses of Vector or List. In addition,
    a few low-level concrete subclasses of general interest (e.g. DataFrame,
    Rle, and Hits) are implemented in the S4Vectors package itself (many
    more are implemented in the IRanges package and in other Bioconductor
    infrastructure packages)."""

    bioc = "S4Vectors"

    with default_args(get_full_repo=True):
        version("0.50.1", commit="dfc837c68d33d9dfb2ba620c8cad386b8a730fa2")  # bioc 3.23
        version("0.48.1", commit="ae25d08aa5b02dca895179b5b6ac52656c4547f3")  # bioc 3.22
        version("0.46.0", commit="f4a665d66e3d84099b551ae03840c727a374c178")  # bioc 3.21
        version("0.44.0", commit="79c39487a5fa9470cc86fe3f62033ff2cc9aae79")  # bioc 3.20
        version("0.42.1", commit="cc0a6d7b29ba55545f979d7448e2f5029563a219")  # bioc 3.19
        version("0.40.2", commit="8cd5cb3cbd469be6a8c9621461e0e16a314506c6")  # bioc 3.18
        version("0.38.2", commit="6878c63a79eaacfd164a16d6815746cca5e80dba")  # bioc 3.17
        version("0.38.0", commit="e80c24e1481033741147a0677fb42ce455e7da74")
        version("0.36.2", commit="16710086622163297633a06af763892cef210a5c")  # bioc 3.16
        version("0.36.0", commit="af58701957ffdd9209031dd6a8dee3acdc58e999")
        version("0.34.0", commit="f590de3ec4d896a63351d0c1925d3856c0bd5292")
        version("0.32.3", commit="ad90e78fd3a4059cfcf2846498fb0748b4394e1a")
        version("0.28.1", commit="994cb7ef830e76f8b43169cc72b553869fafb2ed")
        version("0.26.1", commit="935769c7e2767230feb47f6f8147e0e2908af4f0")
        version("0.22.1", commit="d25e517b48ca4184a4c2ee1f8223c148a55a8b8a")
        version("0.20.1", commit="1878b2909086941e556c5ea953c6fd86aebe9b02")
        version("0.18.3", commit="d6804f94ad3663828440914920ac933b934aeff1")
        version("0.16.0", commit="00fec03fcbcb7cff37917fab0da28d91fdf9dc3d")
        version("0.14.7", commit="40af17fe0b8e93b6a72fc787540d2961773b8e23")

    depends_on("c", type="build")

    depends_on("r@4.1.0:", type=("build", "run"), when="@0.49.3:")
    depends_on("r@4.0.0:", type=("build", "run"), when="@0.28.1:")
    depends_on("r@3.3.0:", type=("build", "run"))

    depends_on("r-biocgenerics@0.53.2:", type=("build", "run"), when="@0.45.2:")
    depends_on("r-biocgenerics@0.37.0:", type=("build", "run"), when="@0.32.3:")
    depends_on("r-biocgenerics@0.36.0:", type=("build", "run"), when="@0.28.1:")
    depends_on("r-biocgenerics@0.31.1:", type=("build", "run"), when="@0.26.1:")
    depends_on("r-biocgenerics@0.23.3:", type=("build", "run"), when="@0.16.0:")
    depends_on("r-biocgenerics@0.21.1:", type=("build", "run"))
