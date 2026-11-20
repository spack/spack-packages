# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class GolangciLint(GoPackage):
    """golangci-lint is a fast Go linters runner. It runs linters in parallel,
    uses caching, supports YAML configuration, integrates with all major IDEs,
    and includes over a hundred linters."""

    homepage = "https://github.com/golangci/golangci-lint"

    git = "https://github.com/golangci/golangci-lint.git"

    maintainers("ebagrenrut")

    license("GPL-3.0-only")

    # Note: We use a git-versioned package instead of an archive because the
    # golangci-lint build process relies on repo-derived metadata to define variable
    # values used when tracking its version.
    version("2.15.0", tag="v2.15.0", commit="25c5369a93aacb8cccea0d46e1569ca4a194564d")

    depends_on("go@1.26:", type="build")

    build_directory = "cmd/golangci-lint"
