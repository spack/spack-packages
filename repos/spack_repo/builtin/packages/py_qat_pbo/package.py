# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatPbo(PythonPackage):
    """Module qat-pbo [bf6e819] - Compiled by Bull"""

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
            "1.7.0-cp310",
            sha256="820553fee0d59b03bb3c2bf258d14ce01b5e49bcf41abe3e3bf417ae318b142d",
        )
        version(
            "1.7.0-cp311",
            sha256="95b85412869fc94673d8ab675d15dccf5cec46da048b25d44179d05b5204e8b1",
        )
        version(
            "1.7.0-cp312",
            sha256="7db5d98bef2c36cfe1b6bf7de78cf8171b21f43ee4d218f55f3c296b47ad1820",
        )
        version(
            "1.7.0-cp313",
            sha256="0a8b7ed052e95da887ce8bd8837a233dfecea70d185199256049ac9844f509f1",
        )
        version(
            "1.7.0-cp314",
            sha256="805cbbc08e29dec12901881db3454545c9bc75fdf6e327000e147a04da111c21",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.7.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.7.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.7.0-cp310",
            sha256="76d775f2a16ff308331df5220f1bf55379373a22729762ae1d5b6cdd509c48d1",
        )
        version(
            "1.7.0-cp311",
            sha256="a6bf982970a75282bcf9eea74189ef18ffd11d473760dc6404a9a0534e104553",
        )
        version(
            "1.7.0-cp312",
            sha256="9c0ae0f30958ae4b553cd01b6bcc89a387bcbcec34cfe69c52c713db0eaf5f14",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.7.0-cp310",
            sha256="cd05f1acffb84bb951328fcec8a294a7543d21a37bf933b1d92d465af95a1fec",
        )
        version(
            "1.7.0-cp311",
            sha256="1ea0838dfe69cee895e942cfd3305d840452b9f65d3e8c239719f9161dda0665",
        )
        version(
            "1.7.0-cp312",
            sha256="c1a7445d5ad173f96eee078bfce3978a9bad1c109bbe499b64eac599fdfd777b",
        )
        version(
            "1.7.0-cp313",
            sha256="ee9c63d4c61b557e1a68e99807b3e1ff94322f4cdf1a9da906827b75a6487795",
        )
        depends_on("python@3.13", type=("build", "run"), when="@1.7.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.7.0-cp310",
            sha256="36d2778ef003783ba3f4914746f3010af51cd8e124954888601a8892a8cc7303",
        )
        version(
            "1.7.0-cp311",
            sha256="6087372cd74d18b2319939d97a80a2ae10fa63a29e8d6b89f87266c3ca2720e3",
        )
        version(
            "1.7.0-cp312",
            sha256="63af8bc8aa6583d2da7ec502facd77f76e967650fd3fa64bc9f54ba66dae441c",
        )
        version(
            "1.7.0-cp313",
            sha256="c406f361983594eeef319ab24c873ae9bdf94222cde5a5786e535e8790e3d41c",
        )
        version(
            "1.7.0-cp314",
            sha256="1848ad4f480756fad402e0c6cc00842adc8899fddb87fdaba345494787cd1f57",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.7.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.7.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.7.0-cp310",
            sha256="8cd1d9d092c2b6fdb583a00f61ec04a9618a4d91e3be8b9999fb838064ed9fe7",
        )
        version(
            "1.7.0-cp311",
            sha256="2efc2525040425652617e183fd7f90e475162f9199bdd68f90470d9843d0925d",
        )
        version(
            "1.7.0-cp312",
            sha256="53bbed78b827334dac3b096ac1ecffc3b4dd67d9b3d26558cf10dde173eeef59",
        )
        version(
            "1.7.0-cp313",
            sha256="869adb8121913468cc38c7ed15e5d73f2925ff88ccc2807201bbfdd3345e4dea",
        )
        version(
            "1.7.0-cp314",
            sha256="056a83d811da18a1948d1f30bd868cb5781802953037a5a1f5f14091e1b8b9c5",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.7.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.7.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "1.7.0-cp310",
            sha256="65c4b0593739603748af11355245ba1b08d010f7eb0ed31f5d9c8574de116d41",
        )
        version(
            "1.7.0-cp311",
            sha256="048b4b187a5ac501b44e3719017bf975e87a0c469be387a5c890d464ba811d7a",
        )
        version(
            "1.7.0-cp312",
            sha256="c51b1ad0ad30c38fae1a2df46362b4d27c65e768375567f0d11c7579b3e20191",
        )
        version(
            "1.7.0-cp313",
            sha256="e44d75afa678394dfe2b8e07676f91bf75e9efb1d087017cd50d146a3793f93b",
        )
        version(
            "1.7.0-cp314",
            sha256="381165ff04e3211126d441517eaf587ce79836368f79be1a0f07398b50e8dc4f",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.7.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.7.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@1.7.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.7.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.7.0-cp310")

    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-qat-comm")
        depends_on("py-qat-core")
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
