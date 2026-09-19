# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPykdtree(PythonPackage):
    """pykdtree is a kd-tree implementation for fast nearest neighbour search in Python."""

    homepage = "https://github.com/storpipfugl/pykdtree"
    pypi = "pykdtree/pykdtree-1.4.3.tar.gz"

    license("LGPL-2.1-or-later")

    # Add the relevant versions and their SHA-256 checksums from PyPI
    version("1.4.3", sha256="d9187930ffb8c822c52595b64948b47346694ee2a49e2702420b58f743d786f5")

    # Build system backends
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")

    # Runtime and Link Dependencies
    depends_on("py-numpy@1.16:", type=("build", "run"))

    # OpenMP is required for multi-threaded queries
    depends_on("llvm-openmp", when="%apple-clang", type=("build", "link"))

    def install_options(self, spec, prefix):
        # Optional: Hand over specific compilation variables if building on macOS
        options = []
        if "%apple-clang" in spec:
            options.append("--build-option=--use-openmp")
        return options
