# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libheif(CMakePackage):
    """libheif is an HEIF and AVIF file format decoder and encoder."""

    homepage = "https://github.com/strukturag/libheif"
    url = "https://github.com/strukturag/libheif/archive/refs/tags/v1.12.0.tar.gz"

    license("LGPL-3.0-or-later")

    version("1.21.2", sha256="79996de959d28ca82ef070c382304683f5cdaf04cbe2953a74587160a3710a36")
    version("1.12.0", sha256="086145b0d990182a033b0011caadb1b642da84f39ab83aa66d005610650b3c65")

    variant("gdk-plugin", default=True, description="Build gdk-pixbuf plugin")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.13:", type="build")
    depends_on("gdk-pixbuf", when="+gdk-plugin")
    depends_on("jpeg")
    depends_on("libpng")

    def cmake_args(self):
        args = [
                self.define_from_variant("WITH_GDK_PIXBUF", "gdk-plugin"),
        ]
        return args
