# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatCore(PythonPackage):
    """Module qat-core [a96d937] - Compiled by Bull"""

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
            "1.13.1-cp314",
            sha256="8f763437cf683e6dd37df033c30dad8faf7320c89a6ec55a0cb286a86df24d21",
        )
        version(
            "1.13.1-cp313",
            sha256="ef0667fac8895c23d51948cf580d5e119af6aa364f34b8c9b376aec7e56fa6ad",
        )
        version(
            "1.13.1-cp312",
            sha256="e9e127efc0102bcf8c9b38a0d10f577a5a213c7e32726bb0bfe7f1bdcb010173",
        )
        version(
            "1.13.1-cp311",
            sha256="9e65113b9e8fe834217868e02259275734dac0b7261a78de73d1255fac3908d1",
        )
        version(
            "1.13.1-cp310",
            sha256="c0df4e5a1e3c6ac863ada026d49542ad8be5109227877475d44187139124023a",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.13.1-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.13.1-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.13.1-cp312",
            sha256="3d623cc7c0596a98d0d036aa60689bb5a022721cfc7e2c7a9f4efd4a70e79f86",
        )
        version(
            "1.13.1-cp311",
            sha256="9e4dbd16f816d38243d987d66a23bedbbe5c3cd08115ad9cfd6dbd3e2f3e4228",
        )
        version(
            "1.13.1-cp310",
            sha256="0f492d26cce3fd2d4ab94371b5ebb28adf9e0b94e184346d9cfa74a4d5c78cdf",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.13.1-cp313",
            sha256="554e64e5cd1794d7900d83357ed55ede7d7d4f24eeafd9551ff4e26cbcd400ee",
        )
        version(
            "1.13.1-cp312",
            sha256="7c5bc7b20bc336874395ec74129272a1ceaa378875d0270d5d5f3b6cfa896240",
        )
        version(
            "1.13.1-cp311",
            sha256="12358585c59c70fe96f5c67b0c5cd5d597a9a2d629dc520d3d61d9f8618f9e7a",
        )
        version(
            "1.13.1-cp310",
            sha256="664ef00285ff2f303402c3ba81db32d59e97c1a97de8e4a11468536c91e38a69",
        )
        depends_on("python@3.13", type=("build", "run"), when="@1.13.1-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.13.1-cp314",
            sha256="5722778af05364c7942b7a1edafb5581fb14df6b86c61e841b0f3a5e9996eefe",
        )
        version(
            "1.13.1-cp313",
            sha256="41a6e5ed1a5a53f18ee29914213ae4a9580b3193f085c35839616135c210acd6",
        )
        version(
            "1.13.1-cp312",
            sha256="b9d72a383c590a2d310ee92bfe4b3463eb512a3c527f984b03183f8106372b64",
        )
        version(
            "1.13.1-cp311",
            sha256="f974c0781e74609a991ecd30f3de0c3c6d2197025d72501c7c39e9b349eed547",
        )
        version(
            "1.13.1-cp310",
            sha256="fcf3af6ae8bf4ff08ac61e1ffb397adf695b5656cd7e9c55b5e64a18d321bdd4",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.13.1-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.13.1-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.13.1-cp314",
            sha256="4f947e03e213e9339d6a199229a1ecaba4c70fb2612848470f2f806650591a4c",
        )
        version(
            "1.13.1-cp313",
            sha256="02aa848608ad9723e52ec6b552a722bd2b4a8b66cc234111ff32dcee1f2fa241",
        )
        version(
            "1.13.1-cp312",
            sha256="c89eb607d4b9324f5156eed17bbb8c518daedd7403066866fdf5c4fab2d1f33b",
        )
        version(
            "1.13.1-cp311",
            sha256="a3ac6b18dc926464df82a1a1d6d9bc64cd6313bfb1c59894b6fac81002d97e69",
        )
        version(
            "1.13.1-cp310",
            sha256="4cb4217289aae3c49662c8d4e8d71173b7564839313320531d4c3d065db74e80",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.13.1-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.13.1-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "1.13.1-cp314",
            sha256="f7748405bc8c0436cea50bd00bb45603aaff33d76c4d42a11e45b771a043434c",
        )
        version(
            "1.13.1-cp313",
            sha256="386a26d84e8b4db44542acba8d441d463a0a6bb97ed4e660d3be4cbf927f339e",
        )
        version(
            "1.13.1-cp312",
            sha256="75d3d44e6d3b7a43eaca56ce8a7c983b207a292605a784befa95d69ecdce7e3e",
        )
        version(
            "1.13.1-cp311",
            sha256="d7534c219638de1fe3a9b093c9613d3ff904a7bf5ec8dd8b869dcbcf689546bf",
        )
        version(
            "1.13.1-cp310",
            sha256="2481231e02f9b2ec612ed239a857ae8cf51d2a7cbbaa7f74b362da7a6eb59c6d",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.13.1-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.13.1-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@1.13.1-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.13.1-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.13.1-cp310")

    with default_args(type="run"):
        depends_on("thrift@0.21.0 +python")
        depends_on("py-numpy@2")
        depends_on("py-bitstring")
        depends_on("py-wand")
        depends_on("py-dill")
        depends_on("py-matplotlib")
        depends_on("py-pillow")
        depends_on("py-svgwrite")
        depends_on("py-jax")
        depends_on("py-ipython")
        depends_on("py-qat-comm")

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
