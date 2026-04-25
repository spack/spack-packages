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

    version("0.4.1", sha256="9d957babfaa216512a542a39dd1b0389384b3d444b55353032e7b707c2cfc969")

    depends_on("cxx", type="build")

    depends_on("libdeflate")
    depends_on("isa-l")
    depends_on("highway")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make(f"PREFIX={prefix}", "install")
