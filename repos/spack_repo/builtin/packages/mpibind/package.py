# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Mpibind(AutotoolsPackage):
    """A portable runtime library that automatically maps
    parallel applications to heterogeneous hardware architectures,
    optimizing resource affinity for CPUs, GPUs, and memory"""

    homepage = "https://mpibind.llnl.gov"
    git = "https://github.com/LLNL/mpibind.git"

    maintainers("eleon")

    license("MIT")

    # This package uses 'git describe --tags' to get the
    # package version in Autotools' AC_INIT, thus
    # 'get_full_repo' is needed.
    # Furthermore, the package can't be cached because
    # AC_INIT would be missing the version argument,
    # which is derived with git.
    version("master", branch="master", get_full_repo=True)
    version("0.23.0", commit="7d23407726004c7092a20ebdf6e9661f020b4ae7", no_cache=True)
    version("0.22.0", commit="7181024843b110074ad87009a7a671bb666f90a4", no_cache=True)
    version("0.21.0", commit="e8dca93adff52d464bffe7281f7ac0c3a63be4c0", no_cache=True)
    version("0.20.0", commit="8cd20ed9353a69336415193da90d86de789b1e3c", no_cache=True)

    # mpibind does not depend on CUDA or ROCm, but uses
    # these variants to configure hwloc accordingly
    variant("cuda", default=False, description="Build with support for NVIDIA GPUs")
    variant("rocm", default=False, description="Build with support for AMD GPUs")

    variant("flux", default=False, description="Build the Flux plugin")
    variant("python", default=False, description="Build the Python bindings")

    # See slurm dependency below
    # variant("slurm", default=False,
    #         description="Build the Slurm plugin")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("hwloc@2:+libxml2", type="link")
    depends_on("hwloc@2:+pci", type="link", when=(sys.platform != "darwin"))

    depends_on("hwloc@2: +cuda +nvml", type="link", when="+cuda")
    depends_on("hwloc@2.4: +rocm +opencl", type="link", when="@:0.19 +rocm")
    depends_on("hwloc@2.4: +rocm", type="link", when="@0.20: +rocm")

    # Need mpibind v0.23+ and hwloc v2.12+ for NV Grace Hopper
    depends_on("hwloc@2.12: +cuda +nvml", type="link", when="@0.23: +cuda target=neoverse_v2:")
    conflicts(
        "@:0.22 +cuda target=neoverse_v2:", msg="version 0.23+ is needed for NVIDIA Grace Hopper"
    )

    # flux-core >= 0.30.0 supports FLUX_SHELL_RC_PATH,
    # which is needed to load the plugin into Flux
    depends_on("flux-core@0.30:", type="link", when="+flux")

    # The slurm spack package does not provide
    # slurm.pc (pkgconf). If mpibind can't find
    # slurm's includedir, the plugin won't be built.
    # If slurm.pc is provided by slurm at some point,
    # uncomment the dependency below, otherwise,
    # make sure this works:
    #   pkg-config --variable=includedir slurm
    # depends_on("slurm", type="link",
    #            when="+slurm")

    depends_on("python@3:", type=("build", "run"), when="+python")
    depends_on("py-cffi", type=("build", "run"), when="+python")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")

    @when("+flux")
    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        """Load the mpibind plugin into Flux"""
        env.prepend_path("FLUX_SHELL_RC_PATH", join_path(self.prefix, "share", "mpibind"))

    # To build and run the C unit tests, make sure 'libtap'
    # is installed and recognized by pkgconfig.
    # To build and run the Python unit tests, make sure 'pycotap'
    # is installed in your Python environment.
    # Unfortunately, 'tap' and 'pycotap' are not in Spack.
