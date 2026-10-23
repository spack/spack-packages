# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatVariational(PythonPackage):
    """Module qat-variational [d19d6f8] - Compiled by Bull"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    machine = platform.machine().lower()
    system = platform.system().lower()
    if system == "linux":
        libc = ctypes.CDLL("libc.so.6")
        libc.gnu_get_libc_version.restype = ctypes.c_char_p
        glibc_version = libc.gnu_get_libc_version().decode()
        if Version(glibc_version) >= Version("2.34"):
            glibc_version = "2_34"
        elif Version(glibc_version) >= Version("2.28"):
            glibc_version = "2_28"
        platform_tag = f"manylinux_{glibc_version}_{machine}"
    elif system == "darwin":
        platform_tag = "macosx_11_0_arm64"
    elif system == "windows":
        platform_tag = "win_amd64"

    if "macosx_11_0_arm64" == platform_tag:
        version(
            "1.8.0-cp310",
            sha256="480dc5baba6a4531ae874b6e453370f4463727f57589ad3b61fc90f5a57177d8",
        )
        version(
            "1.8.0-cp311",
            sha256="a2e6fdd627f18cc64e6f660927ad623a41ebb788ba6e2673ccc7184b939c705f",
        )
        version(
            "1.8.0-cp312",
            sha256="add1973af1cf769db337e27856d0b77c01c55654bb3e72b0227793c37ae01b92",
        )
        version(
            "1.8.0-cp313",
            sha256="b5bd55025c2cad7e274a7953a525ed2e28f95ee6030b0fbdb4b05352caeb4a7f",
        )
        version(
            "1.8.0-cp314",
            sha256="f4b80466364683aa4a81f75436b427ef3c3b6be86900f88d2f59923a707068e3",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.8.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.8.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.8.0-cp310",
            sha256="f54cc3c12a48911d3cd57eec59f4bc888a2ad1abf977691f38f14cf580dec0d6",
        )
        version(
            "1.8.0-cp311",
            sha256="cbd7d2bb4490dff93ba61299c5420512140b226d041326d36db6ce79d4161be1",
        )
        version(
            "1.8.0-cp312",
            sha256="b9bbb517acc3b6c94db3ca86977d88d403abcf8fe6851c1915c81ea9f1f71dfe",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.8.0-cp310",
            sha256="e88a15447c2e5b64b3f3252fb731b32d8602c13c3d185a31d16060918ea42da6",
        )
        version(
            "1.8.0-cp311",
            sha256="589816856805844c2f0a873d73a41bc2f4485b4fe336f39660f0a62a3bea7b6b",
        )
        version(
            "1.8.0-cp312",
            sha256="7036464fd20da46f2bb570b61bced3097fc3bf62c429974304db24b5d596052c",
        )
        version(
            "1.8.0-cp313",
            sha256="44413942c26ca18080a5743c7422fb3dfb395d0188aac20d56983c94a208fe45",
        )
        depends_on("python@3.13", type=("build", "run"), when="@1.8.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.8.0-cp310",
            sha256="45d408819ccaec72d32934d00f118604509bf6bbd695115e3cdac67e51a8b0b5",
        )
        version(
            "1.8.0-cp311",
            sha256="0c87abe61a1660a7df95351eceb4116fb3e2abe1fe4f798290f4fcdd8cbcdaa8",
        )
        version(
            "1.8.0-cp312",
            sha256="6a901435009fb9cbf990cc9fa15cb387a289a15899ac80a4b97e5ce1b61c7c64",
        )
        version(
            "1.8.0-cp313",
            sha256="355d917f1bf4f7549c114d9cc551177f9cadd26bb2d9d11fb75b819522f9b354",
        )
        version(
            "1.8.0-cp314",
            sha256="322d4e6b157100f004b1ea5b4b694b68dd38f50cedacf292206a51fafb83a5aa",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.8.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.8.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.8.0-cp310",
            sha256="1b186681e078d98b50e5a41abf6def665f849b534ab52a738f6a451fccfe37c5",
        )
        version(
            "1.8.0-cp311",
            sha256="b5a47797932a0fbcb241d3edd171e86375489df9780750d60d9d73252b58207c",
        )
        version(
            "1.8.0-cp312",
            sha256="68263f9681397ccb22cf24e59ba8a1a50685150d817426621f6528914c659c1d",
        )
        version(
            "1.8.0-cp313",
            sha256="3bb777da727370d694439f46d4982c5ee80cbb2040b0b636119ec2656dbad475",
        )
        version(
            "1.8.0-cp314",
            sha256="7b5d749e6d6130d7a34807159f6adfee7eb59421c69addffe082d7f82a4f7a9a",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.8.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.8.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "1.8.0-cp310",
            sha256="1244a5a0dcac9742dc1d67d6861265249677d75ff31453ec651e774de4afa22b",
        )
        version(
            "1.8.0-cp311",
            sha256="ed28891517053cf8b933fff808104e2245837d60dad583f81bd329b1e4a5924e",
        )
        version(
            "1.8.0-cp312",
            sha256="f3d5642da5b7d13f666265bdbaab7c16b3061c1810a2865f40ff401389aa9504",
        )
        version(
            "1.8.0-cp313",
            sha256="554f29442d3c2f4c79f6d00df9f40fd39c144c1cf8266208df26f66578537b9d",
        )
        version(
            "1.8.0-cp314",
            sha256="f15cd06b2975bfb5edd1a9e9e191b26a44e672f671be51d73ecec4969d9292cd",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.8.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.8.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@1.8.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.8.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.8.0-cp310")

    with default_args(type="run"):
        depends_on("py-numpy@2")
        depends_on("py-networkx")
        depends_on("py-scipy")
        depends_on("py-qat-comm")
        depends_on("py-qat-core")
        depends_on("py-qat-anapli")
        depends_on("py-qat-lang")

    def url_for_version(self, version):
        split_name = self.name.split("-")[1:]
        dash_name = "-".join(split_name)
        underscored_name = "_".join(split_name)
        first_letter = dash_name[0]
        url = "https://files.pythonhosted.org/packages/{1}/{3}/{4}/{5}-{0}-{1}-{1}-{2}.whl"
        pkg_ver = version.up_to_3
        cp_ver = version.string.split("-")[1]
        return url.format(
            pkg_ver, cp_ver, self.platform_tag, first_letter, dash_name, underscored_name
        )
