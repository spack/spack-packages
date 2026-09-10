# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAntipickle(PythonPackage):
    """Like pickle. But different."""

    homepage = "https://pypi.org/project/antipickle"
    pypi = "antipickle/antipickle-0.2.0.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("0.2.0", sha256="361f37beacfa54081b20af54afaeb0420c7b12a3b3e4c932e083b07f9d3e7143")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-msgpack@1.0.4:", type=("build", "run"))
