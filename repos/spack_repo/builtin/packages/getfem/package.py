# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Getfem(AutotoolsPackage):
    """GetFEM is an open source library for solving potentially coupled systems
    of linear and nonlinear partial differential equations with the finite
    element method. It works in arbitrary dimension and allows to couple 1D,
    2D and 3D problems. GetFEM is interfaced with Python, Scilab, Octave and
    Matlab scripting languages.
    """

    homepage = "https://getfem.org"
    url = "http://download-mirror.savannah.gnu.org/releases/getfem/stable/getfem-5.4.4.tar.gz"

    maintainers("CodingYayaToure")

    license("LGPL-3.0-or-later")

    version("5.4.4", sha256="52795d577953cd1a96bb9e55fdf426bf6a042f59b08c02accf2726d2476ce4dd")

    variant("python", default=False, description="Build the Python interface")
    variant("mumps", default=False, description="Enable MUMPS sparse solver support")
    variant("mpi", default=False, description="Enable MPI parallel support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("blas")
    depends_on("lapack")

    depends_on("python@3:", when="+python")
    depends_on("py-numpy", when="+python")

    depends_on("mumps", when="+mumps")
    depends_on("mpi", when="+mpi")

    def configure_args(self):
        args = ["--with-pic"]

        if "+python" in self.spec:
            args.append("--enable-python")
        else:
            args.append("--disable-python")

        if "+mumps" in self.spec:
            args.append("--enable-mumps")

        if "+mpi" in self.spec:
            args.append("--enable-mpi")

        return args
