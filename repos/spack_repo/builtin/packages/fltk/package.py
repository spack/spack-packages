# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Fltk(Package):
    """FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit for
    UNIX/Linux (X11), Microsoft Windows, and MacOS X. FLTK provides
    modern GUI functionality without the bloat and supports 3D
    graphics via OpenGL and its built-in GLUT emulation.

    FLTK is designed to be small and modular enough to be statically
    linked, but works fine as a shared library. FLTK also includes an
    excellent UI builder called FLUID that can be used to create
    applications in minutes.

    """

    homepage = "https://www.fltk.org/"
    url = "https://github.com/fltk/fltk/archive/refs/tags/release-1.3.3.tar.gz"
    git = "https://github.com/fltk/fltk.git"

    version("master", branch="master")
    version("1.4.4", sha256="cbf5f7846af596206e8e4489e14c9981f98d7b37168110a00dcd26d8d479a669")
    version("1.4.3", sha256="6a11c0bf91b7b193a87a1928c32a953f36d7dd4b65fef3e9d0c40a51882f97a6")
    version("1.3.7", sha256="019f65810fb0ea5acac14c852193e8f374e822e6a3034a3c80ed8676f6f3a090")
    version("1.3.3", sha256="186bdc4234bea74bce4d47f186d41d35bdd47d48dbe5f829513a2183fbf8f3b2")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("pkgconfig", type="build", when="@1.3.7")

    depends_on("libx11")
    depends_on("freetype", when="@1.4.3:")

    patch("font.patch", when="@1.3.3")

    # https://github.com/fltk/fltk/commits/master/src/Fl_Tree_Item.cxx
    #  -Fix return value test, as pointed out by Albrecht.
    patch("fix_compare_val.patch", when="@:1.3.3")
    # https://github.com/fltk/fltk/commits/master/test/menubar.cxx
    # -Allow compilation with -std=c++11
    # -Add missing cast (part of patch for STR #2813).
    patch("type_cast.patch", when="@:1.3.3")

    variant("shared", default=True, description="Enables the build of shared libraries")

    variant("gl", default=True, description="Enables opengl support")

    variant("xft", default=False, description="Enables Anti-Aliased Fonts")

    # variant dependencies
    depends_on("gl", when="+gl")

    depends_on("libxft", when="+xft")

    def install(self, spec, prefix):
        options = [
            "--prefix=%s" % prefix,
            "--enable-localjpeg",
            "--enable-localpng",
            "--enable-localzlib",
        ]

        if spec.satisfies("+shared"):
            options.append("--enable-shared")

        if spec.satisfies("+xft"):
            # https://www.fltk.org/articles.php?L374+I0+TFAQ+P1+Q
            options.append("--enable-xft")
        else:
            options.append("--disable-xft")

        if spec.satisfies("~gl"):
            options.append("--disable-gl")

        # FLTK needs to be built in-source
        autogen = Executable("./autogen.sh")
        autogen()
        configure(*options)
        make()
        make("install")

    def patch(self):
        # Remove flags not recognized by the NVIDIA compiler
        if self.spec.satisfies("%nvhpc"):
            filter_file(
                'OPTIM="-Wall -Wunused -Wno-format-y2k $OPTIM"',
                'OPTIM="-Wall $OPTIM"',
                "configure",
                string=True,
            )
            filter_file('OPTIM="-Os $OPTIM"', 'OPTIM="-O2 $OPTIM"', "configure", string=True)
            filter_file(
                'CXXFLAGS="$CXXFLAGS -fvisibility=hidden"',
                'CXXFLAGS="$CXXFLAGS"',
                "configure",
                string=True,
            )
            filter_file(
                'OPTIM="$OPTIM -fvisibility=hidden"', 'OPTIM="$OPTIM"', "configure", string=True
            )
