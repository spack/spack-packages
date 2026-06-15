# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *


class Kynema(BundlePackage):
    """Kynema is a suite of general purpose fluid dynamics
    simulation codes for coupling structured and unstructured
    grids with overset. It also includes a flexible multi-body
    solver"""

    homepage = "https://github.com/kynema"
    maintainers("jrood-nrel")

    version("1.0")

    # Simple list of applications in the suite at the moment
    depends_on("kynema-driver")
    depends_on("kynema-sgf")
    depends_on("kynema-ugf")
    depends_on("kynema-fmb")
    depends_on("tioga")
