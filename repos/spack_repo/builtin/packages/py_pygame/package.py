# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPygame(PythonPackage):
    """Pygame is a free and open-source cross-platform library for the development
    of multimedia applications like video games using Python. It uses the Simple
    DirectMedia Layer library and several other popular libraries to abstract
    the most common functions, making writing these programs a more intuitive task."""

    homepage = "https://www.pygame.org/"
    pypi = "pygame/pygame-2.5.2.tar.gz"

    license("LGPL-2.1-only")

    version("2.6.1", sha256="56fb02ead529cee00d415c3e007f75e0780c655909aaa8e8bf616ee09c9feb1f")
    version("2.5.2", sha256="c1b89eb5d539e7ac5cf75513125fb5f2f0a2d918b1fd6e981f23bf0ac1b1c24a")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.6:", type=("build", "run"))
