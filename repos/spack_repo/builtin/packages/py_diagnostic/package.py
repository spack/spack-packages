# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDiagnostic(PythonPackage):
    """Present errors that contain causes better understand what happened."""

    homepage = "https://github.com/pradyunsg/diagnostic"
    pypi = "diagnostic/diagnostic-3.0.0.tar.gz"

    license("MIT")

    version("3.0.0", sha256="5c80d7f77706dca775cc85d7b0492e4e96385dade2103052cf06cf6ab105b855")

    depends_on("py-flit-core@3.2:3", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-rich")
        depends_on("py-markdown-it-py")
        depends_on("py-docutils")
