# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    # Versions 0.7.0+ have both CUDA 12 and CUDA 13 precompiled binary versions
    "1.0.0-13": {
        "Linux-x86_64": (
            "0a155540d7b90d42105d38886fa630f1ec91d7b05580a28bd1fa04fa16e19ffe",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-1.0.0.35_cuda13-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "bd40403a984ab25ad7ac96d54d14863645256c7dca449fdf9836309d7b80e308",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-sbsa/libcudss-linux-sbsa-1.0.0.35_cuda13-archive.tar.xz",
        ),
    },
    "1.0.0-12": {
        "Linux-x86_64": (
            "b8c882c3ebc8b319886f5a06e74311c5eea09846925ba5a19892de4921201746",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-1.0.0.35_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "01e0008823e2980b197fed1102a1fe85b4bf0eef60bdf516c9052745804619e8",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-sbsa/libcudss-linux-sbsa-1.0.0.35_cuda12-archive.tar.xz",
        ),
    },
    "0.8.0-13": {
        "Linux-x86_64": (
            "ba18f5fd80dcbbe905d158caac5b3061d848442bb5abd477b5f296b4257a4937",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.8.0.10_cuda13-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "c5fe7e5796792e10c3c5971bbb169ab3040ba61fe6fc99bdcbc02cf0f1ed9409",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-sbsa/libcudss-linux-sbsa-0.8.0.10_cuda13-archive.tar.xz",
        ),
    },
    "0.8.0-12": {
        "Linux-x86_64": (
            "29716a05c64b28531309afcb7a9dd5044081a43197e72bdd0fbf29e9b4ee4707",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.8.0.10_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "11cf97c8cecf3a651bab1890894c8b8793666a17ad3002104e573efa564af231",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.8.0.10_cuda12-archive.tar.xz",
        ),
    },
    "0.7.1-13": {
        "Linux-x86_64": (
            "84b34ebe7fad40ec10f2aab2957a63b6070bd8ce16e3ada3e6bcac7317256347",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.7.1.4_cuda13-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "de8295cb6773992bd1ca7e2ad93caae1fd18eba39175f0101b85d53abd3e0179",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-sbsa/libcudss-linux-sbsa-0.7.1.4_cuda13-archive.tar.xz",
        ),
    },
    "0.7.1-12": {
        "Linux-x86_64": (
            "946571d9ea164f948e402dd97a14541cb90fbec800336cfa7ae644af5937632f",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.7.1.4_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "f283c31b6badf4a5277014295705eac8e6e28f27de30d746719ea1cef7a750b8",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.7.1.4_cuda12-archive.tar.xz",
        ),
    },
    "0.7.0-13": {
        "Linux-x86_64": (
            "939606e8d062ee0fc28094e7be19e22191662e8593bc7f5eec16220ad836feb9",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.7.0.20_cuda13-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "f915eb581ab965d0baa74cd1e529086fce00e9d14d9366da4480b5ef7fabb8a6",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-sbsa/libcudss-linux-sbsa-0.7.0.20_cuda13-archive.tar.xz",
        ),
    },
    "0.7.0-12": {
        "Linux-x86_64": (
            "c98d5ef87e8b6a356b21a678715033b19620ce58b5fa64c97e25e6d3e76e42dc",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.7.0.20_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "ce3de5e6a0cee00fd1fc355881308ef0c692c6e14b6a5625aa35a7f9df98b846",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.7.0.20_cuda12-archive.tar.xz",
        ),
    },
    # Versions 0.6.0 and older only have CUDA 12 precompiled binaries
    "0.6.0": {
        "Linux-x86_64": (
            "159ce1d4e3e4bba13b0bd15cf943e44b869c53b7a94f9bac980768c927f02e75",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.6.0.5_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "e6f5d5122d735f9dbfd42c9eaba067a557a5613ee4a6001806935de11aff4b09",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.6.0.5_cuda12-archive.tar.xz",
        ),
    },
    "0.5.0": {
        "Linux-x86_64": (
            "5245d2ba26a590839e2f1dd074f87e39ee5cc201c3b29245b35c7060d59c37a5",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.5.0.16_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "5d07496e90fc0afb334a7e434c86c6083b1e8cf56dc65d70a01bd811e54096d7",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.5.0.16_cuda12-archive.tar.xz",
        ),
    },
}


class Cudss(Package):
    """NVIDIA cuDSS is a GPU-accelerated Direct Sparse Solver library
    for solving linear systems with very sparse matrices"""

    homepage = "https://developer.nvidia.com/cudss"

    maintainers("ddement", "imciner2")

    skip_version_audit = ["platform=darwin", "platform=windows"]

    for ver, packages in _versions.items():
        pkg = packages.get(f"{platform.system()}-{platform.machine()}")
        if pkg:
            version(ver, sha256=pkg[0], url=pkg[1])

            ver_split = ver.split("-")
            if len(ver_split) == 2:
                _, cuda_ver = ver_split
                depends_on("cuda@{}".format(cuda_ver), when="@{}".format(ver))

    # Versions without CUDA 13 builds
    depends_on("cuda@12", when="@:0.6")

    variant(
        "mpi",
        default=False,
        description="Build a communication layer for the selected MPI implementation",
    )

    depends_on("mpi", when="+mpi")

    # patchelf --add-rpath requires 0.14+ (see add_cuda_rpath)
    depends_on("patchelf@0.14:", type="build")

    conflicts(
        "+mpi",
        when="@:0.6 target=aarch64:",
        msg="cuDSS aarch64 archives provide communication-layer sources starting at 0.7.0",
    )

    def install(self, spec, prefix):
        install_tree(".", prefix)

        if "+mpi" in spec:
            # NVIDIA calls this source and build target "openmpi", but it uses
            # the standard MPI API and can be built against any MPI provider.
            # Use a provider-neutral installed name because the concrete MPI
            # dependency, rather than the filename, identifies its ABI.
            with working_dir("src"):
                with set_env(
                    CUDA_PATH=spec["cuda"].prefix,
                    CUDSS_PATH=self.stage.source_path,
                    MPI_PATH=spec["mpi"].prefix,
                    NVCC_PREPEND_FLAGS="-Xlinker=-rpath -Xlinker=%s:%s"
                    % (spec["mpi"].prefix.lib64, spec["mpi"].prefix.lib),
                ):
                    bash = which("bash", required=True)
                    bash("./cudss_build_commlayer.sh", "openmpi")

                comm_layer = "libcudss_commlayer_openmpi.so"
                if not os.path.isfile(comm_layer):
                    raise InstallError(
                        "cuDSS did not produce the requested MPI communication layer"
                    )
                install(comm_layer, join_path(prefix.lib, "libcudss_commlayer_mpi.so"))

    # The prebuilt libcudss.so needs libcublas and libnvrtc, but its RUNPATH is
    # only $ORIGIN, so linking or running fails unless LD_LIBRARY_PATH is set.
    # Append the CUDA lib dir with --add-rpath (not --set-rpath) to keep $ORIGIN,
    # which libcudss.so needs to find its own mtlayer/commlayer libraries.
    @run_after("install")
    def add_cuda_rpath(self):
        patchelf = which("patchelf", required=True)
        cuda_libdirs = self.spec["cuda"].libs.directories
        for lib in find(self.prefix.lib, "libcudss.so*", recursive=False):
            if os.path.islink(lib):
                continue
            for d in cuda_libdirs:
                patchelf("--add-rpath", d, lib)
