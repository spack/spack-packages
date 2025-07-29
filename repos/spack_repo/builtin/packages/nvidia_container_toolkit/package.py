# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform
import shutil
from glob import glob

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "1.17.6": {
        "Linux-aarch64": (
            "b43c34d357a6cf73b01178c627c551d2b1952fd2a7fb506f81286914f49f1a03",
            "https://github.com/NVIDIA/nvidia-container-toolkit/releases/download/v1.17.6/nvidia-container-toolkit_1.17.6_rpm_aarch64.tar.gz",
        ),
        "Linux-x86_64": (
            "e4b40e52035b56eb6aa5916006d4ade798be8cbdaec94ea83ae38cb010348eaf",
            "https://github.com/NVIDIA/nvidia-container-toolkit/releases/download/v1.17.6/nvidia-container-toolkit_1.17.6_rpm_x86_64.tar.gz",
        ),
    }
}


class NvidiaContainerToolkit(Package):
    """NVIDIA Container Toolkit is a package for enabling GPU access within containers"""

    maintainers("scothalverson")
    license("NVIDIA Software License Agreement")

    # Used to unpack the source RPM archives.
    depends_on("libarchive programs='bsdtar'", type="build")

    for ver, packages in _versions.items():
        key = "{0}-{1}".format(platform.system(), platform.machine())
        pkg = packages.get(key)
        if pkg:
            version(ver, sha256=pkg[0], url=pkg[1], expand=False)

    def install(self, spec, prefix):
        bsdtar = which("bsdtar")
        tar_file = glob(join_path(self.stage.source_path, "nvidia-container-toolkit*.tar.gz"))[0]
        tar_params = ["-x", "-f", tar_file]
        bsdtar(*tar_params)
        rpm_files = glob(join_path(self.stage.source_path, "release-*/packages/centos7/*/*.rpm"))
        for rpm_file in rpm_files:
            rpm_params = ["-x", "-f", rpm_file]
            bsdtar(*rpm_params)

        for directory in ["bin", "include", "lib", "lib64", "share"]:
            shutil.copytree(self.stage.source_path + "/usr/" + directory, prefix + "/" + directory)
