# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Cdi(AutotoolsPackage):
    """
    CDI is a C and Fortran Interface to access Climate and NWP model Data.
    Supported data formats are GRIB, netCDF, SERVICE, EXTRA and IEG.
    """

    homepage = "https://code.mpimet.mpg.de/projects/cdi"
    url = "https://gitlab.dkrz.de/mpim-sw/libcdi/-/archive/cdi-2.4.0/download.tar.gz"
    git = "https://gitlab.dkrz.de/mpim-sw/libcdi"

    version("2.5.4", sha256="605d4a9192e9657d87bdbe544e31c96b81890e9acdfc137ecc8581721ce5390f")
    version("2.5.3", sha256="e6a97e4af7a18afcc8caee13e2018c61e6885d871fd20441b51d7eae123c8305")
    version("2.5.1.1", sha256="922a62c85ea7b7445f13821ec69516ce36f8ef0965e5fa6e6e560db57f264763")
    version("2.5.1", sha256="639985873f82cd11d5cbfc121939e8d6ea24dc8454314845d5a7abd056878f59")
    version("2.5.0", sha256="511f5fd9414ef68e7f452a4114eae4a319dd8ff45f0e80ab07be2b16d35c79e9")
    version("2.4.3", sha256="b54e110feff209855cebf00751d5bb912ddf6f177bc1471a48a53ea751b982ab")
    version("2.4.0", sha256="f7e27fa067177d89ff95080705863025b9e8d2c5e660352c1e193a42bf3c6683")

    variant(
        "netcdf", default=True, description="This is needed to read/write NetCDF files with CDI"
    )

    with default_args(type="build"):
        depends_on("c")

        depends_on("autoconf")
        depends_on("automake")
        depends_on("libtool")

    depends_on("netcdf-c", when="+netcdf")

    # note:
    # starting from 2.5.1 the provided cmake config file looks for `cdi` instead of `libcdi`,
    # but autotools still builds `cdi`.
    # cmake build system is going to build `libcdi` in future releases.
    patch("cmake-config-libname.patch", when="@2.5.1: build_system=autotools")

    def configure_args(self):
        args = []
        if "+netcdf" in self.spec:
            args.append("--with-netcdf=" + self.spec["netcdf-c"].prefix)
        return args
