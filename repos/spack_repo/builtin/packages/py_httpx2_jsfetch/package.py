# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHttpx2Jsfetch(PythonPackage):
    """httpx2 transports for Emscripten/Pyodide, backed by the JavaScript fetch API."""

    homepage = "https://www.example.com"
    pypi = "httpx2_jsfetch/httpx2_jsfetch-1.0.tar.gz"

    license("BSD-3-Clause")

    version("1.0", sha256="70a0e3eabfef7cce5ad9c629f7d01ca05e418f586646f4ddf14782e4c1454c60")

    depends_on("python@3.12:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-uv-dynamic-versioning@0.14:")
