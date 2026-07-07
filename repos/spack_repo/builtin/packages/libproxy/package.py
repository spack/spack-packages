# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import cmake, meson
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Libproxy(CMakePackage, MesonPackage):
    """libproxy is a library that provides automatic proxy configuration
    management."""

    homepage = "https://libproxy.github.io/libproxy/"
    url = "https://github.com/libproxy/libproxy/archive/0.4.15.tar.gz"

    license("LGPL-2.0-or-later")

    build_system(
        conditional("meson", when="@0.5:"), conditional("cmake", when="@:0.4"), default="meson"
    )

    version("0.5.11", sha256="b364f4dbbffc5bdf196330cb76b48abcb489f38b1543e67595ca6cb7ec45d265")
    version("0.5.10", sha256="84734a0b89c95f4834fd55c26b362be2fb846445383e37f5209691694ad2b5de")
    version("0.5.9", sha256="a1976c3ac4affedc17e6d40cf78c9d8eca6751520ea3cbbec1a8850f7ded1565")
    version("0.5.8", sha256="64e363855012175bf796b37cacddf7bc7e08af0bf406eea94b549ce207987d3e")
    version("0.5.7", sha256="ca64b28a014cffde43f4052ec78b25a8a0f1aa4d78da721c605d64b1591e78dd")
    version("0.5.6", sha256="68cb4548143e843826a35e024dba8ced92117c0982c2cc9a4c8247e32d259603")
    version("0.5.5", sha256="11a2eace773755e79b8d37833985ce475aed4ca4d3e6656defd5eef67b5a00f1")
    version("0.5.4", sha256="a6e2220349b2025de9b6d9d7f8bb347bf0c728f02a921761ad5f9f66c7436de9")
    version("0.5.3", sha256="0d8d8e4dd96239ba173c2b18905c0bb6e161fd5000e1e0aeace16f754e9a9108")
    version("0.5.2", sha256="7d75a2cf1c977056eb86f460daab0247d30e6a34e26ec755aab4de40cfd0a06d")
    version("0.4.18", sha256="0b4a9218d88f6cf9fa25996a3f38329a11f688a9d026141d9d0e966d8fa63837")
    version("0.4.17", sha256="88c624711412665515e2800a7e564aabb5b3ee781b9820eca9168035b0de60a9")
    version("0.4.16", sha256="9e7959d6ae1d6c817f0ac1e253105ce8d99f55d7821c1b6eaef32bf6879c6f0a")
    version("0.4.15", sha256="18f58b0a0043b6881774187427ead158d310127fc46a1c668ad6d207fb28b4e0")
    version("0.4.14", sha256="6220a6cab837a8996116a0568324cadfd09a07ec16b930d2a330e16d5c2e1eb6")
    version("0.4.13", sha256="d610bc0ef81a18ba418d759c5f4f87bf7102229a9153fb397d7d490987330ffd")

    variant("perl", default=False, description="Enable Perl bindings")
    variant("python", default=False, description="Enable Python bindings", when="@0.4.14:0.4")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("zlib-api")
    depends_on("perl", type=("build", "run"), when="+perl")
    depends_on("glib@2.71.3:", when="@0.5:")
    depends_on("curl", when="@0.5:")
    depends_on("gsettings-desktop-schemas", when="@0.5:")
    depends_on("gobject-introspection", when="@0.5:")
    depends_on("vala", when="@0.5:")

    extends("python", when="+python")

    @property
    def libs(self):
        return find_libraries(
            ["libproxy", "libproxy/*"], root=self.prefix, shared=True, recursive=True
        )


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_PERL", "perl"),
            self.define_from_variant("WITH_PYTHON3", "python"),
            self.define("WITH_DOTNET", False),
            self.define("WITH_PYTHON2", False),
            self.define("WITH_VALA", False),
        ]
        if self.spec.satisfies("+python"):
            args.append(self.define("PYTHON3_SITEPKG_DIR", python_platlib))
        return args


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        return ["-Dpacrunner-duktape=False", "-Ddocs=False"]
