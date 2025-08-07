# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesPyyaml(PythonPackage):
    """Typing stubs for PyYAML"""

    pypi = "types-PyYAML/types_pyyaml-6.0.12.20250516.tar.gz"

    license("Apache-2.0")

    version(
        "6.0.12.20250516",
        sha256="9f21a70216fc0fa1b216a8176db5f9e0af6eb35d2f2932acb87689d03a5bf6ba",
    )

    # pyproject.yaml in types-PyYAML/types_pyyaml-6.0.12.20250516.tar.gz
    depends_on("py-setuptools@77.0.3:", type="build")
