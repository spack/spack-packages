# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *


class Glx(BundlePackage):
    """Shim package for the GLX library."""

    homepage = "https://www.khronos.org/registry/OpenGL/index_gl.php"

    version("1.4")

    # GLX is only supported on Linux-like platforms
    conflicts("platform=windows")
    conflicts("platform=darwin")

    depends_on("libglx")
    provides("gl@4.5")

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ):
        env.prepend_path("OpenGL_ROOT", self.home)

    @property
    def home(self):
        return self.spec["libglx"].home

    @property
    def headers(self):
        return self.spec["libglx"].headers

    @property
    def libs(self):
        return self.spec["libglx"].libs

    @property
    def gl_headers(self):
        return find_headers("GL/gl", root=self.gl_home, recursive=True)

    @property
    def gl_libs(self):
        return self.spec["libglx"].libs
