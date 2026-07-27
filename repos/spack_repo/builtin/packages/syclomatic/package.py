# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Syclomatic(CMakePackage):
    """SYCLomatic is a tool to assist developers in migrating existing CUDA
    code to SYCL C++ heterogeneous programming.  The main binary is ``c2s``
    (also available as ``dpct``).
    """

    homepage = "https://oneapi-src.github.io/SYCLomatic/"
    git = "https://github.com/oneapi-src/SYCLomatic.git"

    maintainers("rscohn2")

    license("Apache-2.0 WITH LLVM-exception")

    requires(
        "platform=linux",
        msg="Upstream SYCLomatic works on Linux and Windows, but the spack "
        "package is only available on Linux",
    )

    # Daily release builds – tags are YYYYMMDD
    version("SYCLomatic", branch="SYCLomatic")
    version(
        "20260506",
        commit="119286ff2e066bc1f6e92d68a0e4359a703581d3",
        submodules=False,
    )
    version(
        "20260429",
        commit="0c5c6fb01003af342c9edac3d730218797e78650",
        submodules=False,
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.14:", type="build")
    depends_on("ninja", type="build")
    depends_on("python@3:", type="build")

    variant(
        "targets",
        default=("X86", "NVPTX"),
        values=str,
        multi=True,
        description="LLVM targets to build",
    )

    # The CMakeLists.txt lives under the llvm/ subdirectory of the repo.
    root_cmakelists_dir = "llvm"
    install_targets = ["install-c2s"]

    def cmake_args(self):
        targets = ";".join(self.spec.variants["targets"].value)
        return [
            self.define("LLVM_ENABLE_PROJECTS", "clang"),
            self.define("LLVM_TARGETS_TO_BUILD", targets),
            self.define("CMAKE_BUILD_TYPE", "Release"),
        ]

    def build(self, spec, prefix):
        # Skip generic LLVM build; install-c2s will build only what is needed.
        pass
