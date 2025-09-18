# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.qmake import QMakePackage
from spack.package import *
import os


class Klayout(QMakePackage):
    """KLayout - Your Mask Layout Friend."""

    homepage = "https://www.klayout.org"
    url = "https://www.klayout.org/downloads/source/klayout-0.30.2.tar.bz2"

    license("GPL-3.0", checked_by="mminutoli")

    version("0.30.2", sha256="49896397f2e7ec689bd2fa2f26488395fc0441e974ed267aee344eb47cdabfbc")

    depends_on("cxx", type="build")
    depends_on("qt@5.15.15")
    depends_on("python")

    def qmake(self, spec, prefix):
        pass

    def build(self, spec, prefix):
        pass

    def install(self, spec: Spec, prefix: Prefix) -> None:
        build_script = Executable("./build.sh")
        build_script('-without-qt-multimedia', '-nolibgit2', '-noruby', '-prefix', prefix, '-qmake', qmake.exe[0])

    def setup_run_environment(self, env):
        # The build system does not follow the usual convention of putting
        # binaries under bin and libraries under lib.
        #
        # Exporting the main klayout binary should be enough.
        env.prepend_path('PATH', os.path.join(self.prefix, 'klayout'))
