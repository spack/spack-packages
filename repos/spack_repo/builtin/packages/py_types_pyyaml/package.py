# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesPyyaml(PythonPackage):
    """This is a type stub package for the PyYAML package.
    It can be used by type checkers to check code that uses PyYAML."""

    homepage = "https://pypi.org/project/types-PyYAML/"
    pypi = "types_PyYAML/types_pyyaml-6.0.12.20250915.tar.gz"

    license("MIT")

    version(
        "6.0.12.20250915",
        sha256="0f8b54a528c303f0e6f7165687dd33fafa81c807fcac23f632b63aa624ced1d3",
    )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
