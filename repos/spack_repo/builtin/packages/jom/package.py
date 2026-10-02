# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os
import re

from spack_repo.builtin.build_systems import qmake
from spack_repo.builtin.build_systems.qmake import QMakePackage

from spack.package import *


class Jom(QMakePackage):
    """jom is a clone of nmake, Microsoft's make implementation, that supports the
    execution of multiple independent commands in parallel. It is a drop-in
    replacement for nmake and understands the same command line options."""

    homepage = "https://wiki.qt.io/Jom"
    url = "https://github.com/qt-labs/jom/archive/refs/tags/v1.1.7.tar.gz"
    git = "https://code.qt.io/qt-labs/jom.git"

    tags = ["build-tools", "windows"]

    license("GPL-3.0-only")

    version("1.1.7", sha256="17d3b34b8a1fd5a20acbafc504525b884be9b83f36b0e309d139b0922e09a1d3")
    version("1.1.6", sha256="4718c916404fdd850b457c86e9100f8ad594c73b53ec9e224045c2f05aa15a0f")
    version("1.1.5", sha256="ff72c0d484dac9792037354479984aa97c011011de556cc548d2423946ce1947")
    version("1.1.4", sha256="e6d4bda0c9a264cb4ba1440d05df3728d6d0b55e3f3caa895a313fea1bd7d405")

    provides("nmake")

    executables = ["^jom$"]

    depends_on("cxx", type="build")

    requires("platform=windows", msg="jom is an nmake clone and only builds on Windows")
    # jom is a Qt5 program: both jom.pro and CMakeLists.txt want Qt5 Core, so
    # qt-base, which is Qt6, cannot act as its qmake provider.
    requires("^[virtuals=qmake] qt", msg="jom requires Qt5, which qt-base (Qt6) does not provide")
    # jom.pro hard-errors below 5.2.0 via its minQtVersion() check
    depends_on("qt@5.2:", when="^[virtuals=qmake] qt")

    # The inherited check phase runs `make check`, which does not exist on Windows
    build_time_test_callbacks = []

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("/VERSION", output=str, error=str)
        match = re.search(r"jom version (\S+)", output)
        return match.group(1) if match else None

    @property
    def jom_exe(self):
        return os.path.join(self.prefix.bin, "jom.exe")

    def setup_dependent_package(self, module, dependent_spec):
        """Stand in for nmake in dependents that build with an nmake makefile."""
        module.nmake = Executable(self.jom_exe)
        module.jom = Executable(self.jom_exe)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("PATH", self.prefix.bin)
        # jom reads its default arguments from JOMFLAGS, falling back to MAKEFLAGS.
        # Without this jom saturates every core regardless of Spack's job count.
        jobs = determine_number_of_jobs(parallel=dependent_spec.package.parallel)
        env.set("JOMFLAGS", "/J {0}".format(jobs))


class QMakeBuilder(qmake.QMakeBuilder):
    def qmake_args(self):
        # app.pro appends a 'd' to the target name for debug builds; pin the
        # configuration so the installed binary is always jom.exe
        return ["CONFIG+=release"]

    def install(self, pkg, spec, prefix):
        # jom's .pro files declare no INSTALLS target. src/app/app.pro sets
        # DESTDIR = ../../bin, so the binary lands in <source>/bin.
        mkdirp(prefix.bin)
        install(os.path.join(self.build_directory, "bin", "jom.exe"), prefix.bin)
