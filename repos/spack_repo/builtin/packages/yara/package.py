# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Yara(AutotoolsPackage):
    """YARA is a tool aimed at (but not limited to) helping malware researchers
    to identify and classify malware samples"""

    homepage = "https://virustotal.github.io/yara/"
    url = "https://github.com/VirusTotal/yara/archive/v3.9.0.tar.gz"

    license("BSD-3-Clause")

    version("4.5.2", sha256="1f87056fcb10ee361936ee7b0548444f7974612ebb0e681734d8de7df055d1ec")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")
