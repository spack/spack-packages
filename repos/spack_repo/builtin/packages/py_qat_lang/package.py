# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatLang(PythonPackage):
    """Module qat-lang [8f49858] - Compiled by Bull"""

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

    if "macosx_11_0_arm64" == platform_tag:
        version(
            "3.4.0-cp310",
            sha256="f0e83b20c88afb071e495e599bdfa8acded08c24d0760cf6d3926d0603b9b0c1",
        )
        version(
            "3.4.0-cp311",
            sha256="9de5596f89f71e19e9b74f377eef476fdf358530df311dc7128a315d239f3c4f",
        )
        version(
            "3.4.0-cp312",
            sha256="6e78644170ffb34b0cf6981190f43a40df8ebf523252cf8a58297b02d82bffd6",
        )
        version(
            "3.4.0-cp313",
            sha256="ca4fffa57c66c98a0257a9c5c9745dcd92be66e9264effcd934be03bcbffec40",
        )
        version(
            "3.4.0-cp314",
            sha256="3c8a0e7d7249bf0d3e6e94f47e5e5666c22f0a6b9f353afd203e5b11a47d471b",
        )
        depends_on("python@3.14", type=("build", "run"), when="@3.4.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@3.4.0-cp313")
    if "manylinux_2_28_aarch64" == platform_tag:
        version(
            "3.4.0-cp310",
            sha256="f900eeb2ada997a7a727eca2fc5d165598588132910f4704f45bd942472aaa8b",
        )
        version(
            "3.4.0-cp311",
            sha256="5562ac9a98dc926d4b6da2fb09a6be6e21496e0ec44a2c1e01503762df93f026",
        )
        version(
            "3.4.0-cp312",
            sha256="0bd4367f521ef63942bc3e6a4b8e7b6ee16e0f73cab9cfe31c11024998bb43f1",
        )
    if "manylinux_2_28_x86_64" == platform_tag:
        version(
            "3.4.0-cp310",
            sha256="8a1eeaa0a802d7fcd3281136c914a98a46f55762e33bf547f3e8b659240ac785",
        )
        version(
            "3.4.0-cp311",
            sha256="f3fe70819738af1d2823eab649ac44d1036d53ea90fe8349a9ac6499f2664600",
        )
        version(
            "3.4.0-cp312",
            sha256="2d79fdfaa0ed1d236ee8b15c29d6af166a1b382077ec4603fc4834d5ba08fe17",
        )
        version(
            "3.4.0-cp313",
            sha256="8236d8c8cd218d73e448873664097aec93da03f9c809f81134293f2f68d0ba05",
        )
        depends_on("python@3.13", type=("build", "run"), when="@3.4.0-cp313")
    if "manylinux_2_34_aarch64" == platform_tag:
        version(
            "3.4.0-cp310",
            sha256="791dc9225de5ef4d9ebd4001151d77d65b1195d9de042b974afaa00d40669c4d",
        )
        version(
            "3.4.0-cp311",
            sha256="70dcf0a0615c080164d663abd388e60161cd15d57e35d2a57f3f946ae7bf60e5",
        )
        version(
            "3.4.0-cp312",
            sha256="e5aa9c6b7aab1699c80b0800fe37189bd1483fd43ebeabf6f6193a4f31ad8c8f",
        )
        version(
            "3.4.0-cp313",
            sha256="dbd30679a43230237756f7e043fe7e45d92013d7880a2cbd731e1b84cc037c2c",
        )
        version(
            "3.4.0-cp314",
            sha256="4b40dd1ec4475fe8bc4219e28c82784ad67ecc4d58a1ef65fdc3388a332674ec",
        )
        depends_on("python@3.14", type=("build", "run"), when="@3.4.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@3.4.0-cp313")
    if "manylinux_2_34_x86_64" == platform_tag:
        version(
            "3.4.0-cp310",
            sha256="3d432eedb29f6da4fc62cfed038c6884b765967f9f6f019debcdd7ef8049bde7",
        )
        version(
            "3.4.0-cp311",
            sha256="6dbf258dacf9b477f9200cec5978ee70b34de5516f060520e10f34fedc0c3edb",
        )
        version(
            "3.4.0-cp312",
            sha256="a2a7e96584d86f3a5c7d8805a8bc7a6505b0e24730c21f75c9bdfd6684f6ecd1",
        )
        version(
            "3.4.0-cp313",
            sha256="cd7e3b3a4687f9424b1328ec84db4376b00f4d6f91843931765d7b05e95ea6ba",
        )
        version(
            "3.4.0-cp314",
            sha256="4ad820ce08120e0484d146ee54255101abaa6881789c578460b7e02ae05b48a2",
        )
        depends_on("python@3.14", type=("build", "run"), when="@3.4.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@3.4.0-cp313")
    if "win_amd64" == platform_tag:
        version(
            "3.4.0-cp310",
            sha256="a14e8f12136a96d3b19bde46492b862992c11338482a50d2f584e49a9a61dfcb",
        )
        version(
            "3.4.0-cp311",
            sha256="66115d28ce19049f060ae48c9bcbc37a512e6f5a65006eb886847cf3b5bf136c",
        )
        version(
            "3.4.0-cp312",
            sha256="92dae302b5a99c73e9ab62ba422524f090be9ebc6342eda6e652318dc9b69140",
        )
        version(
            "3.4.0-cp313",
            sha256="6f7d7adbf239c93e6d509b78ef348d63b21353ccf88e11153e8d355834d75715",
        )
        version(
            "3.4.0-cp314",
            sha256="3df89eba26dff11af521a9ed79439bc16c1f7b1cccf6f57fdfa2c21f9bc270fe",
        )
        depends_on("python@3.14", type=("build", "run"), when="@3.4.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@3.4.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@3.4.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@3.4.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@3.4.0-cp310")

    with default_args(type="run"):
        depends_on("thrift@0.21.0 +python")
        depends_on("py-ply@3.11")
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
