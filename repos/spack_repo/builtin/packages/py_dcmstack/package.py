# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDcmstack(PythonPackage):
    """Stack DICOM images into volumes and convert to Nifti."""

    homepage = "https://github.com/moloney/dcmstack"
    pypi = "dcmstack/dcmstack-0.9.0.tar.gz"

    license("MIT")

    version("0.9.0", sha256="9e131226fb00cdc72f5c2ad61f82b37020d3f97f272d1becb880168bd4504860")

    depends_on("python@3.8:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools")

    # from src/dcmstack/info.py
    with default_args(type=("build", "run")):
        depends_on("py-pydicom@0.9.7:")
        depends_on("py-nibabel@2.5.1:")
        depends_on("py-pylibjpeg-libjpeg", when="^python@3.7:")
