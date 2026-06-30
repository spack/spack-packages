# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTermcolor(PythonPackage):
    """ANSII Color formatting for output in terminal."""

    pypi = "termcolor/termcolor-1.1.0.tar.gz"

    license("MIT")

    version("3.3.0", sha256="348871ca648ec6a9a983a13ab626c0acce02f515b9e1983332b17af7979521c5")
    version("3.1.0", sha256="6a6dd7fbee581909eeec6a756cff1d7f7c376063b14e4a298dc4980309e55970")
    version("1.1.0", sha256="1d6d69ce66211143803fbc56652b41d73b4a400a2891d7bf7a1cdf4c02de613b")

    depends_on("python@3.10:", type=("build", "run"), when="@3.2:")
    depends_on("python@3.9:", type=("build", "run"), when="@2.5:")

    with default_args(type="build"):
        with when("@3:"):
            depends_on("py-hatch-vcs")
            depends_on("py-hatchling@1.27:")
        with when("@:1"):
            depends_on("py-setuptools")
