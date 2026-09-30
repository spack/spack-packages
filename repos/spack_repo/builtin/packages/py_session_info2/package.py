# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySessionInfo2(PythonPackage):
    """Print versions of imported packages."""

    homepage = "https://github.com/flying-sheep/session-info2"
    pypi = "session_info2/session_info2-0.4.2.tar.gz"

    license("MPL-2.0")

    version("0.4.2", sha256="d85d730621d6f75df60e15dad21258f2750f04c0c0ee5958a7bf92342c039d76")

    depends_on("python@3.12:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-hatch-vcs")
        depends_on("py-hatch-docstring-description")
