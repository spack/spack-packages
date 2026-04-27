# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRadicalGtod(PythonPackage):
    """RADICAL-GTOD provides a single method, gtod, which returns the current
    time in seconds since epoch (01.01.1970) with sub-second resolution and a
    binary tool, radical-gtod, which is a compiled binary and does not require
    the invocation of the Python interpreter."""

    homepage = "https://radical-cybertools.github.io"
    git = "https://github.com/radical-cybertools/radical.gtod.git"
    pypi = "radical_gtod/radical_gtod-1.90.0.tar.gz"

    maintainers("andre-merzky")

    license("LGPL-3.0-or-later")

    version("develop", branch="devel")
    version("1.90.0", sha256="70889239d3a60f8f323f62b942939665464fa368c4a00d0fbc49c878658f57b2")

    depends_on("c", type="build")  # generated
    depends_on("py-radical-utils@1.90:1.99", type=("build", "run"), when="@1.90:")
    depends_on("py-setuptools", type="build")
