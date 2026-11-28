# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCramjam(PythonPackage):
    """Thin Python bindings to de/compression algorithms in Rust."""

    homepage = "https://github.com/milesgranger/cramjam"
    pypi = "cramjam/cramjam-2.11.0.tar.gz"

    license("MIT", checked_by="wdconinc")

    version("2.14.0", sha256="050095380dc01a7f3dc2b8bcd9de2cbf4a208a8aab32301c760ea3c280d641bd")
    version("2.11.0", sha256="5c82500ed91605c2d9781380b378397012e25127e89d64f460fea6aeac4389b4")

    depends_on("c", type="build")
    depends_on("rust@1.85:", when="@2.14:", type="build")
    depends_on("rust", type="build")
    depends_on("py-maturin@1.8.2:", when="@2.13:", type="build")
    depends_on("py-maturin@0.14:", type="build")
    depends_on("python@3.11:", when="@2.12:", type=("build", "run"))
    depends_on("python@:3.14", when="@:2.11", type=("build", "run"))
