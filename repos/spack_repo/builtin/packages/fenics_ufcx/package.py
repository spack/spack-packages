# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class FenicsUfcx(CMakePackage):
    """FFCx provides the ufcx.h interface header for generated finite element
    kernels, used by DOLFINx. ufcx.h can be installed from the FFCx repo
    without a Python build or runtime dependency."""

    homepage = "https://github.com/FEniCS/ffcx"
    git = "https://github.com/FEniCS/ffcx.git"
    url = "https://github.com/FEniCS/ffcx/archive/v0.4.2.tar.gz"
    maintainers("ma595", "jhale", "garth-wells", "chrisrichardson")

    license("Unlicense")

    version("main", branch="main", no_cache=True)
    version("0.11.0", sha256="7df1c086c0398b72343a5f047c7e6aa17ea05f1ba123e3e0ca858d6a133b13bd")
    version("0.10.0", sha256="fa27e2dc68988cbf9aca537eb5a58483f75cc719c1a383713b7f8cca49844ff9")
    version("0.9.0", sha256="afa517272a3d2249f513cb711c50b77cf8368dd0b8f5ea4b759142229204a448")
    with default_args(deprecated=True):
        version("0.8.0", sha256="8a854782dbd119ec1c23c4522a2134d5281e7f1bd2f37d64489f75da055282e3")

    depends_on("cmake@3.19:", type="build")
    depends_on("c", type="build")

    root_cmakelists_dir = "cmake"
