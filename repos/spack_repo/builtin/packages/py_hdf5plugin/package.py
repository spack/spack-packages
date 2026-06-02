# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHdf5plugin(PythonPackage):
    """hdf5plugin provides HDF5 compression filters (namely: Blosc, Blosc2,
    BitShuffle, BZip2, FciDecomp, LZ4, Sperr, SZ, SZ3, Zfp, ZStd) and makes
    them usable from h5py."""

    homepage = "https://github.com/silx-kit/hdf5plugin"
    pypi = "hdf5plugin/hdf5plugin-6.0.0.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("6.0.0", sha256="847ed9e96b451367a110f0ba64a3b260d38d64bbf3f25751858d3b56e094cfe0")

    variant("openmp", default=True, description="Build with OpenMP support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-setuptools@77:", type="build")
    depends_on("py-py-cpuinfo@9.0.0", type="build")

    depends_on("py-h5py@3:", type=("build", "run"))

    def setup_build_environment(self, env):
        env.set("HDF5PLUGIN_HDF5_DIR", self.spec["hdf5"].prefix)

        # Disable all optimizations as set by script
        # Spack compiler wrapper will handle it all on its own
        for feat in ["SSE2", "SSSE3", "AVX2", "AVX512", "NATIVE"]:
            env.set(f"HDF5PLUGIN_{feat.upper()}", "False")

        if "+openmp" in self.spec:
            env.set("HDF5PLUGIN_OPENMP", "True")
