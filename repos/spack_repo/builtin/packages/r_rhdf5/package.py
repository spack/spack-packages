# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRhdf5(RPackage):
    """R Interface to HDF5.

    This package provides an interface between HDF5 and R. HDF5's main
    features are the ability to store and access very large and/or complex
    datasets and a wide variety of metadata on mass storage (disk) through a
    completely portable file format. The rhdf5 package is thus suited for
    the exchange of large and/or complex datasets between R and other
    software package, and for letting R applications work on datasets that
    are larger than the available RAM."""

    bioc = "rhdf5"

    with default_args(get_full_repo=True):
        version("2.56.0", commit="cef3c44c71c0f51dbd651d44f9d784581c0b7ba0")  # bioc 3.23
        version("2.52.1", commit="f8211976d6f0438546c704565ae85bba914c3c61")  # bioc 3.21
        version("2.44.0", commit="0f6e367ca9e97c37c683cd0f97c06732a67146f0")  # bioc 3.17
        version("2.42.0", commit="fa26027d57b5b6d1c297446d9bbed74d5710c5d2")
        version("2.40.0", commit="fb6c15a3199f3ffd746fb9a381d574d17fef45a2")  # bioc 3.15
        version("2.38.0", commit="f6fdfa807f5cd5a4d11d4aa6ebfaa81c118b4c3f")
        version("2.34.0", commit="ec861b81fc6962e844bf56b7549ba565a7e4c69c")
        version("2.28.1", commit="e230fa34d6f3e97dd4e6065115675baf5e8213bb")
        version("2.26.2", commit="81e11258db493661a19cf83e142b690ecac4e6cf")
        version("2.24.0", commit="e926e8ce4e77082781afb943324a1e6745385b48")
        version("2.22.0", commit="4431bdc0a2bcbb8086ee08a0f2300129b808d1be")
        version("2.20.0", commit="37b5165325062728bbec9167f89f5f4b794f30bc")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("r@4.0.0:", type=("build", "run"), when="@2.38.0:")
    depends_on("r@3.5.0:", type=("build", "run"), when="@2.26.2:")

    depends_on("r-rhdf5filters@1.15.5:", type=("build", "run"), when="@2.47.7:")
    depends_on("r-rhdf5filters", type=("build", "run"), when="@2.34.0:")

    depends_on("r-rhdf5lib@1.33.3:", when="@2.56.0:")
    depends_on("r-rhdf5lib@1.13.4:", when="@2.38.0:")
    depends_on("r-rhdf5lib@1.11.0:", when="@2.34.0:")
    depends_on("r-rhdf5lib@1.3.2:", when="@2.26.2:")
    depends_on("r-rhdf5lib", when="@2.24.0:")

    depends_on("gmake", type="build")

    depends_on("zlib-api")

    # Historical dependencies

    depends_on("r-s4vectors", type=("build", "run"), when="@2.45.1:2.47.0")
    depends_on("r-zlibbioc", type=("build", "run"), when="@:2.28.1")

    # > error: 'H5O_info2_t' has no member named 'addr'
    conflicts("^r-rhdf5lib@2:", when="@:2.54")

    # > error: subscripted value is neither array nor pointer nor vector
    conflicts("^r@4.6:", when="@2.24:2.50")

    # Linking fails due to incompatible format of Rhdf5lib::pkgconfig output
    conflicts("^r-rhdf5lib@1.12:", when="@2.26")

    # > error: 'H5F_LIBVER_18' undeclared
    conflicts("^r-rhdf5lib@1.4:", when="@2.24")

    # > error: passing argument 2 of 'H5Iget_name' from incompatible pointer type
    conflicts("%gcc@14:", when="@2.20:2.22")

    def flag_handler(self, name, flags):
        # > error: conflicting types for '_h5fileLock'; have 'struct SEXPREC *(struct SEXPREC *)'
        # > note: previous declaration of '_h5fileLock' with type 'struct SEXPREC *(void)'

        if self.spec.satisfies("@:2.46 %gcc@13:"):
            if name == "cflags":
                flags.append("-std=gnu17")

        return (flags, None, None)
