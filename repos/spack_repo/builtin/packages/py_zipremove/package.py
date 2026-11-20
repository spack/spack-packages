# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyZipremove(PythonPackage):
    """This package extends the native zipfile module with remove-related capabilities."""

    homepage = "https://github.com/danny0838/zipremove"
    pypi = "zipremove/zipremove-0.10.0.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("0.10.0", sha256="3c5957c115447b54299d3a23128764b59c4558fc98c4b878ff2dbc5db8a62021")

    depends_on("py-setuptools@61.0:", type="build")

    depends_on("python@3.7:", type=("build", "run"))
