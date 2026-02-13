# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySetuptoolsCpp(PythonPackage):
    """Simplified packaging for pybind11-based C++ extensions"""

    homepage = "https://github.com/dmontagu/setuptools-cpp"
    pypi = "setuptools_cpp/setuptools_cpp-0.1.0.tar.gz"

    maintainers("dorton")

    license("MIT")

    version("0.1.0", sha256="4fd5e08603237578d06d28efd592d9847b523ede3e502f660be44b1e6254674d")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "run"))
    depends_on("cxx", type="build")
