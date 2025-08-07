# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMicrosoftAurora(PythonPackage):
    """Implementation of the Aurora model."""

    homepage = "https://github.com/microsoft/aurora"
    pypi = "microsoft_aurora/microsoft_aurora-1.7.0.tar.gz"

    maintainers("adamjstewart")

    license("MIT")

    version("1.7.0", sha256="1c285f5b39e7f5f47f7dc11c5c4f16edb63998179141a4ee27e66ce4b764d0ba")

    with default_args(type="build"):
        depends_on("py-hatchling@1.8:")
        depends_on("py-hatch-vcs")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-torch")
        depends_on("py-einops")
        depends_on("py-timm")
        depends_on("py-huggingface-hub")
        depends_on("py-pydantic")
        depends_on("py-xarray")
        depends_on("py-netcdf4")
        depends_on("py-azure-storage-blob")
