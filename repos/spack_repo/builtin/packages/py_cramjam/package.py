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

    version("2.11.0", sha256="5c82500ed91605c2d9781380b378397012e25127e89d64f460fea6aeac4389b4")

    depends_on("c", type="build")
    depends_on("rust", type="build")
    depends_on("py-maturin@0.14:", type="build")
