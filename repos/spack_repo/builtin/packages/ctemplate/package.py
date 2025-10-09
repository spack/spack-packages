# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ctemplate(AutotoolsPackage):
    """This library provides an easy to use and lightning fast text
    templating system to use with C++ programs."""

    homepage = "http://github.com/OlafvdSpek/ctemplate"
    url = "http://github.com/OlafvdSpek/ctemplate/archive/ctemplate-2.3.tar.gz"

    maintainers("nicolin", "connoraird")
    license("BSD-3-Clause", checked_by="connoraird")

    version("2.4", sha256="ccc4105b3dc51c82b0f194499979be22d5a14504f741115be155bd991ee93cfa")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")
