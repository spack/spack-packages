# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Ann(Package):
    """Approximate Nearest Neighbor Searching library."""

    homepage = "https://www.cs.umd.edu/~mount/ANN/"
    url = "https://www.cs.umd.edu/~mount/ANN/Files/1.1.2/ann_1.1.2.tar.gz"

    test_requires_compiler = True

    maintainers("prudhomm")

    license("LGPL-2.1-or-later")

    version("1.1.2", sha256="eea03f2e224b66813226d775053316675375dcec45bd263674c052d9324a49a5")

    depends_on("cxx", type=("build", "test"))

    conflicts("platform=windows")

    def install(self, spec, prefix):
        cxx = Executable(spack_cxx)
        mkdirp("spack-build")

        objects = []
        for source in sorted(find("src", "*.cpp")):
            stem = source.replace("/", "_").replace(".cpp", ".o")
            obj = join_path("spack-build", stem)
            cxx("-c", source, "-Iinclude", "-O3", "-fPIC", "-o", obj)
            objects.append(obj)

        ar = which("ar", required=True)
        ar("crs", "libann.a", *objects)

        mkdirp(prefix.lib)
        install("libann.a", prefix.lib)

        shared_name = "libann." + shared_library_suffix(spec)
        if spec.satisfies("platform=darwin"):
            # Use the installed path so clients can load the dylib after the stage is removed.
            shared_lib = join_path(prefix.lib, shared_name)
            cxx("-dynamiclib", "-Wl,-install_name," + shared_lib, "-o", shared_lib, *objects)
        else:
            # Preserve the existing Linux SONAME and relative symlinks.
            shared_lib = join_path(prefix.lib, shared_name + ".0.0.0")
            cxx("-shared", "-Wl,-soname," + shared_name + ".0", "-o", shared_lib, *objects)
            with working_dir(prefix.lib):
                symlink(shared_name + ".0.0.0", shared_name + ".0")
                symlink(shared_name + ".0", shared_name)

        install_tree("include/ANN", prefix.include.ANN)

    def _test_nearest_neighbor(self, linkage):
        source = join_path(self.test_suite.current_test_data_dir, "nearest_neighbor.cpp")
        executable = join_path(os.getcwd(), "ann-" + linkage)
        cxx = Executable(self.spec["cxx"].package.cxx)
        args = ["-std=c++11", source, "-I" + self.prefix.include]
        if linkage == "shared":
            args += ["-L" + self.prefix.lib, "-lann", "-Wl,-rpath," + self.prefix.lib]
        else:
            args += [join_path(self.prefix.lib, "libann.a")]
        cxx(*args, "-o", executable)
        Executable(executable)()

    def test_shared(self):
        """Compile and run an exact nearest-neighbor search using the shared library."""
        self._test_nearest_neighbor("shared")

    def test_static(self):
        """Compile and run an exact nearest-neighbor search using the static library."""
        self._test_nearest_neighbor("static")
