# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRioxarray(PythonPackage):
    """rasterio xarray extension."""

    homepage = "https://github.com/corteva/rioxarray"
    pypi = "rioxarray/rioxarray-0.4.1.post0.tar.gz"

    license("Apache-2.0")
    maintainers("adamjstewart")

    version("0.21.0", sha256="a292d96f4d6412c05ff09629b72523ae2e9c42598183f5e9c555fc368f867c0f")
    version("0.20.0", sha256="8bfc7e979edc7e30b4671d638a9be0e5a7d673dab2ea88e2445d3c7745599c02")
    version("0.19.0", sha256="7819a0036fd874c8c8e280447cbbe43d8dc72fc4a14ac7852a665b1bdb7d4b04")
    version("0.17.0", sha256="46c29938827fff268d497f7ae277077066fcfbac4e53132ed3d4e2b96455be62")
    version("0.16.0", sha256="a98ea9306739f119b63ffc2245f5d7d23ca1638b99c50ca282d932901f9272e8")
    version(
        "0.4.1.post0", sha256="f043f846724a58518f87dd3fa84acbe39e15a1fac7e64244be3d5dacac7fe62b"
    )

    variant("interp", default=False, when="@0.16:", description="Enable interpolation routines")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:", when="@0.20:")
        depends_on("python@3.10:", when="@0.16:")
        depends_on("py-packaging", when="@0.16:")
        depends_on("py-rasterio@1.4.3:", when="@0.19:")
        depends_on("py-rasterio@1.3:", when="@0.16:")
        depends_on("py-rasterio")
        depends_on("py-xarray@2024.7:2025.11", when="@0.19:")
        depends_on("py-xarray@2022.3:2025.11", when="@0.16:")
        depends_on("py-xarray@0.17:2025.11")
        depends_on("py-pyproj@3.3:", when="@0.16:")
        depends_on("py-pyproj@2.2:")
        depends_on("py-numpy@2:", when="@0.20:")
        depends_on("py-numpy@1.23:", when="@0.16:")

        depends_on("py-scipy", when="+interp")
        depends_on("py-scipy", when="@0.4")
