# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPymdownExtensions(PythonPackage):
    """Extensions for Python Markdown."""

    homepage = "https://github.com/facelessuser/pymdown-extensions"
    pypi = "pymdown_extensions/pymdown_extensions-9.5.tar.gz"

    license("MIT")

    version("10.21", sha256="39f4a020f40773f6b2ff31d2cd2546c2c04d0a6498c31d9c688d2be07e1767d5")
    version("9.5", sha256="3ef2d998c0d5fa7eb09291926d90d69391283561cf6306f85cd588a5eb5befa0")

    depends_on("py-hatchling@0.21.1:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@10.21:")
        depends_on("python@3.7:", when="@9.5")
        depends_on("py-markdown@3.6:", when="@10.21:")
        depends_on("py-markdown@3.2:", when="@9.5")
        depends_on("py-pyyaml", when="@10.21:")
