# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaNvtiff(PythonPackage):
    """NVIDIA nvTIFF native runtime libraries"""

    homepage = "https://docs.nvidia.com/cuda/nvtiff/index.html"

    skip_version_audit = ["platform=darwin", "platform=windows"]

    maintainers("thomas-bouvier")

    system = platform.system().lower()
    arch = platform.machine()
    if "linux" in system and arch == "x86_64":
        version(
            "0.6.0.78-cuda130",
            sha256="b49d9cd2e33d389fa2aeb00bffb1c4a22e24b47de498ebfca367de9262181f5a",
            url="https://files.pythonhosted.org/packages/e8/7e/0e5f6e0cad026f0422db016d325aa9b9026d133507a3baacce31c6c22ad3/nvidia_nvtiff_cu13-0.6.0.78-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.6.0.78-cuda120",
            sha256="b48517578de6f1a6e806e00ef0da6d673036957560efbe9fa2934707d5d18c00",
            url="https://files.pythonhosted.org/packages/62/4b/24805e9c56936dd57a1830b65b53234853f429cea5edbcbfdf853ceebdcf/nvidia_nvtiff_cu12-0.6.0.78-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.5.0.67-cuda120",
            sha256="97787f710beea7a7990b48d1dde57318e82716bdea61407db6eaced8ac511dc6",
            url="https://files.pythonhosted.org/packages/81/67/c503df80ea3c2384bc8ed177164a1339ff49180835de01aa6597cfcad3a0/nvidia_nvtiff_cu12-0.5.0.67-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.5.0.67-cuda110",
            sha256="42881265c130cd62c031c154cfe108e5fb51c515b329dab627c60c46a4cbf764",
            url="https://files.pythonhosted.org/packages/2e/13/27a18d88ed9001a98c80d3ffb1f0eec7fb77e277b7468421dc37ddebed6f/nvidia_nvtiff_cu11-0.5.0.67-py3-none-manylinux2014_x86_64.whl",
        )
    elif "linux" in system and arch == "aarch64":
        version(
            "0.6.0.78-cuda130",
            sha256="d33120be5a31b09253d06cdfb63a3b4e60998b04e2b031049348715751e449e8",
            url="https://files.pythonhosted.org/packages/52/5a/b641ea5de0e6b6838b9b75ac00ca57e3d8a5b7ac2df8a4b890a2da7407c9/nvidia_nvtiff_cu13-0.6.0.78-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.6.0.78-cuda120",
            sha256="9193a46eaef2d52a92178c34e2404f621b581d651d2c7ab2d83c24fee6fcc136",
            url="https://files.pythonhosted.org/packages/41/19/9529fbda1e7a24b45649c9bc86cf6490d5b53f63e6b17d851f1528ff8380/nvidia_nvtiff_cu12-0.6.0.78-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.5.0.67-cuda120",
            sha256="cdaeff98d909d8ee885f1ab97da8cab06b7c1f1159f4da478f0afd21ac603155",
            url="https://files.pythonhosted.org/packages/e9/27/d5528e059ddc6a2ae5f7df0bb602d96d0593b0c585597d04c987a5240da9/nvidia_nvtiff_cu12-0.5.0.67-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.5.0.67-cuda110",
            sha256="d043962a7c24085a85e93285f314a8c90bdbefef9ed48b74f943c02b3ce3f47e",
            url="https://files.pythonhosted.org/packages/1a/b2/3b470a42ab20920f40a6138cc345379e412bfee0d58a989fb26bc6b15581/nvidia_nvtiff_cu11-0.5.0.67-py3-none-manylinux2014_aarch64.whl",
        )

    cuda130_versions = ("@0.6.0.78-cuda130",)
    cuda120_versions = ("@0.6.0.78-cuda120", "@0.5.0.67-cuda120")
    cuda110_versions = ("@0.5.0.67-cuda110",)

    for v in cuda130_versions:
        depends_on("cuda@13", when=v, type=("build", "run"))
    for v in cuda120_versions:
        depends_on("cuda@12", when=v, type=("build", "run"))
    for v in cuda110_versions:
        depends_on("cuda@11", when=v, type=("build", "run"))

    depends_on("python@3.8:", when="@0.5:", type=("build", "run"))
