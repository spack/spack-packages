# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Generalbrokenlines(CMakePackage):
    """Advanced track fitting: A trajectory based on General Broken Lines is a
    track refit to add the description of multiple scattering to an initial
    trajectory based on the propagation in a magnetic field (and average energy
    loss)."""

    homepage = "https://github.com/GeneralBrokenLines/GeneralBrokenLines"
    url = "https://github.com/GeneralBrokenLines/GeneralBrokenLines/archive/refs/tags/V04-00-00.tar.gz"
    git = "https://github.com/GeneralBrokenLines/GeneralBrokenLines.git"

    license("LGPL-2.0-only", checked_by="paulgessinger")

    version("main", branch="main")
    version("04-00-06", sha256="e14fa97daf16834999f0b9764b2041da3a0510c15f6304874fc2df48e197b420")
    version("04-00-05", sha256="d3e574b1838a9d28d52ce0b206c73ec8dc57e5a3b81257571e39556d0d18bb82")
    version("04-00-04", sha256="040c0d8425d89f735967cf312780e0f56f36f714eaf105c2a63dbd7ea2ce19b7")
    version("04-00-03", sha256="b2f18f396dca5a9b9c27fa7b7962cd433e8a6ae5d7869a9a8e0e4010f48fd37b")
    version("04-00-01", sha256="69e75cc58d27a93f03553e1cbaa982afeba6229d42db4ae640a2c4af0011179d")
    version("04-00-00", sha256="136d73f9c7d31de110af6eb4dd3329afdd1a9ff1befb3b85b94aaac1395ff6f0")

    patch("cmake-dependencies.patch", when="@4.0.0")

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
