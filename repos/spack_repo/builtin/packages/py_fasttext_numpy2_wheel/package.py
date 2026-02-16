# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFasttextNumpy2Wheel(PythonPackage):
    """Library for efficient text classification and representation
    learning, fixed for numpy 2 compatibility."""

    homepage = "https://github.com/hynky1999/Fasttext-np-2.0.0"
    pypi = "fasttext_numpy2_wheel/fasttext_numpy2_wheel-0.9.2.tar.gz"

    maintainers("thomas-bouvier")

    version("0.9.2", sha256="484bb7efb0d07c5b6235c8ab44d5e7ddcde5727a25dbc04d18175f777c1e799c")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@0.7:", type="build")
    depends_on("py-numpy@2:", type=("build", "run"))
    depends_on("py-pybind11@2.2:", type=("build", "run"))

    depends_on("cxx", type="build")
