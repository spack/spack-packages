# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatQuops(PythonPackage):
    """Module qat-quops [6336474] - Compiled by Bull"""

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
            "1.6.0-cp310",
            sha256="6a2700549e7ffdffbe04275f594dc0bd9bb7e1f02e45ab8e34534beb2eb49b4a",
        )
        version(
            "1.6.0-cp311",
            sha256="6e4bb3331eba3d7b11a3a3eff5257959de747328adf2cb6840a6c1703a4b7590",
        )
        version(
            "1.6.0-cp312",
            sha256="cb6dbb07568772224fb6ed198a6a11e08ceb2e2664378da78863c21e00518401",
        )
        version(
            "1.6.0-cp313",
            sha256="67efe650c937ef4114a20ecab02a1718106460c0c04f153c51c3ee71806b65f0",
        )
        version(
            "1.6.0-cp314",
            sha256="04bc8c88c2696f80bfdcebdb4d326be2699b740040b7cb543e2ad5d8ca59e61b",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.6.0-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.6.0-cp310",
            sha256="dab4828a05404d351c07069aa1692b7fe954bdeb8574be8ca182d107502dff1b",
        )
        version(
            "1.6.0-cp311",
            sha256="8bb20691a640243835512d4000e16ef9a23eb088b27d9e2eb82107dc1305b455",
        )
        version(
            "1.6.0-cp312",
            sha256="9e15ef4f09ef4f61cb15eb457a699a0578dab3245aa9968be7be81fbd90d4d11",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.6.0-cp310",
            sha256="05d75388abb233adcf5972b5f0e1b526e39ae84888f386258251a45ab910f08f",
        )
        version(
            "1.6.0-cp311",
            sha256="9ded54c1ce02158388ebf9e217ca2a5b232ed2c83d685242feaf4bafde2f3293",
        )
        version(
            "1.6.0-cp312",
            sha256="89e5ea71ce9ae4a9b613bf19cd8a980e9e63f03af1764103073fd93a9ff1f730",
        )
        version(
            "1.6.0-cp313",
            sha256="8a54a6c7496c0e1bdfab9a5cb2a56709ad573a3b3999c78daa257230e73a9daa",
        )
        depends_on("python@3.13", type=("build", "run"), when="@1.6.0-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.6.0-cp310",
            sha256="d434490ce5a3d813120803581bbca1d90b0df20e25ae3e982c878978857fdb4e",
        )
        version(
            "1.6.0-cp311",
            sha256="ad520e16f3598c35d136207e55ae89cf0935fd80836370c533b46a5c6279ef23",
        )
        version(
            "1.6.0-cp312",
            sha256="25c2db50b83c53c5f549e355fb482cc0cf3c419bc6dd9cdb8a77aea0e8c250f9",
        )
        version(
            "1.6.0-cp313",
            sha256="99aa6b2c1f4ebdf76a7f42123c274018b3decae17fcc8f427c772fa6abdb5ba3",
        )
        version(
            "1.6.0-cp314",
            sha256="df3d44ead4968345b016ad964b7f9fbc6e1178b4d5e9b435165a113ed4061b5e",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.6.0-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.6.0-cp310",
            sha256="d8f48e98efd37f7a8807fb7bd9ee16f5c2ee3f16cfe04f13751dab772beb4442",
        )
        version(
            "1.6.0-cp311",
            sha256="493d9a1ae23e32798ad9e08bbef8002613f55934506171cebd0180fafa64dff8",
        )
        version(
            "1.6.0-cp312",
            sha256="1fb72a032b12387e9913804664b75f6f411283bea859d59f9111692f844ccdd7",
        )
        version(
            "1.6.0-cp313",
            sha256="ca51fc97b528a7001861bdcd2e376d512f49953d29651dfe70c90db4377cd745",
        )
        version(
            "1.6.0-cp314",
            sha256="752a68b9fadfc52fda54917ab550d5ddd61d00ec762468401562ab090bf5e2b0",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.6.0-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "1.6.0-cp310",
            sha256="c29cef9251d10237c6282e3ccb0529bdc8c2e385f830821e2b9a8783a46c2500",
        )
        version(
            "1.6.0-cp311",
            sha256="6313752fad4cd46b2609586d2a3e11e53f2ba38cc1efd7ab23de0461639128c4",
        )
        version(
            "1.6.0-cp312",
            sha256="73b91b782992140cefaa1fb4c67537b5bbfcbcb67551929e2203735bfe67ef65",
        )
        version(
            "1.6.0-cp313",
            sha256="d7d80117d5d56f2151c8c18af3fb9debcbca52c78bef9a69ed12238014e70e87",
        )
        version(
            "1.6.0-cp314",
            sha256="78199795f99228aa1c28ec561673fb2fbe0b445e816851b5796a11129ac5e35b",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.6.0-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.6.0-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@1.6.0-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.6.0-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.6.0-cp310")

    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-matplotlib")
        depends_on("py-cvxpy")
        depends_on("py-qat-comm")
        depends_on("py-qat-core")
        depends_on("py-qat-lang")

    def url_for_version(self, version):
        platform_tag = next(sys_tags()).platform
        if platform_tag in self.supported_tag:
            url = "https://pypi.io/packages/{1}/q/qat-quops/qat_quops-{0}-{1}-{1}-{2}.whl"
            pkg_ver = version.up_to_3
            cp_ver = version.string.split("-")[1]
            return url.format(pkg_ver, cp_ver, platform_tag)
        else:
            raise ValueError(f"Tag {tag} is not implemented.")
