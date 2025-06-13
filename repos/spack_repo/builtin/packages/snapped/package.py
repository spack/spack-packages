# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Snapped(CargoPackage):
    """Snapped is a parallel program snapshotter designed for debugging deadlocks and crashes in programs. It acts as a wrapper around the GDB Machine Interface (GDB-MI), leveraging the capabilities of GDB to provide robust debugging features. """

    homepage = "https://github.com/besnardjb/snapped/"
    git  = "https://github.com/besnardjb/snapped.git"

    maintainers("carlos-delgado15")

    license("UNKNOWN", checked_by="carlos-delgado15")

    version("0.1.0", commit="c6e87d2")
