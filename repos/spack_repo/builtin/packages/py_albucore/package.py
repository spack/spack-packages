# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAlbucore(PythonPackage):
    """High-performance image processing functions for deep learning and computer vision."""

    homepage = "https://github.com/albumentations-team/albucore"
    pypi = "albucore/albucore-0.0.24.tar.gz"

    license("MIT")

    version("0.0.24", sha256="f2cab5431fadf94abf87fd0c89d9f59046e49fe5de34afea8f89bc8390253746")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@45:", type="build")
    depends_on("py-numpy@1.24.4:", type=("build", "run"))
    depends_on("py-typing-extensions@4.9:", type=("build", "run"), when="^python@:3.9")
    depends_on("py-stringzilla@3.10.4:", type=("build", "run"))
    depends_on("py-simsimd@5.9.2:", type=("build", "run"))
    depends_on("opencv@4.9.0.80:+python3+contrib", type=("build", "run"))
