# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *


class Bbmap(MakefilePackage, SourceforgePackage):
    """Short read aligner for DNA and RNA-seq data."""

    homepage = "https://bbmap.org/tools/bbmap"
    sourceforge_mirror_path = "bbmap/BBMap_38.63.tar.gz"

    license("BSD-3-Clause-LBNL")

    version("39.59", sha256="a657b6f04f35125b31e431317927d3adc0a3d3655a36014aceb0e3fceb0d4cb0")
    version("39.01", sha256="98608da50130c47f3abd095b889cc87f60beeb8b96169b664bc9d849abe093e6")
    version("38.63", sha256="089064104526c8d696164aefa067f935b888bc71ef95527c72a98c17ee90a01f")
    version("37.78", sha256="f2da19f64d2bfb7db4c0392212668b425c96a27c77bd9d88d8f0aea90a193509")
    version("37.36", sha256="befe76d7d6f3d0f0cd79b8a01004a2283bdc0b5ab21b0743e9dbde7c7d79e8a9")

    variant(
        "usejni",
        default=False,
        description=(
            "Compile the libbbtoolsjni library for accelerated versions of BBMap, Dedupe, "
            "BBMerge, and IceCreamFinder"
        ),
    )

    # Building BBMap's jni libraries requires gcc, per the BBMap docs
    depends_on("c", type="build", when="+usejni")
    requires("%c=gcc", when="+usejni")
    depends_on("java@8:", type=("build", "link", "run"))

    def edit(self, spec, prefix):
        makefile = "makefile.linux"

        if spec.satisfies("platform=darwin"):
            makefile = "makefile.osx"

        with working_dir(join_path(self.build_directory, "jni")):
            rename(makefile, "Makefile")

    @when("+usejni")
    def build(self, spec, prefix):
        with working_dir(join_path(self.build_directory, "jni")):
            # BBMap comes with a pre-compiled x86_64 library that must first be removed
            make("clean")
            make()

    @when("~usejni")
    def build(self, spec, prefix):
        with working_dir(join_path(self.build_directory, "jni")):
            # When not building libbbtoolsjni, we should still remove the pre-compiled
            # library for x86_64, as it may fail on other platforms.
            make("clean")

    def install(self, spec, prefix):
        install_tree(".", prefix.bin)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("BBMAP_CONFIG", self.prefix.bin.config)
        env.set("BBMAP_RESOURCES", self.prefix.bin.resources)
