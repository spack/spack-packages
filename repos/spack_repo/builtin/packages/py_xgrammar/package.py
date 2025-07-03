# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXgrammar(PythonPackage):
    """Fast, Flexible and Portable Structured Generation"""

    pypi = "xgrammar/xgrammar-0.1.18.tar.gz"

    license("Apache-2.0")

    version("0.1.18", sha256="a0438a0f9262fff1d0e4f184268eb759f094243edce92b67eb7aa5f245c47471")

    depends_on("py-pydantic", type=["build", "run"])
    depends_on("py-transformers@4.38.0:", type=["build", "run"])
    depends_on("py-torch@1.10.0:", type=["build", "run"])
    depends_on("py-triton", type=["build", "run"])
    depends_on("py-scikit-build-core@0.10.0:", type="build")
    depends_on("py-nanobind@2.5.0", type="build")
    depends_on("ninja", type=["build"])

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        python_ver = self.spec["python"].version.up_to(2)
        env.set(
            "nanobind_DIR",
            join_path(
                self.spec["py-nanobind"].prefix.lib,
                f"python{python_ver}",
                "site-packages",
                "nanobind",
                "cmake",
            ),
        )
