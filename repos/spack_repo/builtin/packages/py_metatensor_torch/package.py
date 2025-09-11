# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatensorTorch(PythonPackage):
    """Torchscript bindings for metatensor"""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-torch/metatensor_torch-0.7.5.tar.gz"

    import_modules = ["metatensor.torch"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.8.0", sha256="240ea8c37328f6bb61ec9f3e482131f0875c73166a0e349a8dd8b85204c58bd7")

    depends_on("py-vesin", type=("build", "run"))
    depends_on("py-torch@2.1:", type=("build", "run"))
    depends_on("py-metatensor-core@0.1.13:0.1", type=("build", "run"))

    # pyproject.toml
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    depends_on("cmake@3.16:", type="build")
