# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUvBuild(PythonPackage):
    """The uv build backend."""

    homepage = "https://github.com/astral-sh/uv"
    pypi = "uv_build/uv_build-0.8.2.tar.gz"

    tags = ["build-tools"]

    version("0.8.2", sha256="7f80aa603eb67d1816917c1dc372de89a81bf082c9330418a604c5eedab54c46")

    depends_on("py-maturin@1", type="build")
