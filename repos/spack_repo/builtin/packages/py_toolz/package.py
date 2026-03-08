# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyToolz(PythonPackage):
    """A set of utility functions for iterators, functions, and dictionaries"""

    homepage = "https://github.com/pytoolz/toolz/"
    pypi = "toolz/toolz-0.9.0.tar.gz"

    license("BSD-3-Clause")

    version("1.1.0", sha256="27a5c770d068c110d9ed9323f24f1543e83b2f300a687b7891c1a6d56b697b5b")  # FIXME
    version("1.0.0", sha256="2c86e3d9a04798ac556793bced838816296a2f085017664e4995cb40a1047a02")  # FIXME
    version("0.12.1", sha256="ecca342664893f177a13dac0e6b41cbd8ac25a358e5f215316d43e2100224f4d")  # FIXME
    version("0.12.0", sha256="88c570861c440ee3f2f6037c4654613228ff40c93a6c25e0eba70d17282c6194")
    version("0.9.0", sha256="929f0a7ea7f61c178bd951bdae93920515d3fbdbafc8e6caf82d752b9b3b31c9")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.5:", type=("build", "run"), when="@0.11.0:")
