# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

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
    # Use Scipion's download server as the official site no longer hosts some deprecated versions
    url = "https://scipion.cnb.csic.es/downloads/scipion/software/em/motioncor2-1.6.4.tgz"

    version("1.6.4", sha256="bcb70ddde38daa7722e007f2509bae928c8603530524b6a36ed79f4ca7b3edb8")
    version("1.5.0", sha256="20cdb46efe3f3c578071ddbd9e9f45c8462b0cbb2fc5b3cfb2d0b66ded0d30e0")
    version("1.4.5", sha256="2f04bceb6069cd4f91a51447aac07b887be46206e094555bc445e89944ed2851")

    # Deprecated versions, no longer available in official site
    with default_args(deprecated=True):
        version("1.6.3", sha256="16c97516992d638ea817a943185213874dfad7d87a6bb71e102598922bb35c75")
        version("1.4.7", sha256="1c6ee6b76413db2d044a0048957a23907ad3217225d5e1a3659df3c3947d0e2c")
        version("1.4.4", sha256="1ced27bbc46a437ea1e5af8c9c842c9789da100d860d3663fc8215266cb4678e")
        version("1.0.5", sha256="84bf9c4f06666090303b81777d2e579f073e204ed40746f5286d9cfe26047cf8")

    depends_on("patchelf", type="build")

    with default_args(type="run"):
        depends_on("cuda@9.2,10.1:10.2,11.1:11.8,12.1", when="@1.6.4")
        depends_on("cuda@10.1:10.2,11.1:11.8", when="@1.6.3")
        depends_on("cuda@10.1:10.2,11.1:11.6", when="@1.5.0")
        depends_on("cuda@10.2,11.1:11.5", when="@1.4.7")
        depends_on("cuda@10.0:10.2,11.1:11.3", when="@1.4.4:1.4.5")
        depends_on("cuda@8.0,9.1", when="@1.0.5")

    depends_on("libtiff", type="run")

    def install(self, spec, prefix):
        spec_version = (
            spec.version if spec.version not in ("1.0.5") else "v{0}".format(spec.version)
        )
        cuda_version = (
            spec["cuda"].version.up_to(2).joined
            if spec.version != "1.0.5"
            else spec["cuda"].version.up_to(2)
        )

        mkdirp(prefix.bin)

        if spec.satisfies("@1.0.5"):
            install(
                "bin/MotionCor2_Cuda{0}_{1}".format(cuda_version, spec_version),
                join_path(prefix.bin, "MotionCor2"),
            )
        else:
            install(
                "bin/MotionCor2_{0}_Cuda{1}*".format(spec_version, cuda_version),
                join_path(prefix.bin, "MotionCor2"),
            )

    @run_after("install")
    def ensure_rpaths(self):
        patchelf = which("patchelf")
        patchelf(
            "--set-rpath", self.spec["cuda"].prefix.lib64, join_path(self.prefix.bin, "MotionCor2")
        )
