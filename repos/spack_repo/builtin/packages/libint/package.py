# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *

TUNE_VARIANTS_CP2K = ("cp2k-lmax-4", "cp2k-lmax-5", "cp2k-lmax-6", "cp2k-lmax-7")
TUNE_VARIANTS_MOLGW = ("molgw-lmax-4", "molgw-lmax-5", "molgw-lmax-6", "molgw-lmax-7")
TUNE_VARIANTS = tuple(["none"]) + TUNE_VARIANTS_CP2K + TUNE_VARIANTS_MOLGW


class Libint(AutotoolsPackage):
    """Libint is a high-performance library for computing
    Gaussian integrals in quantum mechanics.
    """

    homepage = "https://github.com/evaleev/libint"
    url = "https://github.com/evaleev/libint/archive/v2.11.1.tar.gz"

    maintainers("dev-zero", "hfp")

    license("LGPL-3.0-only")

    version("2.11.2", sha256="f2fba90579d95f535a93decdae98028ef3a982e6570e1547a0916186f51e86f2")
    version("2.11.1", sha256="58ab0f893d94cbed3ab35a6c26ec5e4d8541c59889407a6d30c50b8ea415bdf3")
    version("2.9.0", sha256="4929b2f2d3e53479270be052e366e8c70fa154a7f309e5c2c23b7d394159687d")
    version("2.6.0", sha256="4ae47e8f0b5632c3d2a956469a7920896708e9f0e396ec10071b8181e4c8d9fa")
    version("2.4.2", sha256="86dff38065e69a3a51d15cfdc638f766044cb87e5c6682d960c14f9847e2eac3")
    version("2.4.1", sha256="0513be124563fdbbc7cd3c7043e221df1bda236a037027ba9343429a27db8ce4")
    version("2.4.0", sha256="52eb16f065406099dcfaceb12f9a7f7e329c9cfcf6ed9bfacb0cff7431dd6019")
    version("2.2.0", sha256="f737d485f33ac819d7f28c6ce303b1f3a2296bfd2c14f7c1323f8c5d370bb0e3")
    version("2.1.0", sha256="43c453a1663aa1c55294df89ff9ece3aefc8d1bbba5ea31dbfe71b2d812e24c8")
    version("1.1.6", sha256="f201b0c621df678cfe8bdf3990796b8976ff194aba357ae398f2f29b0e2985a6")
    version("1.1.5", sha256="ec8cd4a4ba1e1a98230165210c293632372f0e573acd878ed62e5ec6f8b6174b")

    variant("generic", default=False, description="Avoid specialization and larger code size")
    variant("shared", default=True, description="Build shared library")
    variant("debug", default=False, description="Enable debug symbols")
    variant(
        "tune",
        default="none",
        multi=False,
        values=TUNE_VARIANTS,
        description="Tune libint for use with the given package",
    )
    variant("fma", default=True, description="Generate code utilizing FMA")
    variant("cxx", default=False, description="Build and install the C++ API")

    description_fortran = "Build and install Fortran bindings"
    variant("fortran", default=False, description=description_fortran)
    for tune in TUNE_VARIANTS_CP2K:
        variant("fortran", default=True, description=description_fortran, when=f"tune={tune}")

    # Build dependencies
    depends_on("fortran", type="build", when="+fortran")
    depends_on("cxx", type="build")
    depends_on("c", type="build")

    depends_on("autoconf@2.52:", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("python", type="build")
    depends_on("cmake@3.19:", when="@2.6.0:", type="build")

    # Libint2 dependencies
    # Boost is only needed if the Fortran interface is built
    # A header-only installation (with no specific libraries)
    # is sufficient (Boost.with_default_variants not needed)
    depends_on("boost", when="@2: +fortran")
    # Eigen is optional and not strictly necessary
    depends_on("eigen", when="@2.7.0: +cxx")
    depends_on("gmp+cxx", when="@2:")
    # unicode variable names in @2.9.0:
    # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=67224
    conflicts("%gcc@:9", when="@2.9.0:", msg="libint@2.9.0: requires at least gcc 10")

    for tvariant in TUNE_VARIANTS[1:]:
        conflicts(
            f"tune={tvariant}",
            when="@:2.5",
            msg=(
                "for versions prior to 2.6, tuning for specific"
                "codes/configurations is not supported"
            ),
        )

    def url_for_version(self, version):
        base_url = "https://github.com/evaleev/libint/archive"
        if version == Version("1.0.0"):
            return f"{base_url}/LIBINT_1_00.tar.gz"
        elif version < Version("2.1.0"):
            return f"{base_url}/release-{version.dashed}.tar.gz"
        else:
            return f"{base_url}/v{version}.tar.gz"

    def autoreconf(self, spec, prefix):
        if self.spec.satisfies("@2:"):
            which("bash")("autogen.sh")
        else:
            # Fall back since autogen is not available
            libtoolize()
            aclocal("-I", "lib/autoconf")
            autoconf()

    @property
    def optflags(self):
        flags = "-O2"

        # microarchitecture-specific optimization flags should be controlled
        # by Spack, otherwise we may end up with contradictory or invalid flags
        # see https://github.com/spack/spack/issues/17794

        return flags

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Set optimization flags
        env.set("CFLAGS", self.optflags)
        env.set("CXXFLAGS", self.optflags)

        spec = self.spec
        if spec.satisfies("%fj +fortran"):
            env.set("LDFLAGS", "--linkfortran")

        # Change AR to xiar if compiling with Intel and if xiar is found
        intel = spec.satisfies("%intel") or spec.satisfies("%intel-oneapi-compilers")
        if intel and which("xiar"):
            env.set("AR", "xiar")

    def configure_args(self):
        config_args = []

        if self.spec.satisfies("+shared"):
            config_args += ["--enable-shared"]

        if self.spec.satisfies("@2: ^boost"):
            # --with-boost option available only from version 2 and above
            config_args += [f"--with-boost={self.spec['boost'].prefix}"]

        # Optimization flag names have changed in libint2
        if self.version < Version("2.0.0"):
            config_args += [
                f"--with-cc-optflags={self.optflags}",
                f"--with-cxx-optflags={self.optflags}",
            ]
        else:
            config_args += [
                f"--with-cxx-optflags={self.optflags}",
                f"--with-cxxgen-optflags={self.optflags}",
            ]

        # Options required by CP2K, removed in libint2
        if self.version < Version("2.0.0"):
            config_args += ["--with-libint-max-am=5", "--with-libderiv-max-am1=4"]

        if self.spec.satisfies("@2.6.0:"):
            # Two phases: (1) (generateprint specialized code, (2) actual build
            config_args += ["--with-libint-exportdir=generated"]
            config_args += self.enable_or_disable("debug", activation_value=lambda x: "opt")
            config_args += self.enable_or_disable("fma")

            if self.spec.satisfies("+fma") and "avx2" in self.spec.target:
                config_args += ["--with-real-type=libint2::simd::VectorAVXDouble"]

            # Keep code-size at an acceptable limit (independent of "+generic"),
            # cf. https://github.com/evaleev/libint/wiki#program-specific-notes
            config_args += ["--disable-unrolling"]

            # Not providing this option is ~40% code size increase (on x86-64)
            if self.spec.satisfies("+generic"):
                config_args += ["--enable-generic-code"]

            tune_value = self.spec.variants["tune"].value
            if tune_value.startswith("cp2k"):
                lmax = int(tune_value.split("-lmax-")[1])
                config_args += [
                    "--enable-eri=1",
                    "--enable-eri2=1",
                    "--enable-eri3=1",
                    f"--with-max-am={lmax}",
                    f"--with-eri-max-am={lmax},{lmax - 1}",
                    f"--with-eri2-max-am={lmax + 2},{lmax + 1}",
                    f"--with-eri3-max-am={lmax + 2},{lmax + 1}",
                    "--with-opt-am=3",
                ]
            if tune_value.startswith("molgw"):
                lmax = int(tune_value.split("-lmax-")[1])
                config_args += [
                    "--enable-1body=1",
                    "--enable-eri=0",
                    "--enable-eri2=0",
                    "--enable-eri3=0",
                    "--with-multipole-max-order=0",
                    f"--with-max-am={lmax}",
                    f"--with-eri-max-am={lmax}",
                    f"--with-eri2-max-am={lmax}",
                    f"--with-eri3-max-am={lmax}",
                    "--with-opt-am=2",
                    "--enable-contracted-ints",
                ]

        return config_args

    @property
    def build_targets(self):
        if self.spec.satisfies("@2.6.0:"):
            return ["export"]

        return []

    @when("@2.6.0:")
    def build(self, spec, prefix):
        """
        Starting from libint 2.6.0 we're using the 2-stage build
        to get support for the Fortran bindings, required by some
        packages (CP2K notably).
        """

        # upstream says that using configure/make for the generated code
        # is deprecated and one should use CMake

        # skip tarball creation and removal of dir with generated code
        filter_file("&& rm -rf $(EXPORTDIR)", "", "export/Makefile", string=True)

        make("export")
        # now build the library
        with working_dir(os.path.join(self.build_directory, "generated")):
            if spec.satisfies("@2.6.0"):
                config_args = [
                    f"--prefix={prefix}",
                    "--enable-shared",
                    f"--with-boost={spec['boost'].prefix}",
                    f"--with-cxx-optflags={self.optflags}",
                ]
                config_args += self.enable_or_disable("debug", activation_value=lambda x: "opt")
                config_args += self.enable_or_disable("fortran")
                configure = Executable("./configure")
                configure(*config_args)
                make()
            else:
                cmake_args = [
                    "..",
                    f"-DCMAKE_INSTALL_PREFIX={prefix}",
                    "-DLIBINT2_BUILD_SHARED_AND_STATIC_LIBS=ON",
                ]
                if spec.satisfies("+fortran"):
                    cmake_args.append("-DENABLE_FORTRAN=ON")
                if not spec.satisfies("+cxx"):
                    cmake_args.append("-DREQUIRE_CXX_API=OFF")
                if spec.satisfies("+debug"):
                    cmake_args.append("CMAKE_BUILD_TYPE=Debug")
                cmake = Executable("cmake")
                mkdirp("build")
                with working_dir("build"):
                    cmake(*cmake_args)
                    make()

    @when("@2.6.0:")
    def check(self):
        path = join_path(self.build_directory, "generated")
        if self.spec.satisfies("@2.9.0:"):
            path = join_path(path, "build")
        with working_dir(path):
            make("check")

    @when("@2.6.0:")
    def install(self, spec, prefix):
        path = join_path(self.build_directory, "generated")
        if self.spec.satisfies("@2.9.0:"):
            path = join_path(path, "build")
        with working_dir(path):
            make("install")

    @when("@:2.6.0")
    def patch(self):
        # Use Fortran compiler to link the Fortran example, not the C++
        # compiler
        if self.spec.satisfies("+fortran"):
            if not self.spec.satisfies("%fj"):
                filter_file(
                    "$(CXX) $(CXXFLAGS)",
                    "$(FC) $(FCFLAGS)",
                    "export/fortran/Makefile",
                    string=True,
                )

    @property
    def libs(self):
        return find_libraries("libint2", self.spec.prefix, shared=True, recursive=True)
