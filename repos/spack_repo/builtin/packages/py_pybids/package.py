# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPybids(PythonPackage):
    """bids: interface with datasets conforming to BIDS"""

    homepage = "https://github.com/bids-standard/pybids"
    pypi = "pybids/pybids-0.13.1.tar.gz"

    license("MIT")

    version("0.22.0", sha256="98e7957e47c08d3c131de6f6cef629d009abce888849102b33820ca6a9930152")
    version("0.20.0", sha256="a68b577426942e50e6ac37e011463361d00a378d19b75df817619450357ebbb6")
    version("0.16.3", sha256="10e279350c8d14ca602c0d4469a5e4bf7ff393e8643c831a546ae735b6b82cc3")
    version("0.16.1", sha256="1a6ab06d375f3b783e738826e6d220b2f4145419b4b02f4edbcc8cb7c9b2208a")
    version("0.15.3", sha256="4d99c979bc4bc209cff70a02d1da309c9bf8c6b0338e2a0b66ebea77c7f3c461")
    version("0.15.1", sha256="0253507a04dbfea43eb1f75a1f71aab04be21076bfe96c004888000b802e38f2")
    version("0.14.0", sha256="73c4d03aad333f2a7cb4405abe96f55a33cffa4b5a2d23fad6ac5767c45562ef")
    version("0.13.2", sha256="9692013af3b86b096b5423b88179c6c9b604baff5a6b6f89ba5f40429feb7a3e")
    version("0.13.1", sha256="c920e1557e1dae8b671625d70cafbdc28437ba2822b2db9da4c2587a7625e3ba")
    version("0.9.5", sha256="0e8f8466067ff3023f53661c390c02702fcd5fe712bdd5bf167ffb0c2b920430")
    version("0.8.0", sha256="fe60fa7d1e171e75a38a04220ed992f1b062531a7452fcb7ce5ba81bb6abfdbc")

    with default_args(type="build"):
        depends_on("py-setuptools", when="@0.15.6:")
        depends_on("py-setuptools@30.3:60,61.0.1:", when="@:0.15.5")
        depends_on("py-versioneer+toml", when="@0.15.6:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.21:")
        depends_on("python@3.9:", when="@0.18:")
        depends_on("python@3.8:", when="@0.16:")

        depends_on("py-numpy@1.25:", when="@0.22:")
        depends_on("py-numpy@1.23:", when="@0.19:")
        depends_on("py-numpy@1.19:", when="@0.16:")
        depends_on("py-numpy")

        depends_on("py-scipy@1.11:", when="@0.22:")
        depends_on("py-scipy@1.9:", when="@0.19:")
        depends_on("py-scipy@1.5:", when="@0.16:")
        depends_on("py-scipy")

        depends_on("py-nibabel@5.1:", when="@0.22:")
        depends_on("py-nibabel@4:", when="@0.18:")
        depends_on("py-nibabel@3:", when="@0.16:")
        depends_on("py-nibabel@2.1:")

        depends_on("py-pandas@2:", when="@0.21:")
        depends_on("py-pandas@1.5:", when="@0.19:")
        depends_on("py-pandas@0.25.2:", when="@0.16:")
        depends_on("py-pandas@0.23:")

        depends_on("py-formulaic@0.3:", when="@0.19:")
        depends_on("py-formulaic@0.2.4:0.5", when="@0.15.6:0.18")
        depends_on("py-formulaic@0.2.4:0.3", when="@0.15.1:0.15.5")
        depends_on("py-formulaic@0.2.4:0.2", when="@0.14:0.15.0")

        depends_on("py-sqlalchemy@1.4.31:", when="@0.19:")
        depends_on("py-sqlalchemy@1.3.16:", when="@0.16:")
        depends_on("py-sqlalchemy@:1.3", when="@0.12.4:0.15")
        depends_on("py-sqlalchemy")

        depends_on("py-bids-validator@1.14.7:", when="@0.18:")
        depends_on("py-bids-validator@1.11:", when="@0.16:")
        depends_on("py-bids-validator")

        depends_on("py-bidsschematools@1.1:", when="@0.22:")

        depends_on("py-num2words@0.5.10:", when="@0.19:")
        depends_on("py-num2words@0.5.5:", when="@0.16:")
        depends_on("py-num2words")

        depends_on("py-click@8:", when="@0.15.2:")
        depends_on("py-click", when="@0.12.1:")

        depends_on("py-universal-pathlib@0.2.2:", when="@0.17:")
        depends_on("py-frozendict@2.3:", when="@0.19:")

        # Historical dependencies
        depends_on("py-patsy", when="@:0.13")
