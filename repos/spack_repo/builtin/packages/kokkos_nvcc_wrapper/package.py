# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.packages.kokkos.package import Kokkos

from spack.package import *


class KokkosNvccWrapper(Package):
    """The NVCC wrapper provides a wrapper around NVCC to make it a
    'full' C++ compiler that accepts all flags"""

    # We no longer maintain this as a separate repo
    # Download the Kokkos repo and install from there
    homepage = "https://github.com/kokkos/kokkos"
    git = "https://github.com/kokkos/kokkos.git"
    url = "https://github.com/kokkos/kokkos/releases/download/4.4.01/kokkos-4.4.01.tar.gz"

    maintainers("Rombur")

    license("BSD-3-Clause")

    for v, vargs in Kokkos.versions.items():
        version(str(v), **vargs)

    depends_on("cxx", type="build")  # needed for self.compiler.cxx

    depends_on("cuda")

    def install(self, spec, prefix):
        src = os.path.join("bin", "nvcc_wrapper")
        mkdir(prefix.bin)
        install(src, prefix.bin)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        wrapper = join_path(self.prefix.bin, "nvcc_wrapper")
        env.set("CUDA_ROOT", dependent_spec["cuda"].prefix)
        env.set("NVCC_WRAPPER_DEFAULT_COMPILER", self.compiler.cxx)
        env.set("KOKKOS_CXX", self.compiler.cxx)
        env.set("MPICH_CXX", wrapper)
        env.set("OMPI_CXX", wrapper)
        env.set("MPICXX_CXX", wrapper)  # HPE MPT

    @property
    def kokkos_cxx(self) -> str:
        return join_path(self.prefix.bin, "nvcc_wrapper")
