# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFlexcache(PythonPackage):
    """Flexcache is a flexible caching library for Python,
    providing convenient and efficient caching mechanisms."""

    homepage = "https://github.com/hgrecco/flexcache"
    pypi = "flexcache/flexcache-0.3.tar.gz"

    license("BSD-3-Clause")

    version("0.3", sha256="18743bd5a0621bfe2cf8d519e4c3bfdf57a269c15d1ced3fb4b64e0ff4600656")

    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-typing-extensions", type=("build", "run"))
