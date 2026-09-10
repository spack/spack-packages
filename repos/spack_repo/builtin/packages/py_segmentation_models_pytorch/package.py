# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySegmentationModelsPytorch(PythonPackage):
    """Python library with Neural Networks for Image Segmentation based on PyTorch."""

    homepage = "https://github.com/qubvel/segmentation_models.pytorch"
    pypi = "segmentation_models_pytorch/segmentation_models_pytorch-0.2.0.tar.gz"

    license("MIT")
    maintainers("adamjstewart")

    version("0.5.0", sha256="cabba8aced6ef7bdcd6288dd9e1dc2840848aa819d539c455bd07aeceb2fdf96")
    version("0.4.0", sha256="8833e63f0846090667be6fce05a2bbebbd1537776d3dea72916aa3db9e22e55b")

    with default_args(type="build"):
        depends_on("py-setuptools@61:")

    with default_args(type=("build", "run")):
        depends_on("py-huggingface-hub@0.24:")
        depends_on("py-numpy@1.19.3:")
        depends_on("pil@8:")
        depends_on("py-safetensors@0.3.1:", when="@0.5:")
        depends_on("py-timm@0.9:")
        depends_on("py-torch@1.8:")
        depends_on("py-torchvision@0.9:")
        depends_on("py-tqdm@4.42.1:")

        # Historical dependencies
        depends_on("py-efficientnet-pytorch@0.6.1:", when="@0.4")
        depends_on("py-pretrainedmodels@0.7.1:", when="@0.4")
        depends_on("py-six@1.5:", when="@0.4")
