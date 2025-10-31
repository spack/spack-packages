# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySimpervisor(PythonPackage):
    """
    simpervisor provides the SupervisedProcess class that provides async methods
    start, ready, terminate, and kill to manage it.
    """

    homepage = "https://github.com/jupyterhub/simpervisor"
    pypi = "simpervisor/simpervisor-0.4.tar.gz"

    license("BSD-3-Clause")

    version("1.0.0", sha256="7eb87ca86d5e276976f5bb0290975a05d452c6a7b7f58062daea7d8369c823c1")
    version("0.4", sha256="cec79e13cdbd6edb04a5c98c1ff8d4bd9713e706c069226909a1ef0e89d393c5")

    depends_on("python@3.8:", type="build", when="@1:")
    depends_on("py-hatchling", type="build", when="@1:")

    # Historical dependencies
    depends_on("py-setuptools", type="build", when="@:0")
