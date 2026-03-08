# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrimesh(PythonPackage):
    """Import, export, process, analyze and view triangular meshes"""

    homepage = "https://github.com/mikedh/trimesh"
    pypi = "trimesh/trimesh-2.38.10.tar.gz"

    license("MIT")

    version("4.11.2", sha256="30fbde5b8dd7c157e7ff4d54286cb35291844fd3f4d0364e8b2727f1b308fb06")
    version("4.10.1", sha256="2067ebb8dcde0d7f00c2a85bfcae4aa891c40898e5f14232592429025ee2c593")
    version("4.9.0", sha256="ad907a223867f614ef1598d85a4c978845f39365cb7ccc93fa5800901fba3ef9")
    version("4.8.3", sha256="d2a1974efccb0737a1faac14d69740c644bb6738a99c790c1df752fe72c2a759")
    version("4.7.4", sha256="8d242dfabd9bc4e99a4f0c75bf8c0a41fbb252924e3484b53a8b0096accb49e1")
    version("4.6.13", sha256="2950dd6c3c9c9948a652f7a2966319b47130467bbbf447b254e02b9d90c94f14")
    version("4.5.3", sha256="b1af60399f64f4715d744c5195754068bfeb98981b92feb0c15d016c99379f87")
    version("4.4.9", sha256="e9f54cb4ef70f9db49446cad3845b7a8043fc7d62d9192b241741f3fb0d813ac")
    version("4.3.2", sha256="1450dbd1aae8dd825eddd56c5a7d7d1b35cad7efc2c63d535e19569577c25916")
    version("4.2.4", sha256="6aeb201638587b46ff85dfacced8b81a9322977345ebfcae5d26a3cbfd496576")
    version("4.1.8", sha256="a06d147a3a947bef0e72049917f2e7fd00bbd0689f8871e4908e447a53c5fb40")
    version("4.0.10", sha256="36e33b1145e5d505b41f250f180c9e5432390e1b7808cbbfb9f50b28d5b46cdc")
    version("3.23.5", sha256="bdfd669eccc4b3faff2328200a49408cd5ecad9f19b6022c4adb554bbb3a2621")
    version("3.22.5", sha256="2e4df41d285b55205e89c95fc4952477b5b61dfbcbb19894758a9e6cb23ba2dc")
    version("3.21.7", sha256="c2d1addcf502522488890440dcdc4ed673c4df95d00e2a567ebc1229d0c186d1")
    version("3.20.2", sha256="ead4ab5a8be055311c7037a5505af0f04d6087288f994b040125bc9063d40613")
    version("3.19.4", sha256="bcfd4a8655482e59fa03475f8e73284ae213e145ea7661311309bf7807013888")
    version("3.18.3", sha256="955a01041af3ca1ad2991d85334c68f1424108e4a1c1a60eac8a5e030427efa3")
    version("3.17.1", sha256="025bb2fa3a2e87bdd6873f11db45a7ca19216f2f8b6aed29140fca57e32c298e")
    version("2.38.10", sha256="866e73ea35641ff2af73867c891d7f9b90c75ccb8a3c1e8e06e16ff9af1f8c64")

    variant(
        "easy",
        default=False,
        description="Install soft dependencies and unlock extra functionality",
    )

    depends_on("py-setuptools@40.8:", type="build")

    depends_on("py-chardet", type=("build", "run"), when="+easy")
    depends_on("py-colorlog", type=("build", "run"), when="+easy")
    depends_on("py-jsonschema", type=("build", "run"), when="+easy")
    depends_on("py-lxml", type=("build", "run"), when="+easy")
    depends_on("py-mapbox-earcut", type=("build", "run"), when="+easy")
    depends_on("py-msgpack", type=("build", "run"), when="+easy")
    depends_on("py-networkx", type=("build", "run"), when="+easy")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("pil", type=("build", "run"), when="+easy")
    depends_on("py-pycollada", type=("build", "run"), when="+easy")
    depends_on("py-pyglet@:1", type=("build", "run"), when="+easy")
    depends_on("py-requests", type=("build", "run"), when="+easy")
    depends_on("py-rtree", type=("build", "run"), when="+easy")
    depends_on("py-scipy", type=("build", "run"), when="+easy")
    depends_on("py-setuptools", type=("build", "run"), when="+easy")
    depends_on("py-shapely", type=("build", "run"), when="+easy")
    depends_on("py-svgpath", type=("build", "run"), when="+easy")
    depends_on("py-sympy", type=("build", "run"), when="+easy")
    depends_on("py-xxhash", type=("build", "run"), when="+easy")
