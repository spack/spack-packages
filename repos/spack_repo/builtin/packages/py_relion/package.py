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

    # scripts/eer_trajectory_handler.py uses np.str0, removed in numpy 2.0 (renamed to np.str_).
    patch("numpy2-str0-compat.patch")

    # align_tilt_series/__init__.py eagerly imports both the AreTomo and IMOD alignment
    # backends at module load - without py-lil-aretomo installed, the whole command fails to
    # start even for IMOD-only use. Makes the AreTomo import optional (try/except).
    patch("aretomo-optional-import.patch")

    variant("cuda", default=True, description="Build with CUDA (recommended)")
    # AreTomo is a closed-source prebuilt binary hard-tied to CUDA 10.1/10.2/11.1-11.8,
    # conflicting with py-torch's CUDA 12+ requirement (see aretomo/package.py). Off by
    # default; IMOD-based alignment (fiducials/patch tracking) is unaffected either way - see
    # aretomo-optional-import.patch above.
    variant(
        "aretomo",
        default=False,
        description="Enable AreTomo tilt-series alignment (needs old CUDA via py-lil-aretomo)",
    )

    # 3.10 and 3.11 are verified working (napari+PyQt5+numpy+pydantic install and smoke test).
    # 3.12 is excluded: pyhmmer has no cp312 wheel and napari+PyQt5 segfaults on Viewer()
    # construction. No ceiling: verified through 3.13, no specific break known beyond it.
    depends_on("python@3.10:3.11,3.13:")

    with default_args(type=("build", "run")):
        # Floors below come from a cross-repo API-compatibility audit of
        # environment_blackwell.yml (relion, relion-classranker, relion-blush, DynaMight,
        # topaz, model-angelo) - lowest verified-working version for each. No ceilings unless
        # a specific break is known: "verified compatible up to X" during that audit isn't
        # evidence that X+1 breaks anything.
        depends_on("py-torchvision@0.22.1:")
        depends_on("py-tqdm@4.65.0:")
        depends_on("py-mrcfile@1.4.3:")
        # get_particle_poses/{spheres,filaments}.py import scipy directly.
        depends_on("py-scipy@1.11.2:")
        depends_on("py-starfile@0.5.6:")
        depends_on("py-loguru@0.7.0:")
        depends_on("py-scikit-learn@1.3.0:")
        depends_on("py-umap-learn@0.5.3:")
        # matplotlib up to 3.8.3 caps numpy at <2.0, conflicting with the numpy floor below.
        depends_on("py-matplotlib@3.9.0:")
        # pydantic's v1 compat shim (which relion's own _metadata_models classes rely on) is
        # documented as removed in v3.0 - capped at the 2.x line, not an arbitrary patch version.
        depends_on("py-pydantic@1.10.18:2")
        depends_on("py-napari+all@0.4.18:")
        # 5.15.x is PyQt5's own stable minor line; PyQt6 is a different API entirely, so cap
        # before crossing that boundary.
        depends_on("py-pyqt5@5.15.9:5")
        depends_on("py-typer@0.9.0:")
        depends_on("py-biopython@1.81:")
        depends_on("py-seaborn@0.12.2:")
        # numpy<2.0 doesn't support python@3.13. The only removed-symbol breaks found in the
        # audit pool (this file's own np.str0, fixed via patch above; DynaMight's np.product,
        # irrelevant here) are both fixed, so no ceiling.
        depends_on("py-numpy@1.26.1:")
        depends_on("py-click@:8.1")
        depends_on("py-mdocfile")
        depends_on("py-rich")
        depends_on("py-einops")
        depends_on("py-lil-aretomo", when="+aretomo")
        # Default tilt-series alignment backend (IMOD fiducials/patch tracking); AreTomo is opt-in.
        depends_on("py-yet-another-imod-wrapper")
        depends_on("py-makefun")
        depends_on("py-lru-dict")
        # scripts/filament_selection.in does `import dill as pickle` directly.
        depends_on("py-dill")
        # pint's numpy-quantity glue code calls np.cumproduct at import time, removed in numpy
        # 2.0 (renamed to cumprod) - breaks napari's own import (napari imports pint) and
        # cascades into every relion_python_tomo_* wrapper that touches napari. Fixed in
        # pint 0.24.
        depends_on("py-pint@0.24:")
        # get_particle_poses/spheres.py imports morphosamplers directly.
        depends_on("py-morphosamplers")
        depends_on("topaz-3dem", type="run")
        depends_on("model-angelo", type="run")
        # Named alongside Blush and ModelAngelo as one of relion's three Python modules in
        # relion's own README (invoked via relion_python_dynamight).
        depends_on("dynamight", type="run")
        depends_on("py-relion-blush", type="run")
        depends_on("py-relion-classranker", type="run")

        for arch in CudaPackage.cuda_arch_values:
            depends_on(
                f"tsne-cuda@3.0.1 +cuda cuda_arch={arch} +python",
                when=f"@5.0 +cuda cuda_arch={arch}",
            )
            # torch 2.7.1+ is needed for Blackwell GPU kernel support. No ceiling: verified up
            # to 2.13.0, no specific break known beyond it.
            depends_on(
                f"py-torch@2.7.1: +cuda cuda_arch={arch}",
                when=f"@5.0 +cuda cuda_arch={arch}",
            )

        depends_on("py-torch@2.7.1: ~cuda", when="@5.0 ~cuda")

    # Set version so setuptools won't complain about not being able to determine it
    def setup_build_environment(self, env):
        env.set("SETUPTOOLS_SCM_PRETEND_VERSION", str(self.spec.version))
