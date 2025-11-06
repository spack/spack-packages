# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RAnnaffy(RPackage):
    """Annotation tools for Affymetrix biological metadata.

    Functions for handling data from Bioconductor Affymetrix annotation data
    packages. Produces compact HTML and text reports including experimental
    data and URL links to many online databases. Allows searching biological
    metadata using various criteria."""

    bioc = "annaffy"

    license("LGPL-2.1-or-later")

    version("1.72.0", commit="7cb439706a7e93fb5b44ead374010077a44ea78b")
    version("1.70.0", commit="c99e81259adb39b5d8e954fd7afe7f93675229bc")
    version("1.68.0", commit="fa930c0bbdca9828a130ab06d86c65d451380830")
    version("1.66.0", commit="aa1afa1509754128d27508228c1f39f51a8da043")

    depends_on("r@2.5.0:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"), when="@1.64.2:")
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-annotationdbi@0.1.15:", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
