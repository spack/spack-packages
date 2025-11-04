# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Aretomo(Package):
    """AreTomo, an abbreviation for Alignment and Reconstruction for Electron
    Tomography, is a GPU accelerated software package that fully automates
    motion-corrected marker-free tomographic alignment and reconstruction in a
    single package."""

    # AreTomo can be downloaded from the UCSF website
    # https://msg.ucsf.edu/software
    # AreTomo is not open-source. It is free for academic use only.
    homepage = "https://doi.org/10.1016/j.yjsbx.2022.100068"
    manual_download = True

    maintainers("Markus92")

    version(
        "1.3.4",
        url=f"file://{os.getcwd()}/AreTomo_1.3.4_Feb222023.zip",
        sha256="d331e4a1843fd8e457b6c58e3ab4255582673f024bfb0fae08cd54fc0c0c77e7",
    )

    depends_on("patchelf", type="build")

    depends_on("cuda@10.1,10.2,11.1:11.8", type="link")

    def install(self, spec, prefix):
        cuda_version = spec["cuda"].version.up_to(2).joined

        mkdirp(prefix.bin)
        install(
            "AreTomo_{0}_Cuda{1}_*".format(spec.version, cuda_version),
            join_path(prefix.bin, "AreTomo"),
        )

    @run_after("install")
    def ensure_rpaths(self):
        patchelf = which("patchelf")
        patchelf(
            "--set-rpath", self.spec["cuda"].prefix.lib64, join_path(self.prefix.bin, "AreTomo")
        )
