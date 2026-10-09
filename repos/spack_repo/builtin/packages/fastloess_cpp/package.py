# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class FastloessCpp(CargoPackage):
    """High-performance LOESS (Locally Estimated Scatterplot Smoothing)
    C++ bindings, implemented in Rust."""

    homepage = "https://github.com/thisisamirv/loess-project"
    url = "https://github.com/thisisamirv/loess-project/archive/refs/tags/v2.0.0.tar.gz"
    git = "https://github.com/thisisamirv/loess-project.git"

    maintainers("thisisamirv")

    license("MIT OR Apache-2.0", checked_by="thisisamirv")

    # version() lines below are appended/updated by release-cpp.yml's
    # spack-release job on every release; keep newest first.
    version(
        "2.0.0",
        sha256="9a6b5bfd879b321af54e4cae016716b74499a50d0cecb8e3665ce1ed9703968c",
    )
    version(
        "1.1.0",
        sha256="ba786a2984431bb18480f055fc29dc52c4f0c69f44a961be35541bca07549869",
    )

    depends_on("c", type="build")
    depends_on("rust@1.89:", type="build")

    @property
    def headers(self):
        return find_headers("fastloess", root=self.prefix.include, recursive=False)

    @property
    def libs(self):
        return find_libraries("libfastloess_cpp", root=self.prefix, recursive=True)

    def build(self, spec, prefix):
        # bindings/cpp is a member of the repo's Cargo workspace, so the
        # build output lands in target/release at the workspace root, not
        # under bindings/cpp/target -- build by package name instead of cd'ing.
        cargo("build", "--release", "--lib", "-p", "fastloess-cpp")

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        mkdirp(prefix.lib)
        include_dir = join_path("bindings", "cpp", "include")
        install(join_path(include_dir, "fastloess.hpp"), prefix.include)
        install(join_path(include_dir, "fastloess.h"), prefix.include)

        release_dir = join_path("target", "release")
        if spec.satisfies("platform=windows"):
            mkdirp(prefix.bin)
            install(join_path(release_dir, "fastloess_cpp.dll"), prefix.bin)
            install(join_path(release_dir, "fastloess_cpp.dll.lib"), prefix.lib)
        elif spec.satisfies("platform=darwin"):
            install(join_path(release_dir, "libfastloess_cpp.dylib"), prefix.lib)
        else:
            install(join_path(release_dir, "libfastloess_cpp.so"), prefix.lib)
        install(join_path(release_dir, "libfastloess_cpp.a"), prefix.lib)
