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

    with default_args(get_full_repo=True):
        version("0.38.2", commit="63285a4ab9f3b74c894e5f709e9cde408fca78c0")  # bioc 3.23
        version("0.34.1", commit="93033ab216a0503fb48d948e1dae9c8943fab8ea")  # bioc 3.21
        version("0.26.0", commit="e3bdae96838a8ed45f18697f072f3c4ec011aa03")
        version("0.24.0", commit="68ee3d0626c234ee1e9248a6cb95b901e4b3ad90")  # bioc 3.16
        version("0.22.0", commit="4a5afd117b189b40bd409c7aff60e09d41797472")
        version("0.20.0", commit="829b52916ec54bb4f1a3c6f06c9955f3e28b3592")
        version("0.16.1", commit="c95eba771ad3fee1b49ec38c51cd8fd1486feadc")
        version("0.10.0", commit="4781d073110a3fd1e20c4083b6b2b0f260d0cb0a")
        version("0.8.0", commit="7c23cf46558de9dbe7a42fba516a9bb660a0f19f")
        version("0.6.6", commit="bdb0ac0eee71edd40ccca4808f618fa77f595a64")
        version("0.4.1", commit="ffe932ef8c255614340e4856fc6e0b44128a27a1")
        version("0.2.7", commit="909c2ce1665ebae2543172ead50abbe10bd42bc4")

    depends_on("c", type="build")

    depends_on("r@4.0:", type=("build", "run"), when="@0.20:")
    depends_on("r@3.4:", type=("build", "run"))

    depends_on("r-biocgenerics@0.53.3:", type=("build", "run"), when="@0.33.2:")
    depends_on("r-biocgenerics@0.51.3:", type=("build", "run"), when="@0.31.13:")
    depends_on("r-biocgenerics@0.51.2:", type=("build", "run"), when="@0.31.12:")
    depends_on("r-biocgenerics@0.43.4:", type=("build", "run"), when="@0.24:")
    depends_on("r-biocgenerics@0.37:", type=("build", "run"), when="@0.20.1:")
    depends_on("r-biocgenerics@0.31.5:", type=("build", "run"), when="@0.16.1:")
    depends_on("r-biocgenerics@0.27.1:", type=("build", "run"), when="@0.8:")
    depends_on("r-biocgenerics@0.25.1:", type=("build", "run"), when="@0.6.6:")
    depends_on("r-biocgenerics", type=("build", "run"))

    depends_on("r-iranges@2.17.3:", type=("build", "run"), when="@0.10:")
    depends_on("r-iranges@2.11.17:", type=("build", "run"), when="@0.4.1:")
    depends_on("r-iranges", type=("build", "run"))

    depends_on("r-matrix", type=("build", "run"), when="@0.10.0:")
    depends_on("r-matrixgenerics@1.1.3:", type=("build", "run"), when="@0.16.1:")

    depends_on("r-sparsearray@1.7.5:", type=("build", "run"), when="@0.33.5:")
    depends_on("r-sparsearray@1.5.42:", type=("build", "run"), when="@0.31.14:")
    depends_on("r-sparsearray@1.5.21:", type=("build", "run"), when="@0.31.8:")
    depends_on("r-sparsearray@1.5.18:", type=("build", "run"), when="@0.31.7:")
    depends_on("r-sparsearray@1.5.12:", type=("build", "run"), when="@0.31.5:")
    depends_on("r-sparsearray@1.5.11:", type=("build", "run"), when="@0.31.4:")
    depends_on("r-sparsearray@1.5.9:", type=("build", "run"), when="@0.31.3:")
    depends_on("r-sparsearray@1.1.10:", type=("build", "run"), when="@0.27.5:")
    depends_on("r-sparsearray@1.1.5:", type=("build", "run"), when="@0.27.3:")
    depends_on("r-sparsearray", type=("build", "run"), when="@0.27.2:")

    depends_on("r-s4arrays@1.5.4:", type=("build", "run"), when="@0.31.7:")
    depends_on("r-s4arrays@1.5.3:", type=("build", "run"), when="@0.31.5:")
    depends_on("r-s4arrays@1.3.5:", type=("build", "run"), when="@0.29.9:")
    depends_on("r-s4arrays@1.3.4:", type=("build", "run"), when="@0.29.8:")
    depends_on("r-s4arrays@1.3.3:", type=("build", "run"), when="@0.29.2:")
    depends_on("r-s4arrays@1.1.1:", type=("build", "run"), when="@0.27.1:")
    depends_on("r-s4arrays@1.0.1:", type=("build", "run"), when="@0.26.1:")

    depends_on("r-s4vectors@0.27.2:", type=("build", "run"), when="@0.16.1:")
    depends_on("r-s4vectors@0.21.7:", type=("build", "run"), when="@0.10:")
    depends_on("r-s4vectors@0.19.15:", type=("build", "run"), when="@0.8:")
    depends_on("r-s4vectors@0.17.43:", type=("build", "run"), when="@0.6.6:")
    depends_on("r-s4vectors@0.15.3:", type=("build", "run"), when="@0.4.1:")
    depends_on("r-s4vectors@0.14.3:", type=("build", "run"))

    depends_on("r-biocparallel", type=("build", "run"), when="@0.6.6:0.10.0")
    depends_on("r-matrixstats", type=("build", "run"), when="@:0.10.0")

    # > Error in matchSignature(signature, fdef, where) :
    #     more elements in the method signature (2) than in the generic signature (1)
    #       for function 'type<-'
    conflicts("^r-biocgenerics@0.44:", when="@:0.22")

    # > Error in reconcilePropertiesAndPrototype(name, slots, prototype, superClasses,  :
    #     no definition was found for superclass "DataTable" in the specification
    #         of class "DelayedMatrix"
    conflicts("^r-s4vectors@0.26:", when="@:0.10")
