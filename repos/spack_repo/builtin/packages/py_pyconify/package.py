# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyconify(PythonPackage):
    """Pyconify is a wrapper for the Iconify API.

    Iconify is a versatile icon framework that includes 100+ icon sets with
    more than 100,000 icons from FontAwesome, Material Design Icons, DashIcons,
    Feather Icons, EmojiOne, Noto Emoji and many other open source icon
    sets."""

    homepage = "https://github.com/pyapp-kit/pyconify"
    pypi = "pyconify/pyconify-0.2.1.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.2.1", sha256="8dd53757d9fbed41711434460932b2b5dbc25da720cd9f9a44af0187b2dfc07d")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-hatchling", type="build")

    depends_on("py-requests", type=("build", "run"))
