# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class P3dfft3(AutotoolsPackage):
    """P3DFFT++ (a.k.a. P3DFFT v. 3) is a new generation of P3DFFT library
    that aims to provide a comprehensive framework for simulating multiscale
    phenomena. It takes the essence of P3DFFT further by creating an
    extensible, modular structure uniquely adaptable to a greater range
    of use cases."""

    homepage = "https://www.p3dfft.net"
    url = "https://github.com/sdsc/p3dfft.3/archive/refs/tags/v3.0.0.tar.gz"
    git = "https://github.com/sdsc/p3dfft.3.git"

    version("develop", branch="master")
    version(
        "3.1.2",
        sha256="c487393eab301ca0ad0c6f69ddaade59f3eed437222fb7f85ed7b23ce5eea5f1",
        url="https://github.com/sdsc/p3dfft.3/archive/refs/tags/v.3.1.2.tar.gz",
    )
    version(
        "3.1.1",
        sha256="85becdd05bb0ba84802cd1932f34ad44299487f83f92f08c58ad15a2615a3797",
        url="https://github.com/sdsc/p3dfft.3/archive/refs/tags/v.3.1.1.tar.gz",
    )
    version("3.1.0", sha256="39c8d60083a6c9cd7e043135544057bdff5fe41475d44afc11c3b9c9a397b5d4")
    version("3.0.1", sha256="65791f6385d80d99f7ec164f53f491acd64f7819862a4b0fba22bd7c198f0b50")
    version("3.0.0", sha256="1c549e78097d1545d18552b039be0d11cdb96be46efe99a16b65fd5d546dbfa7")

    variant("fftw", default=True, description="Builds with FFTW library")
    variant("essl", default=False, description="Builds with ESSL library")
    variant("mpi", default=True, description="Enable MPI support.")
    variant(
        "measure",
        default=False,
        description="Define if you want to use the measure fftw planner flag",
    )
    variant(
        "estimate",
        default=False,
        description="Define if you want to use the estimate fftw planner flag",
    )
    variant(
        "patient",
        default=False,
        description="Define if you want to use the patient fftw planner flag",
    )

    # TODO: Add more configure options!

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("mpi", when="+mpi")
    depends_on("fftw", when="+fftw")
    depends_on("essl", when="+essl")

    def configure_args(self):
        args = []

        if "%gcc" in self.spec:
            args.append("--enable-gnu")
            args.append("CFLAGS=-Wno-error=implicit-int")
            args.append("FCFLAGS=-fallow-argument-mismatch")

        if "%intel" in self.spec:
            args.append("--enable-intel")

        if "%xl" in self.spec:
            args.append("--enable-ibm")

        if "%cce" in self.spec:
            args.append("--enable-cray")

        if "+mpi" in self.spec:
            args.append("CC=%s" % self.spec["mpi"].mpicc)
            args.append("CXX=%s" % self.spec["mpi"].mpicxx)
            args.append("FC=%s" % self.spec["mpi"].mpifc)

        if "+openmpi" in self.spec:
            args.append("--enable-openmpi")

        if "+fftw" in self.spec:
            args.append("--enable-fftw")

            if "@:3.0.0" in self.spec:
                args.append("--with-fftw-lib=%s" % self.spec["fftw"].prefix.lib)
                args.append("--with-fftw-inc=%s" % self.spec["fftw"].prefix.include)
            else:
                args.append("--with-fftw=%s" % self.spec["fftw"].prefix)

            if "fftw+measure" in self.spec:
                args.append("--enable-fftwmeasure")
            if "fftw+estimate" in self.spec:
                args.append("--enable-fftwestimate")
            if "fftw+patient" in self.spec:
                args.append("--enable-fftwpatient")

        if "+essl" in self.spec:
            args.append("--enable-essl")
            args.append("--with-essl-lib=%s" % self.spec["essl"].prefix.lib)
            args.append("--with-essl-inc=%s" % self.spec["essl"].prefix.include)

        if "+mkl" in self.spec:
            args.append("--enable-mkl")
            args.append("--with-mkl-lib=%s" % self.spec["mkl"].prefix.lib)
            args.append("--with-mkl-inc=%s" % self.spec["mkl"].prefix.include)

        return args
