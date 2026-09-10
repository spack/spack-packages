# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPylibjpegLibjpeg(PythonPackage):
    """
    A Python wrapper for libjpeg, with a focus on use as a plugin for for pylibjpeg.
    """

    homepage = "https://github.com/pydicom/pylibjpeg-libjpeg"
    pypi = "pylibjpeg_libjpeg/pylibjpeg_libjpeg-2.4.0.tar.gz"

    license("GPL-3.0-or-later")

    version("2.4.0", sha256="2798ca404a8834447efefa89a03563ce93abdbe4146ea35901680f975959f501")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-poetry-core@1.8:1")
        depends_on("py-cython@3:")
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@2")
