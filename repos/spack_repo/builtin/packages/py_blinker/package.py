# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBlinker(PythonPackage):
    """Fast, simple object-to-object and broadcast signaling"""

    homepage = "https://blinker.readthedocs.io"
    pypi = "blinker/blinker-1.4.tar.gz"
    git = "https://github.com/pallets-eco/blinker.git"

    license("MIT")

    version("1.9.0", sha256="b4ce2265a7abece45e7cc896e98dbebe6cead56bcf805a3d23136d145f5445bf")
    version("1.6.2", sha256="4afd3de66ef3a9f8067559fb7a1cbe555c17dcbe15971b05d1b625c3e7abe213")
    version("1.4", sha256="471aee25f3992bd325afa3772f1063dbdbbca947a041b8b89466dc00d606f8b6")

    depends_on("python@3.9:", type=("build", "run"), when="@1.9:")
    depends_on("py-flit-core@:4", type="build", when="@1.6.3:")

    with when("@:1.6.2"):
        depends_on("py-setuptools@61.2:", type="build", when="@1.6:")
        depends_on("py-setuptools", type="build")
