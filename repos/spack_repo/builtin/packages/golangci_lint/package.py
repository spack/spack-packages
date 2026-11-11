# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class GoLangCiLint(GoPackage):
    """golangci-lint is a fast Go linters runner. It runs linters in parallel,
    uses caching, supports YAML configuration, integrates with all major IDEs,
    and includes over a hundred linters."""

    homepage = "https://github.com/golangci/golangci-lint"
    url = "https://github.com/golangci/golangci-lint/archive/refs/tags/v2.15.0.tar.gz"

    license("GPL-3.0-only")

    maintainers("ebagrenrut")

    version("2.15.0", sha256="5411598703f014f1128b209f3d46da6f9f2c99a68783c90f846b4db1c8c08742")

    depends_on("go@1.26:", type="build")

    build_args = [join_path(self.stage.source_path, "cmd", "golangci-lint")]
