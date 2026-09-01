# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import glob
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Coolprop(CMakePackage):
    """CoolProp is a C++ library that implements pure and pseudo-pure fluid
    equations of state and transport properties for 122 components, as well
    as mixture properties using high-accuracy Helmholtz-energy-based mixing
    rules.
    """

    homepage = "https://coolprop.org/"
    url = "https://github.com/CoolProp/CoolProp/archive/refs/tags/v6.8.0.tar.gz"
    git = "https://github.com/CoolProp/CoolProp.git"

    license("MIT")

    version("8.0.0", tag="v8.0.0")
    version("develop", branch="master")

    variant("shared", default=True, description="Build the shared library (otherwise static)")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.14:", type="build")
    depends_on("python@3:", type="build")

    # nlohmann-json, fmt, Eigen, msgpack-c, valijson, IF97, boost-headers, and
    # multicomplex are all fetched and built by CoolProp's own cmake/dependencies.cmake
    # via CPM.cmake (pinned git tags, network access required during configure) - left
    # as CoolProp's default rather than redirected to spack-provided packages.

    def cmake_args(self):
        spec = self.spec
        shared = spec.satisfies("+shared")

        return [
            # CMakeLists.txt force-overwrites CMAKE_INSTALL_PREFIX from this
            # variable, so spack's own -DCMAKE_INSTALL_PREFIX would otherwise
            # be silently discarded.
            self.define("COOLPROP_INSTALL_PREFIX", self.prefix),
            self.define("COOLPROP_SHARED_LIBRARY", shared),
            self.define("COOLPROP_STATIC_LIBRARY", not shared),
            self.define("BUILD_TESTING", False),
            self.define("COOLPROP_EES_MODULE", False),
            self.define("COOLPROP_WINDOWS_PACKAGE", False),
        ]

    @run_after("install")
    def install_links(self):
        """CoolProp installs into shared_library/<system>/<bitness>bit/ (or the
        equivalent static_library/... layout) rather than the usual lib/,
        include/. Add the conventional symlinks so the package is usable like
        any other spack-installed library.
        """
        if self.spec.satisfies("platform=darwin"):
            system_dir = "Darwin"
        elif self.spec.satisfies("platform=windows"):
            system_dir = "Windows"
        else:
            system_dir = "Linux"

        with working_dir(self.prefix):
            if os.path.isdir("shared_library"):
                if not os.path.exists("lib"):
                    symlink(os.path.join("shared_library", system_dir, "64bit"), "lib")
                libdirs = glob.glob(os.path.join("shared_library", system_dir, "*bit*"))
                if libdirs and not os.path.exists("lib"):
                    symlink(libdirs[0], "lib")
                if not os.path.exists("include") and os.path.isdir(
                    os.path.join("shared_library", "include")
                ):
                    symlink(os.path.join("shared_library", "include"), "include")
            elif os.path.isdir("static_library"):
                if not os.path.exists("include") and os.path.isdir(
                    os.path.join("static_library", "include")
                ):
                    symlink(os.path.join("static_library", "include"), "include")
                libdirs = glob.glob(os.path.join("static_library", system_dir, "*bit*"))
                if libdirs and not os.path.exists("lib"):
                    symlink(libdirs[0], "lib")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+shared"):
            env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
