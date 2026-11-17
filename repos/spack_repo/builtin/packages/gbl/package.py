# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gbl(CMakePackage):
    """General Broken Lines: Advanced track fitting library"""

    homepage = "https://millepede.pages.desy.de/general-broken-lines/"
    git = "https://gitlab.desy.de/millepede/general-broken-lines"
    url = "https://gitlab.desy.de/millepede/general-broken-lines/-/archive/V04-00-08/general-broken-lines-V04-00-08.tar.gz"

    tags = ["hep"]

    version("main", branch="main")
    version("04-00-08", sha256="e70c0ce60f2b7c14568a6598b3b6d6fff263de4dfa37ec4422e8f3b970081437")
    version("03-01-04", sha256="67b3756b74bcd61c47a4a30108f28f86eaa0fe9afeb0d240c253d332f3a989b0")
    version("02-04-01", commit="1061b643c6656fbf7ceba579997eb43f0a9e9d3c")
    version("02-01-03", commit="8acaade19c20e9ef23d1244a555fead6ef149c33")

    depends_on("cxx", type="build")  # generated
    depends_on("c", type="build", when="@:04-00-00")  # generated
    depends_on("fortran", type="build")  # generated

    variant("root", default=True, description="Support ROOT for user I/O")
    depends_on("eigen", type=("build", "link"))
    depends_on("root", type=("build", "link"), when="+root")
    depends_on("mille", when="@04-00-00:")
    depends_on("mille +root", when=("@04-00-00: +root"))

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        eigen_inc = self.spec["eigen"].prefix.include.eigen3
        args = [
            self.define("EIGEN3_INCLUDE_DIR", eigen_inc),
            self.define_from_variant("SUPPORT_ROOT", "root"),
        ]
        return args
