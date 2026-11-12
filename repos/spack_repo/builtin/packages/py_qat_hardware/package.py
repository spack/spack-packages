# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import ctypes
import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQatHardware(PythonPackage):
    """Module qat-hardware [87c30b3] - Compiled by Bull"""

    homepage = "https://www.bull.com/en/solutions/quantum-computing"

    supplier = "Organization: Bull SAS"

    maintainers("LydDeb")

    supported_tag = ["manylinux_2_28_x86_64"]

    version(
        "1.7.2-cp313", sha256="3f4b1dcde5dc34d5db45b724da04442bb672d266e64be769d1cd10316d673373"
    )
    version(
        "1.7.2-cp312", sha256="e4bac354fe69d54839d17feb29716b8014fe75d744e842590e2eb81b2c621843"
    )
    version(
        "1.7.2-cp311", sha256="68a670b11cd83d3d98cc583444f8a30594229c33d3cca6d06eec079650b5de31"
    )
    version(
        "1.7.2-cp310", sha256="cdb8bd6ad8959216c7fad0f0dd72895c5181acf13fc2a85ff912ce2f85831790"
    )




    if "macosx_11_0_arm64" == platform_tag:
        version(
            "1.7.2-cp310",
            sha256="f525ce4c64927c938a4cc781fae69a46b5e2197998e11ba7200f495a88eabe73",
        )
        version(
            "1.7.2-cp311",
            sha256="685e847f01f80d79ad84c14bed6f74fce1a168adce265a8dc3106e4bbc8252c7",
        )
        version(
            "1.7.2-cp312",
            sha256="de9534ef9156393345a6c2361ee1edd8d0e935755626f22f78e4620d5ab07e27",
        )
        version(
            "1.7.2-cp313",
            sha256="abadf37c49416a95c4302dc83780ace78553868789d701b870c5446480789ecc",
        )
        version(
            "1.7.2-cp314",
            sha256="c1f92b680edb386d665e79bc581c69171a2af60067aaba97fbb92a1fed35a3c2",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.7.2-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.7.2-cp313")
    elif "manylinux_2_28_aarch64" == platform_tag:
        version(
            "1.7.2-cp310",
            sha256="dc365a0162db0205279c4b96fb55c117cb50a49a7c48589a375620d448bddac7",
        )
        version(
            "1.7.2-cp311",
            sha256="7d0c5435ae89b423dc57a2dedf1175b21b504a5fec7884b368a1d1155e65637d",
        )
        version(
            "1.7.2-cp312",
            sha256="7069f57a423db70bb936dc1ebb84c7094955b5c089cf65e4cbc0cef4488efad0",
        )
    elif "manylinux_2_28_x86_64" == platform_tag:
        version(
            "1.7.2-cp310",
            sha256="cdb8bd6ad8959216c7fad0f0dd72895c5181acf13fc2a85ff912ce2f85831790",
        )
        version(
            "1.7.2-cp311",
            sha256="68a670b11cd83d3d98cc583444f8a30594229c33d3cca6d06eec079650b5de31",
        )
        version(
            "1.7.2-cp312",
            sha256="e4bac354fe69d54839d17feb29716b8014fe75d744e842590e2eb81b2c621843",
        )
        version(
            "1.7.2-cp313",
            sha256="3f4b1dcde5dc34d5db45b724da04442bb672d266e64be769d1cd10316d673373",
        )
        depends_on("python@3.13", type=("build", "run"), when="@1.7.2-cp313")
    elif "manylinux_2_34_aarch64" == platform_tag:
        version(
            "1.7.2-cp310",
            sha256="edb81a903676848dae7481a068549f566d337311e57e91f8ea8d6fcdf4416a6b",
        )
        version(
            "1.7.2-cp311",
            sha256="f5ed0ea7102d6e011bc35341f95d20d7cec84959927facb87c14fba61be56bd1",
        )
        version(
            "1.7.2-cp312",
            sha256="42f96c535de4f2631d06b31a2a762bdca2dbab5318db8e434d0e900c03d73b36",
        )
        version(
            "1.7.2-cp313",
            sha256="ef63bb16f11749be8bf9c1c6aaeaebe5b0b3fbcc62a9e5293d320457b5199041",
        )
        version(
            "1.7.2-cp314",
            sha256="b5ec08ba7e8863331365b603128c285328d4dacfe26eae6b5a5116cc4537b369",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.7.2-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.7.2-cp313")
    elif "manylinux_2_34_x86_64" == platform_tag:
        version(
            "1.7.2-cp310",
            sha256="f2870ced592c44ce5775afc5eb4bfbe917ba7a1ee2505b7dde228a185eb49dd6",
        )
        version(
            "1.7.2-cp311",
            sha256="112cc378af64774a45eaf0cde6101953fe83ed7faf60baddce9a090185b212c4",
        )
        version(
            "1.7.2-cp312",
            sha256="becc50041247a53a556584f1d66f33421951be57bc56e63b8f31b269b98ad17d",
        )
        version(
            "1.7.2-cp313",
            sha256="7cd824c026b05b1d605d977ca3bbfde179ecb0fde2597ca886526e5e5d94121d",
        )
        version(
            "1.7.2-cp314",
            sha256="42e72891422fa45b15ff54c86875eff993e64e342c5a22b7ec23c98062ec0562",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.7.2-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.7.2-cp313")
    elif "win_amd64" == platform_tag:
        version(
            "1.7.2-cp310",
            sha256="1349c897e658173f0f1d37fc25c45b3c37cb847d662205186df7ed478f2396f8",
        )
        version(
            "1.7.2-cp311",
            sha256="f76d1ef03a695a4c67fd6c5f2809d450baa86af3e5079a98b09685dd957fefb9",
        )
        version(
            "1.7.2-cp312",
            sha256="ce7f60f3c7f168246fcb390e4b710e79ccf4de3e7b7af2328e7032eea8c27ced",
        )
        version(
            "1.7.2-cp313",
            sha256="008b03ae5b05b4a3dd36fcfda583d261567159dd36be643e9574713cbc5fa870",
        )
        version(
            "1.7.2-cp314",
            sha256="48e1875c916b1da95caa82670c240a605f17c6402a8655c2b9d678bcc333d113",
        )
        depends_on("python@3.14", type=("build", "run"), when="@1.7.2-cp314")
        depends_on("python@3.13", type=("build", "run"), when="@1.7.2-cp313")

    depends_on("python@3.12", type=("build", "run"), when="@1.7.2-cp312")
    depends_on("python@3.11", type=("build", "run"), when="@1.7.2-cp311")
    depends_on("python@3.10", type=("build", "run"), when="@1.7.2-cp310")

    with default_args(type="run"):
        depends_on("py-qutip")
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
