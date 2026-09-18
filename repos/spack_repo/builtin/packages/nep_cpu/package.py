# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class NepCpu(Package):
    """NEP_CPU is a standalone C++ implementation of the neuroevolution
    potential (NEP) from the GPUMD project. Used by ABACUS (@3.9.0.27:
    with +nep) as an external NEP library via CMake's FindNEP."""

    homepage = "https://github.com/brucefan1983/NEP_CPU"
    url = "https://github.com/brucefan1983/NEP_CPU/archive/refs/tags/v1.4.tar.gz"

    maintainers("s8ga")

    license("GPL-3.0-or-later", checked_by="s8ga")

    version("1.4", sha256="8a1689fee2954d7fe24bd0c65f7069df8d9c6d82a2095bcb95094d8849e14882")

    depends_on("cxx", type="build")

    sanity_check_is_file = [join_path("lib", "libnep.a"), join_path("include", "nep.h")]

    def install(self, spec, prefix):
        # NEP_CPU ships no build system; compile src/ manually and archive.
        # Use src/ (class NEP), not libs/include/, which still carries the
        # stale NEP3 class in v1.4 — ABACUS expects class NEP.
        mkdirp(prefix.include, prefix.lib)

        for header in ("nep.h", "nep_utilities.h", "neighbor_nep.h", "ewald_nep.h", "dftd3para.h"):
            install(join_path("src", header), prefix.include)

        cxx = which(os.environ["CXX"])
        objects = []
        for source in ("nep.cpp", "neighbor_nep.cpp", "ewald_nep.cpp"):
            obj = source.replace(".cpp", ".o")
            cxx(
                "-fPIC",
                "-std=c++11",
                f"-I{prefix.include}",
                "-c",
                join_path("src", source),
                "-o",
                obj,
            )
            objects.append(obj)

        ar = which("ar")
        ar("rcs", join_path(prefix.lib, "libnep.a"), *objects)
