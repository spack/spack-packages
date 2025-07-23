# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Xcrysden(MakefilePackage):
    """XCrySDen is a crystalline and molecular structure visualisation program aiming at display of
    isosurfaces and contours, which can be superimposed on crystalline structures and interactively
    rotated and manipulated.
    """

    homepage = "http://www.xcrysden.org/XCrySDen.html"
    url = "http://www.xcrysden.org/download/xcrysden-1.6.2.tar.gz"

    version("1.6.3-rc2", sha256="0565f55dfb67c73a824569bd2f02875f1e15c7214b86736fce4cacc3f5a189fe")
    version("1.6.3-rc1", sha256="dac69eb6c37a64cb26e8e0fb378698786df61109ceea364f3878f0cbbe28c966")
    version("1.6.2", sha256="811736ee598bec1a5b427fd10e4e063a30dd7cadae96a43a50b36ce90a4f503f")
    version("1.6.1", sha256="8a9c6d83c4a9e189dbb977a04ccf1b260871e945afdf1ca75830616a6cb442c5")
    version("1.6.0-rc3", sha256="8a41d4ac45da77e2885dba55a55ba5dd0dab79cce90dd3e147ceed937917a754")
    version("1.6.0-rc2", sha256="063ffc4775b3ac5f93b41ee554242dd09577a910968a53468a8077b547769054")
    version("1.6.0-rc1", sha256="f1368d7eda680013c025f77b5f97185e0a7d9862abc56e083b077b115aadd170")
    version("1.6.0", sha256="9ee1d9a1113c72722f0c7c6e08e70a568b6ee7a2f81a25ac636f46b16741b0b6")
    version(
        "1.5.60-cyg", sha256="ac1f2102abba9bc66f642be8d3b07f644612524219d4c99441f1c8b88b0a6457"
    )
    version("1.5.60", sha256="a695729f1bb3e486b86a74106c06a392c8aca048dc6b0f20785c3c311cfb2ef4")
    version(
        "1.5.53-cyg", sha256="b680ef6bf435495827d28b55f2c01fe88becc2d003d6a3da446e160330204d71"
    )
    version("1.5.53", sha256="9eff395b63a3490e8bbb7d8c8501d1ecf3e1157897eb066baae7fcaf7f0788be")

    depends_on("mesa~llvm", type=("link", "run"))
    depends_on("mesa-glu", type=("link", "run"))
    depends_on("tk", type=("link", "run"))
    depends_on("tcl", type=("build", "link", "run"))
    depends_on("tcl-togl@2:", type=("link", "run"))
    depends_on("tcl-bwidget@1.9:", type=("link", "run"))
    depends_on("fftw@3:", type=("link", "run"))
    depends_on("libx11",type=("build", "link", "run"))
    depends_on("libxmu",type=("build", "link", "run"))

    depends_on("c", type="build")
    depends_on("fortran", type="build")


    parallel = False

    @run_before("edit")
    def copy_system_makefile(self):
        copy("system/Make.sys-shared", "Make.sys")

    def build(self, spec, prefix):
        make("xcrysden")

    def edit(self, spec, prefix):
        togl_lib = "Togl" + str(spec["tcl-togl"].version.up_to(2))
        tcl_lib = "tcl" + str(spec["tcl"].version.up_to(2))
        tk_lib = "tk" + str(spec["tk"].version.up_to(2))

        env["prefix"] = prefix

        makefile = FileFilter("Makefile")
        makefile.filter("xcrysden:.*","xcrysden: usage bindir src-C src-F src-Tcl")

        makesys = FileFilter("Make.sys")
        makesys.filter(
            "CFLAGS.*=.*","CFLAGS += -fcommon -ffast-math -funroll-loops -fPIC -pedantic -Wall"
        )
        makesys.filter(
            "X_LIB.*=.*", "X_LIB = -L{0} -lX11 -L{1} -lXmu".format(spec["libx11"].prefix.lib, spec["libxmu"].prefix.lib)
        )
        makesys.filter(
            "X_INCDIR.*=.*", "X_INCDIR = -I{0} -I{1}".format(spec["libx11"].prefix.include, spec["libxmu"].prefix.include)
        )
        makesys.filter(
            "TCL_LIB.*=.*", "TCL_LIB = -L{0} -l{1}".format(spec["tcl"].prefix.lib, tcl_lib)
        )
        makesys.filter(
            "TOGL_LIB.*=.*",
            "TOGL_LIB = -L{0} -l{1}".format(join_path(spec["tcl-togl"].prefix.lib, togl_lib), togl_lib),
        )
        makesys.filter(
            "TK_LIB.*=.*", "TK_LIB = -L{0} -l{1}".format(spec["tk"].prefix.lib, tk_lib)
        )
        makesys.filter("^GL_LIB.*=.*", "GL_LIB = -L{0} -lGL".format(spec["mesa"].prefix.lib))
        makesys.filter(
            "GLU_LIB.*=.*", "GLU_LIB = -L{0} -lGLU".format(spec["mesa-glu"].prefix.lib)
        )
        makesys.filter(
            "FFTW3_LIB.*=.*", "FFTW3_LIB = -L{0} -lfftw3".format(spec["fftw"].prefix.lib)
        )

        makesys.filter("TCL_INCDIR.*=.*", "TCL_INCDIR = -I{0}".format(spec["tcl"].prefix.include))
        makesys.filter(
            "TOGL_INCDIR.*=.*", "TOGL_INCDIR = -I{0}".format(spec["tcl-togl"].prefix.include)
        )
        makesys.filter("TK_INCDIR.*=.*", "TK_INCDIR = -I{0}".format(spec["tk"].prefix.include))
        makesys.filter("^GL_INCDIR.*=.*", "GL_INCDIR = -I{0}".format(spec["mesa"].prefix.include))
        makesys.filter(
            "FFTW3_INCDIR.*=.*", "FFTW3_INCDIR = -I{0}".format(spec["fftw"].prefix.include)
        )
