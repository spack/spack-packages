# Copyright Spack Project Developers. See COPYRIGHT file for details.
# 
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage
from spack.package import *


class Exacmech(CMakePackage, CudaPackage, ROCmPackage):
    """GPU-friendly materials library with a focus on crystal plasticity methods"""

    homepage = "https://github.com/LLNL/exacmech"
    url = "https://github.com/llnl/ExaCMech/archive/refs/tags/v0.4.3.tar.gz"
    git = "https://github.com/llnl/ExaCMech.git"

    maintainers("rcarson3")

    version("develop", branch="develop")
    version("v0.4.3", sha256="0740d0eb6b8eb4036dd3b50a9e3061f0986a09c5398ad62b892d3ed221493152", url="https://github.com/llnl/ExaCMech/archive/refs/tags/v0.4.3.tar.gz")
    version("v0.4.2", sha256="66d88d9c19271a43cb511479e00a399f14b11952fe10720eb276dd7db467721c", url="https://github.com/llnl/ExaCMech/archive/refs/tags/v0.4.2.tar.gz")
    version("v0.4.1", sha256="ff0e748bcc7172fc99700974cc2e64f169d7369706a803d110061fccfa3d99a9", url="https://github.com/llnl/ExaCMech/archive/refs/tags/v0.4.1.tar.gz")
    version("v0.4.0", sha256="18f4790552333a6e15487ef277be7fe6476f838b51a11fb0da3b0244b5edd5aa", url="https://github.com/llnl/ExaCMech/archive/refs/tags/v0.4.0.tar.gz")
    version("v0.3.4", sha256="76448be985ed2869298b899dd92f48da1ff6113523e13c1b0e611a434cfb7bd2", url="https://github.com/llnl/ExaCMech/archive/refs/tags/v0.3.4.tar.gz")
    version("v0.3.0", sha256="c879c18c0947f6a6c921b6784ebf436ed75b2af061be428b6eaf60f30b26697d", url="https://github.com/llnl/ExaCMech/archive/refs/tags/v0.3.0.tar.gz")
    version("v0.2.0", sha256="3a2b229b493cfb3490c4a4cbe280c32de8f361f0aa4b9a2a84412dcbfa7e5db6", url="https://github.com/llnl/ExaCMech/archive/refs/tags/v0.2.0.tar.gz")

    variant("openmp", default=False)
    variant("shared", default=False)

    depends_on("blt", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("snls")
    depends_on("raja")
    depends_on("camp")
    depends_on("chai")
    depends_on("umpire")

    # variant dependent dependencies
    depends_on("raja+openmp", when="+openmp")
    depends_on("cub", when="+cuda")

    def cmake_args(self):
        args = [
            self.define('RAJA_DIR', join_path(self.spec['raja'].prefix, 'lib/cmake/raja')),
            self.define('SNLS_DIR', self.spec['snls'].prefix),
            self.define('CAMP_DIR', self.spec['camp'].prefix),
            self.define('CHAI_DIR', self.spec['chai'].prefix),
            self.define('UMPIRE_DIR', self.spec['umpire'].prefix),
            self.define('BLT_SOURCE_DIR', self.spec['blt'].prefix),
            self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
            self.define('ENABLE_SNLS_V03', 'ON'),
            self.define('ENABLE_GTEST', 'OFF'),
            self.define('ENABLE_MINIAPPS', 'OFF'),
            self.define_from_variant('ENABLE_OPENMP', 'openmp'),
            self.define('CMAKE_CUDA_SEPARABLE_COMPILATION', 'ON'),
            self.define_from_variant('ENABLE_CUDA', 'cuda'),
            self.define_from_variant('ENABLE_HIP', 'rocm'),
            self.define('ENABLE_TESTS', 'OFF'),
        ]
        return args
