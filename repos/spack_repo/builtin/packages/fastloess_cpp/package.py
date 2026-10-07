# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import textwrap
from typing import ClassVar

from spack.package import *
from spack_repo.builtin.build_systems.cargo import CargoPackage


class FastloessCpp(CargoPackage):
    """High-performance LOESS (Locally Estimated Scatterplot Smoothing)
    C++17 bindings, implemented in Rust. Supports multivariate batch,
    streaming, and online smoothing, robust outlier handling, confidence and
    prediction intervals, cross-validation, and parallel execution. Provides
    shared and static libraries with an owning C++ interface and a
    C-compatible API."""

    homepage = "https://thisisamirv.github.io/loess-project/cpp/"
    url = "https://github.com/thisisamirv/loess-project/archive/refs/tags/v3.0.0.tar.gz"
    git = "https://github.com/thisisamirv/loess-project.git"

    test_requires_compiler = True
    sanity_check_is_file: ClassVar[list[str]] = [
        join_path("include", "fastloess.hpp"),
        join_path("include", "fastloess.h"),
    ]
    sanity_check_is_dir: ClassVar[list[str]] = ["include", "lib"]

    maintainers("thisisamirv")

    license("MIT OR Apache-2.0", checked_by="thisisamirv")

    # version() lines below are appended/updated by release-cpp.yml's
    # spack-release job on every release; keep newest first.
    version("3.0.0", sha256="33940eaa0c6d972194225060d6ab95361e3664f685578855fe6f5da4cfad926e")
    version(
        "2.0.0",
        sha256="9a6b5bfd879b321af54e4cae016716b74499a50d0cecb8e3665ce1ed9703968c",
    )
    version(
        "1.1.0",
        sha256="ba786a2984431bb18480f055fc29dc52c4f0c69f44a961be35541bca07549869",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
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
        version_header = join_path(include_dir, "fastloess_version.h")
        if os.path.isfile(version_header):
            install(version_header, prefix.include)

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

    def test_cxx_smoke(self):
        """Compile and run a linear fit against the installed C++ library."""
        source = "fastloess_spack_smoke.cpp"
        with open(source, "w", encoding="utf-8") as stream:
            stream.write(
                textwrap.dedent("""\
                #include <fastloess.hpp>
                #include <cmath>
                #include <vector>

                int main() {
                    const std::vector<double> x = {1, 2, 3, 4, 5, 6};
                    const std::vector<double> y = {3, 5, 7, 9, 11, 13};
                    fastloess::LoessOptions options;
                    options.fraction = 1.0;
                    options.iterations = 0;
                    options.parallel = false;
                    options.boundary_policy = "noboundary";
                    options.surface_mode = "direct";
                    fastloess::Loess model(options);
                    const auto result = model.fit(x, y).value();
                    if (!result.valid() || result.size() != y.size()) return 1;
                    for (std::size_t index = 0; index < y.size(); ++index) {
                        const double fitted = result.y_value(index);
                        if (!std::isfinite(fitted) ||
                            std::abs(fitted - y[index]) > 1e-8) return 2;
                    }
                    return 0;
                }
                """)
            )

        cxx = which(os.environ["CXX"])
        windows = self.spec.satisfies("platform=windows")
        executable = "fastloess_spack_smoke.exe" if windows else "fastloess_spack_smoke"
        compiler_name = os.path.basename(os.environ["CXX"]).lower()
        if compiler_name in ("cl", "cl.exe", "clang-cl", "clang-cl.exe"):
            cxx(
                "/std:c++17",
                "/EHsc",
                f"/I{self.prefix.include}",
                source,
                join_path(self.prefix.lib, "fastloess_cpp.dll.lib"),
                f"/Fe:{executable}",
            )
        else:
            link_flags = (
                [join_path(self.prefix.lib, "fastloess_cpp.dll.lib")]
                if windows
                else [
                    f"-L{self.prefix.lib}",
                    "-lfastloess_cpp",
                    f"-Wl,-rpath,{self.prefix.lib}",
                ]
            )
            cxx(
                "-std=c++17",
                f"-I{self.prefix.include}",
                source,
                *link_flags,
                "-o",
                executable,
            )

        smoke = Executable(join_path(os.getcwd(), executable))
        if windows:
            smoke.add_default_env(
                "PATH",
                os.pathsep.join([str(self.prefix.bin), os.environ.get("PATH", "")]),
            )
        smoke()
