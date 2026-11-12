# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Sfcgal(CMakePackage):
    """
    SFCGAL is a C++ wrapper library around CGAL with the aim of supporting
    ISO 19107:2013 and OGC Simple Features Access 1.2 for 3D operations.
    It provides standard compliant geometry types and operations, that can be
    accessed from its C or C++ APIs.
    """

    homepage = "http://www.sfcgal.org/"
    url = "https://gitlab.com/sfcgal/SFCGAL/-/archive/v2.3.0/SFCGAL-v2.3.0.tar.gz"
    old_github_urlbase = "https://github.com/Oslandia/SFCGAL/archive/v{0}.tar.gz"  # up to 1.3.8

    license("LGPL-2.0-or-later")

    version("2.3.0", sha256="5f6aa1838e5ae31523ebf410cde0240b7a88d7e062b7ffff945e4fae2aaba0fa")
    version("2.2.0", sha256="bb6bb77ddb58523d8c229764de23699f99c1a7011d873419afd2a67df85602a2")

    with default_args(deprecated=True):
        version("1.5.1", sha256="ea5d1662fada7de715ad564dc810c3059024ed81ae393f5352489f706fdfa3b1")
        version("1.4.1", sha256="1800c8a26241588f11cddcf433049e9b9aea902e923414d2ecef33a3295626c3")
        version(
            "1.3.8",
            sha256="5154bfc67a5e99d95cb653d70d2b9d9293d3deb3c8f18b938a33d68fec488a6d",
            url=old_github_urlbase.format("1.3.8"),
        )
        version(
            "1.3.7",
            sha256="30ea1af26cb2f572c628aae08dd1953d80a69d15e1cac225390904d91fce031b",
            url=old_github_urlbase.format("1.3.7"),
        )

    variant("eigen", default=False, description="Enable Eigen support")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("cmake@2.8.6:")
        depends_on("nlohmann-json@3.11:", when="@2.3:")

    # Ref: https://oslandia.github.io/SFCGAL/installation.html, but starts to work @4.7:
    # Ref: https://gitlab.com/sfcgal/SFCGAL/-/blob/v1.5.1/NEWS?ref_type=tags
    # and looking at CMakeLists.txt find_package(CGAL) declaration
    # for different versions (around line 70)
    # @1.3.8:1.3.10 (from comments) cgal@4.3 is minimal, @4.13 recommended, @5 supported?
    depends_on("cgal +core")
    depends_on("cgal@4.7:4", when="@1.3.8")
    depends_on("cgal@4.7:5.1", when="@1.3.9")
    depends_on("cgal@4.7:5.2", when="@1.3.10")
    depends_on("cgal@5.6", when="@1.4:1.5")
    depends_on("cgal@5.6:6.0", when="@2.0:2.2")
    depends_on("cgal@5.6:6.2", when="@2.3")

    boost_variants = "boost+program_options+serialization+thread"
    depends_on(boost_variants, when="@2:")
    depends_on(boost_variants + "+chrono+filesystem+system+timer", when="@:1")

    depends_on("boost@1.84:1.89", when="@2.3:")
    depends_on("boost@1.84:1.88", when="@2:2.2")
    depends_on("boost@1.74:1.88", when="@1.5:1")
    depends_on("boost@1.54:1.88", when="@:1.4")
    conflicts("boost@1.81:1.83", msg="redefine errors with std::numeric_limits<__float128>")

    depends_on("mpfr@2.2.1:")
    depends_on("gmp@4.2:")
    depends_on("eigen", when="+eigen")

    @property
    def command(self):
        return Executable(self.prefix.bin.join("sfcgal-config"))

    def cmake_args(self):
        # It seems viewer is discontinued as of v1.3.0
        # https://github.com/Oslandia/SFCGAL/releases/tag/v1.3.0
        # Also, see https://github.com/Oslandia/SFCGAL-viewer
        args = []
        if self.spec.satisfies("+eigen"):
            args.append(self.define("SFCGAL_WITH_EIGEN", "ON"))
        if self.spec.satisfies("@1.3:1.5"):
            args.append(self.define("SFCGAL_BUILD_VIEWER", "OFF"))
        args.append(self.define("BUILD_SHARED_LIBS", "ON"))
        return args

    @property
    def libs(self):
        # Override because libs have different case than Spack package name
        name = "libSFCGAL*"
        # We expect libraries to be in either lib64 or lib directory
        for root in (self.prefix.lib64, self.prefix.lib):
            liblist = find_libraries(name, root=root, shared=True, recursive=False)
            if liblist:
                break
        return liblist
