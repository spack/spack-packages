# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBackportsZstd(PythonPackage):
    """Backport of compression.zstd (PEP 784)."""

    homepage = "https://github.com/rogdham/backports.zstd"
    pypi = "backports_zstd/backports_zstd-1.3.0.tar.gz"

    license("PSF-2.0")

    version("1.3.0", sha256="e8b2d68e2812f5c9970cabc5e21da8b409b5ed04e79b4585dbffa33e9b45ebe2")
    version("1.0.0", sha256="8e99702fd4092c26624b914bcd140d03911a16445ba6a74435b29a190469cce3")

    depends_on("python@3.9:3.13", type=("build", "run"))
    depends_on("py-setuptools@80:", type="build")
    depends_on("zstd", type=("build", "link", "run"))
