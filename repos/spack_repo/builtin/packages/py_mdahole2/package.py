# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMdahole2(PythonPackage):
    """
    A Python interface for the HOLE suite tools to analyze an ion channel pore
    or transporter pathway as a function of time or arbitrary order parameters.
    """

    homepage = "https://github.com/MDAnalysis/mdahole2"
    pypi = "mdahole2/mdahole2-0.5.0.tar.gz"

    maintainers("LydDeb")

    license("LGPL-2.1-only", checked_by="LydDeb")

    version("0.5.0", sha256="39150588b9bc07ebc176bac30d9c3b0bd25003e2e2eac24b622f2a10e5352a1f")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@40.9.0:", type="build")
    depends_on("py-versioningit", type="build")
    depends_on("py-mdanalysis@2.1.0:", type=("build", "run"))
