# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaNvjpeg2k(PythonPackage):
    """NVIDIA nvJPEG2000 native runtime libraries"""

    homepage = "https://docs.nvidia.com/cuda/nvjpeg2000/index.html"

    skip_version_audit = ["platform=darwin", "platform=windows"]

    maintainers("thomas-bouvier")

    system = platform.system().lower()
    arch = platform.machine()
    if "linux" in system and arch == "x86_64":
        version(
            "0.8.1.40-cuda120",
            sha256="326518da11c4b037a0ae2189ec2f7d317c8bd5ddd616413e45da0faa31bd3399",
            url="https://files.pythonhosted.org/packages/fe/3c/7d6ba35508f5cbf6d25149076355188c8ea8303768b9a8272150a38c8063/nvidia_nvjpeg2k_cu12-0.8.1.40-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.8.1.40-cuda110",
            sha256="47b5f2f3217b5bf9935d013152df6e0412d11741bfee81419bdb4ad52d68aeb7",
            url="https://files.pythonhosted.org/packages/9d/15/88dbe4f0ca93a8e5d381a993f384e7eb929d51476fcc905b848b14a2bcd7/nvidia_nvjpeg2k_cu11-0.8.1.40-py3-none-manylinux2014_x86_64.whl",
        )
    elif "linux" in system and arch == "aarch64":
        version(
            "0.8.1.40-cuda120",
            sha256="63dd81d37b0826ad9d1086957815836a9dce45b3cbdb502b5c3566fba8cb4141",
            url="https://files.pythonhosted.org/packages/8c/5a/8618385bb6e1d5f95f59de3a7fe22ed9b3a2c439c541589b7001345ac0aa/nvidia_nvjpeg2k_cu12-0.8.1.40-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.8.1.40-cuda110",
            sha256="5bc4a20f9b00097cfcbbf6d4905668717db5d381425144b06b9fce957b3a793e",
            url="https://files.pythonhosted.org/packages/4f/85/1daca97fbef54307691dde4bbd94b654a0535d3cdff1cb4a75adecc3f2be/nvidia_nvjpeg2k_cu11-0.8.1.40-py3-none-manylinux2014_aarch64.whl",
        )

    cuda120_versions = ("@0.8.1.40-cuda120",)
    cuda110_versions = ("@0.8.1.40-cuda110",)

    for v in cuda120_versions:
        depends_on("cuda@12", when=v, type=("build", "run"))
    for v in cuda110_versions:
        depends_on("cuda@11", when=v, type=("build", "run"))

    depends_on("python@3.8:", when="@0.8:", type=("build", "run"))
