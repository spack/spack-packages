# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class TemplightTools(CMakePackage):
    """Supporting tools for the Templight Profiler"""

    homepage = "https://github.com/mikael-s-persson/templight-tools"
    git = "https://github.com/mikael-s-persson/templight-tools.git"

    license("GPL-3.0-only")

    version("develop", branch="master")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("cmake @2.8.7:")

    depends_on(
        "boost @1.56:1.88 +exception+filesystem+system+graph+program_options+test+container"
    )
