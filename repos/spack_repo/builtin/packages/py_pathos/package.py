# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPathos(PythonPackage):
    """Parallel graph management and execution in heterogeneous computing"""

    homepage = "https://github.com/uqfoundation/pathos"
    pypi = "pathos/pathos-0.3.5.tar.gz"

    license("BSD-3-Clause")

    version("0.3.5", sha256="8fe041b8545c5d3880a038f866022bdebf935e5cf68f56ed3407cb7e65193a61")
    version("0.3.4", sha256="bad4912d0ef865654a7cc478da65f2e1d5b69f3d92c4a7d9c9845657783c0754")
    version("0.3.3", sha256="dcb2a5f321aa34ca541c1c1861011ea49df357bb908379c21dd5741f666e0a58")
    version("0.3.2", sha256="4f2a42bc1e10ccf0fe71961e7145fc1437018b6b21bd93b2446abc3983e49a7a")
    version("0.3.1", sha256="c9a088021493c5cb627d4459bba6c0533c684199e271a5dc297d62be23d74019")
    version("0.3.0", sha256="24fa8db51fbd9284da8e191794097c4bb2aa3fce411090e57af6385e61b97e09")
    version("0.2.9", sha256="a8dbddcd3d9af32ada7c6dc088d845588c513a29a0ba19ab9f64c5cd83692934")
    version("0.2.8", sha256="1f0f27a90f7ab66c423ba796529000fde9360d17b2d8e50097641ff405fc6f15")
    version("0.2.7", sha256="383449988a85f18943610f480f5f3c2077de9e0a2bfa3833c9b6346fe7dacc1b")
    version("0.2.6", sha256="51b48e54870e4f83a262e49b6369116ab2ecc5a217569a84c7ab726e27b1bc10")
    version("0.2.5", sha256="21ae2cb1d5a76dcf57d5fe93ae8719c7339f467e246163650c08ccf35b87c846")
    version("0.2.4", sha256="610dc244b6b5c240396ae392bb6f94d7e990b0062d4032c5e9ab00b594ed8720")
    version("0.2.3", sha256="954c5b0a8b257c375e35d311c65fa62a210a3d65269195557de38418ac9f61f9")
    version("0.2.2.1", sha256="69486cfe8c9fbd028395df445e4205ea3001d7ca5608d8d0b67b67ce98bb8892")
    version("0.2.2", sha256="b18f8e552e6422b5e3beb74f0e9ff84918fb163c584cc947cc7d0845956194a0")
    version("0.2.1", sha256="a153a0a9d093220688ba7972e4a9a95996a6a5caece2feb3576b22e6d474c6a0")
    version("0.2.0", sha256="2f4e67e7914c95fb0cce766bab173eb2c5860ee420108fa183099557ac2e50e9")

    depends_on("py-setuptools@0.6:", type="build")

    # Python
    depends_on("python@3.9:", when="@0.3.5:")
    depends_on("python@3.8:", when="@0.3.0:0.3.4")
    depends_on("python@3.7:", when="@0.2.9")
    depends_on("python@3.6:", when="@0.2.8")
    depends_on("python@3.5:", when="@0.2.6:0.2.7")
    depends_on("python@3.1:", when="@0.2.0:0.2.5")

    # dill
    depends_on("py-dill@0.4.1:", type=("build", "run"), when="@0.3.5:")
    depends_on("py-dill@0.4.0:", type=("build", "run"), when="@0.3.4")
    depends_on("py-dill@0.3.9:", type=("build", "run"), when="@0.3.3")
    depends_on("py-dill@0.3.8:", type=("build", "run"), when="@0.3.2")
    depends_on("py-dill@0.3.7:", type=("build", "run"), when="@0.3.1")
    depends_on("py-dill@0.3.6:", type=("build", "run"), when="@0.3.0")
    depends_on("py-dill@0.3.5:", type=("build", "run"), when="@0.2.9")
    depends_on("py-dill@0.3.4:", type=("build", "run"), when="@0.2.8")
    depends_on("py-dill@0.3.3:", type=("build", "run"), when="@0.2.7")
    depends_on("py-dill@0.3.2:", type=("build", "run"), when="@0.2.6")
    depends_on("py-dill@0.3.1:", type=("build", "run"), when="@0.2.5")
    depends_on("py-dill@0.3.0:", type=("build", "run"), when="@0.2.4")
    depends_on("py-dill@0.2.9:", type=("build", "run"), when="@0.2.3")
    depends_on("py-dill@0.2.8.2:", type=("build", "run"), when="@0.2.2.1")
    depends_on("py-dill@0.2.8.1:", type=("build", "run"), when="@0.2.2")
    depends_on("py-dill@0.2.7:", type=("build", "run"), when="@0.2.1")
    depends_on("py-dill@0.2.5:", type=("build", "run"), when="@0.2.0")

    # pox
    depends_on("py-pox@0.3.7:", type=("build", "run"), when="@0.3.5:")
    depends_on("py-pox@0.3.6:", type=("build", "run"), when="@0.3.4")
    depends_on("py-pox@0.3.5:", type=("build", "run"), when="@0.3.3")
    depends_on("py-pox@0.3.4:", type=("build", "run"), when="@0.3.2")
    depends_on("py-pox@0.3.3:", type=("build", "run"), when="@0.3.1")
    depends_on("py-pox@0.3.2:", type=("build", "run"), when="@0.3.0")
    depends_on("py-pox@0.3.1:", type=("build", "run"), when="@0.2.9")
    depends_on("py-pox@0.3.0:", type=("build", "run"), when="@0.2.8")
    depends_on("py-pox@0.2.9:", type=("build", "run"), when="@0.2.7")
    depends_on("py-pox@0.2.8:", type=("build", "run"), when="@0.2.6")
    depends_on("py-pox@0.2.7:", type=("build", "run"), when="@0.2.5")
    depends_on("py-pox@0.2.6:", type=("build", "run"), when="@0.2.4")
    depends_on("py-pox@0.2.5:", type=("build", "run"), when="@0.2.3")
    depends_on("py-pox@0.2.4:", type=("build", "run"), when="@0.2.2:0.2.2.1")
    depends_on("py-pox@0.2.3:", type=("build", "run"), when="@0.2.1")
    depends_on("py-pox@0.2.2:", type=("build", "run"), when="@0.2.0")

    # ppft
    depends_on("py-ppft@1.7.8:", type=("build", "run"), when="@0.3.5:")
    depends_on("py-ppft@1.7.7:", type=("build", "run"), when="@0.3.4")
    depends_on("py-ppft@1.7.6.9:", type=("build", "run"), when="@0.3.3")
    depends_on("py-ppft@1.7.6.8:", type=("build", "run"), when="@0.3.2")
    depends_on("py-ppft@1.7.6.7:", type=("build", "run"), when="@0.3.1")
    depends_on("py-ppft@1.7.6.6:", type=("build", "run"), when="@0.3.0")
    depends_on("py-ppft@1.7.6.5:", type=("build", "run"), when="@0.2.9")
    depends_on("py-ppft@1.6.6.4:", type=("build", "run"), when="@0.2.8")
    depends_on("py-ppft@1.6.6.3:", type=("build", "run"), when="@0.2.7")
    depends_on("py-ppft@1.6.6.2:", type=("build", "run"), when="@0.2.6")
    depends_on("py-ppft@1.6.6.1:", type=("build", "run"), when="@0.2.4:0.2.5")
    depends_on("py-ppft@1.6.4.9:", type=("build", "run"), when="@0.2.3")
    depends_on("py-ppft@1.6.4.8:", type=("build", "run"), when="@0.2.2:0.2.2.1")
    depends_on("py-ppft@1.6.4.7:", type=("build", "run"), when="@0.2.1")
    depends_on("py-ppft@1.6.4.5:", type=("build", "run"), when="@0.2.0")

    # multiprocess
    depends_on("py-multiprocess@0.70.19:", type=("build", "run"), when="@0.3.5:")
    depends_on("py-multiprocess@0.70.18:", type=("build", "run"), when="@0.3.4")
    depends_on("py-multiprocess@0.70.17:", type=("build", "run"), when="@0.3.3")
    depends_on("py-multiprocess@0.70.16:", type=("build", "run"), when="@0.3.2")
    depends_on("py-multiprocess@0.70.15:", type=("build", "run"), when="@0.3.1")
    depends_on("py-multiprocess@0.70.14:", type=("build", "run"), when="@0.3.0")
    depends_on("py-multiprocess@0.70.13:", type=("build", "run"), when="@0.2.9")
    depends_on("py-multiprocess@0.70.12:", type=("build", "run"), when="@0.2.8")
    depends_on("py-multiprocess@0.70.11:", type=("build", "run"), when="@0.2.7")
    depends_on("py-multiprocess@0.70.10:", type=("build", "run"), when="@0.2.6")
    depends_on("py-multiprocess@0.70.9:", type=("build", "run"), when="@0.2.5")
    depends_on("py-multiprocess@0.70.8:", type=("build", "run"), when="@0.2.4")
    depends_on("py-multiprocess@0.70.7:", type=("build", "run"), when="@0.2.3")
    depends_on("py-multiprocess@0.70.6.1:", type=("build", "run"), when="@0.2.2:0.2.2.1")
    depends_on("py-multiprocess@0.70.5:", type=("build", "run"), when="@0.2.1")
    depends_on("py-multiprocess@0.70.4:", type=("build", "run"), when="@0.2.0")

    def url_for_version(self, version):
        url = "https://pypi.io/packages/source/p/pathos/pathos-{0}.{1}"
        zip_versions = [
            Version("0.2.0"),
            Version("0.2.1"),
            Version("0.2.6"),
            Version("0.2.7"),
            Version("0.2.8"),
        ]
        ext = "zip" if version in zip_versions else "tar.gz"
        return url.format(version, ext)
