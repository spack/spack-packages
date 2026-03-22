# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re
from pathlib import Path

from spack.package import *


class Gnulib(Package):
    """Gnulib is a library of common routines intended to be shared at the source level.

    Gnulib is a dependency of many autotools projects, particularly with the recent development
    of @_g{``./bootstrap``} scripts to generate @_c{``configure``} from version control.

    autoconf tooling may previously have been vendored into @_y{``build-aux/``} without clear
    ownership, contributing to the background labor performed by upstream maintainers and
    Spack packagers.

    Many modules have required patches within spack to overcome transient issues. The progressive
    adoption of gnulib from source will allow for these workarounds to slowly be removed.
    """
    docstring_uses_rich_text = True
    docstring_has_extended_text = True

    homepage = "https://savannah.gnu.org/projects/gnulib"
    git = "https://git.savannah.gnu.org/git/gnulib.git"

    tags = ["core-packages"]
    maintainers("cosmicexplorer")

    executables = ["^gnulib-tool$"]

    # NB: this ends in a close paren!
    #     e.g.:
    # > gnulib-tool (GNU gnulib 2026-03-24)
    _version_at_eol = re.compile(r'gnulib\s+([0-9]+\.[0-9]+\S*)\)$')
    @classmethod
    def determine_version(cls, exe):
        exe = Executable(exe)
        m = cls._version_at_eol.search(exe("--version").splitlines()[0])
        if m:
            return m.group(1)
        return None

    # The files in here are mostly copyright (C) Free Software Foundation, and
    # are under assorted licenses.  Mostly, but not entirely, GPL.
    #
    # The license of each file is stated in that file.
    # Additionally, the files in the modules directory state the license of
    # the code part (in lib/) of the respective module.
    #
    # Some of the source files in lib/ have different licenses than GPL or LGPL.
    # Also, the copy of maintain.texi in doc/ has a verbatim-copying license,
    # and doc/standards.texi and make-stds.texi are GFDL.  Most (but not all)
    # m4/*.m4 files have nearly unlimited licenses.
    license("GPL-3.0-or-later")
    # https://www.gnu.org/software/gnulib/manual/gnulib.html#Gnulib-licensing-1

    version("master", branch="master")
    version("2026-03-24", commit="b75134c814c38876f04029ffc3fae4e90035dc34")

    variant("python", default=True,
            description="use the python implementation of gnulib-tool.py")

    depends_on("python@3:", when="+python", type="run")

    def install(self, spec, prefix):
        install_tree(".", prefix)

    def setup_dependent_package(self, module, dependent_spec):
        module.gnulib_tool = Executable(self.spec.prefix.bin.join("gnulib-tool"))

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        # This is generally
        env.set("GNULIB_SRCDIR", self.prefix)
        if self.spec.satisfies("+python"):
            env.set("GNULIB_TOOL_IMPL", "py")
        else:
            env.set("GNULIB_TOOL_IMPL", "sh")
        if (Path(self.stage.source_path) / '.git').exists():
            env.set("GNULIB_REFDIR", self.stage.source_path)
        else:
            tty.warn("gnulib expects to be used in a git checkout, "
                     f"but {self.stage.source_path} for {self.spec} had no git dir!")
