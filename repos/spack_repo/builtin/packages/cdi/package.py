# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *

# Note:
# download links are in the form
# https://code.mpimet.mpg.de/attachments/download/29309/cdi-2.4.0.tar.gz
# and this maps versions to resource identifiers used internally (e.g. 29309 in the url above)
# so that `url_for_version` can compose the right url for each version.
RESOURCE_ID = {
    "2.4.0": 29309,
    "2.4.3": 29658,
    "2.5.0": 29833,
    "2.5.1": 29860,
    "2.5.1.1": 29871,
    "2.5.3": 30033,
}


class Cdi(AutotoolsPackage):
    """
    CDI is a C and Fortran Interface to access Climate and NWP model Data.
    Supported data formats are GRIB, netCDF, SERVICE, EXTRA and IEG.
    """

    homepage = "https://code.mpimet.mpg.de/projects/cdi"
    url = "https://code.mpimet.mpg.de/attachments/download/29309/cdi-2.4.0.tar.gz"

    version("2.5.3", sha256="1ebf6098b195c0bb13614015b62a63efd2ef3d4ee94f4c69cadcf236854b2303")
    version("2.5.1.1", sha256="a78c577324eb99ef461e90f717b75a1843304ac6613ebd168fdad12f84d78539")
    version("2.5.1", sha256="7e369ed455d153bfbfcb5abd343779dc254b798b0d5ea641cd497a49e39f4de5")
    version("2.5.0", sha256="19654af187d8b29e708b1c7e4726143cf26547966dceba8cc5b68690281ddad9")
    version("2.4.3", sha256="7bf3df83968e15d718857a4823c0bae7d9c16ea17ca95524e1e5b68ab73d2c0d")
    version("2.4.0", sha256="91fca015b04c6841b9eab8b49e7726d35e35b9ec4350922072ec6e9d5eb174ef")

    variant(
        "netcdf", default=True, description="This is needed to read/write NetCDF files with CDI"
    )

    depends_on("netcdf-c", when="+netcdf")

    def url_for_version(self, version):
        return "https://code.mpimet.mpg.de/attachments/download/{}/cdi-{}.tar.gz".format(
            RESOURCE_ID[str(version)], version
        )

    def configure_args(self):
        args = []
        if "+netcdf" in self.spec:
            args.append("--with-netcdf=" + self.spec["netcdf-c"].prefix)
        return args
