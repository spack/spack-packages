# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypingInspection(PythonPackage):
    """Runtime typing introspection tools"""

    homepage = "https://typing-inspection.pydantic.dev/latest/"
    pypi = "typing_inspection/typing_inspection-0.4.2.tar.gz"

    license("MIT", checked_by="RMeli")

    version("0.4.2", sha256="ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464")

    # pyproject.toml
    depends_on("py-hatchling@1.27.0:", type="build")
    depends_on("py-typing-extensions@4.12.0:", type=("build", "run"))
