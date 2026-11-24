# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJplephem(PythonPackage):
    """This package can load and use a Jet Propulsion Laboratory (JPL)
    ephemeris for predicting the position and velocity of a planet or other
    Solar System body."""

    pypi = "jplephem/jplephem-2.9.tar.gz"

    license("MIT")

    version("2.24", sha256="354fe1adae022264ab46f18afb6af26211277cfd7b3ef90400755fcabe93bc11")
    version("2.17", sha256="e1c6e5565c4d00485f1063241b4d1eff044585c22b8e97fad0ff2f6efb8aaa27")
    version("2.9", sha256="9dffb9f3d3f6d996ade875102431fe385e8ea422da25c8ba17b0508d9ca1282b")

    # pip silently replaces distutils with setuptools
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
