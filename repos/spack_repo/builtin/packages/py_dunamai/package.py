# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDunamai(PythonPackage):
    """Dynamic version generation."""

    homepage = "https://github.com/mtkennerly/dunamai"
    pypi = "dunamai/dunamai-1.13.1.tar.gz"

    license("MIT")

    version("1.26.1", sha256="3b46007bd65b00b4824ead0a1aee365fd22d0ec2b9c219497d4fd48f52860c8b")
    version("1.25.0", sha256="a7f8360ea286d3dbaf0b6a1473f9253280ac93d619836ad4514facb70c0719d1")
    version("1.21.2", sha256="05827fb5f032f5596bfc944b23f613c147e676de118681f3bb1559533d8a65c4")
    version("1.18.0", sha256="5200598561ea5ba956a6174c36e402e92206c6a6aa4a93a6c5cb8003ee1e0997")
    version("1.17.0", sha256="459381b585a1e78e4070f0d38a6afb4d67de2ee95064bf6b0438ec620dde0820")
    version("1.13.1", sha256="49597bdf653bdacdeb51ec6e0f1d4d2327309376fc83e6f1d42af6e29600515f")
    version("1.12.0", sha256="fac4f09e2b8a105bd01f8c50450fea5aa489a6c439c949950a65f0dd388b0d20")

    depends_on("python@3.5:3", type=("build", "run"))
    depends_on("py-poetry-core@1:", type="build")

    depends_on("py-packaging@20.9:", type=("build", "run"))
    depends_on("py-importlib-metadata@1.6:", when="^python@:3.7", type=("build", "run"))
