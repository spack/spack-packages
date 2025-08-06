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
        version("1.4.2", sha256="97735aa22d01135933c5b698d8990ed371a89aec90df5193a24400c6460eb276")
        version("1.4.0", sha256="d68c4ab9c6a740a73aede7120854a1fb3aea94279afb5fe2ab50387b725e6329")
        version("1.3.2", sha256="d9fb3537278be179fd9bfa45f58e921649a893b169cbf8fa173ba95fdb831d10")
        version("1.3.1", sha256="861fb9ab9fbe0ca72e538ef7c2f8e5d2ebd02d9b6c852c8d57a48782a3a89547")
        version("1.3.0", sha256="7da654830ec64c4b66a965d184d008f310d90fa4594b9166da1d530381275e5f")
        version("1.2.6", sha256="b16d512bd4a122563d73a568d44bb724fb8b96d0d20662ce1a94274fb39dfaa6")
        version("1.2.3", sha256="49dfe25316f9f65f77861383a583e1cd9b466abd6dc0e9f446ffbdefdafeb370")
        version("1.2.1", sha256="b68db6850d64fc56635ff968b53587c96bb42108ba58a415bef447f0810b9e57")
        version("1.1.0", sha256="1cb7c486d7f575fefcc7dae5037e9bb645842e1e43b22fa3c18fd0e4d2a189db")
        version("1.0.5", sha256="84bf9c4f06666090303b81777d2e579f073e204ed40746f5286d9cfe26047cf8")

    depends_on("patchelf", type="build")

    depends_on("cuda@8.0,9.1", type="run", when="@1.0.5")
    depends_on("cuda@8.0,9.0:9.1", type="run", when="@1.1.0")
    depends_on("cuda@8.0,9.1:9.2", type="run", when="@1.2.1")
    depends_on("cuda@8.0,9.1:9.2,10.0", type="run", when="@1.2.3")
    depends_on("cuda@8.0,9.2,10.1", type="run", when="@1.2.6:1.3.0")
    depends_on("cuda@9.2,10.1:10.2", type="run", when="@1.3.1")
    depends_on("cuda@8.0,9.2,10.0:10.2", type="run", when="@1.3.2")
    depends_on("cuda@9.2,10.0:10.2,11.0", type="run", when="@1.4.0")
    depends_on("cuda@10.0:10.2,11.1", type="run", when="@1.4.2")
    depends_on("cuda@10.0:10.2,11.1:11.3", type="run", when="@1.4.4:1.4.5")
    depends_on("cuda@10.2,11.1:11.5", type="run", when="@1.4.7")
    depends_on("cuda@10.1:10.2,11.1:11.6", type="run", when="@1.5.0")
    depends_on("cuda@10.1:10.2,11.1:11.8", type="run", when="@1.6.3")
    depends_on("cuda@9.2,10.1:10.2,11.1:11.8,12.1", type="run", when="@1.6.4")
    depends_on("libtiff", type="run")

    def install(self, spec, prefix):
        spec_version = (
            spec.version if spec.version not in ("1.0.5", "1.3.1") else "v{0}".format(spec.version)
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
        elif spec.satisfies("@1.1.0:1.3.2"):
            install(
                "bin/MotionCor2_{0}-Cuda{1}".format(spec_version, cuda_version),
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
