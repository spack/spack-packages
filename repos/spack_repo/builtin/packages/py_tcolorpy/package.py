# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTcolorpy(PythonPackage):
    """tcolopy is a Python library to apply true color for terminal text."""

    homepage = "https://github.com/thombashi/tcolorpy"
    pypi = "tcolorpy/tcolorpy-0.1.7.tar.gz"

    license("MIT")

    version("0.1.7", sha256="0fbf6bf238890bbc2e32662aa25736769a29bf6d880328f310c910a327632614")

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")
