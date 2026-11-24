# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPylibjpeg(PythonPackage):
    """
    A Python framework for decoding JPEG and decoding/encoding DICOM RLE data,
    with a focus on supporting pydicom."""

    homepage = "https://github.com/pydicom/pylibjpeg"
    pypi = "pylibjpeg/pylibjpeg-2.1.0.tar.gz"

    license("MIT")

    version("2.1.0", sha256="2decda24982394533f16f1c6a17a6242f3391b95f69fac56c6a598a6b1362105")

    variant(
        "all",
        default=False,
        description="Support JPEG (libjpeg), JPEG 2000 (openjpeg) and Run-Length Encoding (RLE)",
    )

    with default_args(type="build"):
        depends_on("py-flit-core@3.2:3")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")

        depends_on("py-numpy")

        with when("+all"):
            depends_on("py-pylibjpeg-rle")
            depends_on("py-pylibjpeg-openjpeg")
            depends_on("py-pylibjpeg-libjpeg")
