# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpenslidePython(PythonPackage):
    """OpenSlide Python is a Python interface to the OpenSlide library."""

    homepage = "https://github.com/openslide/openslide-python"
    url = "https://github.com/openslide/openslide-python/archive/v1.1.1.tar.gz"

    license("LGPL-2.1-or-later")

    version("1.1.2", sha256="83e064ab4a29658e7ddf86bf1d3e54d2508cc19ece35d55b55519c826e45d83f")

    depends_on("c", type="build")

    depends_on("openslide@3.4.0:")
    depends_on("python@2.6:2.8,3.3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("pil", type=("build", "run"))
