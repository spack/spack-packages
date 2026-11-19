# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gbl(CMakePackage):
    """General Broken Lines: Advanced track fitting library"""

    homepage = "https://millepede.pages.desy.de/general-broken-lines/"
    git = "https://gitlab.desy.de/millepede/general-broken-lines"
    url = "https://github.com/GeneralBrokenLines/GeneralBrokenLines/archive/refs/tags/V04-00-08.tar.gz"

    tags = ["hep"]

    version("main", branch="main")
    version("04-00-08", sha256="7243542f43d5950513c62e39c4a0e1a76fc94ae534a84748d808f3a277bbd43d")
    version("03-01-04", sha256="ba7926d9a79a60aa8b5eb812ba950e0b3df36b6d96b667cdddb5515d3d91f0b3")
    version("02-04-01", commit="dcd972fbf246248e3010610400f80486748f96c0dc399011ebdb7efd1fd44c81",
    deprecated=True)
    version("02-01-03", commit="d54049a2cad6ead3e65d5e2639edf338dbcd9408103ec93c4716de33b63691e6",
    deprecated=True)

    depends_on("cxx", type="build")  # generated
    depends_on("c", type="build", when="@:04-00-00")
    depends_on("fortran", type="build")  # generated

    variant("root", default=True, description="Support ROOT for user I/O")
    depends_on("eigen", type=("build", "link"))
    depends_on("root", type=("build", "link"), when="+root")
    depends_on("mille", when="@04-00-00:")
    depends_on("mille +root", when="@04-00-00: +root")

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        eigen_inc = self.spec["eigen"].prefix.include.eigen3
        args = [
            self.define("EIGEN3_INCLUDE_DIR", eigen_inc),
            self.define_from_variant("SUPPORT_ROOT", "root"),
        ]
        return args
