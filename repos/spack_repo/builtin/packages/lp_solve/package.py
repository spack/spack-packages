# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class LpSolve(Package):
    """lp_solve is a Mixed Integer Linear Programming (MILP) solver."""

    homepage = "https://sourceforge.net/projects/lpsolve/"
    url = "https://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.11/lp_solve_5.5.2.11_source.tar.gz"

    version("5.5.2.11", sha256="6d4abff5cc6aaa933ae8e6c17a226df0fc0b671c438f69715d41d09fe81f902f")

    depends_on("c", type="build")  # generated

    def install(self, spec, prefix):
        # GCC 14+ breaks their isnan() detection and causes failures in the build.
        # GCC 15+ gnu23 default drops implicit-int support, so pin -std=gnu17
        cc_flags = []
        if spec.satisfies("%gcc@14:"):
            cc_flags += ["-Wno-error=implicit-int", "-Wno-error=implicit-function-declaration"]
        if spec.satisfies("%gcc@15:"):
            cc_flags.append("-std=gnu17")
        cc_line = 'c="cc ' + " ".join(cc_flags) + '"' if cc_flags else "c=cc"

        with working_dir("lpsolve55"):
            mkdir(prefix.lib)
            if cc_flags:
                filter_file("^c=cc$", cc_line, "ccc")
            sh = which("sh", required=True)
            sh("-x", "ccc")
            install_tree("bin/ux64", prefix.lib)
        with working_dir("lp_solve"):
            mkdir(prefix.bin)
            if cc_flags:
                filter_file("^c=cc$", cc_line, "ccc")
            sh = which("sh", required=True)
            sh("-x", "ccc")
            install_tree("bin/ux64", prefix.bin)

        mkdirp(prefix.include.lpsolve)
        headers = find(".", "*.h", recursive=False)
        for header in headers:
            install(header, prefix.include.lpsolve)
