# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class CruxToolkit(CMakePackage):
    """Mass spectrometry analysis toolkit."""

    homepage = "https://crux.ms"
    url = "https://github.com/crux-toolkit/crux-toolkit/archive/refs/tags/crux-4.3.2.tar.gz"

    license("Apache-2.0")

    version("4.3.2", sha256="6911c1cb45e5a188036edcbfbaf9ab6d34679321988a88de1cd192f1e4a2630b")

    depends_on("cmake@3.15:", type="build")

    # Additional dependencies are downloaded during build (the logic cannot be disabled)
    # from https://github.com/crux-toolkit/crux-toolkit/blob/crux-4.3.2/ext/CMakeLists.txt
    #
    # MSToolkit 83.27-g20e99ce (Apache-2.0)
    #   https://github.com/mhoopmann/mstoolkit/commits/20e99c
    #
    # ProteoWizard 3.0-25123 (Apache-2.0)
    #   https://noble.gs.washington.edu/crux-downloads/pwiz-src-3_0_25123_b0e5f51.tar.bz2
    #
    # Percolator 3.07.01 (Apache-2.0)
    #   https://github.com/percolator/percolator/commits/310f924
    #
    # Protobuf 3.19.4 (Custom BSD-3-Clause)
    #   https://github.com/protocolbuffers/protobuf/blob/main/LICENSE
    #   https://github.com/protocolbuffers/protobuf/releases/download/v3.19.4/protobuf-all-3.19.4.tar.gz
    #
    # gflags 2.2.2 (BSD-3-Clause)
    #   https://codeload.github.com/gflags/gflags/tar.gz/v2.2.2
    #
    # Comet 2025.01.1 (Apache-2.0)
    #   https://github.com/UWPR/Comet
    #
    # NeoPepXMLParser e89f166 (Apache-2.0)
    #   https://github.com/mhoopmann/NeoPepXMLParser.git
    #
    # Kojak 4307dfa (Apache-2.0)
    #   https://github.com/mhoopmann/kojak.git
