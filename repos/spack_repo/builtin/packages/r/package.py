# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class R(AutotoolsPackage):
    """R is 'GNU S', a freely available language and environment for
    statistical computing and graphics which provides a wide variety of
    statistical and graphical techniques: linear and nonlinear modelling,
    statistical tests, time series analysis, classification, clustering, etc.
    Please consult the R project homepage for further information."""

    homepage = "https://www.r-project.org"
    url = "https://cloud.r-project.org/src/base/R-4/R-4.4.0.tar.gz"

    extendable = True

    executables = ["^R$"]

    license("GPL-2.0-or-later")

    version("trunk", svn="https://svn.r-project.org/R/trunk")
    version("4.5.3", sha256="aa5c1ed4293c7271ac513d654670356ac0e8a6ad5e42be014365d11150b5b8f2")
    version("4.5.2", sha256="0d71ff7106ec69cd7c67e1e95ed1a3cee355880931f2eb78c530014a9e379f20")
    version("4.5.1", sha256="b42a7921400386645b10105b91c68728787db5c4c83c9f6c30acdce632e1bb70")
    version("4.5.0", sha256="3b33ea113e0d1ddc9793874d5949cec2c7386f66e4abfb1cef9aec22846c3ce1")
    version("4.4.3", sha256="0d93d224442dea253c2b086f088db6d0d3cfd9b592cd5496e8cb2143e90fc9e8")
    version("4.4.2", sha256="1578cd603e8d866b58743e49d8bf99c569e81079b6a60cf33cdf7bdffeb817ec")
    version("4.4.1", sha256="b4cb675deaaeb7299d3b265d218cde43f192951ce5b89b7bb1a5148a36b2d94d")
    version("4.4.0", sha256="ace4125f9b976d2c53bcc5fca30c75e30d4edc401584859cbadb080e72b5f030")
    version("4.3.3", sha256="80851231393b85bf3877ee9e39b282e750ed864c5ec60cbd68e6e139f0520330")
    version("4.3.2", sha256="b3f5760ac2eee8026a3f0eefcb25b47723d978038eee8e844762094c860c452a")
    version("4.3.1", sha256="8dd0bf24f1023c6f618c3b317383d291b4a494f40d73b983ac22ffea99e4ba99")
    version("4.3.0", sha256="45dcc48b6cf27d361020f77fde1a39209e997b81402b3663ca1c010056a6a609")

    variant("X", default=False, description="Enable X11 support (TCLTK, PNG, JPEG, TIFF, CAIRO)")
    variant("java", default=False, description="Enable Java support")
    variant("memory_profiling", default=False, description="Enable memory profiling")
    variant("rmath", default=False, description="Build standalone Rmath library")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("findutils", type="build")
    depends_on("texinfo", type="build")

    depends_on("blas")
    requires("^openblas symbol_suffix=none", when="^openblas")
    depends_on("lapack")

    depends_on("zlib-api")
    depends_on("zlib@1.2.5:", when="^[virtuals=zlib-api] zlib")
    depends_on("bzip2")
    depends_on("xz")
    depends_on("zstd", when="@4.5:")
    depends_on("libdeflate", when="@4.4:")
    depends_on("curl+libidn2")
    depends_on("libtirpc")
    depends_on("ncurses")
    depends_on("readline")
    depends_on("pcre2")
    depends_on("gettext")
    depends_on("icu4c")
    depends_on("which", type=("build", "run"))
    depends_on("java", when="+java", type=("build", "run"))

    with when("+X"):
        depends_on("cairo+X+gobject+pdf")
        depends_on("pango+X")
        depends_on("harfbuzz+graphite2")
        depends_on("jpeg")
        depends_on("libpng")
        depends_on("libtiff")
        depends_on("libx11")
        depends_on("libxt")
        depends_on("libxmu")
        depends_on("tcl")
        depends_on("tk")

    # Make R use a symlink to which in Sys.which, otherwise an absolute path
    # gets stored as compressed byte code, which is not relocatable
    patch("relocate-which.patch")

    # CVE-2024-27322 Patch only needed in R 4.3.3 and below; doesn't apply to R older than 3.5.0.
    patch(
        "https://github.com/r-devel/r-svn/commit/f7c46500f455eb4edfc3656c3fa20af61b16abb7.patch?full_index=1",
        sha256="56c77763cb104aa9cb63420e585da63cb2c23bc03fa3ef9d088044eeff9d7380",
        when="@:4.3.3",
    )

    build_directory = "spack-build"

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        # R version 4.3.3 (2024-02-29) -- "Angel Food Cake"
        match = re.search(r"^R version ([^\s]+)", output)
        return match.group(1) if match else None

    @classmethod
    def determine_variants(cls, exes, version):
        variants = []
        for exe in exes:
            output = Executable(exe)("CMD", "config", "--all", output=str, error=str)

            if "-lX11" in output:
                variants.append("+X")

        return variants

    # R custom URL version
    def url_for_version(self, version):
        """Handle R's customed URL versions"""
        url = "https://cloud.r-project.org/src/base"
        return url + "/R-%s/R-%s.tar.gz" % (version.up_to(1), version)

    @property
    def etcdir(self):
        return join_path(prefix, "rlib", "R", "etc")

    @run_after("install")
    def install_rmath(self):
        if "+rmath" in self.spec:
            with working_dir(join_path(self.build_directory, "src", "nmath", "standalone")):
                make()
                make("install", parallel=False)

    def configure_args(self):
        spec = self.spec
        prefix = self.prefix

        extra_rpath = join_path(prefix, "rlib", "R", "lib")

        blas_flags: str = spec["blas"].libs.ld_flags
        lapack_flags: str = spec["lapack"].libs.ld_flags

        # R uses LAPACK in Fortran, which requires libmkl_gf_* when gfortran is used.
        # TODO: cleaning this up seem to require both compilers as dependencies and use variants.
        if (
            spec.satisfies("^[virtuals=lapack] intel-oneapi-mkl")
            and "gfortran" in self.compiler.fc
        ):
            xlp64 = "ilp64" if spec["lapack"].satisfies("+ilp64") else "lp64"
            blas_flags = blas_flags.replace(f"mkl_intel_{xlp64}", f"mkl_gf_{xlp64}")
            lapack_flags = lapack_flags.replace(f"mkl_intel_{xlp64}", f"mkl_gf_{xlp64}")

        config_args = [
            "--with-internal-tzcode",
            "--libdir={0}".format(join_path(prefix, "rlib")),
            "--enable-R-shlib",
            "--enable-R-framework=no",
            "--without-recommended-packages",
            f"LDFLAGS=-Wl,-rpath,{extra_rpath}",
            f"--with-blas={blas_flags}",
            f"--with-lapack={lapack_flags}",
            "ac_cv_path_PDFLATEX=",
            "ac_cv_path_PDFTEX=",
            "ac_cv_path_TEX=",
            "ac_cv_path_TEXI2DVI=",
            f"--with-libintl-prefix={spec['gettext'].prefix}",
        ]

        if "+X" in spec:
            config_args.append("--with-cairo")
            config_args.append("--with-jpeglib")
            config_args.append("--with-libpng")
            config_args.append("--with-libtiff")
            config_args.append("--with-tcltk")
            config_args.append("--with-x")

            tcl_config_path = join_path(spec["tcl"].libs.directories[0], "tclConfig.sh")
            config_args.append("--with-tcl-config={0}".format(tcl_config_path))

            tk_config_path = join_path(spec["tk"].libs.directories[0], "tkConfig.sh")
            config_args.append("--with-tk-config={0}".format(tk_config_path))
        else:
            config_args.append("--without-cairo")
            config_args.append("--without-jpeglib")
            config_args.append("--without-libpng")
            config_args.append("--without-libtiff")
            config_args.append("--without-tcltk")
            config_args.append("--without-x")

        config_args.extend(self.enable_or_disable("java"))

        if "+memory_profiling" in spec:
            config_args.append("--enable-memory-profiling")

        # Set FPICFLAGS for compilers except 'gcc'.
        if self.compiler.name != "gcc":
            config_args.append("FPICFLAGS={0}".format(self.compiler.cc_pic_flag))

        return config_args

    @run_after("install")
    def copy_makeconf(self):
        # Ensure full library flags are included in Makeconf
        for _lib, _pkg in [
            ("lzma", "xz"),
            ("bz2", "bzip2"),
            ("z", "zlib-api"),
            ("tirpc", "libtirpc"),
            ("icuuc", "icu4c"),
        ]:
            filter_file(
                f"-l{_lib}",
                f"-L{self.spec[_pkg].libs.directories[0]} -l{_lib}",
                join_path(self.etcdir, "Makeconf"),
            )

        # Make a copy of Makeconf because it will be needed to properly build R
        # dependencies in Spack.
        src_makeconf = join_path(self.etcdir, "Makeconf")
        dst_makeconf = join_path(self.etcdir, "Makeconf.spack")
        install(src_makeconf, dst_makeconf)

    # To respect order of execution, we should filter after we made the copy above
    filter_compiler_wrappers("Makeconf", relative_root=os.path.join("rlib", "R", "etc"))

    # ========================================================================
    # Set up environment to make install easy for R extensions.
    # ========================================================================

    @property
    def r_lib_dir(self):
        return join_path("rlib", "R", "library")

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        # Set R_LIBS to include the library dir for the
        # extension and any other R extensions it depends on.
        r_libs_path = []
        for d in dependent_spec.traverse(deptype=("build", "run")):
            if d.package.extends(self.spec):
                r_libs_path.append(join_path(d.prefix, self.r_lib_dir))

        env.set("R_LIBS", ":".join(r_libs_path))
        # R_LIBS_USER gets set to a directory in HOME/R if it is not set, such as
        # during package installation with the --vanilla flag. Set it to null
        # to ensure that it does not point to a directory that may contain R
        # packages.
        env.set("R_LIBS_USER", "")
        env.set("R_MAKEVARS_SITE", join_path(self.etcdir, "Makeconf.spack"))

        # Use the number of make_jobs set in spack. The make program will
        # determine how many jobs can actually be started.
        env.set("MAKEFLAGS", "-j{0}".format(make_jobs))
        env.set("R_HOME", join_path(self.prefix, "rlib", "R"))

    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        # For run time environment set only the path for dependent_spec and
        # prepend it to R_LIBS
        env.set("R_HOME", join_path(self.prefix, "rlib", "R"))
        if dependent_spec.package.extends(self.spec):
            env.prepend_path("R_LIBS", join_path(dependent_spec.prefix, self.r_lib_dir))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "rlib", "R", "lib"))
        env.prepend_path("PKG_CONFIG_PATH", join_path(self.prefix, "rlib", "pkgconfig"))
        env.set("R_HOME", join_path(self.prefix, "rlib", "R"))

        if "+rmath" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "rlib"))

    def setup_dependent_package(self, module, dependent_spec):
        """Called before R modules' install() methods. In most cases,
        extensions will only need to have one line:
            R('CMD', 'INSTALL', '--library={0}'.format(self.module.r_lib_dir),
              self.stage.source_path)"""

        # R extension builds can have a global R executable function
        module.R = Executable(join_path(self.spec.prefix.bin, "R"))

        # Add variable for library directry
        module.r_lib_dir = join_path(dependent_spec.prefix, self.r_lib_dir)
