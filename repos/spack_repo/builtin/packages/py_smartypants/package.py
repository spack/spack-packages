# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySmartypants(PythonPackage):
    """smartypants is a Python fork of SmartyPants."""

    homepage = "https://github.com/leohemsted/smartypants.py"
    pypi = "smartypants/smartypants-2.0.2.tar.gz"

    license("BSD-3-Clause")

    version("2.0.2", sha256="39d64ce1d7cc6964b698297bdf391bc12c3251b7f608e6e55d857cd7c5f800c6")
    version(
        "2.0.1",
        sha256="b98191911ff3b4144ef8ad53e776a2d0ad24bd508a905c6ce523597c40022773",
        # PyPI only has the wheel
        url="https://github.com/leohemsted/smartypants.py/archive/refs/tags/v2.0.1.tar.gz",
    )

    depends_on("py-setuptools", type="build")
