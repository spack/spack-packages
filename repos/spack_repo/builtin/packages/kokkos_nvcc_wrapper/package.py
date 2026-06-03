# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.generic import Package

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

    version("develop", branch="develop")

    version("5.1.1", sha256="8bdbee0f0ac383436743ad8a9e3e928705b34b31a25a92dc5179c52a3aa98519")
    version("5.1.0", sha256="7bdbdfc88033ed7d940c7940ed8919e1f2b78a9656c69276beb76ad45c41ec4e")
    version("5.0.2", sha256="188817bb452ca805ee8701f1c5adbbb4fb83dc8d1c50624566a18a719ba0fa5e")
    version("5.0.1", sha256="cf7d8515ca993229929be9f051aecd8f93cde325adac8a4f82ed6848adace218")
    version("5.0.0", sha256="c45f3e19c3eb71fc8b7210cb04cac658015fc1839e7cc0571f7406588ff9bcef")
    version("4.7.04", sha256="4213b248c39e112299fa94ee08817e51126fc02996ed6e2ab56aec4cdb80ee1f")
    version("4.7.03", sha256="969e7933b9426219b220f08036e489b3226e6d8cd24eecf2c5b80df8c37443c0")
    version("4.7.02", sha256="a81826ac0a167933d13506bc2a986fb5517038df9abb780fe9bb2c1d4e80803b")
    version("4.7.01", sha256="404cf33e76159e83b8b4ad5d86f6899d442b5da4624820ab457412116cdcd201")
    version("4.7.00", sha256="126b774a24dde8c1085c4aede7564c0b7492d6a07d85380f2b387a712cea1ff5")
    version("4.6.02", sha256="baf1ebbe67abe2bbb8bb6aed81b4247d53ae98ab8475e516d9c87e87fa2422ce")
    version("4.6.01", sha256="b9d70e4653b87a06dbb48d63291bf248058c7c7db4bd91979676ad5609bb1a3a")
    version("4.6.00", sha256="be72cf7fc6ef6b99c614f29b945960013a2aaa23859bfe1a560d8d9aa526ec9c")
    version("4.5.01", sha256="52d003ffbbe05f30c89966e4009c017efb1662b02b2b73190670d3418719564c")
    version("4.5.00", sha256="cbfb742feeb9e649db9eca0394e6ca9a22aa017a1e6aab8576990772a0e3135b")
    version("4.4.01", sha256="3413f0cb39912128d91424ebd92e8832009e7eeaf6fa8da58e99b0d37860d972")
    version("4.4.00", sha256="0b46372f38c48aa088411ac1b7c173a5c90f0fdb69ab40271827688fc134f58b")

    version(
        "4.3.01",
        sha256="5998b7c732664d6b5e219ccc445cd3077f0e3968b4be480c29cd194b4f45ec70",
        url="https://github.com/kokkos/kokkos/archive/4.3.01.tar.gz",
    )
    version(
        "4.3.00",
        sha256="53cf30d3b44dade51d48efefdaee7a6cf109a091b702a443a2eda63992e5fe0d",
        url="https://github.com/kokkos/kokkos/archive/4.3.00.tar.gz",
    )
    version(
        "4.2.01",
        sha256="cbabbabba021d00923fb357d2e1b905dda3838bd03c885a6752062fe03c67964",
        url="https://github.com/kokkos/kokkos/archive/4.2.01.tar.gz",
    )
    version(
        "4.2.00",
        sha256="ac08765848a0a6ac584a0a46cd12803f66dd2a2c2db99bb17c06ffc589bf5be8",
        url="https://github.com/kokkos/kokkos/archive/4.2.00.tar.gz",
    )
    version(
        "4.1.00",
        sha256="cf725ea34ba766fdaf29c884cfe2daacfdc6dc2d6af84042d1c78d0f16866275",
        url="https://github.com/kokkos/kokkos/archive/4.1.00.tar.gz",
    )
    version(
        "4.0.01",
        sha256="bb942de8afdd519fd6d5d3974706bfc22b6585a62dd565c12e53bdb82cd154f0",
        url="https://github.com/kokkos/kokkos/archive/4.0.01.tar.gz",
    )
    version(
        "4.0.00",
        sha256="1829a423883d4b44223c7c3a53d3c51671145aad57d7d23e6a1a4bebf710dcf6",
        url="https://github.com/kokkos/kokkos/archive/4.0.00.tar.gz",
    )
    version(
        "3.7.02",
        sha256="5024979f06bc8da2fb696252a66297f3e0e67098595a0cc7345312b3b4aa0f54",
        url="https://github.com/kokkos/kokkos/archive/3.7.02.tar.gz",
    )

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
