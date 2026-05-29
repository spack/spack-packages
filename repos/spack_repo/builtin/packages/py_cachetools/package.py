# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCachetools(PythonPackage):
    """This module provides various memoizing collections and decorators,
    including variants of the Python 3 Standard Library @lru_cache function
    decorator."""

    homepage = "https://github.com/tkem/cachetools"
    pypi = "cachetools/cachetools-3.1.1.tar.gz"

    license("MIT")

    version("7.1.1", sha256="27bdf856d68fd3c71c26c01b5edc312124ed427524d1ddb31aa2b7746fe20d4b")
    version("6.2.6", sha256="16c33e1f276b9a9c0b49ab5782d901e3ad3de0dd6da9bf9bcd29ac5672f2f9e6")
    version("6.2.4", sha256="82c5c05585e70b6ba2d3ae09ea60b79548872185d2f24ae1f2709d37299fd607")
    version("5.5.2", sha256="1a661caa9175d26759571b2e19580f9d6393969e5dfca11fdb1f947a23e640d4")
    version("5.2.0", sha256="6a94c6402995a99c3970cc7e4884bb60b4a8639938157eeed436098bf9831757")
    version("4.2.4", sha256="89ea6f1b638d5a73a4f9226be57ac5e4f399d22770b92355f92dcb0f7f001693")
    version("4.2.2", sha256="61b5ed1e22a0924aed1d23b478f37e8d52549ff8a961de2909c69bf950020cff")
    version("3.1.1", sha256="8ea2d3ce97850f31e4a08b0e2b5e6c34997d7216a9d2c98e0f3978630d4da69a")

    with default_args(type=("build", "run")):
        depends_on("python@3.5:3", when="@4.2.2:")
        depends_on("python@3.7:3", when="@5.2.0:")
        depends_on("python@3.9:3", when="@6:")

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-setuptools@46.4.0:", when="@4.2.2:")
        depends_on("py-setuptools@61.0.0:", when="@6.2.3:")
