# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatensorOperations(PythonPackage):
    """Operations to manipulate metatensor data types."""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-operations/metatensor_operations-0.3.3.tar.gz"

    import_modules = ["metatensor.operations"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.3.3", sha256="432d267ce1f3c5ee11994d5348e70bc517a3c19ef68982af7bb470463e3c1b6b")

    extends("python@3.9:")
    variant("torch", default=False, description="With PyTorch")

    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    depends_on("py-metatensor-core@0.1.13:0.1", type=("build", "run"))
