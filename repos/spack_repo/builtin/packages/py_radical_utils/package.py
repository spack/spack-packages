# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRadicalUtils(PythonPackage):
    """RADICAL-Utils contains shared code and tools for various
    RADICAL-Cybertools packages."""

    homepage = "https://radical-cybertools.github.io"
    git = "https://github.com/radical-cybertools/radical.utils.git"
    pypi = "radical_utils/radical_utils-1.91.1.tar.gz"

    maintainers("andre-merzky")

    license("MIT")

    version("develop", branch="devel")
    version("1.91.1", sha256="5293f375f699161e451982b2e7668613c24e2562252f65e765ebbc83d8ae0118")

    depends_on("py-colorama", type=("build", "run"))
    depends_on("py-msgpack", type=("build", "run"))
    depends_on("py-netifaces", type=("build", "run"))
    depends_on("py-ntplib", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))
    depends_on("py-regex", type=("build", "run"))
    depends_on("py-setproctitle", type=("build", "run"))
    with default_args(type="build"):
        depends_on("py-setuptools")
