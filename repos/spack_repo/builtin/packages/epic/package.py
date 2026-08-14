# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Epic(CMakePackage):
    """EpIC is a modern and versatile Monte Carlo generator used in
    studying exclusive processes. These processes are sensitive to
    generalised parton distributions (GPDs), which describe the 3D
    partonic structure of hadrons in the language of quantum
    chromodynamics (QCD). EpIC has been developed to support the
    current and future experimental programmes, like Electron-Ion
    Collider (EIC) to be constructed in Brookhaven National Laboratory."""

    homepage = "https://pawelsznajder.github.io/epic"
    url = "https://github.com/pawelsznajder/epic/archive/refs/tags/v.1.1.8.tar.gz"
    git = "https://github.com/pawelsznajder/epic.git"

    tags = ["hep"]

    maintainers("wdconinc")

    license("GPL-3.0", checked_by="wdconinc")

    version("1.1.8", sha256="f2b9add278e614fb012856e7b9df676789cb47d33af66438e7962a849f025339")

    depends_on("cxx", type="build")
    depends_on("cmake@3.5:", type="build")

    depends_on("partons")
    depends_on("partons-elementary-utils")
    depends_on("partons-numa")
    depends_on("sfml@:2")
    depends_on("cln")
    depends_on("gsl")
    depends_on("apfelxx")
    depends_on("lhapdf")
    depends_on("libxml2")
    depends_on("root")
    depends_on("hepmc3 +rootio")
    depends_on("boost")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path(self.stage.source_path, "bin", "epic"), prefix.bin)
        install_tree(
            join_path(self.stage.source_path, "data"),
            join_path(prefix.share, "epic", "data"),
        )
