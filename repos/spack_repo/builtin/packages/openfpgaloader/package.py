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
    version("1.1.1", sha256="ca965f933c52a2a9dbb318df4d4de70fac5f095a8e64523f81036ab467a4b567")
    version("1.1.0", sha256="d2d3da194e3e578ce81f1156f85c128eb6021b73b0c67bbeec9cd5d8bea35fda")
    version("1.0.0", sha256="cf19b596e5dea21891b1be3cb9a04be7a1501926ee0919dcc5c9f1b6d3bd0a96")
    version("0.13.1", sha256="372f1942dec8a088bc7475f94ccf5a86264cb74e9154d8a162b8d4d26d3971e3")
    version("0.12.1", sha256="8fb2d1aa3a0de50222f6286c47220a5bc7b73708b60fb7d58f764deebd43d82d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("libusb")
    depends_on("libftdi")

    def setup_run_environment(self, env):
        env.prepend_path("OPENFPGALOADER_SOJ_DIR", f"{self.prefix}/share/openFPGALoader")
