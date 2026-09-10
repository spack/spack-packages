# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Vbfnlo(AutotoolsPackage):
    """VBFNLO is a fully flexible parton level Monte Carlo program
    for the simulation of vector boson fusion, double and triple
    vector boson production in hadronic collisions at
    next to leading order in the strong coupling constant."""

    homepage = "https://www.itp.kit.edu/vbfnlo/wiki/doku.php?id=overview"
    url = "https://github.com/vbfnlo/vbfnlo/archive/v3.0.0beta5.tar.gz"

    tags = ["hep"]

    license("GPL-2.0-only")

    version("3.0", sha256="b9df02603e4f801f866360c720191a29afdb958d0bd4369ea7d810e761503e51")
    version("2.7.1", sha256="13e33d73d8a8ef64094621f87e6f94e01712e76cc19a86298d0b52cfcb9decca")

    # Documentation is broken on some systems:
    # See https://github.com/vbfnlo/vbfnlo/issues/2
    variant("doc", default=False, description="Build documentation")

    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated
    depends_on("c", type="build")

    depends_on("hepmc")
    depends_on("gsl")
    depends_on("lhapdf")
    depends_on("looptools")
    depends_on("automake", type="build")
    depends_on("autoconf", type="build")
    depends_on("m4", type="build")
    depends_on("libtool", type="build")
    # needed as tcsh is hardcoded in m4/vbfnlo.m4, could be patched out in the future
    depends_on("tcsh", type="build")

    @when("@2.7.1")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.unset("F77")

    def configure_args(self):
        args = [
            "--with-hepmc=" + self.spec["hepmc"].prefix,
            "--with-gsl=" + self.spec["gsl"].prefix,
            "--with-LHAPDF=" + self.spec["lhapdf"].prefix,
            "--with-LOOPTOOLS=" + self.spec["looptools"].prefix,
            "FCFLAGS=-std=legacy",
        ]

        return args

    @when("@3: ~doc")
    def patch(self):
        filter_file("lib src doc", "lib src", "Makefile.am")
