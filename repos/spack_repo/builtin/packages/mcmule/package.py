# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems import meson
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Mcmule(MesonPackage):
    """McMule (Monte Carlo for MUons and other LEptons) is a framework for
    fully differential higher-order QED calculations of scattering and decay
    processes involving leptons."""

    homepage = "https://mcmule.readthedocs.io"
    git = "https://gitlab.com/mule-tools/mcmule.git"

    maintainers("wdconinc")

    tags = ["hep"]

    license("GPL-3.0-or-later", checked_by="wdconinc")

    # OpenLoops, COLLIER, handyG, alphaQED and pymule are vendored as git
    # submodules and built as meson subprojects without external dependency
    # fallback.
    version("devel", branch="devel", submodules=True)
    version(
        "0.8.0", tag="v0.8.0", commit="de32e762ca44ab82345d4a511f7b64ab61ba9bd4", submodules=True
    )
    version(
        "0.7.0", tag="v0.7.0", commit="60997e6591302353c0499f6b87ff8c079116268c", submodules=True
    )
    version(
        "0.6.0", tag="v0.6.0", commit="f47f986f304e77c7090992b5a526f25293e06b4d", submodules=True
    )

    variant(
        "groups",
        values=disjoint_sets(
            ("auto",), ("misc", "mue", "nucl", "mudecrare", "mudec", "ee", "pie", "gg")
        )
        .prohibit_empty_set()
        .with_default("auto")
        .with_non_feature_values("auto"),
        description="Process groups to build (auto: upstream default)",
    )
    variant("examples", default=False, description="Build the examples")

    conflicts("groups=pie", when="@:0.6")
    conflicts("groups=gg", when="@:0.6")

    # Linking against system OpenLoops (needed for static builds) requires
    # matching git checkouts in the source tree, which spack does not provide.
    conflicts("default_library=static", msg="McMule only supports shared builds in Spack")
    # The meson buildtype logic only defines optimization levels for these
    requires("buildtype=release", "buildtype=debug", policy="one_of")

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    requires("%fortran=gcc", msg="McMule only supports gfortran")

    depends_on("meson@0.58:", type="build")
    depends_on("python@3.7:", type="build")  # for tools/pymule submodule

    def patch(self):
        # alphaQED does not install the NSK and KNTW libraries that libmcmule links to
        for build_file, sources in (
            ("nsk-v2.9/meson.build", "vpolNsk.f95"),
            ("kntw-v3.1/meson.build", "vp_kntw_v3_1.f95"),
        ):
            path = join_path("subprojects", "alphaQED", build_file)
            if os.path.exists(path):
                filter_file(rf"^(\s*\['{re.escape(sources)}'.*\],)$", r"\1 install : true,", path)


class MesonBuilder(meson.MesonBuilder):
    def build(self, pkg, spec, prefix):
        # OpenLoops' HLvertices.F90 defines two modules, but meson's dependency
        # scanner only records one module per file, so the process libraries
        # can race ahead of hol_initialisation_dp.mod. Build the core first.
        with working_dir(self.build_directory):
            pkg.module.ninja(
                "-v",
                join_path(
                    "subprojects",
                    "OpenLoops",
                    "lib_src",
                    "openloops",
                    f"libopenloops.{dso_suffix}",
                ),
            )
        super().build(pkg, spec, prefix)

    def meson_args(self):
        args = [
            "-Dtests=false",
            f"-Dexamples={str(self.spec.satisfies('+examples')).lower()}",
        ]
        groups = self.spec.variants["groups"].value
        if "auto" not in groups:
            args.append(f"-Dgroups={','.join(groups)}")
        return args
