# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyperclip(PythonPackage):
    """A cross-platform clipboard module for Python."""

    homepage = "https://github.com/asweigart/pyperclip"
    pypi = "pyperclip/pyperclip-1.7.0.tar.gz"

    license("BSD-3-Clause")

    version("1.11.0", sha256="244035963e4428530d9e3a6101a1ef97209c6825edab1567beac148ccc1db1b6")
    version("1.10.0", sha256="180c8346b1186921c75dfd14d9048a6b5d46bfc499778811952c6dd6eb1ca6be")
    version("1.8.2", sha256="105254a8b04934f0bc84e9c24eb360a591aaf6535c9def5f29d92af107a9bf57")
    version("1.7.0", sha256="979325468ccf682104d5dcaf753f869868100631301d3e72f47babdea5700d1c")

    depends_on("py-setuptools@61:", type="build", when="@1.10:")
    depends_on("py-setuptools", type="build")
    depends_on("xclip", type="run", when="platform=linux")
