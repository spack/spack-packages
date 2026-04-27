# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PodmanCompose(PythonPackage):
    """A container composition tool for Podman"""

    homepage = "https://podman.io"
    url = "https://github.com/containers/podman-compose/archive/refs/tags/v1.4.0.tar.gz"
    maintainers("scothalverson")
    license("Apache-2.0")
    version("1.4.0", sha256="167860361357f32e09660342756442ac6f9adf182f00ade1309b550de48ed494")
    depends_on("podman", type="run")
    depends_on("py-setuptools", type="build")
    depends_on("py-pyyaml")
    depends_on("py-python-dotenv")
