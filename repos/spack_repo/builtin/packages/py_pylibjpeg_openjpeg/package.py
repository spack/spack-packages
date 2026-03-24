# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPylibjpegOpenjpeg(PythonPackage):
    """
    A Python wrapper for openjpeg, with a focus on use as a plugin for for
    pylibjpeg."""

    homepage = "https://github.com/pydicom/pylibjpeg-openjpeg"
    pypi = "pylibjpeg_openjpeg/pylibjpeg_openjpeg-2.5.0.tar.gz"

    license("MIT")

    version("2.5.0", sha256="e0ea4d9e59820b02c8437121ae65cc28e98d9e9150f4a6967f2c3ba805e7f873")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-poetry-core@1.8:1")
        depends_on("py-cython@3:")
        depends_on("py-setuptools")

        depends_on("cmake@3.5:")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@2")

        # version from release notes
        # https://github.com/pydicom/pylibjpeg-openjpeg/blob/v2.5.0/docs/changes/v2.5.0.rst
        depends_on("openjpeg@2.5.3:")
