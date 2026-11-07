# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPathos(PythonPackage):
    """Parallel graph management and execution in heterogeneous computing"""

    homepage = "https://github.com/uqfoundation/pathos"
    pypi = "pathos/pathos-0.2.3.tar.gz"

    license("BSD-3-Clause")

    version("0.3.5", sha256="8fe041b8545c5d3880a038f866022bdebf935e5cf68f56ed3407cb7e65193a61")
    version("0.3.3", sha256="dcb2a5f321aa34ca541c1c1861011ea49df357bb908379c21dd5741f666e0a58")
    version("0.3.2", sha256="4f2a42bc1e10ccf0fe71961e7145fc1437018b6b21bd93b2446abc3983e49a7a")
    version("0.3.1", sha256="c9a088021493c5cb627d4459bba6c0533c684199e271a5dc297d62be23d74019")
    version("0.3.0", sha256="24fa8db51fbd9284da8e191794097c4bb2aa3fce411090e57af6385e61b97e09")
    version("0.2.9", sha256="a8dbddcd3d9af32ada7c6dc088d845588c513a29a0ba19ab9f64c5cd83692934")
    version("0.2.8", sha256="1f0f27a90f7ab66c423ba796529000fde9360d17b2d8e50097641ff405fc6f15")
    version("0.2.3", sha256="954c5b0a8b257c375e35d311c65fa62a210a3d65269195557de38418ac9f61f9")
    version("0.2.0", sha256="2f4e67e7914c95fb0cce766bab173eb2c5860ee420108fa183099557ac2e50e9")

    with default_args(type="build"):
        depends_on("py-setuptools@0.42:", when="@0.2.9:")
        depends_on("py-setuptools@0.6:")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@0.3.5:")
        depends_on("python@3.8:", when="@0.3.2:")
        depends_on("python@3.7:", when="@0.3.0:")
        depends_on("python@2.7:2.8,3.7:", when="@0.2.9")
        depends_on("python@2.7:2.8,3.6:", when="@0.2.8")
        depends_on("python@2.6:2.8,3.1:", when="@:0.2.5")

        depends_on("py-ppft@1.7.8:", when="@0.3.5:")
        depends_on("py-ppft@1.7.6.9:", when="@0.3.3:")
        depends_on("py-ppft@1.7.6.8:", when="@0.3.2:")
        depends_on("py-ppft@1.7.6.7:", when="@0.3.1:")
        depends_on("py-ppft@1.7.6.6:", when="@0.3.0:")
        depends_on("py-ppft@1.7.6.5:", when="@0.2.9:")
        depends_on("py-ppft@1.6.6.4:", when="@0.2.8:")
        depends_on("py-ppft@1.6.4.9:")

        depends_on("py-dill@0.4.1:", when="@0.3.5:")
        depends_on("py-dill@0.3.9:", when="@0.3.3:")
        depends_on("py-dill@0.3.8:", when="@0.3.2:")
        depends_on("py-dill@0.3.7:", when="@0.3.1:")
        depends_on("py-dill@0.3.6:", when="@0.3.0:")
        depends_on("py-dill@0.3.5.1:", when="@0.2.9:")
        depends_on("py-dill@0.3.4:", when="@0.2.8:")
        depends_on("py-dill@0.2.9:")

        depends_on("py-pox@0.3.7:", when="@0.3.5:")
        depends_on("py-pox@0.3.5:", when="@0.3.3:")
        depends_on("py-pox@0.3.4:", when="@0.3.2:")
        depends_on("py-pox@0.3.3:", when="@0.3.1:")
        depends_on("py-pox@0.3.2:", when="@0.3.0:")
        depends_on("py-pox@0.3.1:", when="@0.2.9:")
        depends_on("py-pox@0.3.0:", when="@0.2.8:")
        depends_on("py-pox@0.2.5:")

        depends_on("py-multiprocess@0.70.19:", when="@0.3.5:")
        depends_on("py-multiprocess@0.70.17:", when="@0.3.3:")
        depends_on("py-multiprocess@0.70.16:", when="@0.3.2:")
        depends_on("py-multiprocess@0.70.15:", when="@0.3.1:")
        depends_on("py-multiprocess@0.70.14:", when="@0.3.0:")
        depends_on("py-multiprocess@0.70.13:", when="@0.2.9:")
        depends_on("py-multiprocess@0.70.12:", when="@0.2.8:")
        depends_on("py-multiprocess@0.70.7:")

    def url_for_version(self, version):
        url = self.url.rsplit("/", 1)[0]
        if self.spec.satisfies("@0.2.2:0.2.5,0.2.9:"):
            url += "/pathos-{0}.tar.gz"
        else:
            url += "/pathos-{0}.zip"

        url = url.format(version)
        return url
