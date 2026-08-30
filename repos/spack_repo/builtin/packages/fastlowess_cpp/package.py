# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#
# This file is the source of truth for the fastlowess-cpp Spack recipe. It
# is mirrored into spack/spack-packages by dev/spack_open_pr.sh, which runs
# on every GitHub release (see .github/workflows/release-cpp.yml).
#
# Spack's package API (spack.package, spack_repo.builtin.*) only resolves
# inside a full Spack installation, which isn't present in this workspace.
# pyright: reportMissingImports=false, reportUndefinedVariable=false, reportCallIssue=false

from spack.package import *
from spack_repo.builtin.build_systems.cargo import CargoPackage


class FastlowessCpp(CargoPackage):
    """High-performance LOWESS (Locally Weighted Scatterplot Smoothing)
    C++ bindings, implemented in Rust."""

    homepage = "https://github.com/thisisamirv/lowess-project"
    url = (
        "https://github.com/thisisamirv/lowess-project/archive/refs/tags/v3.1.0.tar.gz"
    )
    git = "https://github.com/thisisamirv/lowess-project.git"

    maintainers("thisisamirv")

    license("MIT OR Apache-2.0", checked_by="thisisamirv")

    # version() lines below are appended/updated by dev/spack_release.py on
    # every release; keep newest first.
    version("3.1.0", sha256="610a6af65a3e8eaa5483332c256e7ce6c3fe2b7ac3ec0f04e08ecd70bf6abe0f")
    version(
        "3.1.0",
        sha256="610a6af65a3e8eaa5483332c256e7ce6c3fe2b7ac3ec0f04e08ecd70bf6abe0f",
    )

    depends_on("c", type="build")
    depends_on("rust@1.89:", type="build")

    build_directory = "bindings/cpp"

    @property
    def headers(self):
        return find_headers("fastlowess", root=self.prefix.include, recursive=False)

    @property
    def libs(self):
        return find_libraries("libfastlowess_cpp", root=self.prefix, recursive=True)

    def build(self, spec, prefix):
        with working_dir(self.build_directory):
            cargo("build", "--release", "--lib")

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            mkdirp(prefix.include)
            mkdirp(prefix.lib)
            install(join_path("include", "fastlowess.hpp"), prefix.include)
            install(join_path("include", "fastlowess.h"), prefix.include)

            release_dir = join_path("target", "release")
            if spec.satisfies("platform=windows"):
                mkdirp(prefix.bin)
                install(join_path(release_dir, "fastlowess_cpp.dll"), prefix.bin)
                install(join_path(release_dir, "fastlowess_cpp.dll.lib"), prefix.lib)
            elif spec.satisfies("platform=darwin"):
                install(join_path(release_dir, "libfastlowess_cpp.dylib"), prefix.lib)
            else:
                install(join_path(release_dir, "libfastlowess_cpp.so"), prefix.lib)
            install(join_path(release_dir, "libfastlowess_cpp.a"), prefix.lib)
