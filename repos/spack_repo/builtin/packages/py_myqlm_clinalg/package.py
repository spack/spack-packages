# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMyqlmClinalg(PythonPackage):
    """Module myqlm-clinalg [d15d507] - Compiled by Bull"""

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
            "0.5.1-cp310",
            sha256="74dc8ae1dfe1be8b1cbb55defd451e72f89cdf582414d86bb2c4eeb28dc68546",
        )
        version(
            "0.5.1-cp311",
            sha256="d2eb1e9b22211d97368b8007ae1852aa119594be161616b994cc20d0950835fd",
        )
        version(
            "0.5.1-cp312",
            sha256="1032b3932db8b578b20de9d3a49f197f0783cf53326032e1abc178064aa9af49",
        )
        version(
            "0.5.1-cp313",
            sha256="ffa66d26fd939c6db1f164725b0e5bada708e699b5ff3cfc2dd67a0c10c2e3d7",
        )
        version(
            "0.5.1-cp314",
            sha256="f6bbdc1ef25f96d3676e10b115e146fdb9b85c61539135d5bc5dec8752c95407",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.5.1-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.5.1-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "0.5.1-cp310",
            sha256="59f05071e511f585705898ee4da2b464dac6e6f8680216e42b045e73fd433cfd",
        )
        version(
            "0.5.1-cp311",
            sha256="5dc1b15a429dcfa2e4063c4df2aceb45ddcd0fa09159b63ed24a74ca601852b6",
        )
        version(
            "0.5.1-cp312",
            sha256="adc12ee248578a74bd145e33a24b57e67b5aaa4fbb2933af054386fe3aad7fe4",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "0.5.1-cp310",
            sha256="06e8db2258082f7ff7edf7b322298257e1ebbba6f2b1ed838f6e42771504fe3c",
        )
        version(
            "0.5.1-cp311",
            sha256="3fc4ef23020ca2c97f0566e6ffbbcef3cc6edeec67c76aad4a77178a6c8f9ba4",
        )
        version(
            "0.5.1-cp312",
            sha256="dbd49c27b2af70266b58204c029bfe8eea9e87c359047354c96b8bce7e027f11",
        )
        version(
            "0.5.1-cp313",
            sha256="b8837adaa0a572a3e5d40c0d1c3682345ac1ec435c93082781d8e6bdef67dd7c",
        )
        depends_on("python@3.13", type=("build", "run"), when="@0.5.1-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "0.5.1-cp310",
            sha256="a28bdcc7067af7fe30f46135018fc033c89013e779c005a74049afb109ea0b6e",
        )
        version(
            "0.5.1-cp311",
            sha256="3ba7df5c3716bc5627a6acb92ad6a0253b26419ca1ecf34898b0687c8a96f6a1",
        )
        version(
            "0.5.1-cp312",
            sha256="9c463ca91a8940e6b316da1853035720ab0cba40a94b6ed10c44fe5829cf4c6e",
        )
        version(
            "0.5.1-cp313",
            sha256="88ff56c717ac0602a88eaaa8ec9eae1e11724a257d62bb11f6ef673cf0e2fe5b",
        )
        version(
            "0.5.1-cp314",
            sha256="7ee0ac8060678e25e59e64494146d7b5ff104851c23665a29b485c5ec7e9af76",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.5.1-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.5.1-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "0.5.1-cp310",
            sha256="54c52edf2ba86eee024cd5ca25f3e355a6e7ed72c2db5e32a23574dbf2a94889",
        )
        version(
            "0.5.1-cp311",
            sha256="4cedb79ec712c69873fe3bc527533dc82bd6f9027f39617d31da9f561487e691",
        )
        version(
            "0.5.1-cp312",
            sha256="56cf11cfc37260c243012d9f1f24a4f2ebca8ffae3a669a6b4dfd9c33d5f7413",
        )
        version(
            "0.5.1-cp313",
            sha256="fad9748dcf61a1c1fc36f5d1873e41ed94d086a7e1b59e02b0d4520c8751414c",
        )
        version(
            "0.5.1-cp314",
            sha256="4b43d4f826e4c1593de38b5672c7e241fca58be3e958fcf4ae039d577437f45c",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.5.1-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.5.1-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "0.5.1-cp310",
            sha256="927eacdd2f0c95e9c10fb55c62b738d35c7941f2410d29c3a3d313f524c6ce1d",
        )
        version(
            "0.5.1-cp311",
            sha256="e37b5c8ef4dd2d4b8188e400901d4e24ba6fd184db17bb47bcbc72527d3045f4",
        )
        version(
            "0.5.1-cp312",
            sha256="abade132d32279625af24d8d154ecbad41d76492c2b89608aaed582f3b1d6739",
        )
        version(
            "0.5.1-cp313",
            sha256="aa7f1d1371a342148eafee78e9bda5d89721409ed4d09316e8a6f80ce04c7e70",
        )
        version(
            "0.5.1-cp314",
            sha256="926a546a25c040fa1d18c3423b79edc6582dd4b019d976848ba430bcdbd35613",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.5.1-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.5.1-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@0.5.1-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@0.5.1-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@0.5.1-cp310")

    with default_args(type="run"):
        depends_on("py-qat-comm")
        depends_on("py-qat-core")
        depends_on("py-qat-lang")
        depends_on("py-qat-linalg-util")
        depends_on("py-qat-fusion")

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
