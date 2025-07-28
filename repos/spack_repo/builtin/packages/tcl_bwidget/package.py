# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *


class TclBwidget(SourceforgePackage, Package):
    """BWidget is a mega-widget package."""

    homepage = "https://core.tcl-lang.org/bwidget/home"
    sourceforge_mirror_path = "tcllib/BWidget/1.9.13/bwidget-1.9.13.tar.gz"
    maintainers("gjsd2")

    license("TCL")

    version("1.9.13", sha256="76d8f42280e7160242186d12437949830eabd5009a6c14f4e7dba0f661403a81")

    depends_on("tcl@8.1:")

    extends("tcl")

    def install(self, spec, prefix):
        install_tree(".", prefix.lib)
