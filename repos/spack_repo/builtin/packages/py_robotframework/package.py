# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRobotframework(PythonPackage):
    """Cross-platform lib for process and system monitoring in Python."""

    homepage = "https://opencollective.com/psutil"
    url = "https://github.com/robotframework/robotframework/archive/v3.2.2.tar.gz"

    license("Apache-2.0")

    version("7.4.1", sha256="6fa65c2708f0d48dd7a05bea2dc96943d0e39fdac9b3eb7290e780200b2cec57")
    version("7.3.2", sha256="82e8bc68dea843a82e710c9b864535811e62bf6e03d3258d8cbb8c78eac30711")
    version("7.2.2", sha256="4581c3a0da0c655b629aa1b56e6ff69256abdfa7ab26ae49e52c264c61f175b0")
    version("7.1.1", sha256="8abeb82324d6e476297ed7d43d7d89518399c2404a26702cf9cac23548bf8a86")
    version("7.0.1", sha256="6c29b9d4e6e9bec36d88a38916eeb1b685f77a9507ffb2fc9ebb465265b5adb9")
    version("6.1.1", sha256="1045dc4482f16737f58686b659f2cd8a91750ecb1707389051ada075f79e9e32")
    version("6.0.2", sha256="a588f6e4b286494d5226bf496725b9092299e275dcccf1bc1cf415f3f7b32858")
    version("5.0.1", sha256="93a9a7504738d7493994c3a7f4f13b4591beb746a26cb141afdb0435909b9c81")
    version("4.1.3", sha256="cbf8efce3a00287154fb4b54d574f292fab3597a15af8eb1d39c7ce171f5c405")
    version("3.2.2", sha256="6b2bddcecb5d1c6198999e38aeaf4c0366542a5e7b5bd788c6a3a36b055d5ea2")
    version("3.2.1", sha256="9805faa0990125ff2c9689b673448d5f47e78470e7a8e95af1606a775fa8379f")

    depends_on("py-setuptools", type=("build", "run"))
