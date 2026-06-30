# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaPhysicsnemo(PythonPackage):
    """A deep learning framework for AI-driven multi-physics systems"""

    homepage = "https://github.com/NVIDIA/physicsnemo"
    pypi = "nvidia-physicsnemo/nvidia_physicsnemo-1.3.0-py3-none-any.whl"
    # Work-around URL until the CI version check can rely on the URL related to a PyPi wheel.
    # ref. https://github.com/spack/spack-packages/pull/2400/changes/a3e13de4f218e3fb6951e8b89dfa914be704313f
    url = "https://pypi.io/packages/py3/n/nvidia-physicsnemo/nvidia_physicsnemo-1.3.0-py3-none-any.whl"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("2.1.1", sha256="86479174f725dd8f569f76f7e688f64721afd2c16421e8516973f46f8febbefc")
    version("2.0.0", sha256="fcea6ac198a2925ab81c3f62011225f53b73e1212e5364aac939ab599c0dfd9d")
    version("1.3.0", sha256="404b5a17cdc00bcc8a2b003304695e4cbd8fff7fc7cca7f140988569c690f6b9")

    variant("sym", default=False, description="Provides extra module: sym")

    # Common dependencies (cf. METADATA)
    with default_args(type=("build", "run")):
        depends_on("python@3.11:3.13", when="@2:")
        depends_on("python@3.10:")
        depends_on("py-einops@0.8.1:", when="@2:")
        depends_on("py-einops@0.8.0:")
        depends_on("py-numpy@1.22.4:")
        depends_on("py-onnx@1.14.0:")
        depends_on("py-packaging@24.2:")
        depends_on("py-requests@2.32.2:")
        depends_on("py-s3fs@2023.5.0:")
        depends_on("py-timm@1.0.22:", when="@2:")
        depends_on("py-timm@1.0.0:")
        depends_on("py-torch@2.10.0:", when="@2.1:")
        depends_on("py-torch@2.4.0:")
        depends_on("py-tqdm@4.60.0:")
        depends_on("py-treelib@1.2.5:")

    # Dependencies exclusive to version 2.x.x (cf. METADATA)
    with default_args(type=("build", "run"), when="@2:"):
        depends_on("py-cftime@1.6.5:")
        depends_on("py-gitpython@3.1.49:", when="@2.1:")
        depends_on("py-gitpython@3.1.40:")
        depends_on("py-h5py@3.15.1:")
        depends_on("py-hydra-core@1.3.2:")
        depends_on("py-importlib-metadata@8.7.1:")
        depends_on("py-jaxtyping@0.3.3:")
        depends_on("py-nvtx@0.2.10:")
        depends_on("py-omegaconf@2.3.0:")
        depends_on("py-pandas@2.2.0:")
        depends_on("py-tensordict@0.11", when="@2.1:")
        depends_on("py-tensordict@0.10.0:")
        depends_on("py-termcolor@3.2.0:")
        depends_on("py-torchvision@0.25.0:", when="@2.1:")
        depends_on("py-torchvision@0.19.0:")
        depends_on("py-urllib3@2.7.0:", when="@2.1:")
        depends_on("py-warp-lang@1.13.0:", when="@2.1:")
        depends_on("py-warp-lang@1.5.0:")
        depends_on("py-sympy@1.12:", when="@2.1:+sym")

    # Dependencies exclusive to version 1.3.0 (cf. METADATA)
    depends_on("py-setuptools@77.0.3:", type=("build"), when="@1.3.0")
    with default_args(type=("build", "run"), when="@1.3.0"):
        depends_on("py-certifi@2023.7.22:")
        depends_on("py-fsspec@2023.1.0:")
        depends_on("py-xarray@2023.1.0:")
        depends_on("py-zarr@2.14.2:")
