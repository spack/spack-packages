# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrameVtk(PythonPackage):
    """
    trame-vtk extend trame widgets with components that can interface with VTK and/or ParaView.
    """

    homepage = "https://kitware.github.io/trame/"
    pypi = "trame-vtk/trame_vtk-2.10.0.tar.gz"

    maintainers("LydDeb")

    license("BSD License")

    version("2.11.1", sha256="db1f316ba69c29b9292775c3f73567604aa366742c06030d8507d5bd56424492")
    version("2.10.0", sha256="0e4cabd78c1e8b67da857ba5c3a404a2195cb3e849a252bae51575291bef01ad")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-trame-client@3.4:3", type=("build", "run"))
