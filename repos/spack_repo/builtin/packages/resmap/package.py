# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *

class Resmap(Package):
    """ResMap (Resolution Map) is an easy to use software package for computing the local resolution of
    3D density maps studied in structural biology, primarily electron cryo-microscopy (cryo-EM)."""

    homepage = "https://resmap.sourceforge.net/"
    url = "https://sourceforge.net/projects/resmap/files/ResMap-1.1.4-linux64/download"

    version("1.1.4", sha256="e85c8c535acc284def560d78aaf67dac4a16a1c4c7b46b341e99a3fbe761bd18", expand=False)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(self.stage.archive_file, prefix.bin.ResMap)
        set_executable(prefix.bin.ResMap)
