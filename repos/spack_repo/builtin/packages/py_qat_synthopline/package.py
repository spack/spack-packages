# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatSynthopline(PythonPackage):
    """Module qat-synthopline [f641e66] - Compiled by Bull"""

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
            "0.6.0-cp310",
            sha256="39a6510e782d41e55ba5ce33a843453047246776997bf1415920842e8620abed",
        )
        version(
            "0.6.0-cp311",
            sha256="bdee0836836b652121ecd37dd5100e854856b883ff40bf1628047b45df48c22a",
        )
        version(
            "0.6.0-cp312",
            sha256="0d7d019b1ddb3a1aa295922941558a1a6ae2ac76ab11957d2fdf351c263ed917",
        )
        version(
            "0.6.0-cp313",
            sha256="7f5023e4d9a3a3c811e1b83882264462eb27415f3d6adcce48453ea4a62ae73d",
        )
        version(
            "0.6.0-cp314",
            sha256="6f0219dc425d50796aa9fa1a9d101b1d67ebea8ce25d69c7db4005a9a41a8821",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="b2c6174ef8ff5b7436cf212f37c58e9b2b2c6310807b1fed40bf1907b3992dc1",
        )
        version(
            "0.6.0-cp311",
            sha256="527aaac1c0300a3bf63a775b72ee9c57d97eddbaab72830ac81418bf666c8993",
        )
        version(
            "0.6.0-cp312",
            sha256="22971243fb1e65e34dd0502f2fdecc4c94bf74647c85b27daf73946ed3c31d56",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="f5843febf2c4af918633aab7e29e895b60a352e0a139a262bb696b96a0b6d81e",
        )
        version(
            "0.6.0-cp311",
            sha256="0964bb5fb3ec54ebe045cb502ecb82634eee0d7eff0066abfce64786a77a6469",
        )
        version(
            "0.6.0-cp312",
            sha256="77ae33ed82d4008da3d7f9eb4218a59e175fbf1606e07e7a366d80cde0ebfc44",
        )
        version(
            "0.6.0-cp313",
            sha256="9b114c64163a32af550ba28274ca48ddbb1b92ac57c0d167719d53411fc490e8",
        )
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="8b7a57e9db29bbac853e25f306f7924f8626fb9269c5a3b128178772f08cbf48",
        )
        version(
            "0.6.0-cp311",
            sha256="469c50f5f5785b34dadaea65f12af6f6207d374ddc1601c9bec9fea19b9adc98",
        )
        version(
            "0.6.0-cp312",
            sha256="f5816a45d96057ced01969915600fc6fb4f632204163278e11b91fe4e2f7bf01",
        )
        version(
            "0.6.0-cp313",
            sha256="b90a1a6db5fb9e14780d3654364b0ec8aea3331e5f65732c42c6976edcda96f4",
        )
        version(
            "0.6.0-cp314",
            sha256="a3ecab51964571f257519616dfa2b8d4d0671932e48e5b34c9b66c7f8b904eae",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="d9e59e0f9a28537b9f0bddfde5a5b33235f7b279987865dc803fa44fc9693d18",
        )
        version(
            "0.6.0-cp311",
            sha256="3ef2307a766d4cb9558ad4defe6773f8921509e391c852ae7edb8627455039ea",
        )
        version(
            "0.6.0-cp312",
            sha256="d6e5e4851a12a0b6c9927416985b113e67b27a43bc384c2a2fcb70ec7206faf3",
        )
        version(
            "0.6.0-cp313",
            sha256="667a45f564754c57ec129387c7edcad807b8908a268fa4a366f8865539181dd4",
        )
        version(
            "0.6.0-cp314",
            sha256="0fb226aa5a72ac13f28f91a92df818863f8cfcddb3f7e3eb36eab8746915d927",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="b415e195130c64c1d4fa2663a5493ad8956015f959ddf39fef04d20be92e4ef0",
        )
        version(
            "0.6.0-cp311",
            sha256="65fb7fbb6697c5c8eb4fa232a14a012c6e78df2615f3bac38f1c19a563be1913",
        )
        version(
            "0.6.0-cp312",
            sha256="4438c199afd89df9f5ad01a64a98ffe0bd90311e1f72b219a6721f482000d492",
        )
        version(
            "0.6.0-cp313",
            sha256="97f15d8e63fea940964b9bcc55f4a97c44a1d6c6f08d29a21164c76007e6110e",
        )
        version(
            "0.6.0-cp314",
            sha256="e22e6b6695db25b53b3f41085a4564d7fade974ffd1f964b434d87b05ca627e7",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@0.6.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@0.6.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@0.6.0-cp310")

    with default_args(type="run"):
        depends_on("py-networkx")
        depends_on("py-numpy")
        depends_on("py-stim")
        depends_on("py-rich")
        depends_on("py-qat-comm")
        depends_on("py-qat-core")
        depends_on("py-qat-devices")
        depends_on("py-qat-lang")
        depends_on("py-qat-nnize")
        depends_on("py-qat-pbo")

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
