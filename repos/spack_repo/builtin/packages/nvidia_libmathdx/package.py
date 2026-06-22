# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class NvidiaLibmathdx(Package):
    """NVIDIA MathDx runtime code-generation library"""

    homepage = "https://developer.nvidia.com/cublasdx-downloads"
    url = "https://developer.download.nvidia.com/compute/cublasdx/redist/cublasdx/cuda12/libmathdx-Linux-x86_64-0.3.1-cuda12.0.tar.gz"

    maintainers("LydDeb")

    version("0.3.1", sha256="b282f95f0028b39880e7e77155ecd015700905286afd88bd631072894090f9d9")

    def install(self, spec, prefix):
        install_tree(".", prefix)
