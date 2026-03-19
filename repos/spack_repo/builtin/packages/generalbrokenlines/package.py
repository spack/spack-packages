# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install generalbrokenlines
#
# You can edit this file again by typing:
#
#     spack edit generalbrokenlines
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Generalbrokenlines(CMakePackage):
    """Advanced track fitting: A trajectory based on General Broken Lines is a
    track refit to add the description of multiple scattering to an initial
    trajectory based on the propagation in a magnetic field (and average energy
    loss)."""

    homepage = "https://gitlab.desy.de/millepede/general-broken-lines"
    url = "https://gitlab.desy.de/millepede/general-broken-lines/-/archive/V04-00-00/general-broken-lines-V04-00-00.tar.gz"
    git = "https://gitlab.desy.de/millepede/general-broken-lines.git"

    license("LGPL-2.0-only", checked_by="paulgessinger")

    version("main", branch="main")
    version("04-00-00", sha256="ac2818cd7b8f84cb75c721521320f6c85ff8423bcf9b6be6d2bfee6e205a07db")

    variant("root", default=False, description="Enable ROOT support")

    _cxxstd_values = ["17", "20", "23"]
    variant(
        "cxxstd",
        default="20",
        values=_cxxstd_values,
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("mille")
    depends_on("eigen@2.91:")

    for cxxstd in _cxxstd_values:
        depends_on(f"root cxxstd={cxxstd}", when=f"+root cxxstd={cxxstd}")

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        args = [
            self.define_from_variant("SUPPORT_ROOT", "root"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ]

        return args
