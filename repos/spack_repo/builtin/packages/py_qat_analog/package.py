# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatAnalog(PythonPackage):
    """Module qat-analog [a5f3e1d] - Compiled by Bull"""

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
            "0.8.0-cp310",
            sha256="1d387b8d40c2182af8ef9e0c6508482254114124befec12c483229c26038d00e",
        )
        version(
            "0.8.0-cp311",
            sha256="62c9687ba3ceb81909decadc317f4c0a8f5957e4e2c9aa9b81233f7a2f6946e3",
        )
        version(
            "0.8.0-cp312",
            sha256="980623a41d4406490a1a8c00187892a62c3245d02d691391ae8700eeaec215c2",
        )
        version(
            "0.8.0-cp313",
            sha256="5684afb5766d5d5d8992c55c72de5083bea09bf3e1f74a9f5faba7c4a852f84b",
        )
        version(
            "0.8.0-cp314",
            sha256="fd4a8b7d3c0c78c6695eaad50c12cdf2d1baa0fe913a85172241ec376665db1d",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.8.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.8.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "0.8.0-cp310",
            sha256="a6123a9c7de1731d9663302d93914c0654cbe89c4bf5b240e41e2dd3f8bf58b9",
        )
        version(
            "0.8.0-cp311",
            sha256="609ba7e4e2f4378aa90787c9bea99990ab46d9322f4d4400cf54482df010fc0a",
        )
        version(
            "0.8.0-cp312",
            sha256="bb3283619aaaaabbc526d0c206523f87ad41ddab1f179c9024f1cde7db1a7bef",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "0.8.0-cp310",
            sha256="77016bb0898d6a9b3e486c33b39aa54cdf172d80fe14d2b347f2e4ccebfec057",
        )
        version(
            "0.8.0-cp311",
            sha256="7d180567191b4ce07f1cbb0a13bc75255fa654585077b227c135ba00c070a553",
        )
        version(
            "0.8.0-cp312",
            sha256="4994e4a672e9db2a5e5ef79723183fc7fdbafe68bd07247df4dbdbe786a55ebd",
        )
        version(
            "0.8.0-cp313",
            sha256="12a475987a42c44370e67a4b070b978a651c09b3b3c0ea49158533f89aa35287",
        )
        depends_on("python@3.13", type=("build", "run"), when="@0.8.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "0.8.0-cp310",
            sha256="98a96d9c38789614421cef1ebec8d6dcb87152fe3bb8099658bdbe20da6af4e4",
        )
        version(
            "0.8.0-cp311",
            sha256="78c92fc5f5cd4191ee6293e4c97e8d0b387a03197452f4608d13153171423fdc",
        )
        version(
            "0.8.0-cp312",
            sha256="2a94259ebb5fd2d6c10aedefe6ddc883b01e68c32b0294f879b02974f56f15a7",
        )
        version(
            "0.8.0-cp313",
            sha256="0e866f236fc66b5880e438f13e470b8858737956fd1c49c9762dd5791fc76d7f",
        )
        version(
            "0.8.0-cp314",
            sha256="590dd140e5333718574872061856ff8c18b3e97797231749d2c3d8c5225bafb7",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.8.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.8.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "0.8.0-cp310",
            sha256="08712b8dff3bbe9c622457073505eaf769575a5f3aba65ff084d77582a97972a",
        )
        version(
            "0.8.0-cp311",
            sha256="fe9a85ba8db9537e52c7584241e10dd395e1be06ae4c5e101482ff330464a74a",
        )
        version(
            "0.8.0-cp312",
            sha256="5a37c37881b816b728742ce3fe172829f01792b9e721386b0802f90be5dd7899",
        )
        version(
            "0.8.0-cp313",
            sha256="8ce45413466f965972937663c04674d2ce7e065e54d544b1f62c47e77cf37006",
        )
        version(
            "0.8.0-cp314",
            sha256="c1f5856724c7d2ca8344331a494bf9eab765455b22049c15ef25da220f9d78a5",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.8.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.8.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "0.8.0-cp310",
            sha256="652e258b0127cffd579e97d36591239dc9cd4036c253ee35cabdf6bb455e4409",
        )
        version(
            "0.8.0-cp311",
            sha256="bba194e2a7254f63dfdcea059e8f31f4d2da4ebfa7a47601b2bc40296e25b4ef",
        )
        version(
            "0.8.0-cp312",
            sha256="395a16e16843996585b5355f88a94af21fe590acd59d24b5239f5117bd3e6fbd",
        )
        version(
            "0.8.0-cp313",
            sha256="55f2c97b4b7374bfe52744816cb55828649eebf76ba87f67776585b21095fd22",
        )
        version(
            "0.8.0-cp314",
            sha256="527f4c37e63dc576fd96b06996e6d6a53c6c9d507d76e3a95140438684a9b133",
        )
        depends_on("python@3.14", type=("build", "run"), when="@0.8.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@0.8.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@0.8.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@0.8.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@0.8.0-cp310")

    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-qutip@5:")
        depends_on("py-qat-comm")
        depends_on("py-qat-core")
        depends_on("py-qat-hardware")
        depends_on("py-qat-lang")
        depends_on("py-qat-quops")

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
