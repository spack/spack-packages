# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Grace(AutotoolsPackage):
    """Grace is a WYSIWYG 2D plotting tool for the X Window System and M*tif."""

    homepage = "https://plasma-gate.weizmann.ac.il/Grace"
    # The main site (ftp://plasma-gate.weizmann.ac.il/pub/grace/)
    # is currently unavailable so we use one of the mirrors instead.
    url = "ftp://ftp.fu-berlin.de/unix/graphics/grace/src/grace5/grace-5.1.25.tar.gz"

    maintainers("RemiLacroix-IDRIS")

    license("GPL-2.0-or-later")

    version("5.1.25", sha256="751ab9917ed0f6232073c193aba74046037e185d73b77bab0f5af3e3ff1da2ac")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("libx11")
    depends_on("libxext")
    depends_on("libxmu")
    depends_on("libxp")
    depends_on("libxt")
    depends_on("libice")
    depends_on("libsm")
    depends_on("motif")
    # Some Motif builds (e.g. 2.3.8) compile Xpm support INTO libXm.so
    # rather than as a separate libXpm, but grace's configure explicitly
    # probes for "-lXpm" as a standalone library ("checking for
    # XpmCreatePixmapFromData in -lXpm... no" -> reported as "M*tif has
    # not been found", which is misleading since the real problem has
    # nothing to do with Motif itself). libxpm (standalone, X.Org)
    # provides that symbol regardless of how the system/vendor Motif was
    # built.
    depends_on("libxpm")
    depends_on("jpeg")
    depends_on("libpng")
    depends_on("fftw@2.0:2")
    depends_on("netcdf-c")

    def patch(self):
        # Spack's FFTW2 has prefixed headers so patch the code accordingly.
        # We are not patching "ac-tools/aclocal.m4" since it is not needed
        # currently and would require to run "autoreconf".
        filter_file("<fftw.h>", "<dfftw.h>", "configure", "src/fourier.c")
        filter_file(
            "char   filename[128];",
            "char   filename[4096];",
            "T1lib/type1/scanfont.c",
            string=True,
        )
        filter_file(
            "char CurFontName[120];",
            "char CurFontName[4096];",
            "T1lib/type1/fontfcn.c",
            string=True,
        )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # With libxpm linked, the link check itself passes ("checking for
        # XpmCreatePixmapFromData in -lXpm... yes"), but configure also
        # probes for the bare header "xpm.h" (not "X11/xpm.h", which is
        # where libxpm actually installs it -- standard X.Org convention).
        # Without the bare header, the final combined check ("a Motif >=
        # 1002 compatible API") still fails even though the link works.
        env.append_flags("CPPFLAGS", "-I{0}".format(self.spec["libxpm"].prefix.include.X11))
        # The include for motif should be injected automatically via the
        # normal depends_on-based compiler wrapper, but in practice that
        # was not enough to make "Xm/XmAll.h" resolve during configure.
        # Add it explicitly, same pattern as libxpm above, rather than
        # rely on auto-injection always working.
        env.append_flags("CPPFLAGS", "-I{0}".format(self.spec["motif"].prefix.include))
        # The final "a Motif >= 1002 compatible API" check is not just a
        # compile check -- it uses ac_fn_c_try_run, which COMPILES AND
        # RUNS a test binary calling XmVersion/XmRegisterConverters
        # (Xm/XmAll.h) during configure itself. At that point the final
        # RPATH has not been applied yet (that only happens at the real
        # link/install step), so the dynamic linker can't find
        # libXm.so/libXpm.so and the test binary fails to start --
        # autoconf then reports "Motif not found" even though compiling
        # and linking both succeeded. Make the libraries findable at
        # configure time via LD_LIBRARY_PATH.
        env.prepend_path("LD_LIBRARY_PATH", self.spec["motif"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libxpm"].prefix.lib)
        # Newer GCC (14+) treats several patterns that used to be mere
        # warnings as hard errors by default: implicit function
        # declarations (e.g. exit() used without <stdlib.h> -- including
        # in the autoconf-generated conftest.c for the check above, which
        # otherwise fails to even compile), K&R-style function
        # definitions without explicit parameter types (Xbae/Draw.c,
        # legal C89, now -Wimplicit-int), and implicit int/pointer
        # conversions. Downgrade these back to warnings so the build can
        # proceed as it always has on older GCC.
        if self.spec.satisfies("%gcc@14:"):
            env.append_flags(
                "CFLAGS",
                "-Wno-error=implicit-function-declaration "
                "-Wno-error=implicit-int "
                "-Wno-error=int-conversion",
            )

    def configure_args(self):
        args = []
        args.append("--with-fftw")
        # Spack's FFTW2 has prefixed libraries
        args.append("--with-fftw-library=-ldfftw")
        for driver in ["jpeg", "png"]:
            args.append("--enable-{0}drv".format(driver))
        args.append("--enable-netcdf")
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Grace installs a subfolder in the prefix directory
        # so we account for that...
        env.prepend_path("PATH", self.prefix.grace.bin)
