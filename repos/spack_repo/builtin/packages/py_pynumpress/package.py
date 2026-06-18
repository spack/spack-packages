# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPynumpress(PythonPackage):
    """A wrapper around the MSNumpress library for mass spectrometry numerical data compression."""

    homepage = "https://github.com/mobiusklein/pynumpress"
    pypi = "pynumpress/pynumpress-0.0.9.tar.gz"

    license("Apache-2.0")

    version("0.0.9", sha256="c0dafd7837cee64fc59eb5fc0f941a1324e631a2d5b2d6ac7e28becfd29bd86e")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy")
