# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFitsio(PythonPackage):
    """A python package for FITS input/output wrapping cfitsio"""

    homepage = "https://github.com/esheldon/fitsio"
    pypi = "fitsio/fitsio-1.2.6.tar.gz"

    license("GPL-2.0-or-later", checked_by="lgarrison")

    version("1.2.6", sha256="33b0cdbc53f1779e3d0a765d5ab474baf6c86eccf7c21375a07671f7b09b33af")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("cfitsio@4.4.1:", type=("build", "link", "run"))

    def setup_build_environment(self, env):
        env.set("FITSIO_USE_SYSTEM_FITSIO", "1")
