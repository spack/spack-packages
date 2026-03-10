# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGemmi(PythonPackage):
    """Library for structural biology."""

    homepage = "https://github.com/project-gemmi/gemmi"
    pypi = "gemmi/gemmi-0.7.1.tar.gz"

    maintainers("LydDeb")

    license("MPL-2.0", checked_by="LydDeb")

    version("0.7.1", sha256="73bb4a2c574ef7586efdf0161aae22bb75c0301af5e9cc22252877e707facdd2")
    version("0.6.7", sha256="5c0809329ba8a9711fdb1655d13c14e226828933e33e8816091a09d3f0ce35ce")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.15:3.22", type="build")

    depends_on("python@3.8:3.10", type=("build", "run"), when="@0.7.1:")
    depends_on("python@3.7:", type=("build", "run"), when="@0.6.7")
    depends_on("py-scikit-build-core@0.11.1:0.11", type=("build", "run"), when="@0.7.1:")
    depends_on("py-scikit-build-core@0.10.5:0.10", type=("build", "run"), when="@0.6.7")
    depends_on("py-nanobind@2.4:", type=("build", "run"), when="@0.7.1:")
    depends_on("py-pybind11@2.6.2:", type=("build", "run"), when="@0.6.7:0.6")
    depends_on("py-pybind11-stubgen@2.5.1:2.5", type=("build", "run"), when="@0.6.7")
    depends_on("py-typing-extensions@4.0:", type=("build", "run"), when="@0.7.1")
    depends_on("py-numpy", type=("build", "run"), when="@0.6.7")
