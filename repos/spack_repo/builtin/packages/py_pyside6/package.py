# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyside6(PythonPackage):
    """Qt for Python"""

    homepage = "https://doc.qt.io/qtforpython-6"
    git = "https://github.com/PySide/pyside-setup"
    url = "https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-6.11.1-src/pyside-setup-everywhere-src-6.11.1.tar.xz"

    license("LGPL-3.0-only OR GPL-3.0-only OR GPL-2.0-only", checked_by="melven")

    version("6.11.1", sha256="6ffd9835bb0dd2c56f061d62f1616bb1707cfc0202b80e3165d6be087f3965e2")

    variant("tools", default=False, description="Include wrappers for qt-tools")
    variant("qt3d", default=False, description="Include wrappers for qt-3d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # see https://wiki.qt.io/Qt_for_Python#Python_compatibility_matrix
    depends_on("python@3.10:3.14", type=("build", "run"))
    conflicts("python+freethreading")

    depends_on("cmake@3.22:", type="build")
    depends_on("ninja", type="build")

    # requirements.txt says == but let's take this as minimal versions...
    depends_on("py-setuptools@78.1.0:", type="build")
    depends_on("py-packaging@24.2:", type="build")
    depends_on("py-build@1.2.2:", type="build")
    depends_on("py-wheel@0.46.3:", type="build")
    depends_on("py-distro@1.9.0:", type="build")
    depends_on("patchelf@0.17.2:", type="build")
    depends_on("py-numpy@2.2.0:", type="build")
    depends_on("py-mypy@1.15.0:", type="build")

    # can also build without opengl but generates warnings. network and accessibility seem required.
    depends_on("qt-base@6.11: +network +accessibility +opengl")
    # can also build without tools but generates warnings...
    depends_on("qt-tools@6.11:", when="+tools")
    # can also build without qt-3d
    depends_on("qt-3d@6.11:", when="+qt3d")

    # suggested llvm version for building on https://doc.qt.io/qtforpython-6/building_from_source/linux.html
    depends_on("llvm@20.1.3: +clang", type="build")

    def patch(self):

        # shiboken include paths: misses non-qt-base paths (QtUiTools in qt-tools and Qt3D... in qt-3d)
        additional_includes = []
        if "+tools" in self.spec:
            additional_includes += [self.spec["qt-tools"].prefix.include]
        if "+qt3d" in self.spec:
            additional_includes += [self.spec["qt-3d"].prefix.include]
        if additional_includes:
            filter_file(
                "=${shiboken_include_dirs}",
                ":".join(
                    [
                        "=${shiboken_include_dirs}",
                        *additional_includes
                    ]
                ),
                "sources/pyside6/cmake/Macros/PySideModules.cmake",
                string=True,
            )

        # the --rpath flag below seems broken for linux
        filter_file(
            "pyside_build.update_rpath(executables)",
            "pyside_build.update_rpath(executables + pyside_build.package_libraries(destination_dir))",
            "build_scripts/platforms/unix.py",
            string=True,
        )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("LLVM_INSTALL_DIR", self.spec["llvm"].prefix)

    def install_options(self, spec, prefix):
        args = [
            "--parallel={0}".format(make_jobs),
            "--ignore-git",
            # if you want to debug build problems, uncomment this
            #"--verbose-build",
            #"--log-level=verbose",
            "--qtpaths={0}".format(spec["qt-base"].prefix.bin.qtpaths),
        ]

        # fix rpaths
        args.append("--rpath={0}".format(":".join(self.rpath)))

        if self.run_tests:
            args.append("--build-tests")
        return args

    def install(self, spec, prefix):
        python("setup.py", "install", "--prefix=" + prefix, *self.install_options(spec, prefix))

