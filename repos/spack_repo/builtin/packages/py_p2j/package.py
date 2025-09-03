# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyP2j(PythonPackage):
    """p2j: Convert Python scripts to Jupyter notebook with minimal intervention"""

    homepage = "https://github.com/raibosome/python2jupyter"
    pypi = "p2j/p2j-1.3.2.tar.gz"

    license("MIT", checked_by="mll8777")

    version("1.3.2", sha256="6a492350953a87ceaf190b13141242f604b597efd668c2b026241c4a4f4777f5")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.6:", type=("build", "run"))
