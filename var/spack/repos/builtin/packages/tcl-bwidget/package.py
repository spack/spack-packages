# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class TclBwidget(Package):
    """BWidget is a mega-widget package."""

    homepage = "https://core.tcl-lang.org/bwidget/home"
    url = "http://sourceforge.net/projects/tcllib/files/BWidget/1.9.13/bwidget-1.9.13.tar.gz"

    version("1.9.13", sha256="76d8f42280e7160242186d12437949830eabd5009a6c14f4e7dba0f661403a81")

    depends_on("tcl@8.1:")

    extends("tcl")

    def install(self, spec, prefix):
        tcl_lib_path = join_path(self.spec["tcl"].prefix.lib, "bwidget" + str(self.version.up_to(3)))
        install_tree(".", prefix)
        copy_tree(prefix, tcl_lib_path)

