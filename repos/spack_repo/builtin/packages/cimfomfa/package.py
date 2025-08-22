# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install cimfomfa
#
# You can edit this file again by typing:
#
#     spack edit cimfomfa
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack.package import *
import shutil


class Cimfomfa(AutotoolsPackage):
    """This library supports both MCL, a cluster algorithm for graphs, and zoem, a macro/DSL language.
    It supplies abstractions for memory management, I/O, associative arrays, strings, heaps, and a few other things."""

    homepage = "https://github.com/micans/cimfomfa"
    url = "https://github.com/micans/cimfomfa/archive/refs/tags/21-361.tar.gz"

    license("GPL-2.0-only", checked_by="emwjacobson")

    version("21-361", sha256="e554f7838a16dfee79999b28133abf58dce01ac9a18f99c38c4183805b5b19d4")

    depends_on("c", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("foo")

    def autoreconf(self, spec, prefix):
        # The configure file isn't named properly
        shutil.move("configure.ac.in", "configure.ac")
        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
