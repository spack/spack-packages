# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIpythonPygmentsLexers(PythonPackage):
    """Defines a variety of Pygments lexers for highlighting IPython code."""

    homepage = "https://github.com/ipython/ipython-pygments-lexers"
    pypi = "ipython_pygments_lexers/ipython_pygments_lexers-1.1.1.tar.gz"

    license("BSD-3-Clause")

    version("1.1.1", sha256="09c0138009e56b6854f9535736f4171d855c8c08a563a0dcd8022f78355c7e81")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-flit-core@3.2:3", type="build")

    depends_on("py-pygments", type=("build", "run"))
