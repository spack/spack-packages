# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ambertools(CMakePackage):
    """AmberTools is a free, useful standalone package and a prerequisite
    for installing Amber itself. The AmberTools suite is free of charge,
    and its components are mostly released under the GNU General Public
    License (GPL). A few components are included that are in the public
    domain or which have other, open-source, licenses. The libsander and
    libpbsa libraries use the LGPL license.

    A manual download is required for AmberTools. Spack will search your current
    directory for the download files. Alternatively, add the files to a mirror
    so that Spack can find them. For instructions on how to set up a mirror, see
    https://spack.readthedocs.io/en/latest/mirrors.html
    """

    homepage = "https://ambermd.org/AmberTools.php"
    url = f"file://{os.getcwd()}/ambertools25.tar.bz2"
    manual_download = True

    maintainers("d-beltran")

    version(
        "22jlmrcc",
        sha256="1571d4e0f7d45b2a71dce5999fa875aea8c90ee219eb218d7916bf30ea229121",
        deprecated=True,
    )
    version(
        "26",
        sha256="5d46eef3c2bb7d5bf9e8c0c38add34406ea67e3f0e4097ac9d11d8a544538c9c",
        url=f"file://{os.getcwd()}/AmberTools26.tar.bz2",
    )
    version("25", sha256="ac009b2adeb25ccd2191db28905b867df49240e038dc590f423edf0d84f8a13b")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("tcsh", type="build")
    depends_on("zlib", type=("build", "run"))
    depends_on("bzip2", type=("build", "run"))
    depends_on("blas", type=("build", "run"))
    depends_on("lapack", type=("build", "run"))
    depends_on("arpack-ng", type=("build", "run"))
    depends_on("netcdf-c", type=("build", "run"))
    depends_on("netcdf-fortran", type=("build", "run"))
    depends_on("fftw", type=("build", "run"))
    depends_on("readline", type=("build", "run"))
    depends_on("netlib-xblas~plain_blas", type=("build", "run"))
    # Specific variants needed for boost according to build logs
    depends_on(
        "boost+thread+system+program_options+iostreams+regex+timer+chrono+filesystem+graph",
        type=("build", "run"),
    )
    # Python dependencies
    depends_on("python@3.8:3.10 +tkinter", when="@22jlmrcc", type=("build", "run"))
    depends_on("python@3.11:", when="@25:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    with default_args(when="@26:", type=("build", "run")):
        depends_on("py-setuptools@:81")
        depends_on("py-pandas")
        depends_on("py-numba")
        depends_on("py-gemmi")
        depends_on("py-biopython")
        depends_on("py-rich")
        depends_on("py-freesasa")
        depends_on("py-scikit-learn")
        depends_on("py-sympy")
        depends_on("py-pydantic")
        depends_on("py-psutil")
        depends_on("py-networkx")
        depends_on("python@3.11 +tkinter")

    # Cython is required only when building from a non-release
    # Amber source tree. The AmberTools release has pre-cythonized pytraj.
    # Add this dependency only if building a non-release source.

    def cmake_args(self):
        # Translated from ambertools build/run_cmake script
        # We also add the TRUST_SYSTEM_LIBS argument mentioned in the ambertools guide
        #   https://ambermd.org/pmwiki/pmwiki.php/Main/CMake-Guide-to-Options
        args = [
            self.define("COMPILER", "GNU"),
            self.define("MPI", False),
            self.define("CUDA", False),
            self.define("INSTALL_TESTS", True),
            self.define("DOWNLOAD_MINICONDA", False),
            self.define("TRUST_SYSTEM_LIBS", True),
            # This is to avoid the x11 (X11_Xext_LIB) error
            # It is equivalent to the "-noX11" flag accoridng to the docs:
            # https://ambermd.org/pmwiki/pmwiki.php/Main/CMake-Common-Options
            self.define("BUILD_GUI", False),
        ]
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("AMBER_PREFIX", self.prefix)
        env.set("AMBERHOME", self.prefix)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("AMBER_PREFIX", self.prefix)
        env.set("AMBERHOME", self.prefix)

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):
        make("test.serial")

    # Temporarily copy netcdf.h header file to netcdf-fortran/include to pass the Ambertools
    # cmake check (quickest fix, will probably cause problems, needs to change)
    @run_before("cmake")
    def fix_check(self):
        cp = Executable("cp")
        cp(
            self.spec["netcdf-c"].headers.directories[0] + "/netcdf.h",
            self.spec["netcdf-fortran"].headers.directories[0],
        )

    # On aarch64 the link of AmberTools' "resp" fails with
    #   relocation truncated to fit: R_AARCH64_ADR_PREL_PG_HI21 against symbol
    #   `files_' defined in COMMON section
    # because resp.F declares very large COMMON blocks that the default "small" code
    # model cannot address. Building everything with -mcmodel=large breaks the CMake
    # Fortran/C and BLAS configure checks, so only the resp target is changed, after
    # configuration. (gfortran on aarch64 has no -mcmodel=medium; large is not
    # compatible with PIE, hence -fno-pie / -no-pie.)
    @run_after("cmake")
    def resp_large_code_model(self):
        if not self.spec.satisfies("target=aarch64:"):
            return
        resp_dir = join_path(
            self.build_directory, "AmberTools", "src", "etc", "CMakeFiles", "resp.dir"
        )
        flags_make = join_path(resp_dir, "flags.make")
        link_txt = join_path(resp_dir, "link.txt")
        if os.path.exists(flags_make):
            filter_file(r"^(Fortran_FLAGS = .*)$", r"\1 -mcmodel=large -fno-pie", flags_make)
        if os.path.exists(link_txt):
            filter_file(r"-o resp ", "-no-pie -o resp ", link_txt)
