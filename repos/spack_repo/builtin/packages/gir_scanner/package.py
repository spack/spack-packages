# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems import meson
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class GirScanner(MesonPackage):
    """The gi-r-scanner is from the GObject Introspection and required for building full glib."""

    homepage = "https://wiki.gnome.org/Projects/GObjectIntrospection"
    url = "https://download.gnome.org/sources/gobject-introspection/1.72/gobject-introspection-1.72.0.tar.xz"

    maintainers("michaelkuhn")

    license("LGPL-2.0-or-later AND GPL-2.0-or-later AND MIT")

    version("1.86.0", sha256="920d1a3fcedeadc32acff95c2e203b319039dd4b4a08dd1a2dfd283d19c0b9ae")

    depends_on("c", type="build")  # generated

    depends_on("pkgconfig", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")

    # Does not build with sed from Darwin
    depends_on("sed", when="platform=darwin", type="build")

    # depends_on("cairo+gobject")
    depends_on("glib-bootstrap@2.86:", when="@1.86", type="link")

    depends_on("libffi")
    depends_on("python", type=("build", "run"))

    with when("^python@3.12:"):
        depends_on("py-setuptools@48:", type=("build", "run"))
        patch("setuptools.patch", when="@1.78:")

    # g-ir-scanner uses distutils
    # - https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/361
    # - https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/395
    # for new enough versions we import setuptools first
    # patch("setuptools.patch", when="@1.78: ^python@3.12:")

    def url_for_version(self, version):
        url = "https://download.gnome.org/sources/gobject-introspection/{0}/gobject-introspection-{1}.tar.xz"
        return url.format(version.up_to(2), version)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("GI_SCANNER_DISABLE_CACHE", "1")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))
        env.set("GI_SCANNER_DISABLE_CACHE", "1")

    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))

    @property
    def parallel(self):
        return not self.spec.satisfies("%fj")


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        args = []
        args.append("-Dcairo=disabled")
        args.append("-Ddoctool=disabled")
        # args.append("-Dbuild_introspection_data=false")

        return args

    @run_after("install")
    def clean_install(self):
        rm = which("rm")
        binaries = ["g-ir-compiler", "g-ir-generate", "g-ir-annotation-tool", "g-ir-inspect"]
        rm("-r", self.prefix.include, join_path(self.prefix.share, "man"))
        rm("-r", join_path(self.prefix.share, "aclocal"))
        for b in binaries:
            rm(join_path(self.prefix.bin, b))
