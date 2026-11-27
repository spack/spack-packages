# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAgentDetector(PythonPackage):
    """Detect AI coding agents from their execution environment or User-Agent."""

    homepage = "https://github.com/patrick91/agent-detector"
    pypi = "agent_detector/agent_detector-2.0.0.tar.gz"

    license("MIT")

    version("2.0.0", sha256="19c8ae185dbdca23c24abdcd8ac2cf58b8e84dc284c6f6db536656601f9ffc3f")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
