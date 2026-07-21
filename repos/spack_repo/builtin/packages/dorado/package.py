# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Dorado(CMakePackage, CudaPackage):
    """Dorado is a high-performance, easy-to-use, open source basecaller
    for Oxford Nanopore reads."""

    homepage = "https://github.com/nanoporetech/dorado"
    git = "https://github.com/nanoporetech/dorado.git"
    url = "https://github.com/nanoporetech/dorado/archive/refs/tags/v0.5.1.tar.gz"

    maintainers("snehring")

    version("1.4.0", commit="ba44a0132a6fc54ffa790add140ebf6006a5a994", submodules=True)
    version("1.2.0", commit="f9443bb8695f075dadc60bf4d1d92d8fd4361668", submodules=True)
    version("1.1.1", commit="e72f14925cd435fff823ebf244ce2195b135a863", submodules=True)
    version("1.0.2", commit="c758d2f6b01db2993282b4705f75d0cd53af43b8", submodules=True)
    version("0.9.6", commit="0949eb8de80dce9a198c08c0e37e31ed1eb627fc", submodules=True)
    version("0.8.3", commit="98456f7e595e64c0ec4bc13bda6cbdbe96c12039", submodules=True)
    version("0.7.4", commit="a9de62e43eea37ce4e912faedb5ac57cd9b1c7dc", submodules=True)
    version("0.6.3", commit="19d900eb9ff5e85e8deec77106def424b6d517d3", submodules=True)
    version("0.5.3", commit="d9af343c0097e0e60503231e036d69e6eda2f19a", submodules=True)
    version("0.5.1", commit="a7fb3e3d4afa7a11cb52422e7eecb1a2cdb7860f", submodules=True)

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("git", type="build")
    depends_on("curl", type="build")
    depends_on("cuda")
    depends_on("hdf5@:1+hl+cxx+szip")
    depends_on("htslib@1.15.1", when="@:0.5")
    depends_on("htslib@1.21", when="@0.6:1.1")
    depends_on("htslib@1.22", when="@1.2.0:")
    depends_on("openssl")
    depends_on("zstd")
    depends_on("libdeflate")
    depends_on("zlib-api")

    conflicts("%gcc@:8", msg="Dorado requires at least gcc@9 to compile.")
    conflicts("%gcc@13:", msg="Dorado will not build with gcc@13 and newer.")

    patch("hdf5-libaec-0.5.3.patch", when="@:0.5.3")
    patch("hdf5-libaec-0.6.3.patch", when="@0.6:0.9")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libdeflate"].prefix.lib64)
        env.prepend_path("LIBRARY_PATH", self.spec["libdeflate"].prefix.lib64)

    def patch(self):
        if self.spec.satisfies("@:0.9"):  # 1.0 removes these lines from the CMakeLists.txt files
            filter_file(
                "add_dependencies(dorado_lib htslib_project)", "", "CMakeLists.txt", string=True
            )
            filter_file(
                "add_dependencies(dorado_utils htslib_project)",
                "",
                "dorado/utils/CMakeLists.txt",
                string=True,
            )

            if self.spec.satisfies("@0.9.5:0.9.6"):
                filter_file(
                    "add_dependencies(dorado_secondary htslib_project)",
                    "",
                    "dorado/secondary/CMakeLists.txt",
                    string=True,
                )

        # Make CMake use spack's hdflib
        with open("cmake/Htslib.cmake", "w") as f:
            f.write("include_directories(${HTSLIB_PREFIX}/include)\n")
            f.write("add_library(htslib SHARED IMPORTED)\n")
            f.write(
                "set_target_properties(htslib PROPERTIES IMPORTED_LOCATION "
                "${HTSLIB_PREFIX}/lib/libhts.so)\n"
            )

    def cmake_args(self):
        htslib_prefix = self.spec["htslib"].prefix
        args = [f"-DHTSLIB_PREFIX={htslib_prefix}", f"-DDORADO_INSTALL_PATH={self.prefix}"]
        return args
