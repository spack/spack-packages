# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOrjson(PythonPackage):
    """Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy."""

    homepage = "https://github.com/ijl/orjson"
    pypi = "orjson/orjson-3.8.7.tar.gz"

    license("Apache-2.0")
    maintainers("LydDeb")

    version("3.11.5", sha256="82393ab47b4fe44ffd0a7659fa9cfaacc717eb617c93cde83795f14af5c2e9d5")
    version("3.11.1", sha256="48d82770a5fd88778063604c566f9c7c71820270c9cc9338d25147cbf34afd96")
    version("3.10.18", sha256="e8da3947d92123eda795b68228cafe2724815621fe35e8e320a9e9593a4bcd53")
    version("3.10.3", sha256="2b166507acae7ba2f7c315dcf185a9111ad5e992ac81f2d507aac39193c2c818")
    version("3.9.15", sha256="95cae920959d772f30ab36d3b25f83bb0f3be671e986c72ce22f8fa700dae061")
    version("3.8.14", sha256="5ea93fd3ef7be7386f2516d728c877156de1559cda09453fc7dd7b696d0439b3")
    version("3.8.7", sha256="8460c8810652dba59c38c80d27c325b5092d189308d8d4f3e688dbd8d4f3b2dc")

    with default_args(type=("build", "run")):
        depends_on("python@:3.14")
        depends_on("python@:3.12", when="@:3.10.3")
        depends_on("python@3.8:", when="@3.9:")
        depends_on("python@3.7:", when="@3.8")

    with default_args(type="build"):
        depends_on("c")
        depends_on("rust@1.85:", when="@:3.11.5")
        # Error during the build of version 3.11.1
        # due to feature avx512_target_feature
        # cf. https://github.com/spack/spack-packages/pull/3281
        # Workaround: rust@:1.88
        # Solved since 3.11.2
        depends_on("rust@:1.88", when="@:3.11.1")
        depends_on("rust@1.82:", when="@3.10.14:")
        depends_on("rust@1.72:", when="@3.9:")
        depends_on("rust@1.60:", when="@3.8")
        depends_on("py-maturin@1", when="@3.9:")
        depends_on("py-maturin@0.13:0.14", when="@3.8")
