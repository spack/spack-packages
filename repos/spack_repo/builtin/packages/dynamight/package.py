# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Dynamight(PythonPackage, CudaPackage):
    """Estimating dynamics from cryo-EM images."""

    homepage = "https://github.com/3dem/DynaMight"
    git = "https://github.com/3dem/DynaMight.git"

    maintainers("Markus92")

    license("BSD-3-Clause")

    # no release tags exist upstream - pinned to the commit used in
    # environment_blackwell.yml's git+https install. Dashless digits
    # (matching topaz-3dem/model-angelo's date-version convention) since
    # hatch-vcs's version detection rejects "2025-09-18" as an invalid
    # PEP 440 version.
    version("20250918", commit="358db04d5c2ec2997f3f17060a456293f0b02185")

    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    # This is a git checkout at a specific commit, not a tagged release, so
    # hatch-vcs's own git-tag version detection isn't reliable.
    def setup_build_environment(self, env):
        env.set("SETUPTOOLS_SCM_PRETEND_VERSION", str(self.spec.version))

    variant("cuda", default=True, description="Build with CUDA (recommended)")
    # The tsne-cuda and py-torch dependencies below are only selected for a
    # specific cuda_arch, not for +cuda alone - cuda_arch=none (the
    # CudaPackage default) would match neither `when` clause, silently
    # installing without them.
    conflicts(
        "cuda_arch=none",
        when="+cuda",
        msg="Must specify CUDA compute capabilities of your GPU, see "
        "https://developer.nvidia.com/cuda-gpus",
    )

    with default_args(type=("build", "run")):
        # Floors below come from a cross-repo API-compatibility audit
        # (py-relion, model-angelo, etc. - DynaMight was one of the six
        # repos in that pool). No ceilings unless a specific break is
        # known: "verified compatible up to X" during that audit isn't
        # evidence that X+1 breaks anything.
        depends_on("py-numpy@1.26.1:")
        depends_on("py-mrcfile@1.4.3:")
        depends_on("py-starfile@0.5.6:")
        depends_on("py-scikit-learn@1.3.0:")
        depends_on("py-umap-learn@0.5.3:")
        # floor raised past 3.8.3, which caps numpy at <2.0.
        depends_on("py-matplotlib@3.9.0:")
        depends_on("py-napari+all@0.4.18:")
        # 5.15.x is PyQt5's own stable minor line; PyQt6 is a different
        # API entirely, so cap before crossing that boundary.
        depends_on("py-pyqt5@5.15.9:5")
        depends_on("py-typer@0.9.0:")
        depends_on("py-biopython@1.81:")
        depends_on("py-tqdm@4.65.0:")
        depends_on("py-tensorboard")

        for arch in CudaPackage.cuda_arch_values:
            depends_on(
                f"tsne-cuda@3.0.1 +cuda cuda_arch={arch} +python",
                when=f"+cuda cuda_arch={arch}",
            )
            # No ceiling: only verified up to 2.13.0, no specific break
            # known beyond it.
            depends_on(
                f"py-torch@2.7.1: +cuda cuda_arch={arch}",
                when=f"+cuda cuda_arch={arch}",
            )
        depends_on("py-torch@2.7.1: ~cuda", when="~cuda")
