# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQlmaas(PythonPackage):
    """Module qlmaas [e9a398e] - Compiled by Bull"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    if "macosx_11_0_arm64" == platform_tag:
        version(
            "1.13.4-cp310",
            sha256="8593fad923c14b6cd9d574528da418515bc7885bd594074543133e82ae6efe99",
        )
        version(
            "1.13.4-cp311",
            sha256="3ccfd9f685715affb823ee225343a7f6af7f73cc521aed7fb68d6d5dd03ea283",
        )
        version(
            "1.13.4-cp312",
            sha256="ad7e19d922f4c67659eb455a2235197832f5748a486b83922218147bafe8d23d",
        )
        version(
            "1.13.4-cp313",
            sha256="b4cc89ef12ae421aa2741e4482cafa5a93cdc195e29de10c9f3c618fe8fa5f0b",
        )
        version(
            "1.13.4-cp314",
            sha256="d71fb221a67bada314220844b96eef151325b0117165362fb684dde7797f3fcd",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.13.4-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.13.4-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.13.4-cp310",
            sha256="ca7c48571c6944613b173a4966d851a36f0c5e4dd9ff42faed3c38591a01e6bc",
        )
        version(
            "1.13.4-cp311",
            sha256="efe576900dc7d483fcb2c0e185a4706e2ccb1813bcbf08a8ab81ad0b7fe6f9f3",
        )
        version(
            "1.13.4-cp312",
            sha256="ab5126be6ced2e8730d23909bebcc866b43260e6b978b78a1a2a567a39b57a76",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.13.4-cp310",
            sha256="893974af0f0735370a565b9ceea27f89aeac7ad0d55208effc2fc32230cfa463",
        )
        version(
            "1.13.4-cp311",
            sha256="c80359710f1f8ccb75b4d7e5992a7a5e389943c69735d2c0749e7d6654e478e1",
        )
        version(
            "1.13.4-cp312",
            sha256="c1c12030341eb3d40c362dbbf80c9a168e5d5e96a390551c670cf72cc4c849d9",
        )
        version(
            "1.13.4-cp313",
            sha256="91a5b65552ce2828c60f2e443d439b8ef959a31ce8fc337e0d45597de15c20b2",
        )
        depends_on("python@3.13", type=("build", "run"), when="@1.13.4-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.13.4-cp310",
            sha256="24112cf5326ed942b0909081ec6c467249fb0c6bd1a5739dcffbe4d69cd1beb4",
        )
        version(
            "1.13.4-cp311",
            sha256="84c9e42de38a2210bd12cf53a8356cad8731b16005455ebf539b8758f34d220a",
        )
        version(
            "1.13.4-cp312",
            sha256="c0b3259b908df2e2f28b8ba854ccea2b1f114312cd7b50873fe34907e19710e5",
        )
        version(
            "1.13.4-cp313",
            sha256="144834b0bc8636b2332f770823772e7cbb2d9d002a060dbb002878f78b756ecb",
        )
        version(
            "1.13.4-cp314",
            sha256="27ddf17c62eff5bad65664214862b3ceec95531188dff476d88445125b685886",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.13.4-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.13.4-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.13.4-cp310",
            sha256="ca4d5e4a25630475bbd4cd766de641b0928acf9528ea29531d3beef6bf7fbd3a",
        )
        version(
            "1.13.4-cp311",
            sha256="2ecafc4176594c4841d1147bc944f9de598f45fd95baa9f302acad5e8517df0a",
        )
        version(
            "1.13.4-cp312",
            sha256="d2d9bda476553958f7ad0f3e634dd353e4f0dcf23c619caed177272aa78e50f3",
        )
        version(
            "1.13.4-cp313",
            sha256="3de4bd6d5b057b50f81c1aedfc8d43a7e4884608b0fb672af77f743d462a895c",
        )
        version(
            "1.13.4-cp314",
            sha256="f74128890f9bc470d8ed702bdd7591331ac7175bf0af448ff118220fd288fc2b",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.13.4-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.13.4-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "1.13.4-cp310",
            sha256="954a4a25423925ffeca156d385f6b31f5ca34136adac40c96d207113ce9b1096",
        )
        version(
            "1.13.4-cp311",
            sha256="af00f83aa212a7932b69acae2c8a6cc5027dd7b870a1e95dc93a5149463821f3",
        )
        version(
            "1.13.4-cp312",
            sha256="e1532ff5930debb3e39f3361a09b97a65a7e132cba06fa0e6e17b8a90a189cde",
        )
        version(
            "1.13.4-cp313",
            sha256="f531e7ecef32a6f354ee7262892c215118bbcb9d9016c726e0bc9aeb08b66a8a",
        )
        version(
            "1.13.4-cp314",
            sha256="e47eec3fbca20b4f5e42fea515439aa34ae9a579c98af41d431c1fa41e809566",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.13.4-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.13.4-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@1.13.4-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.13.4-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.13.4-cp310")

    with default_args(type="run"):
        depends_on("py-dill")
        depends_on("py-prompt-toolkit")
        depends_on("py-prettytable")
        depends_on("py-pyopenssl")
        depends_on("py-cffi")
        depends_on("py-qat-hardware@1.7.1:")
        depends_on("py-qat-quops@1.6.0:")
        depends_on("py-packaging")
        depends_on("py-websockets")
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
