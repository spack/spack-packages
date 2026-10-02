# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCons(PythonPackage):
    """An implementation of Lisp/Scheme-like cons in Python."""

    homepage = "https://github.com/pythological/python-cons"
    pypi = "cons/cons-0.4.7.tar.gz"

    license("LGPL-3.0-only")

    version("0.4.7", sha256="0a96cd2abd6a9f494816c1272cf5583a960041750c2d7a48eeeccd47ce369dfd")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("py-logical-unification@0.4:", type=("build", "run"))
