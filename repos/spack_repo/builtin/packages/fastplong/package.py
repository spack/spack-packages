# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Fastplong(MakefilePackage):
    """Ultrafast preprocessing and quality control for long reads (Nanopore,
    PacBio, Cyclone, etc.)."""

    homepage = "https://github.com/OpenGene/fastplong"
    url = "https://github.com/OpenGene/fastplong/archive/refs/tags/v0.4.1.tar.gz"

    maintainers("emwjacobson")

    license("MIT", checked_by="emwjacobson")

    version("0.7.0", sha256="c0afdf30f06e61e9837de30377894074b108cbd79b7a018501545806878e2b68")
    version("0.6.0", sha256="d4c81c6e80adc558293e1d3d78faab5bf11eb0a248b87accb288406faaede823")
    version("0.5.0", sha256="6e1937a10107cb500c6bc62aa6df796890fb31aadad2fdc54cb84f8efaf7bf96")
    version("0.4.1", sha256="9d957babfaa216512a542a39dd1b0389384b3d444b55353032e7b707c2cfc969")

    depends_on("cxx", type="build")

    depends_on("libdeflate")
    depends_on("isa-l")
    depends_on("highway")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make(f"PREFIX={prefix}", "install")
