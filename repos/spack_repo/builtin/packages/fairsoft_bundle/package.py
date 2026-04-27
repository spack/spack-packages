# Copyright Spack Project Developers. See COPYRIGHT for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *


class FairsoftBundle(BundlePackage):
    """Bundle package providing default environment for FAIR software"""

    homepage = "https://github.com/FairRootGroup/FairSoft"
    maintainers("dennisklein", "fuhlig1", "jezwilkinson")

    # Releases:
    version("2025-05")

    variant("graphics", default=False, description="Enable graphical support in ROOT")
    variant("mt", default=False, description="Enable multithreading for GEANT4")

    # Some normal packages
    depends_on("faircmakemodules")

    # Pin some variants:
    depends_on("geant4 ~threads", when="~mt")
    depends_on("geant4 +threads", when="+mt")
    depends_on("geant4 ~qt~vecgeom~opengl~x11~motif")

    # ensure that OpenBLAS uses CMake build system (default Makefile causes issues on some Macs)
    depends_on("openblas build_system=cmake ~dynamic_dispatch")

    # Generic ROOT dependencies
    depends_on("root +fortran+pythia8+vc~vdt")
    # Mostly for the experiments:
    depends_on("root +python+tmva+mlp+xrootd+sqlite")
    # FFTW for Panda
    depends_on("root +fftw")
    depends_on("fftw~mpi")
    depends_on("root +spectrum", when="@2025-05:")
    depends_on("root ~x~opengl~aqua", when="~graphics")
    depends_on("root +x+opengl", when="+graphics")

    # Using "platform=" in a when clause gets concretized too late.
    # and our root recipe disables +aqua on non-macOS now.
    # depends_on("root +aqua", when="+graphics platform=darwin")
    depends_on("root +aqua", when="+graphics")

    # Version-specific dependencies for FairSoft releases
    depends_on("pythia8@8.313", when="@2025-05")
    depends_on("root@6.36.00", when="@2025-05")
    depends_on("vmc@2-1", when="@2025-05")
    depends_on("geant3@4-4", when="@2025-05")
    depends_on("vgm@5-3-1", when="@2025-05")
    depends_on("geant4-vmc@6-7-p1", when="@2025-05")
    depends_on("fairsoft-config fairsoft_version=may25", when="@2025-05", type="run")
