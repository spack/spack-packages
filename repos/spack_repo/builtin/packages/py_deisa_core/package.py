# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeisaCore(PythonPackage):
    """Core Deisa tools and utilities."""

    homepage = "https://github.com/deisa-project/deisa-core"
    pypi = "deisa-core/deisa-core-0.2.0.tar.gz"

    version("0.2.0", sha256="94df0fdbdaf1c48df82adc1b72c1fdea6c68dc65cb99f080f535886a8235cfb6")

    depends_on("py-setuptools", type="build")
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
