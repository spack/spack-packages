# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *

class PyMetatensorTorch(PythonPackage):
    """Torchscript bindings for metatensor"""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-core/metatensor_core-0.1.14.tar.gz"

    import_modules = ["metatensor"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    extends("python")
    depends_on("python@3.9:")
    depends_on("py-numpy", type=("run", "build"))
    depends_on("py-vesin", type=("run", "build"))
    depends_on("py-torch@2.6:", type=("build", "run"))
    depends_on("libmetatensor@0.1.14:0.1", type=("build", "run"))

    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    depends_on("cmake@3.16:", type="build")
