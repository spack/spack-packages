# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Xcrysden(MakefilePackage):
    """XCrySDen is a crystalline and molecular structure visualisation program aiming at display of
    isosurfaces and contours, which can be superimposed on crystalline structures and interactively
    rotated and manipulated.
    """

    homepage = "http://www.xcrysden.org/XCrySDen.html"
    url = "http://www.xcrysden.org/download/xcrysden-1.6.2.tar.gz"
    maintainers("gjsd2")

    license("GPL-2.0-or-later")

    version("1.6.3-rc2", sha256="0565f55dfb67c73a824569bd2f02875f1e15c7214b86736fce4cacc3f5a189fe")
    version("1.6.2", sha256="811736ee598bec1a5b427fd10e4e063a30dd7cadae96a43a50b36ce90a4f503f")
    version("1.6.1", sha256="8a9c6d83c4a9e189dbb977a04ccf1b260871e945afdf1ca75830616a6cb442c5")
    version("1.6.0", sha256="9ee1d9a1113c72722f0c7c6e08e70a568b6ee7a2f81a25ac636f46b16741b0b6")

    depends_on("mesa", type=("link", "run"))
    depends_on("mesa-glu", type=("link", "run"))
    depends_on("tk", type=("link", "run"))
    depends_on("tcl", type=("build", "link", "run"))
    depends_on("tcl-togl@2:", type=("link", "run"))
    depends_on("tcl-bwidget@1.9:", type=("link", "run"))
    depends_on("fftw@3:", type=("link", "run"))
    depends_on("libx11", type=("build", "link", "run"))
    depends_on("libxmu", type=("build", "link", "run"))

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    parallel = False

    @run_before("edit")
    def copy_system_makefile(self):
        copy("system/Make.sys-shared", "Make.sys")

    def build(self, spec, prefix):
        make("xcrysden")

    def edit(self, spec, prefix):
        togl_lib = f"Togl{spec['tcl-togl'].version.up_to(2)}"
        tcl_lib = f"tcl{spec['tcl'].version.up_to(2)}"
        tk_lib = f"tk{spec['tk'].version.up_to(2)}"

        env["prefix"] = prefix

        makefile = FileFilter("Makefile")
        makefile.filter("xcrysden:.*", "xcrysden: usage bindir src-C src-F src-Tcl")

        makesys = FileFilter("Make.sys")
        makesys.filter(
            "CFLAGS.*=.*", "CFLAGS += -fcommon -ffast-math -funroll-loops -fPIC -pedantic -Wall"
        )
        makesys.filter(
            "X_LIB.*=.*",
            f"X_LIB = -L{spec['libx11'].prefix.lib} -lX11 -L{spec['libxmu'].prefix.lib} -lXmu",
        )
        makesys.filter(
            "X_INCDIR.*=.*",
            f"X_INCDIR = -I{spec['libx11'].prefix.include} -I{spec['libxmu'].prefix.include}",
        )
        makesys.filter("TCL_LIB.*=.*", f"TCL_LIB = -L{spec['tcl'].prefix.lib} -l{tcl_lib}")
        makesys.filter(
            "TOGL_LIB.*=.*",
            f"TOGL_LIB = -L{join_path(spec['tcl-togl'].prefix.lib, togl_lib)} -l{togl_lib}",
        )
        makesys.filter("TK_LIB.*=.*", f"TK_LIB = -L{spec['tk'].prefix.lib} -l{tk_lib}")
        makesys.filter("^GL_LIB.*=.*", f"GL_LIB = -L{spec['mesa'].prefix.lib} -lGL")
        makesys.filter("GLU_LIB.*=.*", f"GLU_LIB = -L{spec['mesa-glu'].prefix.lib} -lGLU")
        makesys.filter("FFTW3_LIB.*=.*", f"FFTW3_LIB = -L{spec['fftw'].prefix.lib} -lfftw3")
        makesys.filter("TCL_INCDIR.*=.*", f"TCL_INCDIR = -I{spec['tcl'].prefix.include}")
        makesys.filter("TOGL_INCDIR.*=.*", f"TOGL_INCDIR = -I{spec['tcl-togl'].prefix.include}")
        makesys.filter("TK_INCDIR.*=.*", f"TK_INCDIR = -I{spec['tk'].prefix.include}")
        makesys.filter("^GL_INCDIR.*=.*", f"GL_INCDIR = -I{spec['mesa'].prefix.include}")
        makesys.filter("FFTW3_INCDIR.*=.*", "FFTW3_INCDIR = -I{spec['fftw'].prefix.include}")
