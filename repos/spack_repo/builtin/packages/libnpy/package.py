# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Libnpy(Package):
    """libnpy is a header-only C++ library for reading and writing NumPy
    ``.npy``/``.npz`` files. Used by ABACUS for DeePKS/ML descriptor I/O."""

    homepage = "https://github.com/llohse/libnpy"
    url = "https://github.com/llohse/libnpy/archive/refs/tags/v1.0.1.tar.gz"

    maintainers("s8ga")

    version("1.0.1", sha256="43452a4db1e8c1df606c64376ea1e32789124051d7640e7e4e8518ab4f0fba44")
    version("1.0", sha256="512ba412ec800e5da5075293941b36f7c47bcea09b6ad79934d8461d674bbc39")

    license("MIT", checked_by="s8ga")

    depends_on("cxx", type="build")

    sanity_check_is_file = [join_path("include", "npy.hpp")]

    def install(self, spec, prefix):
        install_tree("include", prefix.include)
