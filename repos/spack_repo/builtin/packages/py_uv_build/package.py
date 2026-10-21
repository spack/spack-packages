# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUvBuild(PythonPackage):
    """The uv build backend."""

    homepage = "https://github.com/astral-sh/uv"
    pypi = "uv_build/uv_build-0.8.2.tar.gz"

    license("Apache-2.0 OR MIT")

    tags = ["build-tools"]

    version("0.13.0", sha256="bd2614f24a58dccd4865d4f86ddd91dd01fd0efab4632e033186a8423b8a3515")
    version("0.11.33", sha256="b09dcd86e4bbb31f4d85470892771e7c8786b3bd9b6519f7ce7480517b4d1381")
    version("0.11.6", sha256="3ca25d4fca52e0598084fab352a4cafe737043f5682e3cb654164f033ba6d736")
    version("0.8.2", sha256="7f80aa603eb67d1816917c1dc372de89a81bf082c9330418a604c5eedab54c46")

    depends_on("python@3.8:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-maturin@1")

        # from Cargo.toml
        depends_on("rust@1.97:", when="@0.12.22:")
        depends_on("rust@1.95:", when="@0.11.29:")
        depends_on("rust@1.92:", when="@0.10.10:")
        depends_on("rust@1.86:")

        # otherwise: libbz2.so.1.0 => not found
        depends_on("c", when="@:0.11")

    depends_on("bzip2", when="@:0.11")
