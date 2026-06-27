# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRfc3987Syntax(PythonPackage):
    """Helper functions to syntactically validate strings according to RFC 3987."""

    homepage = "https://github.com/willynilly/rfc3987-syntax"
    pypi = "rfc3987_syntax/rfc3987_syntax-1.1.0.tar.gz"

    license("MIT")

    version("1.1.0", sha256="717a62cbf33cffdd16dfa3a497d81ce48a660ea691b1ddd7be710c22f00b4a0d")

    with default_args(type="build"):
        depends_on("py-hatchling")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")

        depends_on("py-lark@1.2.2:")
