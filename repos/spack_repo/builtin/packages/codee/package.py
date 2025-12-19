# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import tarfile

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Codee(Package):
    """Codee simplifies and accelerates code review and testing,
    making it easier for teams to create high-quality, efficient
    programs that meet industry standards. Codee identifies
    improvement opportunities and provides clear reports to guide
    both developers and managers in applying the right enhancements. 
    
    Codee consists of a formatter (Codee Formatter) and a static
    code analyzer (Codee Analyzer). The formatter is, with certain
    limitations, free to use after accepting the end user license
    agreement (EULA). Licensed users have access to all features
    of the formatter and to the static code analyzer."""

    homepage = "https://www.codee.com"
    # fake sha256, add correct one
    maintainers("climbfuji", "e2b09ec21660f01fecffb715e0120265216943f038d0e48a9868713e54f0zzzz")

    version("2025.4.4", sha256="ADDSHA256HERE")

    variant("accept-eula", default=False, description="Accept the EULA")

    # Licensing
    #FROM arm_forge license_required = False
    #FROM arm_forge license_comment = "#"
    #FROM arm_forge license_files = ["licences/Licence"]
    #FROM arm_forge license_vars = [
    #FROM arm_forge     "ALLINEA_LICENSE_DIR",
    #FROM arm_forge     "ALLINEA_LICENCE_DIR",
    #FROM arm_forge     "ALLINEA_LICENSE_FILE",
    #FROM arm_forge     "ALLINEA_LICENCE_FILE",
    #FROM arm_forge ]
    #FROM arm_forge license_url = "https://developer.arm.com/documentation/101169/latest/Use-Arm-Licence-Server"

    # TODO ADD CONFLICTS FOR ANYTHING ELSE THAN LINUX x86_64 here, or replace hardcoded linux-x86_64 below (2x)

    def url_for_version(self, version):
        return f"https://codee.com/release/codee-{version}-linux-x86_64.tar.gz"

    @run_before("install")
    def abort_without_eula_acceptance(self):
        install_example = "spack install codee +accept-eula"
        license_terms_path = os.path.join(self.stage.source_path, "license_terms")
        if not self.spec.variants["accept-eula"].value:
            raise InstallError(
                "\n\n\nNOTE:\nUse +accept-eula "
                + "during installation "
                + "to accept the license terms in:\n"
                + f"Formatter (free): {join_path(license_terms_path, "EULA_Formatter.txt")}}\n"
                + f"Formatter/Analyzer: {join_path(license_terms_path, "EULA.txt")}}\n"
                + f"                    {join_path(license_terms_path, "Third_Party_Licenses.txt")}}\n"
                + "Example: '{0}'\n".format(install_example)
            )

    def install(self, spec, prefix):
        codee_tar = tarfile.open(
                name=f"codee-{self.version}-linux-x86_64.tar.gz"
            )
        install_tree(self.install_dir[self.version.string], prefix)

    #def setup_run_environment(self, env: EnvironmentModifications) -> None:
    #    # Only PATH is needed for Codee.
    #    # Adding lib to LD_LIBRARY_PATH can cause conflicts with Forge's internal libs.
    #    env.clear()
    #    env.prepend_path("PATH", join_path(self.prefix, "bin"))
