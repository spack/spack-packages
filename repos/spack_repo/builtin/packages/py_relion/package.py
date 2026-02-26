# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRelion(PythonPackage, CudaPackage):
    """This is a helper package for relion, not to be used by end-users.

    relion (for REgularised LIkelihood OptimisatioN, pronounce rely-on) is a
    software package that employs an empirical Bayesian approach for electron
    cryo-microscopy (cryo-EM) structure determination.
    """

    homepage = "https://relion.readthedocs.io/en/latest/"
    url = "https://github.com/3dem/relion/archive/refs/tags/5.0.1.tar.gz"

    maintainers("Markus92")

    license("GPL-2", checked_by="Markus92")

    version("5.0.1", sha256="acbf898e96513b092514a56ff2a255c69a795e7a6f04131eacc8f55e2a900c23")
    version("5.0.0", sha256="5d02d529bfdb396204310b35963f35e5ec40ed9fd10bc88c901119ae7d7739fc")

    variant("cuda", default=True, description="Build with CUDA (recommended)")

    depends_on("python@3.10")
    depends_on("py-setuptools@45:", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-setuptools-scm@6.3:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-torchvision@0.15.2")
        depends_on("py-tqdm@4.65.0")
        depends_on("py-mrcfile@1.4.3")
        depends_on("py-starfile@0.5.6:")
        depends_on("py-loguru@0.7.0")
        depends_on("py-scikit-learn@1.3.0")
        depends_on("py-umap-learn@0.5.3")
        depends_on("py-matplotlib@3.7.2")
        depends_on("py-pydantic@1.10.19")
        depends_on("py-napari+all@0.4.18")
        depends_on("py-pyqt5@5.15.9")
        depends_on("py-typer@0.9.0")
        depends_on("py-biopython@1.81")
        depends_on("py-fastcluster@1.2.6")
        depends_on("py-seaborn@0.12.2")
        depends_on("py-dill@0.3.7")
        depends_on("py-numpy@:2")
        depends_on("py-click@:8.1")
        depends_on("py-mdocfile")
        depends_on("py-rich")
        depends_on("py-einops")
        depends_on("py-lil-aretomo")
        depends_on("py-makefun")
        depends_on("py-lru-dict")
        depends_on("topaz-3dem", type="run")
        depends_on("model-angelo", type="run")
        depends_on("py-relion-blush", type="run")
        depends_on("py-relion-classranker", type="run")

        for arch in CudaPackage.cuda_arch_values:
            depends_on(
                f"tsne-cuda@3.0.1 +cuda cuda_arch={arch} +python",
                when=f"@5.0 +cuda cuda_arch={arch}",
            )
            depends_on(
                f"py-torch@2.0.1 +cuda cuda_arch={arch}", when=f"@5.0 +cuda cuda_arch={arch}"
            )

        depends_on("py-torch@2.0.1 ~cuda", when="@5.0 ~cuda")

    # Set version so setuptools won't complain about not being able to determine it
    def setup_build_environment(self, env):
        env.set("SETUPTOOLS_SCM_PRETEND_VERSION", str(self.spec.version))
