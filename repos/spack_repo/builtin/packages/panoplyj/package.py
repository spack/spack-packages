# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Panoplyj(Package):
    """Panoply netCDF, HDF and GRIB Data Viewer"""

    homepage = "https://www.giss.nasa.gov/tools/panoply/"
    url = "https://www.giss.nasa.gov/tools/panoply/download/PanoplyJ-5.9.2.tgz"

    maintainers("Chrismarsh")

    # this is a custom license and not SPDX listed
    license("LicenseRef-NASA-GISS-Panoply", checked_by="Chrismarsh")

    # only the most recent is valid
    version("5.9.2", sha256="7cf68f77f6456e56573b0336c877973c852ffdbc46007922f636de1b61d37242")

    # only distributed as jar files
    depends_on("java", type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)

        if self.spec.satisfies("platform=darwin"):
            install("panoply_macos.sh", prefix.bin)
            rename(join_path(prefix.bin, "panoply_macos.sh"), join_path(prefix.bin, "panoply"))
        else:
            install("panoply.sh", prefix.bin)
            rename(join_path(prefix.bin, "panoply.sh"), join_path(prefix.bin, "panoply"))

        install_tree("jars", prefix.bin.jars)
