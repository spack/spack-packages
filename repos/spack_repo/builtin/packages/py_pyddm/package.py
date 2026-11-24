# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyddm(PythonPackage):
    """Generalized drift diffusion modeling for Python."""

    homepage = "https://github.com/mwshinn/PyDDM"
    pypi = "pyddm/pyddm-0.9.0.tar.gz"

    license("MIT")

    version("0.9.0", sha256="98b971de5dcb4e490d4f72c631d9f12f9584cdabeddbb466656cf0f45fe27ffd")

    with default_args(type="build"):
        depends_on("c")

        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.6:")

        depends_on("py-numpy@1.9.2:")
        depends_on("py-scipy@0.16:")
        depends_on("py-matplotlib")
        depends_on("py-paranoid-scientist@0.2.3:")
        depends_on("py-pandas")
