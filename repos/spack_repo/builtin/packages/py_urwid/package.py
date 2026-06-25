# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUrwid(PythonPackage):
    """A full-featured console UI library"""

    homepage = "https://urwid.org/"
    pypi = "urwid/urwid-1.3.0.tar.gz"

    license("LGPL-2.1-only")

    version("2.6.16", sha256="93ad239939e44c385e64aa00027878b9e5c486d59e855ec8ab5b1e1adcdb32a2")
    version("2.1.2", sha256="588bee9c1cb208d0906a9f73c613d2bd32c3ed3702012f51efe318a3f2127eae")
    version("1.3.0", sha256="29f04fad3bf0a79c5491f7ebec2d50fa086e9d16359896c9204c6a92bc07aba2")

    depends_on("c", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@61:", type="build", when="@2.6:")
    depends_on("py-setuptools-scm@7:+toml", type="build", when="@2.6:")
    depends_on("py-wheel", type="build", when="@2.6:")

    depends_on("py-typing-extensions", type="run", when="@2.6:")
    depends_on("py-wcwidth", type="run", when="@2.6:")
