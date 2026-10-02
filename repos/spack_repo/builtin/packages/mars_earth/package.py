# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class MarsEarth(PythonPackage):
    """Pure Python MARS implementation with a Rust-backed runtime core."""

    homepage = "https://github.com/edithatogo/mars"
    pypi = "mars_earth/mars_earth-1.0.4.tar.gz"

    license("Apache-2.0")

    version("1.0.4", sha256="0755aa79c879e06bb83d5e2811435c20e4f81623e1ddd8451b528cd8fe6d7972")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-numpy@1.20:")
        depends_on("py-scipy@1.10:")
        depends_on("py-scikit-learn@1.0:")
        depends_on("py-matplotlib@3.4:")

    depends_on("py-maturin@1.8:", type="build")
    depends_on("rust", type="build")
