# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBidict(PythonPackage):
    """The bidirectional mapping library for Python."""

    homepage = "https://github.com/jab/bidict"
    pypi = "bidict/bidict-0.23.1.tar.gz"

    license("MPL-2.0")

    version("0.23.1", sha256="03069d763bc387bbd20e7d49914e75fc4132a41937fa3405417e1a5a2d006d71")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@40.9:", type="build")
