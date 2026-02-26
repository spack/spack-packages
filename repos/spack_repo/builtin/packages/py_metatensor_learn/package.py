# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatensorLearn(PythonPackage):
    """Building blocks for the atomistic machine learning models based on PyTorch and NumPy"""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-learn/metatensor_learn-0.0.0.tar.gz"

    import_modules = ["metatensor.learn"]

    maintainers("HaoZeke", "Luthaf", "RMeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.4.0", sha256="78ab06157075d754789bf2c048fb2e2cbf75806bd0ef87f8191eae8cb9a4ef23")
    version("0.3.2", sha256="987f63228888882a6189137ddb89f913b2fde1072c3caa83a39b9f5d50388b51")

    # pyproject.toml
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@0.4.0:")
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    # setup.py
    depends_on("py-metatensor-operations@0.3", type=("build", "run"), when="@0.3.2")
    depends_on("py-metatensor-operations@0.4", type=("build", "run"), when="@0.4.0:")
