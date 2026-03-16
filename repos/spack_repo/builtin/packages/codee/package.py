# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform
import sys

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
    url = "https://codee.com/release/codee-2025.4.6-linux-x86_64.tar.gz"

    maintainers("climbfuji")

    version("2025.4.6", sha256="39985b33b42621c17c4b79e37267fa8528de6702dfcde6bc330e114f25575f98")
    version("2025.4.5", sha256="42688ec4214270da59da365ba054d1cbf744cb30593542d6d1e04c26e90bcb14")
    version("2025.4.4", sha256="764bc109945561192c386c080d5359f3faa96f06d0a0b52de0f9064cbbf2799a")

    conflicts("platform=darwin", msg="Codee is not supported on Darwin platforms")

    # Licensing
    license_required = False
    license_url = "https://www.codee.com/pricing"

    def url_for_version(self, version):
        target = None
        suffix = None
        if sys.platform == "linux":
            suffix = "tar.gz"
            if platform.machine() == "aarch64":
                target = "linux-arm64"
            elif platform.machine() == "x86_64":
                target = "linux-x86_64"
        elif sys.platform == "win32":
            suffix = "zip"
            if platform.machine() == "AMD64":
                target = "windows-amd64"
        if not target:
            return None
        return f"https://codee.com/release/codee-{version}-{target}.{suffix}"

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)
