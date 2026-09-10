# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPylibjpegRle(PythonPackage):
    """
    Python bindings for a fast RLE decoder/encoder, with a focus on use as a
    plugin for pylibjpeg."""

    homepage = "https://github.com/pydicom/pylibjpeg-rle"
    pypi = "pylibjpeg_rle/pylibjpeg_rle-2.2.0.tar.gz"

    license("MIT")

    version("2.2.0", sha256="1a37353afbdd6f67aa3c2007879fff8ca30a98552cab7ed7f2aa00725ea4bb27")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-maturin@1")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@2:")
