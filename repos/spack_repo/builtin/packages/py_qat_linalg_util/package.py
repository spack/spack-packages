# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatLinalgUtil(PythonPackage):
    """Module qat-linalg-util [fbfea86] - Compiled by Bull"""

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
            "1.1.0-cp310",
            sha256="b5f5d68979c7f6182a2607555eb248885e7f4da5ec9bdf0fb92c5808d50ea454",
        )
        version(
            "1.1.0-cp311",
            sha256="55eeb330b8ebb961631e5714f3dd1d1b1cc9f0c5a98280044777e31aacd6df0b",
        )
        version(
            "1.1.0-cp312",
            sha256="810bb990e14f6eaddd0144b501c57dacb94b7a92e0d6fd217f93651ae174936b",
        )
        version(
            "1.1.0-cp313",
            sha256="74ebf21ed52459645db8f0e2a874b260e3aea5b3fb8f7cd143c3efdda5c07958",
        )
        version(
            "1.1.0-cp314",
            sha256="5a16e5faa0771c8340a0d5fac06a964a7f4c5066ae4c82e9c32c1a41261b6ae7",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.1.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.1.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.1.0-cp310",
            sha256="0bd979ce36f5e268f7c8d7b9cf2c9cb134916891a0984f30de314742849d555d",
        )
        version(
            "1.1.0-cp311",
            sha256="d8acf736d4f21b6d6e369b2f703be6e1a42da578a5198417db268de592201a8c",
        )
        version(
            "1.1.0-cp312",
            sha256="04ea49a77a36c9ad835a29db9cd70173da706f3c401a5b98de991d1381a50710",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.1.0-cp310",
            sha256="bb61c858b37b3be0d23b9dc29b957b2cbdb7bcc7319385ad417540ba064f05c9",
        )
        version(
            "1.1.0-cp311",
            sha256="734c0204793c94cd9c806b0d93720f9f2585f6572321aca5a4d91faa7d6e0771",
        )
        version(
            "1.1.0-cp312",
            sha256="80d255834f5f7eb2c6fae039cd452ab94c3ae696396216395c81299e6388613f",
        )
        version(
            "1.1.0-cp313",
            sha256="708c1e576fa6d755d734fdcc8f474c307305df75b6464532c22ec48022ccbec8",
        )
        depends_on("python@3.13", type=("build", "run"), when="@1.1.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.1.0-cp310",
            sha256="2210663fb5ba987517d9c0e8bc08fa148fc8d9391ffd2d8bf896c366810196e7",
        )
        version(
            "1.1.0-cp311",
            sha256="a9b6795c50d75dcfe9f5dd414b70b9751a1299c4151a0c1358254dddc0d65c6c",
        )
        version(
            "1.1.0-cp312",
            sha256="aba3299476189881b12ec4628203c38fccb1882041e8463e09d397142f04c679",
        )
        version(
            "1.1.0-cp313",
            sha256="f5a84bd5911629c70a11a81654da537988a38da3c5b0c2b71c411474d0c50556",
        )
        version(
            "1.1.0-cp314",
            sha256="182d653c4ac5fd837eb0642ba7dbac81a438483e69343c78b4ad58eac3909dc3",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.1.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.1.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.1.0-cp310",
            sha256="23637df65dcc0b6835bd8e67f3e58a519427f313e3abdbae686e90927fd60f58",
        )
        version(
            "1.1.0-cp311",
            sha256="480c040beda4cf1a85d0ccb4e031a5ad2725a0d1381d062642ac7d1894576ce4",
        )
        version(
            "1.1.0-cp312",
            sha256="5567c185bb7cbff4f9972e9057c8c7bb429872e5f4c4ed57b83412cd1ff2472b",
        )
        version(
            "1.1.0-cp313",
            sha256="5d39d35b805aeaa3c8a1858d1fec4af29303404def8bc552449b995c2d32a80e",
        )
        version(
            "1.1.0-cp314",
            sha256="6dffa1a093ad6d0163c584bb0898f2a9f71ec4890c6e1199fcb7075e021fa758",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.1.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.1.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "1.1.0-cp310",
            sha256="0473162b3e8b0c6aa8bd2274d3cbea99219ff523b7a1333e926213aae6dd4c2a",
        )
        version(
            "1.1.0-cp311",
            sha256="3d9456861bd7da4754cec3f9f8fe121423900c75a03136d094f5fda82f1d5188",
        )
        version(
            "1.1.0-cp312",
            sha256="f4e476c375097b771b5625a321ddc01f32afc03612fc6dfd200686cead058f1a",
        )
        version(
            "1.1.0-cp313",
            sha256="a3e08ff1e15cf0f712b19437aaf00326dbfc5a6e861badc7f2fbea0943af3cf2",
        )
        version(
            "1.1.0-cp314",
            sha256="fb915ec7966ec1ca69c2e47c7707833f53e90b4ace795a2052f780700a322300",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.1.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.1.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@1.1.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.1.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.1.0-cp310")

    with default_args(type="run"):
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
