# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RS4arrays(RPackage):
    """The S4Arrays package defines the Array virtual class to be extended by other
    S4 classes that wish to implement a container with an array-like semantic. It
    also provides: (1) low-level functionality meant to help the developer of such
    container to implement basic operations like display, subsetting, or coercion
    of their array-like objects to an ordinary matrix or array, and (2) a framework
    that facilitates block processing of array-like objects (typically on-disk
    objects)."""

    bioc = "S4Arrays"

    with default_args(get_full_repo=True):
        version("1.10.1", commit="a4cccbaab0d12176db3670665f0ca6c23bb900be")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@4.3:")
        depends_on("r-matrix")
        depends_on("r-abind")
        depends_on("r-biocgenerics@0.45.2:")
        depends_on("r-s4vectors@0.47.6:")
        depends_on("r-iranges")
