# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Motioncor2(Package):
    """MotionCor2 is a multi-GPU program that corrects beam-induced sample
    motion recorded on dose fractionated movie stacks. It implements a robust
    iterative alignment algorithm that delivers precise measurement and
    correction of both global and non-uniform local motions at
    single pixel level, suitable for both single-particle and
    tomographic images. MotionCor2 is sufficiently fast
    to keep up with automated data collection."""

    homepage = "http://msg.ucsf.edu/em/software"
    manual_download = True

    version("1.6.4", sha256="28bb3e6477abf34fe41a78bcb9da9d77d08e2e89ecd41240fab085a308e6c498")
    version("1.4.7", sha256="8c33969b10916835b55f14f3c370f67ebe5c4b2a9df9ec487c5251710f038e6b")

    depends_on("patchelf", type="build")

    depends_on("cuda@10.2,11.1:11.8,12.1", type="run")
    depends_on("libtiff", type="run")

    def url_for_version(self, version):
        return "file://{0}/MotionCor2_{1}.zip".format(os.getcwd(), version)

    def install(self, spec, prefix):
        cuda_version = spec["cuda"].version.up_to(2).joined

        mkdirp(prefix.bin)
        install(
            "MotionCor2_{0}_Cuda{1}_*".format(spec.version, cuda_version),
            join_path(prefix.bin, "MotionCor2"),
        )

    @run_after("install")
    def ensure_rpaths(self):
        patchelf = which("patchelf", required=True)
        patchelf(
            "--set-rpath", self.spec["cuda"].prefix.lib64, join_path(self.prefix.bin, "MotionCor2")
        )
