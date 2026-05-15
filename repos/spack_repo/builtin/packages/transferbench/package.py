# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary

from spack.package import *


class Transferbench(ROCmLibrary, CMakePackage):
    """TransferBench is a utility capable of benchmarking simultaneous copies between
    user-specified devices (CPUs/GPUs)"""

    homepage = "https://github.com/ROCm/TransferBench"
    url = "https://github.com/ROCm/TransferBench/archive/refs/tags/rocm-6.4.0.tar.gz"

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")
    executables = ["TransferBench"]

    tags = ["rocm"]

    license("MIT")

    version("7.2.1", sha256="ff0dd90869eff77e00bb748149bcfa359d9c7d503c438f4bb64a88a7e39cbc3d")
    version("7.2.0", sha256="4be9d66044827d7b1950b4fd7ce50913d0926822e88e3441f472ca6a62086a15")
    version("7.1.1", sha256="a02afb6130990ae3a980bb512a7d414e009801d24fce56c6f66b449d61dae9e0")
    version("7.1.0", sha256="9d7386abeea5ec290b4299684a0ec810d5241a40f7bb1482e794285baa1a4805")
    version("7.0.2", sha256="f4afbc00029bce5345f06786d6adab9619c1852f919f7750fd602537d5403d60")
    version("7.0.0", sha256="5b4551aba424fe6467034ea2c6232f614f80504b1732578d3d66cc19d9c9d736")
    version("6.4.3", sha256="fb75eb571a059c94ae082b5b8bfa751635b769a77ca40c8477a12a12c4f53ccd")
    version("6.4.2", sha256="241da92846e91ac891662d5cbe560115a2749b93bd9a654a84a9d1f6eb3ca0ef")
    version("6.4.1", sha256="7334dc4e815e7d7e8ccc138475949618ed5dea0ccc9f6b7edac492c6f4b12762")
    version("6.4.0", sha256="3d2d5723278774a26f4889643bd9025a883982b111321106e4343c998b229298")
    version("6.3.3", sha256="b473d47ff44501d111dd13fa2e9f723967df0035219168b490a1c013a123cbf6")
    version("6.3.2", sha256="ae2210b669416f558ec9da85b67f45f31a7705de4d553e54b0eabe2fb8e8f665")
    version("6.3.1", sha256="611fb858d4a2cb48fb8942b1a85c54ab3212fb74952327757f673551e0c507c0")
    version("6.3.0", sha256="1b67f7ac96a44ab20a02e45a94046a0991b46b84efbd9f9639b864189214ded1")

    depends_on("cxx", type="build")
    depends_on("numactl")

    for ver in [
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
        "7.2.1",
    ]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")

    patch("001-link-hsa-numa.patch", when="@:6.4.1")
    patch("001-link-hsa-numa-6.4.2.patch", when="@6.4.2:6.4.3")

    def setup_build_environment(self, env):
        env.set("CXX", self.spec["hip"].hipcc)

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@7.0:"):
            args.append(self.define("HSA_INCLUDE_DIR", self.spec["hsa-rocr-dev"].prefix.include))
            args.append(
                self.define(
                    "HSA_LIBRARY", f"{self.spec['hsa-rocr-dev'].prefix.lib}/libhsa-runtime64.so"
                )
            )
        return args
