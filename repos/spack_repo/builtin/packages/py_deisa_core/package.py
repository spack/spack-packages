# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeisaCore(PythonPackage):
    """Core Deisa tools and utilities."""

    homepage = "https://github.com/deisa-project/deisa-core"
    pypi = "deisa_core/deisa_core-0.2.0.tar.gz"

    version("0.2.0", sha256="94df0fdbdaf1c48df82adc1b72c1fdea6c68dc65cb99f080f535886a8235cfb6")
    version("0.1.0", sha256="d907728d4a2acf0345d3e7b69cbf534678ab93c3cfa39f4040e7455a6f552718")

    depends_on("py-setuptools", type="build")
    depends_on("py-dask", type=("build", "run"), when="@0.2.0:")
    depends_on("py-numpy", type=("build", "run"), when="@0.2.0:")
