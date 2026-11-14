# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Dlv(GoPackage):
    """dlv (pronounced "delve") is a debugger for the Go programming language."""

    homepage = "https://github.com/go-delve/delve"
    url = "https://github.com/go-delve/delve/archive/refs/tags/v1.27.2.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("1.27.2", sha256="8ea5979dfc5978c9690dc1dd533a830815441dd33617f4a61bcdff7d2c3c7e90")

    depends_on("go@1.25:", type=("build", "run"))

    build_directory = "cmd/dlv"
