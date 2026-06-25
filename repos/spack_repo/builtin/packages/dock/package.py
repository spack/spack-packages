# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Dock(Package):
    """DOCK is a molecular docking program used in drug discovery.

    This program, given a protein binding site and a small molecule, tries
    to predict the correct binding mode of the small molecule in the binding
    site, and the associated binding energy."""

    homepage = "http://dock.compbio.ucsf.edu/DOCK_6/index.htm"
    url = "https://github.com/docking-org/dock6/archive/refs/tags/v6.13.1.tar.gz"

    maintainers("snehring")

    license("BSD-3-Clause", checked_by="snehring")

    with when("@=6.9"):
        manual_download = True

    version("6.13.1", sha256="1bfe7ff777e60af6bff785dc74f9f7d1b0403c518c34ce4d1e6db98ac0865db1")

    # I don't think you can actually get 6.9 anymore since they moved to github
    version(
        "6.9",
        sha256="c2caef9b4bb47bb0cb437f6dc21f4c605fd3d0d9cc817fa13748c050dc87a5a8",
        deprecated=True,
        url=f"file://{os.getcwd()}/dock.6.9_source.tar.gz",
    )

    variant("mpi", default=True, description="Enable mpi")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("gmake", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("mpi", when="+mpi")

    def install(self, spec, prefix):
        mkdirp("bin")
        # the object files aren't regenerated after the clean target runs, so let's just not do it
        with working_dir(join_path("src", "docktools", "convgrids")):
            for i in ["gridrdsl.mk", "gridconv.mk"]:
                filter_file("install: clean all", "install: all", i)
        with working_dir("install"):
            copy("gnu", "config.h")
            for i in [r"^CC=.*$", r"^CXX=.*$", r"^FC=.*$"]:
                filter_file(i, "", "config.h")
            filter_file(
                r"^FFLAGS=.*$",
                "FFLAGS=-fno-automatic -fno-second-underscore -fallow-argument-mismatch",
                "config.h",
            )
            if self.spec.satisfies("+mpi"):
                filter_file(r"^CXXFLAGS=.*$", "CXXFLAGS=-DBUILD_DOCK_WITH_MPI", "config.h")
                filter_file(r"CFLAGS=.*$", "CFLAGS=-DBUILD_DOCK_WITH_MPI", "config.h")
                filter_file(r"^DOCK_SUFFIX=.*", "DOCK_SUFFIX=.mpi", "config.h")
                filter_file(r"^LOAD=.*$", f"LOAD={self.spec['mpi'].mpicxx}", "config.h")
            else:
                filter_file(r"^LOAD=.*$", f"LOAD={self.compiler.cxx}", "config.h")
                filter_file(r"^CFLAGS=.*", "", "config.h")

            with open("config.h", "a", encoding="UTF-8") as f:
                f.write(f"DOCKHOME={self.spec.prefix}")
            which("make")("dock")
            which("make")("utils")

        mkdirp(prefix.bin)
        install_tree("bin", prefix.bin)
