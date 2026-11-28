# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatNnize(PythonPackage):
    """Module qat-nnize [f018356] - Compiled by Bull"""

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
            "1.5.0-cp310",
            sha256="0c5b8474cbc668559d7deca0e8e4aaa5a967e41a412305742f5fc80975c0c354",
        )
        version(
            "1.5.0-cp311",
            sha256="a83a423ed9c2df8b5da268d32e84f9544b48969a9f0e3f3d5c107f5eb39578ed",
        )
        version(
            "1.5.0-cp312",
            sha256="af429cb6720642be58e647872b5e222d7b0636638631c74a367586dc64ad6834",
        )
        version(
            "1.5.0-cp313",
            sha256="a4ec690e2e0b2d65be21bbd20148a564e5b186581329e19907ba2b9172886177",
        )
        version(
            "1.5.0-cp314",
            sha256="7be2e25f069521b330974275d945ad4a1428f29ce940fc230f9261f5d2a7fb34",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.5.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.5.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.5.0-cp310",
            sha256="64ce35f94a1e51c25c6ddb78aa3e48b71b689e3353a569d33698c3d60beac421",
        )
        version(
            "1.5.0-cp311",
            sha256="00e88f4a653decef9a66c72555ab25e52d41ade57d00afeb974ccaefe4a09b71",
        )
        version(
            "1.5.0-cp312",
            sha256="ee4f9318042c6901766bd80a9553718cec4ec64202c7059b4b7fa5812fb24c8a",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.5.0-cp310",
            sha256="00892e02620801b8ab39cebf69bbc7f4853b06f7661aaf8b843b1f31f5db636e",
        )
        version(
            "1.5.0-cp311",
            sha256="886cb6c00ccc2683908eb84db779416adc4e4d8db869b200314f15ca6dfda358",
        )
        version(
            "1.5.0-cp312",
            sha256="ac5b5a2de011d034c659f5623a6bac7461950cc7c0ab2d3b7d396f64e41b7c12",
        )
        version(
            "1.5.0-cp313",
            sha256="2f13525558e23be217575d53af604ec5a10f9160b3e2e61e70f109af2877337a",
        )
        depends_on("python@3.13", type=("build", "run"), when="@1.5.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.5.0-cp310",
            sha256="2db6ecd8d0f3c397e84826a63b01e2d921d9ff14296482e0ef653ebe55cee8b2",
        )
        version(
            "1.5.0-cp311",
            sha256="d76afc7b0fccddffc4b00dbafaa298c50c608a3a32d1a2c9230d9ddbacd6cd37",
        )
        version(
            "1.5.0-cp312",
            sha256="1139d9568aa6303a3259d47df8d2ff86f6b5751716dfdbf6deade1f016943375",
        )
        version(
            "1.5.0-cp313",
            sha256="ee55126c79de54cffd143e0c2a72c559d73bc1671c8348dba9a0be27b4f2c56c",
        )
        version(
            "1.5.0-cp314",
            sha256="b6d3629175da74d84d377e23c7db8dfd8861f7282de08fe7794d4305ff75be91",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.5.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.5.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.5.0-cp310",
            sha256="5d2de4b4be7bae90cbe5814e34f43bffa3a38a30ca48af018d9b2335612d1f4c",
        )
        version(
            "1.5.0-cp311",
            sha256="383f803a18b91552eea75942df84d6bcba460557be49b85ef81126902f3ce01b",
        )
        version(
            "1.5.0-cp312",
            sha256="d799cbf62d98f33b7aa54bb46ac45fa32a7e8b00be8ca4d9d2b67bd69d25296c",
        )
        version(
            "1.5.0-cp313",
            sha256="39a3fce755eb69d2f4904a69fbe7c91f43b8c14c8329cb024f614fb68427d843",
        )
        version(
            "1.5.0-cp314",
            sha256="4fc7b07363f387b1c05603ff2489abb7fa7c4f88fafb738f26d991626402c74a",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.5.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.5.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "1.5.0-cp310",
            sha256="611509e60b4e1b4affaf72aacddb0f0d3af4b88474ac3a4516fc0992d207286d",
        )
        version(
            "1.5.0-cp311",
            sha256="23c7cdd6010250682801a36a782ac0b8f14233e3787eb25d9dfdaffb3aa4bfc5",
        )
        version(
            "1.5.0-cp312",
            sha256="77943e5c17a2936917c6ac76c1e04d02205281c0d0bf33a31c28e992cef17ee2",
        )
        version(
            "1.5.0-cp313",
            sha256="d87fd474965f320bb8b3584884c8000fc3ca37e29329dfa2785e6c0630b4ca73",
        )
        version(
            "1.5.0-cp314",
            sha256="c639715a2c50155be03c26c5c21d6a32f30acf8833823acaf8b7425df6adf9e9",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.5.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.5.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@1.5.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.5.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.5.0-cp310")

    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-qat-comm")
        depends_on("py-qat-core")
        depends_on("py-qat-lang")
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
