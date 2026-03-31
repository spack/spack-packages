# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

class Panoplyj(Package):
    """Panoply netCDF, HDF and GRIB Data Viewer"""


    homepage = "https://www.giss.nasa.gov/tools/panoply/"
    url = "https://www.giss.nasa.gov/tools/panoply/download/PanoplyJ-5.9.1.tgz"

    maintainers("Chrismarsh")

    # this is a custom license and not SPDX listed
    license("LicenseRef-NASA-GISS-Panoply", checked_by="Chrismarsh")

    version("5.9.1", sha256="3f019b37f278cd77a5cd5d67494a8eb4ec9beda9e1f9a86de3a221cdae5a2c27")

    # only distributed as jar files
    depends_on("java", type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)

        if self.spec.satisfies("platform=darwin"):
            install("panoply_macos.sh", prefix.bin)
            rename( join_path(prefix.bin,"panoply_macos.sh"), join_path(prefix.bin,"panoply"))
        else:
            install("panoply.sh", prefix.bin)
            rename( join_path(prefix.bin,"panoply.sh"), join_path(prefix.bin,"panoply"))

        install_tree("jars", prefix.bin.jars)
