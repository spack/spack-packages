# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Osmosis(Package):
    """Osmosis is a Java application and library for processing OSM data."""

    homepage = "https://wiki.openstreetmap.org/wiki/Osmosis"
    url = "https://github.com/openstreetmap/osmosis/archive/refs/tags/0.49.2.tar.gz"

    license("Unlicense", checked_by="mtpham99")  # "Public Domain" specified in "build.gradle"

    version("0.49.2", sha256="b355771c35f326ee45431916c2ebe3f81a09ba571c03c3302f5268103f7b7e3c")

    depends_on("java@17", type=("build", "run"), when="@0.49:")
    depends_on("tar", type="build")

    def install(self, spec, prefix):
        tar = which("tar", required=True)
        gradlew = Executable("./gradlew")

        gradlew("--info", "--debug", "clean", "assemble")

        with working_dir("osmosis/build/distributions"):
            tar("xvf", "osmosis--SNAPSHOT.tar", "--strip-components", "1", "--directory", prefix)
