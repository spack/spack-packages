# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ensmallen(CMakePackage):
    """ensmallen is a high-quality C++ library for non-linear numerical
    optimization.

    ensmallen provides many types of optimizers that can be used for
    virtually any numerical optimization task. This includes gradient
    descent techniques, gradient-free optimizers, and constrained
    optimization. ensmallen also allows optional callbacks to customize
    the optimization process."""

    homepage = "https://ensmallen.org"
    url = "https://github.com/mlpack/ensmallen/archive/refs/tags/2.19.1.tar.gz"

    license("BSD-3-Clause")

    version("3.11.0", sha256="8839a6f50aada2a930e7d79e2834a64ea8e782687d1709b7a554ceb4014be533")
    version("3.10.0", sha256="248e2036856f7aa8fab34ca02fa3a79b2c9af20f53b1d26e3de939d150dcbb3a")
    version("2.22.2", sha256="da9ce4bdd07f2c8d950e3797456da3152dfa5d1b0f5987a489fbe224f52e7e4f")
    version("2.22.1", sha256="daf53fe96783043ca33151a3851d054a826fab8d9a173e6bcbbedd4a7eabf5b1")
    version("2.21.1", sha256="820eee4d8aa32662ff6a7d883a1bcaf4e9bf9ca0a3171d94c5398fe745008750")
    version("2.19.1", sha256="f36ad7f08b0688d2a8152e1c73dd437c56ed7a5af5facf65db6ffd977b275b2e")

    variant("openmp", default=True, description="Use OpenMP for parallelization")
    variant("bandicoot", default=False, description="Enable Bandicoot support", when="@3:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.3.2:")
    depends_on("armadillo@9.800.0:")
    depends_on("armadillo@10.8.2:", when="@2.22:")
    depends_on("bandicoot@2.1:", when="@3: +bandicoot")

    def cmake_args(self):
        args = [
            self.define_from_variant("USE_OPENMP", "openmp"),
            self.define_from_variant("USE_BANDICOOT", "bandicoot"),
        ]
        return args
