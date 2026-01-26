# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import platform
import sys
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
    limitations (free-form Fortran only), free to use after accepting
    the end user license agreement (EULA). Licensed users have access
    to all features of the formatter and to the static code analyzer."""

    homepage = "https://www.codee.com"

    maintainers("climbfuji")

    version("2025.4.6", sha256="39985b33b42621c17c4b79e37267fa8528de6702dfcde6bc330e114f25575f98")
    version("2025.4.5", sha256="42688ec4214270da59da365ba054d1cbf744cb30593542d6d1e04c26e90bcb14")
    version("2025.4.4", sha256="764bc109945561192c386c080d5359f3faa96f06d0a0b52de0f9064cbbf2799a")

    variant("accept-eula", default=False, description="Accept the EULA")

    def url_for_version(self, version):
        target = None
        if sys.platform=="linux":
            if platform.machine() == "aarch64":
                target = "linux-arm64"
            elif platform.machine() == "x86_64":
                target = "linux-x86_64"
        if not target:
            raise InstallError(f"Platform {sys.platform}/{platform.machine()} not supported or configured")
        return f"https://codee.com/release/codee-{version}-{target}.tar.gz"

    @run_before("install")
    def abort_without_eula_acceptance(self):
        install_example = "spack install codee +accept-eula"
        if not self.spec.variants["accept-eula"].value:
            spath = self.stage.source_path
            raise InstallError(
                "\n\n\nNOTE:\nUse +accept-eula during installation to accept "
                + "the license terms for the appropriate product in:\n"
                + f"Formatter (free): {join_path(spath, 'EULA_Formatter.txt')}\n"
                + f"Formatter/Analyzer: {join_path(spath, 'EULA.txt')}\n"
                + f"                    {join_path(spath, 'Third_Party_Licenses.txt')}\n"
                + f"Example: '{install_example}'\n"
                + "For the commercial (non-free) version of Codee, place your license "
                + "(codee.lic) in the installation directory or point the environment "
                + "variable CODEE_LICENSE_PATH to the location of the license file.\n"
            )

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
