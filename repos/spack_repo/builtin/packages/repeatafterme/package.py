# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Repeatafterme(MakefilePackage):
    """A package for the extension of repetitive DNA sequences"""

    homepage = "https://github.com/Dfam-consortium/RepeatAfterMe"
    url = "https://github.com/Dfam-consortium/RepeatAfterMe/archive/refs/tags/RepeatAfterMe_V0.0.7.tar.gz"

    maintainers("snehring")

    license("CC0-1.0", checked_by="snehring")

    version("0.7", sha256="8a4c96be6c0fcedf24ee28796fea3bffef022c7479d8f49fbd2f83e56d697f26")

    depends_on("c", type="build")

    parallel = False

    def edit(self, spec, prefix):
        filter_file(r"^INSTDIR = .*$", f"INSTDIR = {spec.prefix}", "Makefile")
        filter_file(r"^\s+@mkdir \$\(INSTDIR\)$", "", "Makefile")
        filter_file(r"^\s+@mkdir \$\(INSTDIR\)/bin$", "\t@mkdir -p $(INSTDIR)/bin", "Makefile")
