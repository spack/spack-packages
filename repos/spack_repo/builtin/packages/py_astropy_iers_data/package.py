# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAstropyIersData(PythonPackage):
    """IERS Earth rotation and leap second table

    Note: This package is not meant for standalone purposes
    but is needed by AstroPy."""

    homepage = "https://github.com/astropy/astropy-iers-data"
    pypi = "astropy-iers-data/astropy_iers_data-0.2024.4.29.0.28.48.tar.gz"

    version(
        "0.2025.10.27.0.39.10",
        sha256="2a0630f810bcba7978cc5f3f92a45910b5ea95d885302b1879b0132e920302ed",
    )
    version(
        "0.2025.9.29.0.35.48",
        sha256="0a7841c9a0ff41e2abafcde984cb6b271cdfd9cb5b13e01d5ddd0ed2e8fc4065",
    )
    version(
        "0.2025.4.28.0.37.27",
        sha256="840efbe7085a20ab1fe3a93bf5eeba28fcb4a0fc4196cbcc1b06d51a182accb0",
    )
    version(
        "0.2025.3.10.0.29.26",
        sha256="dd4865861f00dec8a442ef8135f034675a7b05f17846562e2ea71678f5dbaa97",
    )
    version(
        "0.2024.5.20.0.29.40",
        sha256="7fff3d3404ae8560533ac0e685db7acc02c4d8984faa4ac3d607096879fba2d1",
    )
    version(
        "0.2024.4.29.0.28.48",
        sha256="a2d5acf97e731f1d4a0eab1c8e4c7f454ddc166af06797b141202dd901bd1dfc",
    )

    depends_on("python@3.8:")
    depends_on("py-hatchling", when="@0.2025.6.9.14.9.37:", type="build")
    depends_on("py-hatch-vcs", when="@0.2025.6.9.14.9.37:", type="build")
    depends_on("py-setuptools", when="@:0.2025.6.0.39.3", type="build")
    depends_on("py-setuptools-scm", when="@:0.2025.6.0.39.3", type="build")
    depends_on("py-wheel", when="@:0.2025.6.0.39.3", type="build")
