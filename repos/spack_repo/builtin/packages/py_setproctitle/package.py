# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySetproctitle(PythonPackage):
    """The setproctitle module allows a process to change its title (as
    displayed by system tools such as ps and top)."""

    homepage = "https://github.com/dvarrazzo/py-setproctitle"
    pypi = "setproctitle/setproctitle-1.1.10.tar.gz"

    license("BSD-3-Clause")

    version("1.3.6", sha256="c9f32b96c700bb384f33f7cf07954bb609d35dd82752cef57fb2ee0968409169")
    version("1.2.2", sha256="7dfb472c8852403d34007e01d6e3c68c57eb66433fb8a5c77b13b89a160d97df")
    version("1.1.10", sha256="6283b7a58477dd8478fbb9e76defb37968ee4ba47b05ec1c053cb39638bd7398")

    depends_on("c", type="build")  # generated

    depends_on("py-setuptools", type="build")
