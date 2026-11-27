# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.packages.kokkos.package import Kokkos

from spack.package import *


class Symmetrix(PythonPackage, CudaPackage):
    """Symmetrix: a package for functions equivariant under translation, rotation,
    inversion, and exchange of particles. It provides fast CPU and GPU (Kokkos)
    implementations of MACE and NequIP machine-learning interatomic potentials
    together with an ASE calculator."""

    homepage = "https://github.com/wcwitt/symmetrix"
    git = "https://github.com/wcwitt/symmetrix.git"

    maintainers("mkrack", "wcwitt")

    license("MIT")

    # The sources vendor Kokkos, Kokkos Kernels, sphericart, gpu-lite, nlohmann-json
    # and pybind11 as git submodules
    version("main", branch="main", submodules=True)
    version(
        "0.3.1", tag="v0.3.1", commit="664edba7ff3da0650382e64ed9f57681969408c0", submodules=True
    )
    version(
        "0.3.0", tag="v0.3.0", commit="fc7e53276baa7728f08bee0ddd865a20f82ff998", submodules=True
    )
    version(
        "0.2.0", tag="v0.2.0", commit="3a9063b42ff6f4a91d4b19ba25f2396a6cfef688", submodules=True
    )
    version(
        "0.1.0", tag="v0.1.0", commit="f6c2b2791ef130615e964b77103de876424705bd", submodules=True
    )

    build_directory = "symmetrix"

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # C++20 is required (vendored Kokkos 5)
    conflicts("%gcc@:10.3", msg="symmetrix requires C++20 support (GCC 10.4 or newer)")

    # See symmetrix/pyproject.toml
    depends_on("cmake@3.27:", type="build")
    depends_on("py-scikit-build-core+pyproject@1:", type="build")
    depends_on("py-pybind11", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-ase", type=("build", "run"))

    with when("+cuda"):
        # Vendored Kokkos 5 requires CUDA 12.2 or newer
        depends_on("cuda@12.2:")
        for _arch in CudaPackage.cuda_arch_values:
            if _arch not in Kokkos.spack_cuda_arch_map:
                conflicts(f"cuda_arch={_arch}", msg=f"Kokkos does not support cuda_arch={_arch}")
            elif int(_arch) < 60:
                # The CUDA kernels need double-precision atomicAdd
                conflicts(f"cuda_arch={_arch}", msg="symmetrix+cuda requires sm_60 or newer")
        conflicts("cuda_arch=none", msg="symmetrix+cuda requires a cuda_arch value")

    @run_before("install")
    def remove_march_native(self):
        # Let Spack's compiler wrappers set the target architecture flags
        src = self.stage.source_path
        cmake_files = [join_path(src, "libsymmetrix", "CMakeLists.txt")]
        cmake_files += glob.glob(
            join_path(src, "symmetrix", "source", "cpp", "*", "CMakeLists.txt")
        )
        for cmake_file in cmake_files:
            filter_file(r"\$<\$<COMPILE_LANGUAGE:CXX>:-march=native>", "", cmake_file)
            filter_file(r"-march=native;", "", cmake_file)

    def config_settings(self, spec, prefix):
        defines = {
            "CMAKE_BUILD_TYPE": "Release",
            "SYMMETRIX_KOKKOS": "ON",
            "Kokkos_ENABLE_SERIAL": "ON",
            "Kokkos_ARCH_NATIVE": "OFF",
            "SPHERICART_ARCH_NATIVE": "OFF",
        }
        if spec.satisfies("+cuda"):
            cuda_archs = spec.variants["cuda_arch"].value
            # Kokkos supports only one CUDA architecture at a time
            if len(cuda_archs) != 1:
                raise InstallError("symmetrix supports only one cuda_arch at a time")
            cuda_arch = cuda_archs[0]
            kokkos_arch, _ = Kokkos.spack_cuda_arch_map[cuda_arch]
            defines.update(
                {
                    "CMAKE_CUDA_COMPILER": spec["cuda"].prefix.bin.nvcc,
                    "CMAKE_CUDA_ARCHITECTURES": cuda_arch,
                    "Kokkos_ENABLE_CUDA": "ON",
                    f"Kokkos_ARCH_{kokkos_arch.upper()}": "ON",
                    "SYMMETRIX_SPHERICART_CUDA": "ON",
                }
            )
        else:
            # Prevent the build from picking up a CUDA compiler found on the system
            defines.update(
                {
                    "CMAKE_CUDA_COMPILER": "OFF",
                    "Kokkos_ENABLE_CUDA": "OFF",
                    "SYMMETRIX_SPHERICART_CUDA": "OFF",
                }
            )

        settings = {f"cmake.define.{key}": value for key, value in defines.items()}
        settings["build.tool-args"] = f"-j{make_jobs}"
        settings["build.verbose"] = "true"
        return settings
