# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Hdf5VolLog(AutotoolsPackage):
    """Log-based VOL - an HDF5 VOL Plugin that stores HDF5 datasets in a log-based
    storage layout."""

    homepage = "https://github.com/DataLib-ECP/vol-log-based"
    url = "https://github.com/DataLib-ECP/vol-log-based"
    git = "https://github.com/DataLib-ECP/vol-log-based.git"
    maintainers("hyoklee", "lrknox")

    tags = ["e4s"]

    version("master-1.1", branch="master")

    version("1.4.0", tag="logvol.1.4.0", commit="786d2cc4da8b4a0827ee00b1b0ab3968ef942f99")

    variant("hdf5_examples", default=True, description="Enable HDF5 examples", when="@1.4.0")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("hdf5@1.14.0:", when="@1.4.0:")
    depends_on("mpi")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    # Adds an option to disable examples downloaded during build
    # https://github.com/HDFGroup/vol-log-based/pull/79
    patch("hdf5_examples_option.patch", when="@1.4.0")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("HDF5_PLUGIN_PATH", self.spec.prefix.lib)

    def configure_args(self):
        args = [
            "--enable-shared",
            "--enable-zlib",
            "--with-mpi={}".format(self.spec["mpi"].prefix),
        ]
        args.extend(self.enable_or_disable("hdf5-examples", variant="hdf5_examples"))
        return args
