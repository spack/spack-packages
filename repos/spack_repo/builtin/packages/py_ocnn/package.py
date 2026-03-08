# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOcnn(PythonPackage):
    """O-CNN is an octree-based sparse convolutional neural network
    framework for 3D deep learning."""

    homepage = "https://github.com/octree-nn/ocnn-pytorch"
    pypi = "ocnn/ocnn-2.2.0.tar.gz"

    maintainers("wdconinc")

    license("MIT")

    version("2.3.1", sha256="cbb44189667269975d0427b50a1b14df219ea0ccbdd071f8e50d03b61511dc6b")
    version("2.3.0", sha256="34ce5f02ebf70d2bbd8cb39e7ec93a8aeb624ccf9d1e8ca888799583caf3a06a")
    version("2.2.8", sha256="6c8c3b731d87f04daa2206d227579789ba79364d49524f7351fd1354228057cd")
    version("2.2.7", sha256="f508d33d0743e0d9221541c0b46c6cc4508bf1b5fddab9d12c427147377f6da5")
    version("2.2.6", sha256="6ac9845ecc1e472b387c5acff270254a44ddb2548bcbf0add570f0753c0a4698")
    version("2.2.5", sha256="1f28ffed6aacd3b5c19dd8b8427818f5cbafc0f75e642e8de9674dea9696fc95")
    version("2.2.4", sha256="553202fed4078457283eda1c2e043faaff4242a739169126a0be12b7e670a81c")
    version("2.2.3", sha256="4dfe781117e031e7b490219fb68f9938d97787d73cea53204e8d9479dbff413e")
    version("2.2.2", sha256="627284bcd7d78c14a3bec1695e13ff4b726d47481d3ff863923d01381d588ee2")
    version("2.2.1", sha256="0b0f9d68d699af51d67b3ff940ce96f16245016f990e2d3f2015a998c0101451")
    version("2.2.0", sha256="5fb54305130921ece4cccf1697ec281f49d3e95837ba0e124cab9f8a567ecb80")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-torch@1.6.0:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
