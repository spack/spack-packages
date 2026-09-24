# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXarrayEinstats(PythonPackage):
    """Stats, linear algebra and einops for xarray."""

    homepage = "https://einstats.python.arviz.org/"
    pypi = "xarray_einstats/xarray_einstats-0.11.0.tar.gz"
    git = "https://github.com/arviz-devs/xarray-einstats.git"

    license("Apache-2.0")

    version("0.11.0", sha256="69f48a60f62151d40c49fd6d9a6dc0b970aecef2813a33209e4dcde897fca48b")
    version("0.8.0", sha256="7f1573f9bd4d60d6e7ed9fd27c4db39da51ec49bf8ba654d4602a139a6309d7f")

    depends_on("python@3.12:", when="@0.11.0", type=("build", "run"))
    depends_on("python@3.10:", when="@0.8.0", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-flit-core@3.4:3")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@2:", when="@0.11.0")
        depends_on("py-scipy@1.14:", when="@0.11.0")
        depends_on("py-xarray@2024.07.0:", when="@0.11.0")

        depends_on("py-numpy@1.23:", when="@0.8.0")
        depends_on("py-scipy@1.9:", when="@0.8.0")
        depends_on("py-xarray@2022.9:", when="@0.8.0")
