# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyArvizBase(PythonPackage):
    """Base ArviZ features and converters."""

    homepage = "https://arviz-base.readthedocs.io/"
    pypi = "arviz_base/arviz_base-1.3.0.tar.gz"
    git = "https://github.com/arviz-devs/arviz-base.git"

    license("Apache-2.0")

    version("1.3.0", sha256="285fe0ac413f515d1962644b471d916327446d58247ae7f331043b1bed5a4d5b")

    depends_on("python@3.12:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-flit-core@3.4:3")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@2:")
        depends_on("py-xarray@2024.11.0:")
        depends_on("py-typing-extensions@3.10:")
        depends_on("py-lazy-loader@0.4:")
