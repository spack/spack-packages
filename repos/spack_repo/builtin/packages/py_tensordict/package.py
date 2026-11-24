# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTensordict(PythonPackage):
    """TensorDict is a pytorch dedicated tensor container."""

    homepage = "https://github.com/pytorch/tensordict"

    url = "https://github.com/pytorch/tensordict/archive/refs/tags/v0.11.0.tar.gz"

    maintainers("LydDeb")

    license("BSD", checked_by="LydDeb")

    version("0.11.0", sha256="d16daee34649f0a5056e3647ad3d36a9ae31f42f06d57ef46c6b8e119c749177")

    with default_args(type="build"):
        depends_on("cxx")
        depends_on("c")
        depends_on("cmake@3.22:")
        depends_on("gmake")
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm")
        depends_on("py-wheel")
        depends_on("py-pybind11")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-torch")
        depends_on("py-numpy")
        depends_on("py-cloudpickle")
        depends_on("py-packaging")
        depends_on("py-importlib-metadata")
        depends_on("py-orjson", when="^python@:3.14")
        depends_on("py-pyvers@0.2.2:")
