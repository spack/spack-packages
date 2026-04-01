# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import shutil

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Xictools(MakefilePackage):
    """
    Suite of integrated circuit design tools including Xic (graphical editor)
    and WRspice (circuit simulator) for small and medium scale digital and
    analog integrated circuits. (from http://wrcad.com/products.html)
    """

    homepage = "http://wrcad.com/xictools/index.html"
    url = "https://github.com/wrcad/xictools/archive/refs/tags/xt-4.3.23.tar.gz"

    # See README.md for details
    license(
        "Apache-2.0 AND Spencer-94 AND BSD-4-Clause-UC AND https://www.rle.mit.edu/cpg/copyright_disclaimer.htm AND HPND-UC",
        when="~gpl",
        checked_by="kllrak",
    )
    license(
        "Apache-2.0 AND Spencer-94 AND BSD-4-Clause-UC AND https://www.rle.mit.edu/cpg/copyright_disclaimer.htm AND HPND-UC AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND Minpack",
        when="+gpl",
        checked_by="kllrak",
    )

    version("4.3.23", sha256="f329d71bf637ed09921de6b0f6fdc38443d1a97617ca528a4eafa1be37c99e72")

    # Set as sticky since most will expect WRspice and GUI to be included
    variant(
        "gpl",
        default=True,
        description="Build xictools with LGPL- and GPL-licensed code for WRspice and help system.",
        sticky=True,
    )
    variant("qt", default=True, description="Build xictools with Qt5 GUI.", sticky=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Build tools
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("git", type="build")

    # Library dependencies
    depends_on("gsl")
    depends_on("libjpeg")
    depends_on("libtiff")
    depends_on("ncurses")
    depends_on("qt@5+opengl", when="+qt")

    build_targets = ["all"]
    install_targets = ["install"]

    # Parallel builds seen as unreliable...
    # See https://github.com/JuliaPackaging/Yggdrasil/pull/8155#discussion_r1500792779
    # and https://github.com/wrcad/xictools/issues/28
    parallel = False

    # Remove stray include that breaks building +qt~gpl
    patch("qtmain.cc.patch", when="@4:")

    # Missing function stub for PopUpHelp with +qt~gpl
    patch("qtinterf.cc.patch", when="@4:")

    # Avoid hardcoding path to malloc.h
    patch("malloc-2.8.6.c.patch", when="@4:")

    # 1. fasthenry build assumes that KLU tarball has been unpacked and patched already.
    #    This probably doesn't become apparent unless you accidentally include fasthenry
    #    in a ~gpl build, but was found when constructing this package.py file.
    # 2. xictools/bin assumed to exist before it does during a +qt+gpl build.
    patch("Makefile.in.patch", when="@4:")

    def edit(self, spec: Spec, prefix: Prefix) -> None:

        # Copy Makefile.sample to Makefile
        shutil.copy("Makefile.sample", "Makefile")

        # Configure the Makefile
        makefile = FileFilter("Makefile")

        # Set PREFIX to Spack installation prefix (command-line argument format)
        makefile.filter(r"^PREFIX\s*=.*", f"PREFIX = --prefix={prefix}")

        # Enable direct installation without packaging (command-line argument format)
        makefile.filter(r"^#?\s*ITOPOK\s*=.*", "ITOPOK = --enable-itopok=yes")

        # Set Qt5 graphics location using Spack's qt prefix
        if spec.satisfies("+qt"):
            # since we're only building Qt, just assume its our preference.
            filter_file(r"grpref=GTK2", "grpref=QT5", "xic/bin/xic.sh")
            filter_file(r"grpref=GTK2", "grpref=QT5", "wrspice/bin/wrspice.sh")
            filter_file(r"grpref=GTK2", "grpref=QT5", "mozy/bin/mozy.sh")
            filter_file(r"grpref=GTK2", "grpref=QT5", "mozy/bin/xeditor.sh")
            qt_prefix = spec["qt"].prefix
            makefile.filter(r"^#?\s*GFXLOC\s*=.*", f"GFXLOC = --enable-qt5={qt_prefix}")

        if spec.satisfies("~gpl"):
            makefile.filter(r"^#?\s*NOMOZY\s*=.*", "NOMOZY = --enable-nomozy=yes")

        # Build SUBDIRS based on variants
        subdirs = ["xt_base"]
        if spec.satisfies("+gpl"):
            subdirs.append("$(MOZY)")
            subdirs.append("$(WRSPICE)")
        subdirs.append("$(XIC)")
        subdirs.append("fastcap")

        # Uses KLU, contains LGPL-2.1-or-later components
        if spec.satisfies("+gpl"):
            subdirs.append("fasthenry")

        makefile.filter(r"^SUBDIRS\s*=.*", f"SUBDIRS = {' '.join(subdirs)}")

        make("config")

    def setup_run_environment(self, env):
        env.prepend_path("PATH", join_path(self.prefix, "xictools", "bin"))
