# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Openfpgaloader(CMakePackage):
    """openFPGALoader is a universal utility for programming FPGAs. Compatible 
    with many boards, cables and FPGA from major manufacturers (Xilinx, 
    Altera/Intel, Lattice, Gowin, Efinix, Anlogic, Cologne Chip). 
    openFPGALoader works on Linux, Windows and macOS."""

    homepage = "https://trabucayre.github.io/openFPGALoader/"
    url = "https://github.com/trabucayre/openFPGALoader/archive/refs/tags/v0.12.1.tar.gz"
    git = "https://github.com/trabucayre/openFPGALoader.git"

    maintainers("davekeeshan")

    license("Apache-2.0 OR MIT")

    version("master", branch="master")
    version("0.13.1", sha256="372f1942dec8a088bc7475f94ccf5a86264cb74e9154d8a162b8d4d26d3971e3")
    version("0.12.1", sha256="8fb2d1aa3a0de50222f6286c47220a5bc7b73708b60fb7d58f764deebd43d82d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("libusb", type="build")
    depends_on("libftdi", type="build")

    def setup_run_environment(self, env):
        env.prepend_path("OPENFPGALOADER_SOJ_DIR", f"{self.prefix}/share/openFPGALoader")
