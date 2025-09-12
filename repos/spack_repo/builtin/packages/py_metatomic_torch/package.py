# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatomicTorch(PythonPackage):
    """Torchscript bindings for metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    pypi = "metatomic-torch/metatomic-torch-0.1.2.tar.gz"

    import_modules = ["metatomic.torch"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.4", sha256="c593bbc0fa3a410bd19d4a4a8d0008d5bd1c31a9faaca85b9d6b655ee1133bde")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-vesin", type=("build", "run"))
    depends_on("py-torch@2.1:", type=("build", "run"))
    depends_on("py-metatensor-torch@0.8", type=("build", "run"))
    # >=0.3.0 and <0.4.0
    depends_on("py-metatensor-operations@0.3", type=("build", "run"))
    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    # CMakeLists.txt
    depends_on("cmake@3.16:", type="build")
