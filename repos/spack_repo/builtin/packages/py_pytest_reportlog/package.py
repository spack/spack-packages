# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestReportlog(PythonPackage):
    """Replacement for the --resultlog option, focused in simplicity and extensibility."""

    homepage = "https://github.com/pytest-dev/pytest-reportlog"
    pypi = "pytest_reportlog/pytest_reportlog-1.0.0.tar.gz"

    license("MIT")

    version("1.0.0", sha256="75aec3a92bb53456c3e028605a636579d26f31c6f1e035ad9f706c203cfcb74e")

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-hatch-vcs")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")

        depends_on("py-pytest")
