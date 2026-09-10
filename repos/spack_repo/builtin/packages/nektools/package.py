# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import numbers

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


def is_integral(x):
    """Any integer value"""
    try:
        return isinstance(int(x), numbers.Integral) and not isinstance(x, bool) and int(x) > 0
    except ValueError:
        return False


class Nektools(Package):
    """Tools required by Nek5000"""

    homepage = "https://nek5000.mcs.anl.gov/"
    url = "https://github.com/Nek5000/Nek5000/archive/v17.0.tar.gz"
    git = "https://github.com/Nek5000/Nek5000.git"

    tags = [
        "cfd",
        "flow",
        "hpc",
        "solver",
        "navier-stokes",
        "spectral-elements",
        "fluid",
        "ecp",
        "ecp-apps",
    ]

    version("develop", branch="master")
    version("19.0", sha256="db129877a10ff568d49edc77cf65f9e732eecb1fce10edbd91ffc5ac10c41ad6")
    version("17.0", sha256="4d8d4793ce3c926c54e09a5a5968fa959fe0ba46bd2e6b8043e099528ee35a60")

    # Variant for MAXNEL, we need to read this from user
    variant(
        "MAXNEL",
        default="150000",
        description="Maximum number of elements for Nek5000 tools.",
        values=is_integral,
    )

    # Variants for Nek tools
    variant("genbox", default=True, description="Build genbox tool.")
    variant("n2to3", default=True, description="Build n2to3 tool.")
    variant("postnek", default=True, description="Build postnek tool.")
    variant("reatore2", default=True, description="Build reatore2 tool.")
    variant("genmap", default=True, description="Build genmap tool.")
    variant("nekmerge", default=True, description="Build nekmerge tool.")
    variant("prenek", default=True, description="Build prenek tool.")
    variant("visit", default=False, description="Enable support for visit")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("libx11", when="+prenek")
    depends_on("libx11", when="+postnek")
    # libxt is needed for X11/Intrinsic.h but not for linking
    depends_on("libxt", when="+prenek")
    depends_on("xproto", when="+prenek")
    depends_on("libxt", when="+postnek")
    depends_on("visit", when="+visit")

    def flag_handler(self, name, flags):
        if name == "fflags":
            if self.spec.satisfies("%fortran=xl"):
                # Use '-qextname' to add underscores.
                # Use '-WF,-qnotrigraph' to fix an error about a string: '... ??'
                flags.extend(["-qextname", "-WF,-qnotrigraph"])
            elif self.spec.satisfies("%fortran=gcc"):
                # Use '-std=legacy' to suppress an error that was a warning in older gfortran.
                flags.append("-std=legacy")

        return flags, None, None

    def install(self, spec, prefix):
        tools_dir = "tools"
        bin_dir = "bin"

        fc = env["FC"]
        cc = env["CC"]

        # Build the tools, maketools copy them to Nek5000/bin by default.
        # We will then install Nek5000/bin under prefix after that.
        with working_dir(tools_dir):
            # Update the maketools script to use correct compilers
            filter_file(r"^#FC\s*=.*", 'FC="{0}"'.format(fc), "maketools")
            filter_file(r"^#CC\s*=.*", 'CC="{0}"'.format(cc), "maketools")

            if spec.satisfies("%fortran=xl"):
                # 'xl' adds underscores with '-qextname', so patch the check in 'maketools'.
                filter_file(r"^\$FC -c ", "$FC -qextname -c ", "maketools")

            libx11_lib = find_libraries(
                "libX11", spec["libx11"].prefix.lib, shared=True, recursive=True
            )
            if not libx11_lib:
                libx11_lib = find_libraries(
                    "libX11", spec["libx11"].prefix.lib64, shared=True, recursive=True
                )
            if not libx11_lib:
                raise RuntimeError("libX11 not found in %s/{lib,lib64}" % spec["libx11"].prefix)
            # There is no other way to set the X11 library path except brute
            # force:
            filter_file(r"-L\$\(X\)", libx11_lib.search_flags, join_path("prenek", "makefile"))
            filter_file(r"-L\$\(X\)", libx11_lib.search_flags, join_path("postnek", "makefile"))

            if spec.satisfies("%fortran=xl"):
                # Use '-qextname' when compiling mxm.f
                filter_file(r"\$\(OLAGS\)", "-qextname $(OLAGS)", join_path("postnek", "makefile"))
            # Define 'rename_' function that calls 'rename'
            with open(join_path("postnek", "xdriver.c"), "a") as xdriver:
                xdriver.write("\nvoid rename_(char *from, char *to)\n{\n   rename(from, to);\n}\n")

            maxnel = self.spec.variants["MAXNEL"].value
            filter_file(r"^#MAXNEL\s*=.*", "MAXNEL=" + maxnel, "maketools")

            maketools = Executable("./maketools")

            # Build the tools
            if spec.satisfies("+genbox"):
                maketools("genbox")
            if spec.satisfies("+n2to3"):
                maketools("n2to3")
            if spec.satisfies("+postnek"):
                maketools("postnek")
            if spec.satisfies("+reatore2"):
                maketools("reatore2")
            if spec.satisfies("+genmap"):
                maketools("genmap")
            if spec.satisfies("+nekmerge"):
                maketools("nekmerge")
            if spec.satisfies("+prenek"):
                maketools("prenek")

        # Install Nek5000/bin in prefix/bin
        install_tree(bin_dir, prefix.bin)
