# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNflows(PythonPackage):
    """Normalizing flows implemented in PyTorch"""

    homepage = "https://github.com/bayesiains/nflows"
    pypi = "nflows/nflows-0.14.tar.gz"

    license("MIT")

    version("0.14", sha256="6299844a62f9999fcdf2d95cb2d01c091a50136bd17826e303aba646b2d11b55")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-matplotlib")
        depends_on("py-numpy")
        depends_on("py-tensorboard")
        depends_on("py-torch")
        depends_on("py-tqdm")
