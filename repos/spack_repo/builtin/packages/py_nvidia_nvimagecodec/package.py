# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaNvimagecodec(PythonPackage):
    """A nvImageCodec library of GPU- and CPU- accelerated codecs featuring a unified interface"""

    homepage = "https://docs.nvidia.com/cuda/nvimagecodec/index.html"
    git = "https://github.com/NVIDIA/nvImageCodec.git"

    skip_version_audit = ["platform=darwin", "platform=windows"]

    maintainers("thomas-bouvier")

    system = platform.system().lower()
    arch = platform.machine()
    if "linux" in system and arch == "x86_64":
        version(
            "0.5.0.13-cuda120",
            sha256="24cf0a759b1b02a6c3c0aedf8bf6602643f74c4c6df68c4b1c3c4ec1d48d71b0",
            url="https://files.pythonhosted.org/packages/f0/6d/1c9919912ee97a4f52674f1c2deec7ab80df8fdd9a8b76f8ed4d75ebf799/nvidia_nvimgcodec_cu12-0.5.0.13-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.5.0.13-cuda110",
            sha256="d82ccf33921a35d965e975bfcf7f64472c804cb0f734a8fe692d9dca7e1e8643",
            url="https://files.pythonhosted.org/packages/60/69/d26efdefee269e87c034b229d94bf878ec033fca1b7cd4644395e706cf38/nvidia_nvimgcodec_cu11-0.5.0.13-py3-none-manylinux2014_x86_64.whl",
        )
    elif "linux" in system and arch == "aarch64":
        version(
            "0.5.0.13-cuda120",
            sha256="d76fadc2ed0f9075871627e45f2592c7807a0e944a0505afc21f87ccceb75caa",
            url="https://files.pythonhosted.org/packages/28/9a/f6c9105cb045f52af2096417ce92e7e8fba4d24ffe24d2cc82eb9bbe5534/nvidia_nvimgcodec_cu12-0.5.0.13-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.5.0.13-cuda110",
            sha256="0cb46e2032e2ae91afd48ba65b4a990c786927969110119a611859f6022bc417",
            url="https://files.pythonhosted.org/packages/58/84/2ed139ffa8961549acf168a554187b3cda9820076d687ede9ed95cd458be/nvidia_nvimgcodec_cu11-0.5.0.13-py3-none-manylinux2014_aarch64.whl",
        )

    variant("nvjpeg2k", default=True, description="Enable NVJPEG2K support")
    variant("nvtiff", default=True, description="Enable NVTIFF support")

    cuda120_versions = (
        "@0.5.0.13-cuda120",
    )
    cuda110_versions = (
        "@0.5.0.13-cuda110",
    )

    for v in cuda120_versions:
        depends_on("cuda@12", when=v, type=("build", "run"))
    for v in cuda110_versions:
        depends_on("cuda@11", when=v, type=("build", "run"))

    depends_on("python@3.8:", when="@0.5:", type=("build", "run"))

    depends_on("py-nvidia-nvjpeg2k", type=("build", "run"), when="+nvjpeg2k")
    depends_on("py-nvidia-nvtiff", type=("build", "run"), when="+nvtiff")
