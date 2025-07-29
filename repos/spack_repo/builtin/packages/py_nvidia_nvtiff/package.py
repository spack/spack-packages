# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

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
            "0.5.0.67-cuda120",
            sha256="cdaeff98d909d8ee885f1ab97da8cab06b7c1f1159f4da478f0afd21ac603155",
            url="https://files.pythonhosted.org/packages/e9/27/d5528e059ddc6a2ae5f7df0bb602d96d0593b0c585597d04c987a5240da9/nvidia_nvtiff_cu12-0.5.0.67-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.5.0.67-cuda110",
            sha256="d043962a7c24085a85e93285f314a8c90bdbefef9ed48b74f943c02b3ce3f47e",
            url="https://files.pythonhosted.org/packages/1a/b2/3b470a42ab20920f40a6138cc345379e412bfee0d58a989fb26bc6b15581/nvidia_nvtiff_cu11-0.5.0.67-py3-none-manylinux2014_aarch64.whl",
        )

    cuda120_versions = (
        "@0.5.0.67-cuda120",
    )
    cuda110_versions = (
        "@0.5.0.67-cuda110",
    )

    for v in cuda120_versions:
        depends_on("cuda@12", when=v, type=("build", "run"))
    for v in cuda110_versions:
        depends_on("cuda@11", when=v, type=("build", "run"))

    depends_on("python@3.8:", when="@0.5:", type=("build", "run"))
