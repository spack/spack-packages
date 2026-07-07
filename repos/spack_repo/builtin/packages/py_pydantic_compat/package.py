# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPydanticCompat(PythonPackage):
    """This package provides (unofficial) compatibility mixins and function
    adaptors for pydantic v1-v2 cross compatibility. It allows you to use
    either v1 or v2 API names, regardless of the pydantic version installed.
    (Prefer using v2 names when possible)."""

    homepage = "https://github.com/pyapp-kit/pydantic-compat"
    pypi = "pydantic_compat/pydantic_compat-0.1.2.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.1.2", sha256="c5c5bca39ca2d22cad00c02898e400e1920e5127649a8e860637f15566739373")

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-hatchling", type="build")

    depends_on("py-pydantic", type=("build", "run"))
