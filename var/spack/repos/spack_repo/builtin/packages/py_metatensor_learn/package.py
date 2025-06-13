# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyMetatensorLearn(PythonPackage):
    """Building blocks for the atomistic machine learning models based on PyTorch and NumPy"""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-learn/metatensor_learn-0.3.2.tar.gz"

    import_modules = ["metatensor.learn"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.3.2", sha256="987f63228888882a6189137ddb89f913b2fde1072c3caa83a39b9f5d50388b51")
    extends("python@3.9:")
    variant("torch", default=False, description="With PyTorch")

    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    depends_on("py-pip@22.1:", type="build")
    depends_on("py-torch@2.6:", type="run", when="+torch")
    depends_on("py-numpy", type="run", when="+torch")
    # >=0.3.0 and <0.4.0
    depends_on("py-metatensor-operations@0.3:", type="run", when="@0.3:")
    conflicts("py-metatensor-operations@0.4.0:", when="@0.3:")
