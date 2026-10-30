# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class RapidsCmake(Package):
    """NVIDIA rapids-cmake is a collection of CMake modules that are useful for
    all RAPIDS projects."""

    homepage = "https://docs.nvidia.com/rapids-cmake"
    git = "https://github.com/rapidsai/rapids-cmake.git"

    maintainers("rbberger")

    license("Apache-2.0")

    version("26.10.00", tag="v26.10.00", commit="c47d47dbe2a60a71c2b5de300f4c2b09cc809bff")

    def install(self, spec, prefix):
        install_dir = join_path(prefix.lib.cmake, "rapids-cmake")
        mkdirp(install_dir)
        install_tree(".", install_dir)
