# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRangerFm(PythonPackage):
    """A VIM-inspired filemanager for the console"""

    pypi = "ranger-fm/ranger-fm-1.9.2.tar.gz"
    git = "https://github.com/ranger/ranger.git"

    version("1.9.3", sha256="9476ed1971c641f4ba3dde1b8b80387f0216fcde3507426d06871f9d7189ac5e")
    version("1.9.2", sha256="0ec62031185ad1f40b9faebd5a2d517c8597019c2eee919e3f1c60ce466d8625")

    # Ranger uses the `imghdr` module from the standard library to determine the type of an image
    # file, as the first step in determining whether and how to display a preview of the image.
    # The `imghdr` module was removed from the standard library in Python 3.13, so older versions
    # crash when run with Pythons newer than that.
    depends_on("python@:3.12", when="@:1.9.3")

    # pip silently replaces distutils with setuptools
    depends_on("py-setuptools", type="build")
