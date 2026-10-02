# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatFusion(PythonPackage):
    """Module qat-fusion [721086e] - Compiled by Bull"""

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
            "0.4.0-cp310",
            sha256="b92640c0c8f68187117c8c9e3f7c4892450961c05a31435872af4180e8c39b35",
        )
        version(
            "0.4.0-cp311",
            sha256="68eeb7a4465f9a5121aa24108c1ca4eac17d16a3a431cdbe3c335d13b5191aab",
        )
        version(
            "0.4.0-cp312",
            sha256="52a674cc376baddb71d37da4b280a5416d9dd693aca99b200c844da7f1a732fd",
        )
        version(
            "0.4.0-cp313",
            sha256="afd8b43167d4917ad3b860db8aa0f85ad4bab5049e6b48b16b154f5f4af5ecb7",
        )
        version(
            "0.4.0-cp314",
            sha256="ec9ae33af49c7e3642ee894a994379967c55966c3be3f036c3cc0a2abf6e6f3d",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.4.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.4.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "0.4.0-cp310",
            sha256="6c380dea78dd3733961be9a7c5f65ca97966d55197977e4d1088cd19789dccd3",
        )
        version(
            "0.4.0-cp311",
            sha256="863695ce8bd8c2fd4992ac4fa4c15220a3a61e33b4bcecf8faadd1178b5cb84c",
        )
        version(
            "0.4.0-cp312",
            sha256="4c2cc1619e7694aac7c98ff3edde135592e60ba8ec774d37e4f2634f50bd9d13",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "0.4.0-cp310",
            sha256="782a20acb4cdaf786ab24ab13b6e55e1d4d35efedfd4cf133c4e99b7a7380a0e",
        )
        version(
            "0.4.0-cp311",
            sha256="a168a8d46acb1bc6f6eb1111eeae7fa84da5b7db84bb49bf9b11eb03e5df37f0",
        )
        version(
            "0.4.0-cp312",
            sha256="93dd133331321a1ad2c6ed55b031606ece0baf0f3c7d5535b2f71459ef3b8352",
        )
        version(
            "0.4.0-cp313",
            sha256="c1d85b6cf96d7a465bd51263ab5bd816ceed5fc4c44798094171aebee21663a5",
        )
        depends_on("python@3.13", type=("build", "run"), when="@0.4.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "0.4.0-cp310",
            sha256="adb4f772b6e41b745fb1671a3d89f9518e8edf415fcb7407efaf6f4d32e135cd",
        )
        version(
            "0.4.0-cp311",
            sha256="1d318e701a8c8205b7162629a5ed0c98951f9977e342e1d378ff7bcb5fe0d61e",
        )
        version(
            "0.4.0-cp312",
            sha256="b896e732b90144cdd85b2a767d60d3980cd6e457e6b4bbb558c6b14e74218fff",
        )
        version(
            "0.4.0-cp313",
            sha256="24a4965ac1e0d0cfe6c5fedefc8b2769aa472b24269bd5ca19a56779c6ded175",
        )
        version(
            "0.4.0-cp314",
            sha256="8450bc032fb107b70c83f2dd4e0734b0489cd0290c5aae645aa2649974e280aa",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.4.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.4.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "0.4.0-cp310",
            sha256="ade0b8f40923735187bce60aca1b68da4e2dfa820b0a619707f5077ad2c8fcc0",
        )
        version(
            "0.4.0-cp311",
            sha256="00036e9ab687946c255e2d1276e4b583b6a38b00adb22c44a095f6618e1645f3",
        )
        version(
            "0.4.0-cp312",
            sha256="a50368b79f12270436ea84d239dff313bb019ba94fd8e4c7a39132519b66421c",
        )
        version(
            "0.4.0-cp313",
            sha256="5a43d00f832ae3fa84a610ee525cacefd9df0bbc0c65f77641d0920fae6c9630",
        )
        version(
            "0.4.0-cp314",
            sha256="036c22cb294075d96b5d412494271c2fa54c4cbfa3df7a6c199e64bc78eaed1f",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.4.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.4.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "0.4.0-cp310",
            sha256="fe0ec9fd61435e47283d8b2df31907822168561e68cfb551a4a26654af2cad3c",
        )
        version(
            "0.4.0-cp311",
            sha256="4b46bb68210038b8713cdff6eb0d932df969a6fa2a4e5af22ee6d3beded0f927",
        )
        version(
            "0.4.0-cp312",
            sha256="b73e44f81c83a0c0536ce6bb98b591ee3886551c9d79ab6933c1e3e0003ee708",
        )
        version(
            "0.4.0-cp313",
            sha256="0849c362f366c2eeae7a30b7dbd163c7cca1a02941f0155026a19892b4b29a37",
        )
        version(
            "0.4.0-cp314",
            sha256="85c5c573a6ec5b24bf3678ede0a6cc4351ed109a4a202b2cf3547c4f326ec563",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.4.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.4.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@0.4.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@0.4.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@0.4.0-cp310")

    with default_args(type="run"):
        depends_on("py-numpy@2")
        depends_on("py-matplotlib")
        depends_on("py-networkx")
        depends_on("py-qat-comm")
        depends_on("py-qat-core")

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
