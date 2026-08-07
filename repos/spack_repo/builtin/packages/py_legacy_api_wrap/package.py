# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLegacyApiWrap(PythonPackage):
    """Legacy API wrapper."""

    homepage = "https://github.com/flying-sheep/legacy-api-wrap"
    pypi = "legacy_api_wrap/legacy_api_wrap-1.5.tar.gz"

    license("MPL-2.0")

    version("1.5", sha256="b41ba6532f3ebfe3a897a35a7f97dec3be04b92a450f6c2bcf89f1b91c9cadf2")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatch-docstring-description")
        depends_on("py-hatch-vcs")
        depends_on("py-hatchling")
