# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatComm(PythonPackage):
    """Module qat-comm [6b072af] - Compiled by Bull"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    machine = platform.machine().lower()
    system = platform.system().lower()
    if system == "linux":
        libc = ctypes.CDLL("libc.so.6")
        libc.gnu_get_libc_version.restype = ctypes.c_char_p
        glibc_version = libc.gnu_get_libc_version().decode().replace(".", "_")
        platform_tag = f"manylinux_{glibc_version}_{machine}"
    elif system == "darwin":
        platform_tag = "macosx_11_0_arm64"
    elif system == "windows":
        platform_tag = "win_amd64"

    if "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.9.0-cp313",
            sha256="39accae71c6b08923ea60705fdab506d9c8a2212e6b12cf1a5eb94010fa3c19b",
        )
        version(
            "1.9.0-cp312",
            sha256="3fce6c0dbe63c6263a71417fa46d87e4ae39af03dee6f8c2c16a2e94c85cca78",
        )
        version(
            "1.9.0-cp311",
            sha256="238a1746657f5adf8b98cf1e704159d07c293247a226f0d79d4d004bd064b285",
        )
        version(
            "1.9.0-cp310",
            sha256="1ec5692296a56794128266d615032713c728ec56a8a94ec5d3fafd3d496e9426",
        )
    elif "macosx_11_0_arm64" == platform_tag:
        version(
            "1.9.0-cp314",
            sha256="a34f23658fe2c541c0ddc6d44fb4463b946affb51be5067337f92270558fb236",
        )
        version(
            "1.9.0-cp313",
            sha256="9f299398e6fdc1a9d799965c6bfd86db8ca332cb399f6badbea96098a2cbfa0b",
        )
        version(
            "1.9.0-cp312",
            sha256="4ba226f748849e5c32415c246275b3f0b30cb07ad93567001401a81b89944f64",
        )
        version(
            "1.9.0-cp311",
            sha256="08e65bf240b4e0e3137d2f09ff69ac3a28289bf861699e4ba1c9058e6353661d",
        )
        version(
            "1.9.0-cp310",
            sha256="d5db7832aa3a395f2cd5545d203917d879c0346fe9b3d5be2ecc22ed20382ddc",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.9.0-cp314")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.9.0-cp312",
            sha256="2ae65fe7129b226a2666254f1fa66dbeac5bcaba1485a7641c3d8367ffae95e1",
        )
        version(
            "1.9.0-cp311",
            sha256="284cd84903ca5f34ad6ed7c2c412ae0ab2baa047c7992d366159b1d206573cbf",
        )
        version(
            "1.9.0-cp310",
            sha256="4f56bb32b2d766a4cbccb56843e8997f5850f3e68b2c528605be423669a3c62d",
        )
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.9.0-cp314",
            sha256="771cf5b040412d4fa39af53862bf9672c3ee8acb32892a7db385d1232857c258",
        )
        version(
            "1.9.0-cp313",
            sha256="5b560c8112041df5942d813714fdced92f37e1a24a31b8993e3ea903b0da4893",
        )
        version(
            "1.9.0-cp312",
            sha256="eea8ded446184a645fd225de097aca9b63928b87beee8b859a7bc49185a8cf7f",
        )
        version(
            "1.9.0-cp311",
            sha256="5ebc54c40bf4f7252ff3ea2cc3ef551d11a0076203446657de94b79e33369c15",
        )
        version(
            "1.9.0-cp310",
            sha256="fab0184f5ae9b0b9f5e227a35cf4714eac63f24cd4b0b2f617e037f91114b79f",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.9.0-cp314")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.9.0-cp314",
            sha256="762d7c3c8b35b9a7f212c90894c42aea3d5411d277dae65888c99db79dcf4d03",
        )
        version(
            "1.9.0-cp313",
            sha256="0f85c8a8c80c9ee1a5921755a997cc6129cfcbea1b23d616b791ec5f11b2a588",
        )
        version(
            "1.9.0-cp312",
            sha256="b254896728238bb499b9215aab7408d9cbaae897604aad92ad1ba0bd6eade71d",
        )
        version(
            "1.9.0-cp311",
            sha256="000ed375b7969aafd429a6a48b8d543460cbc692dd0471238aa91f8e57f94d84",
        )
        version(
            "1.9.0-cp310",
            sha256="5319162d67bd165272eabbce6b5e80d52dfd0d22d8dcbb1e5704199b6d38f9db",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.9.0-cp314")
    elif "win_amd64" == platform_tag:
        version(
            "1.9.0-cp314",
            sha256="69d4b9d64b0c9427ea2c48ed4dbeaa38dfd907d5d22828aa7e367614ffebf3ae",
        )
        version(
            "1.9.0-cp313",
            sha256="9c8a41f3c423e7ab92c65b2d5affa99994cae6dc1ae25a3200dbf7bc1fbe483a",
        )
        version(
            "1.9.0-cp312",
            sha256="a9c14b58fbd86ee707de3ba75603c65e00973cc811a7e1faef10a92e513fa0d9",
        )
        version(
            "1.9.0-cp311",
            sha256="bed72819a951b746eaeadd2ec947f4431b420254846a89fd9a790f43ca55ceaf",
        )
        version(
            "1.9.0-cp310",
            sha256="a1b0b441b00c0f9264206a689ff968526b7c84a2b6d82cc435fa6d66aacf1132",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.9.0-cp314")

    depends_on("python@3.13", type=("build", "run"), when="@1.9.0-cp313")
    depends_on("python@3.12", type=("build", "run"), when="@1.9.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.9.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.9.0-cp310")

    with default_args(type="run"):
        depends_on("thrift@0.21.0 +python")
        depends_on("py-numpy@2")

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
