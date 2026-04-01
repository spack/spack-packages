# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyYtDlpEjs(PythonPackage):
    """External JavaScript for yt-dlp supporting many runtimes."""

    homepage = "https://github.com/yt-dlp/ejs"
    pypi = "yt_dlp_ejs/yt_dlp_ejs-0.3.1.tar.gz"

    license("Unlicense AND MIT AND ISC")

    version("0.4.0", sha256="3c67e0beb6f9f3603fbcb56f425eabaa37c52243d90d20ccbcce1dd941cfbd07")
    version("0.3.1", sha256="7f2119eb02864800f651fa33825ddfe13d152a1f730fa103d9864f091df24227")

    with default_args(type="build"):
        depends_on("py-hatchling@1.27:")
        depends_on("py-hatch-vcs")
        depends_on("npm")
