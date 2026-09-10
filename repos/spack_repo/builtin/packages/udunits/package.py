# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Udunits(AutotoolsPackage):
    """Automated units conversion"""

    homepage = "https://www.unidata.ucar.edu/software/udunits"
    url = "https://downloads.unidata.ucar.edu/udunits/2.2.28/udunits-2.2.28.tar.gz"

    maintainers("AlexanderRichert-NOAA")

    license("UCAR")

    # Unidata now only provides the latest version of each X.Y branch.
    # Older 2.2 versions have been deprecated accordingly but are still
    # available in the build cache.
    version("2.2.28", sha256="590baec83161a3fd62c00efa66f6113cec8a7c461e3f61a5182167e0cc5d579e")

    variant("shared", default=True, description="Build shared library")

    depends_on("c", type="build")  # generated

    depends_on("expat")

    @property
    def libs(self):
        return find_libraries(["libudunits2"], root=self.prefix, recursive=True, shared=True)

    def configure_args(self):
        return self.enable_or_disable("shared")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # We need to set UDUNITS2_XML_PATH so that udunits can find its default units file.
        env.set("UDUNITS2_XML_PATH", join_path(self.prefix.share.udunits, "udunits2.xml"))
