# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatDevices(PythonPackage):
    """Module qat-devices [667eff3] - Compiled by Bull"""

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
            sha256="abead2dd54244e13dc993de7291f2721a8537c248d0e42e0f20b2f1ae161ca97",
        )
        version(
            "0.6.0-cp311",
            sha256="8c034700d0e4dac38efb9bbebb1d752dc920050f12426f669177f9445595b66b",
        )
        version(
            "0.6.0-cp312",
            sha256="385b20ac5a5c5e78e8ee958ccf2cb6ea349c99d3a2a94b9b32527c8305edee71",
        )
        version(
            "0.6.0-cp313",
            sha256="ae59fd75194ebe0ed14c2388ae0926339fdbd36eeb6fa0ee945d19503dc95a32",
        )
        version(
            "0.6.0-cp314",
            sha256="c17337e03876a4a05e56f52aea09e07e022a86b6354e4fe60339fd34f5795c58",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="b21324d2732cd0706ba90f5efd988a115953e6d85b9588506be0b1718b55cb50",
        )
        version(
            "0.6.0-cp311",
            sha256="935d1517284ec75d5d37a948a821eb2c9179f37113a82ac5c6133b182b195a0a",
        )
        version(
            "0.6.0-cp312",
            sha256="d69f33815d08c07fdb7740111145a70f38896ceaa82c334a7b5a78f5685ac8cc",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="50067c675e2859c42f1915837c227aed1926b2202ae226acf7377024544e85b1",
        )
        version(
            "0.6.0-cp311",
            sha256="e3a6fb72935f4a27b043db08c9f1598a9cbf3a76dc6e9f012a2babc483a5d4c7",
        )
        version(
            "0.6.0-cp312",
            sha256="085133d0d99919b04d8e3b5edfa21600c755676c41d7966e86f97635014dfcc3",
        )
        version(
            "0.6.0-cp313",
            sha256="8589ba2e6fc85ce0f5ebb524bcfd1fff9dd633f60b3b5c1ecccc42ca6ce2c9b1",
        )
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="d5b628017940789e0bf7323ce14a84c7468046d47ddf17fbe01c2b0dc887c89b",
        )
        version(
            "0.6.0-cp311",
            sha256="1368ebb4be8affee54eccde2001af346b12155b06fe786dd4ef4ef20c1bb500b",
        )
        version(
            "0.6.0-cp312",
            sha256="dfaadca28f6119061f6ae7269e7e976a1b6bc405cbe7caf987771b5ad885d490",
        )
        version(
            "0.6.0-cp313",
            sha256="0c7da71cde121b6b7b1353b1c34ba1b8e824df51ede5fbd41cb0585c1d90d889",
        )
        version(
            "0.6.0-cp314",
            sha256="68d9c0aa43c5b942ae1982a97a1ce6e94d843ec16e4efc3dfb9a91616f21448c",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="de598de794d496813a83c7413507ed4444df09155dd551ff421d08c537177e0a",
        )
        version(
            "0.6.0-cp311",
            sha256="ba2f7a8405728dbc3d715053a3765547de78afef122cc6720e3da287bb9fefd3",
        )
        version(
            "0.6.0-cp312",
            sha256="83fa5143f33e0e6106d213bce0384aa4ad1e891e4c4caa8989f2d5200a8f01a2",
        )
        version(
            "0.6.0-cp313",
            sha256="effb812e8d8f8233a48af12284ad15d51c881b5b0b1d9a30a0326d68806db290",
        )
        version(
            "0.6.0-cp314",
            sha256="f9d71e0e4a8f8d5fc2dfb33c8f0540b2205786bc98ef68d729fa92e9ff9b7e5c",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "0.6.0-cp310",
            sha256="8d0f23ed548eb36a3bf28189a2df9f086f2da9801f38b4d1262884a62ae9ccd1",
        )
        version(
            "0.6.0-cp311",
            sha256="985132c3f187d42fec79dfba677608f215d05f849aa99e686e4ce7261ddf282b",
        )
        version(
            "0.6.0-cp312",
            sha256="14d27263e9780f92c1d66fa9010641c2fb1add3705fbae2cdc96d9e18df13eb3",
        )
        version(
            "0.6.0-cp313",
            sha256="fb2e37112856e3256e6efe2de10bf3838483ecd96e08272594563f28cd5d69e0",
        )
        version(
            "0.6.0-cp314",
            sha256="180b8cf670265bfd1c9d75210dd7daaa686799bf1aa2f05c84017c447a257d96",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.6.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@0.6.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@0.6.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@0.6.0-cp310")

    with default_args(type="run"):
        depends_on("py-networkx")
        depends_on("py-numpy@2")
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
