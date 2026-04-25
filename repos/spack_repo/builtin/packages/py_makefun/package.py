# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMakefun(PythonPackage):
    """makefun helps you create functions dynamically, with the signature of
    your choice. It was largely inspired by decorator and functools, and
    created mainly to cover some of their limitations."""

    homepage = "https://smarie.github.io/python-makefun/"
    pypi = "makefun/makefun-1.16.0.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("1.16.0", sha256="e14601831570bff1f6d7e68828bcd30d2f5856f24bad5de0ccb22921ceebc947")

    depends_on("py-setuptools@39.2:71", type="build")
    depends_on("py-setuptools-scm", type="build")
