# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatAnapli(PythonPackage):
    """Module qat-anapli [88fa1da] - Compiled by Bull"""

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
            "0.3.0-cp310",
            sha256="a64d8245fdc2f47f4af5b0da6cd79a202624041a01d15f683cad2c7b99fa07e5",
        )
        version(
            "0.3.0-cp311",
            sha256="2867985ca5f026ea4a2ac9b544e017519ae3f60ed7694972ec69a4e9317f5235",
        )
        version(
            "0.3.0-cp312",
            sha256="ac792874d6564ab5e3754ba56f8477dcf1de26511b307e26d00b287af732dec8",
        )
        version(
            "0.3.0-cp313",
            sha256="c6a546ef08a4195113ce6cd568b8407eb010f0bc8a1a1982181b993db801e245",
        )
        version(
            "0.3.0-cp314",
            sha256="9af523ea88f41775f51d3017f0fc2635366139611e03481b8bef8c4c5d06f39d",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.3.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.3.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "0.3.0-cp310",
            sha256="bdd0e5fd118648fa76434f281ca2d11faf3c7c9acabe7b42004ff34e398e5a16",
        )
        version(
            "0.3.0-cp311",
            sha256="19d78f263777fe5fc8c08eb13faaf196b857868f47a92b14316840908acf27d7",
        )
        version(
            "0.3.0-cp312",
            sha256="379fcf8a5900a5942050efc2a4e8ab8bfde413ece111a2abb92d951f4c46d4a3",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "0.3.0-cp310",
            sha256="e6aff7433b29dd61777943095f4f2b40896dc50e99a6769adbd5bfb2e9ed458a",
        )
        version(
            "0.3.0-cp311",
            sha256="99411dc555a17bdcbcc17630c646b1587f4a8e9ae9339be7afe9ee0565d1cf39",
        )
        version(
            "0.3.0-cp312",
            sha256="e52ad137ed79a21b6db708287b5492acaaef9351570c4c9d8c6629d23059c867",
        )
        version(
            "0.3.0-cp313",
            sha256="2a14557cf6c5ce409c08f3545368bc0fe4d561bb5373630c013289e82070c8a0",
        )
        depends_on("python@3.13", type=("build", "run"), when="@0.3.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "0.3.0-cp310",
            sha256="7af302ad444ca9805173387b4c4dc74ccb2b334d3ab3b50d9f19df89089a9cd0",
        )
        version(
            "0.3.0-cp311",
            sha256="15fe197b7c91cca748388ab38ebc1ddb8b281cef33baf75274acbc5ebd5e1602",
        )
        version(
            "0.3.0-cp312",
            sha256="5e58f13c0517a7b0a1d6bb4cf5bd35c595b8a840e9cb766d673893bc913b776a",
        )
        version(
            "0.3.0-cp313",
            sha256="a806d6c91543b656a63c7b03aad416ef27cab43b8257125a682f97dbe94d2e13",
        )
        version(
            "0.3.0-cp314",
            sha256="01769e6cf760335b3d2b58d0373aafffd5cd3066c15828fb80feaded98e819ac",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.3.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.3.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "0.3.0-cp310",
            sha256="1bbf32e9ce9d1b10edfcfc2051f951d680e949d565c00a24e72d66d452ef8a6c",
        )
        version(
            "0.3.0-cp311",
            sha256="e3e2362fffd39add608fee874749cfa121ba8e1efa9aa441ec9529cfa13b69fb",
        )
        version(
            "0.3.0-cp312",
            sha256="a682f1a012978eaa5a6c186a04a96323f5dd0d5a1ab34eff9915b2f525943f6e",
        )
        version(
            "0.3.0-cp313",
            sha256="88c44d298bc1a4e47a55b46355465abf40556b96e78ed0c564ddb9b5420348b6",
        )
        version(
            "0.3.0-cp314",
            sha256="5a7dc75c6f371b56cce9e5af7ce4ad40ff1f9b3bf38cdd36f5263030b939c14a",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.3.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.3.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "0.3.0-cp310",
            sha256="2cab52eef067983609482aa348148045d47eeee1cff6b8fe224a81c1b6034295",
        )
        version(
            "0.3.0-cp311",
            sha256="71a64f1ddf1dc306406b00c217833d4f4e2b3b56a1efd11e3e3a984ba5588b5c",
        )
        version(
            "0.3.0-cp312",
            sha256="29f36e7e801bf8650e6df2bbb21096e22643410abda48319e01fee64075e065d",
        )
        version(
            "0.3.0-cp313",
            sha256="f07c6ecce0a49776050e4eaa09acc03d215016cc96c29e3cea2e3ed1b1daf179",
        )
        version(
            "0.3.0-cp314",
            sha256="aad59707ae64c176f198453941b01a1af39686732ff57dc5c8fe2f0025d40cea",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.3.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.3.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@0.3.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@0.3.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@0.3.0-cp310")

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
