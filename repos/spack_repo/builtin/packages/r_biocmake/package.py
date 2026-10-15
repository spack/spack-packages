# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RBiocmake(RPackage):
    """Manages the installation of CMake for building Bioconductor packages."""

    bioc = "biocmake"

    with default_args(get_full_repo=True):
        version("1.4.0", commit="6b43087b270a38c868735325540d49c45e9d7f85")  # bioc 3.23

    depends_on("r-dir-expiry", type=("build", "run"))

    depends_on("cmake@3.24:", type="run")
