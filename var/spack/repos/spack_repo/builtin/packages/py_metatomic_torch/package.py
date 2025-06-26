# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *

class PyMetatomicTorch(PythonPackage):
    """Torchscript bindings for metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    url = "https://github.com/metatensor/metatomic/releases/download/metatomic-torch-v0.1.2/metatomic_torch-0.1.2.tar.gz"
    git = "https://github.com/metatensor/metatomic.git"
    pypi = "metatomic-torch/metatomic-torch-0.1.2.tar.gz"

    import_modules = ["metatomic.torch"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    extends("python")
    depends_on("python@3.9:")
    depends_on("py-numpy", type=("run", "build"))
    depends_on("py-vesin", type=("run", "build"))
    depends_on("py-torch@2.6:", type=("build", "run"))
    depends_on("libmetatensor@0.7.0:0.8.0", type=("build", "run"))
    # >=0.3.0 and <0.4.0
    depends_on("py-metatensor-operations@0.3:0.4.0", type="run", when="@0.3:")
    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    depends_on("cmake@3.16", type="build")
