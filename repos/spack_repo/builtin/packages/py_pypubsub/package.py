# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPypubsub(PythonPackage):
    """Python Publish-Subscribe Package"""

    homepage = "https://github.com/schollii/pypubsub"
    pypi = "pypubsub/pypubsub-4.0.7.tar.gz"

    supplier = "Oliver Schoenborn<oliver.schoenborn@gmail.com>"

    license("BSD-2-Clause", checked_by="mr-c")

    version("4.0.7", sha256="ec8b5cb147624958320e992602380cc5d0e4b36b1c59844d05e425a3003c09dc")

    depends_on("python@3.7:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@68:76")
        depends_on("py-setuptools-scm@7")
