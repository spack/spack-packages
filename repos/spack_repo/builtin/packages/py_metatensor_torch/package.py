# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatensorTorch(PythonPackage):
    """Torchscript bindings for metatensor"""

    homepage = "https://docs.metatensor.org"
    pypi = "metatensor-torch/metatensor_torch-0.7.5.tar.gz"

    import_modules = ["metatensor"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.7.6", sha256="bcc23b535e5b86c0d49096cbf73de67141896f4f14c114515d97b936a78353a1")
    version("0.7.5", sha256="d5180d90e9645d604d7e4817737298565d9d4a95aff7ad9e6407d3b9a5376b13")

    depends_on("py-vesin", type=("run", "build"))
    depends_on("py-torch@2.1:", type=("build", "run"))
    depends_on("py-metatensor-core@0.1.13:0.1", type=("build", "run"))

    # pyproject.toml
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    depends_on("cmake@3.16:", type="build")
