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
    version("0.0.24", sha256="f2cab5431fadf94abf87fd0c89d9f59046e49fe5de34afea8f89bc8390253746")

    depends_on("python@3.10:", type=("build", "run"), when="@0.0.34:")
    depends_on("python@3.9:", type=("build", "run"), when="@0.0.18:0.0.33")

    depends_on("py-hatchling", type="build", when="@0.1:")
    depends_on("py-setuptools@45:", type="build", when="@:0.0.41")

    depends_on("py-numpy@1.24.4:", type=("build", "run"))
    depends_on("py-stringzilla@3.10.4:", type=("build", "run"), when="@0.0.18:")

    depends_on("py-numkong@7.0.0:", type=("build", "run"), when="@0.1:0.1.3")
    depends_on("py-numkong@7.4.5:", type=("build", "run"), when="@0.1.4:")

    depends_on("py-simsimd@5.9.2:", type=("build", "run"), when="@0.0.20:0.0.41")
    depends_on("py-typing-extensions@4.9:", type=("build", "run"), when="@0.0.12:0.0.33 ^python@:3.9")
    depends_on("opencv@4.9.0:+python3+contrib", type=("build", "run"), when="@0.0.4:0.0.34")
