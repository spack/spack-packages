# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAlbucore(PythonPackage):
    """High-performance image processing functions for deep learning and computer vision."""

    homepage = "https://github.com/albumentations-team/albucore"
    pypi = "albucore/albucore-0.1.6.tar.gz"

    license("MIT")

    version("0.1.6", sha256="0afdb9c4840bf060cab8c5b85ebf43c2df4de53c42013988a808aaba1ec0b5b1")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-numpy@1.24.4:", type=("build", "run"))
    depends_on("opencv@=4.9.0+contrib+python3+imgproc+photo", type=("build", "run"))
    depends_on("py-numkong@7.4.5:", type=("build", "run"))
    depends_on("py-stringzilla@3.10.4:", type=("build", "run"))

    import_modules = ["albucore"]
