# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RDelayedarray(RPackage):
    """A unified framework for working transparently with on-disk and in-memory
    array-like datasets.

    Wrapping an array-like object (typically an on-disk object) in a
    DelayedArray object allows one to perform common array operations on it
    without loading the object in memory. In order to reduce memory usage
    and optimize performance, operations on the object are either delayed or
    executed using a block processing mechanism. Note that this also works
    on in-memory array-like objects like DataFrame objects (typically with
    Rle columns), Matrix objects, and ordinary arrays and data frames."""

    bioc = "DelayedArray"

    license("Artistic-2.0")

    with default_args(get_full_repo=True):
        version("0.36.1", commit="1f8a9cbf34a5e998eae016f3410bdfe2bee490e4")
        version("0.26.0", commit="e3bdae96838a8ed45f18697f072f3c4ec011aa03")
        version("0.24.0", commit="68ee3d0626c234ee1e9248a6cb95b901e4b3ad90")
        version("0.22.0", commit="4a5afd117b189b40bd409c7aff60e09d41797472")
        version("0.20.0", commit="829b52916ec54bb4f1a3c6f06c9955f3e28b3592")
        version("0.16.1", commit="c95eba771ad3fee1b49ec38c51cd8fd1486feadc")
        version("0.10.0", commit="4781d073110a3fd1e20c4083b6b2b0f260d0cb0a")
        version("0.8.0", commit="7c23cf46558de9dbe7a42fba516a9bb660a0f19f")
        version("0.6.6", commit="bdb0ac0eee71edd40ccca4808f618fa77f595a64")
        version("0.4.1", commit="ffe932ef8c255614340e4856fc6e0b44128a27a1")
        version("0.2.7", commit="909c2ce1665ebae2543172ead50abbe10bd42bc4")

    depends_on("c", type="build")  # generated

    with default_args(type=("build", "run")):
        depends_on("r@3.4:")
        depends_on("r@4.0.0:", when="@0.20.0:")

        depends_on("r-matrix", when="@0.10.0:")

        depends_on("r-biocgenerics")
        depends_on("r-biocgenerics@0.25.1:", when="@0.6.6:")
        depends_on("r-biocgenerics@0.27.1:", when="@0.8.0:")
        depends_on("r-biocgenerics@0.31.5:", when="@0.16.1:")
        depends_on("r-biocgenerics@0.37.0:", when="@0.20.1:")
        depends_on("r-biocgenerics@0.43.4:", when="@0.24.0:")
        depends_on("r-biocgenerics@0.53.3:", when="@0.36.1:")

        depends_on("r-matrixgenerics@1.1.3:", when="@0.16.1:")

        depends_on("r-s4vectors@0.14.3:")
        depends_on("r-s4vectors@0.15.3:", when="@0.4.1:")
        depends_on("r-s4vectors@0.17.43:", when="@0.6.6:")
        depends_on("r-s4vectors@0.19.15:", when="@0.8.0:")
        depends_on("r-s4vectors@0.21.7:", when="@0.10.0:")
        depends_on("r-s4vectors@0.27.2:", when="@0.16.1:")
        depends_on("r-s4vectors@0.47.6:", when="@0.36.1:")

        depends_on("r-iranges")
        depends_on("r-iranges@2.11.17:", when="@0.4.1:")
        depends_on("r-iranges@2.17.3:", when="@0.10.0:")

        depends_on("r-s4arrays@1.9.3:", when="@0.36.1:")

        depends_on("r-sparsearray@1.7.5:", when="@0.36.1:")

        # Historical
        depends_on("r-matrixstats", when="@:0.10.0")
        depends_on("r-biocparallel", when="@0.6.6:0.10.0")
