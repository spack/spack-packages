# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaNvimagecodec(PythonPackage):
    """A nvImageCodec library of GPU- and CPU- accelerated codecs featuring a unified interface."""

    homepage = "https://docs.nvidia.com/cuda/nvimagecodec/index.html"
    git = "https://github.com/NVIDIA/nvImageCodec.git"

    skip_version_audit = ["platform=darwin", "platform=windows"]

    maintainers("thomas-bouvier")

    system = platform.system().lower()
    arch = platform.machine()
    if "linux" in system and arch == "x86_64":
        version(
            "0.7.0.11-cuda130",
            sha256="6075220b7ece40b5d975969f423e4ff9bc6d02bae4ac64ff8c8bf67d1234b12e",
            url="https://files.pythonhosted.org/packages/0d/ab/e23d570d282394188882526f65a8719bc03e10ce11bc398ea6d81ed5d480/nvidia_nvimgcodec_cu13-0.7.0.11-py3-none-manylinux_2_28_x86_64.whl",
        )
        version(
            "0.7.0.11-cuda120",
            sha256="32d3457859c5784e4c0f6a2f56b6a9afec8fe646cec1cbe4bb5c320948d92dfe",
            url="https://files.pythonhosted.org/packages/73/b4/f06528ebcb82da84f4a96efe7a210c277767cb86ad2f61f8b1a17d17f251/nvidia_nvimgcodec_cu12-0.7.0.11-py3-none-manylinux_2_28_x86_64.whl",
        )
        version(
            "0.6.1.37-cuda120",
            sha256="3b72bc65cfd113ef8a599082ca7f80ef53df0577f13e8489d065ba31d2df78f7",
            url="https://files.pythonhosted.org/packages/13/f4/36906056947347350a4b7441f7431355ff3fbc747c4ae3f9ec9d8e18cffc/nvidia_nvimgcodec_cu12-0.6.1.37-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.6.1.37-cuda110",
            sha256="8d104649aaa7aec4115afd5bea052613b26b6607436dace480bd6823f2f3bd04",
            url="https://files.pythonhosted.org/packages/91/1b/a7a2d2317abf9d04a5e2f2152ae4924e945bcd6235a2d72ae0d5f925e7c7/nvidia_nvimgcodec_cu11-0.6.1.37-py3-none-manylinux2014_x86_64.whl",
        )
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
        version(
            "0.4.1.21-cuda120",
            sha256="3a4c64ea5cf832e908da8a2ff70e77115bcfa2f9b046dbaf5188319a91451220",
            url="https://files.pythonhosted.org/packages/c0/c5/5b5fbd654aca6fc393766df0f15b7e078c982248a6b6fe5a35170ac898f0/nvidia_nvimgcodec_cu12-0.4.1.21-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.4.1.21-cuda110",
            sha256="7c6ad5d717dd80d274caa3773c698adbe2f053a10dbe819d15494ce72f2fbdb7",
            url="https://files.pythonhosted.org/packages/31/f7/1982f473a4ace1015d711a106acfa710ec218cdcb79d6dd9de9778e6f052/nvidia_nvimgcodec_cu11-0.4.1.21-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.4.0.9-cuda120",
            sha256="254b594effa60c94e79bdcb379276fd66b1b56085a0c661902b211a263c50295",
            url="https://files.pythonhosted.org/packages/38/31/3425e3daaabd2deea9754a533876a8c8c957244e3ab574287bd9d6a3744c/nvidia_nvimgcodec_cu12-0.4.0.9-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.4.0.9-cuda110",
            sha256="ea68bd59deebd792b9f0590e53b7f1d4b20e4212c5efee13455c1eade0bd0602",
            url="https://files.pythonhosted.org/packages/ac/7e/23f99745a626a0ba57ab1563e554e170081a3fcf24858cdc1f113fb2a9cd/nvidia_nvimgcodec_cu11-0.4.0.9-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.3.0.5-cuda120",
            sha256="b038b17223bb09b70c846244e7a54ad4147da29f169ea5a95a3b9108e9e33b89",
            url="https://files.pythonhosted.org/packages/67/6d/749eb173622a0f269c967abc0f946970899e90970427b1b8446e8b7ba8d1/nvidia_nvimgcodec_cu12-0.3.0.5-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.3.0.5-cuda110",
            sha256="f32bcaeff6f543234ddda85390928c6eb7944abe7f6c03ea97eccdf170f46b67",
            url="https://files.pythonhosted.org/packages/80/ba/12747756ff654f7c248cfc0bdb21dab385a2ef8dfd620803a73a1c9c59ce/nvidia_nvimgcodec_cu11-0.3.0.5-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.2.0.7-cuda120",
            sha256="4f3987f12291f6da47988e7c98664056ed5b4a9e3068ebe0d03a3646405e2437",
            url="https://files.pythonhosted.org/packages/74/27/614bcb521603e4ff39086a20bc9972cd861286375b9dc067307f21800789/nvidia_nvimgcodec_cu12-0.2.0.7-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.2.0.7-cuda110",
            sha256="c77c7bd7ca3033dc7a84f1657312b4f2d2046ac7c82b7dc9c229b9f2bcf10aea",
            url="https://files.pythonhosted.org/packages/1d/cd/a8f5f21b07bc76eb7fdc1a0dbb644e8f8289ca44ec402ade2cdcc4716f12/nvidia_nvimgcodec_cu11-0.2.0.7-py3-none-manylinux2014_x86_64.whl",
        )
    elif "linux" in system and arch == "aarch64":
        version(
            "0.7.0.11-cuda130",
            sha256="65ee61c93aaed80e21dc5db428bc7641fca6dcc319c166835a961359f7703736",
            url="https://files.pythonhosted.org/packages/55/04/09d25e7af95cfd2a946326ad9276623c1ef6a0063dd85e03296074539ee2/nvidia_nvimgcodec_cu13-0.7.0.11-py3-none-manylinux_2_28_aarch64.whl",
        )
        version(
            "0.7.0.11-cuda120",
            sha256="52d834be8122bb5b8fc3151cc3bedb95368b3e7ac76af0c4561772ab2a847b2b",
            url="https://files.pythonhosted.org/packages/63/48/74d33dd126f84a4212480e2cf07504f457b5bae5acd33c0f6bf839ea17d4/nvidia_nvimgcodec_cu12-0.7.0.11-py3-none-manylinux_2_28_aarch64.whl",
        )
        version(
            "0.6.1.37-cuda120",
            sha256="20067a5006be254afb363b8dc25ac793d935b012b4fd230102f977cbbff31fb3",
            url="https://files.pythonhosted.org/packages/8e/61/f8439c719c7c97d7444ba4f2d9d386ebabab8566518e6a58228543a3421f/nvidia_nvimgcodec_cu12-0.6.1.37-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.6.1.37-cuda110",
            sha256="cb1753e4fae01b1ed95fb7196a8c450e1cc97079b58712a8c69f249831455a8a",
            url="https://files.pythonhosted.org/packages/16/40/aa091d0954bc031a0db4ffa20d9001d9d725ce77c94b4ca3e14222398945/nvidia_nvimgcodec_cu11-0.6.1.37-py3-none-manylinux2014_aarch64.whl",
        )
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
        version(
            "0.4.1.21-cuda120",
            sha256="9bc771f81407e3b02b258161d7d13281f4abf90d1407389edfd5699389dacb01",
            url="https://files.pythonhosted.org/packages/d3/63/8f3da84deda05c554681b64a4752b63494c1d90d6ad5f3ff4f52d0fd6a70/nvidia_nvimgcodec_cu12-0.4.1.21-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.4.1.21-cuda110",
            sha256="983a47a52801b085478549426f7758bd4ee866c47fc1acbe7636a43186c88ea5",
            url="https://files.pythonhosted.org/packages/f8/45/b20e8ca19c469d7f4e631b73ffc37e0ff33570ded2804a8914e851ebfddf/nvidia_nvimgcodec_cu11-0.4.1.21-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.4.0.9-cuda120",
            sha256="a3d853ea6b242929b3c18554527618bb2f03ba3a153090d0076b7b74c6de602c",
            url="https://files.pythonhosted.org/packages/6b/ab/72011d2e45d7e21dcaaa6988c971f8d8480887703f1c3ff0c4358820ee2c/nvidia_nvimgcodec_cu12-0.4.0.9-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.4.0.9-cuda110",
            sha256="133a8896e37e0c69940f2f19b0167c6346e0819d35518b02134aa074c30b2be7",
            url="https://files.pythonhosted.org/packages/6b/e9/8316f9d3b11a5c0a3e350bf8acd6a7625939787159113e3a6e30b742cad6/nvidia_nvimgcodec_cu11-0.4.0.9-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.3.0.5-cuda120",
            sha256="f8a4524913828ac07d80f9572c8e8b74d088698451ba5240ea1afb06bd29fe73",
            url="https://files.pythonhosted.org/packages/09/e0/71abde334ac4fb0506d2ad6064b08b077f42bece682bda8ae55d45f1386f/nvidia_nvimgcodec_cu12-0.3.0.5-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.3.0.5-cuda110",
            sha256="06936e531d5671644db7a7b88a244188ff19aba1194c822062936d464a542d89",
            url="https://files.pythonhosted.org/packages/2f/0c/9383260a99552f076dc344ec7b141c2cfb2afe47f19f5359a9c359d6a8bf/nvidia_nvimgcodec_cu11-0.3.0.5-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.2.0.7-cuda120",
            sha256="ec2a190598f49b328cae3015651d9cea351e5acf770231fc0027ec459dfd3e79",
            url="https://files.pythonhosted.org/packages/a2/17/adc558478077fdc372db916311a6b94b819f4b23877abeb73eff23d342c9/nvidia_nvimgcodec_cu12-0.2.0.7-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.2.0.7-cuda110",
            sha256="909f96878561f6cfe0099f6cc26c57f3295de2ebfd0334022e0b29aab75e250b",
            url="https://files.pythonhosted.org/packages/c8/9f/1cdcefbc5f916440b4ed92a7141914cc45da154ffa9c9ae9c5fa0e6359f2/nvidia_nvimgcodec_cu11-0.2.0.7-py3-none-manylinux2014_aarch64.whl",
        )

    variant("nvjpeg2k", default=True, description="Enable NVJPEG2K support")
    variant("nvtiff", default=True, description="Enable NVTIFF support")

    cuda130_versions = ("@0.7.0.11-cuda130",)
    cuda120_versions = (
        "@0.7.0.11-cuda120",
        "@0.6.1.37-cuda120",
        "@0.5.0.13-cuda120",
        "@0.4.1.21-cuda120",
        "@0.4.0.9-cuda120",
        "@0.3.0.5-cuda120",
        "@0.2.0.7-cuda120",
    )
    cuda110_versions = (
        "@0.6.1.37-cuda110",
        "@0.5.0.13-cuda110",
        "@0.4.1.21-cuda110",
        "@0.4.0.9-cuda110",
        "@0.3.0.5-cuda110",
        "@0.2.0.7-cuda110",
    )

    for v in cuda130_versions:
        depends_on("cuda@13", when=v, type=("build", "run"))
    for v in cuda120_versions:
        depends_on("cuda@12", when=v, type=("build", "run"))
    for v in cuda110_versions:
        depends_on("cuda@11", when=v, type=("build", "run"))

    depends_on("python@3.8:", when="@0.5:", type=("build", "run"))

    depends_on("py-nvidia-nvjpeg2k", type=("build", "run"), when="+nvjpeg2k")
    depends_on("py-nvidia-nvtiff", type=("build", "run"), when="+nvtiff")
