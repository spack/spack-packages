# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRignore(PythonPackage):
    """Python Bindings for the ignore crate."""

    homepage = "https://github.com/fastapilabs/fastapi-cloud-cli"
    pypi = "rignore/rignore-0.8.1.tar.gz"

    license("MIT")

    version("0.8.1", sha256="2b6cf58501e9ff1b6a71c3fd66c8a105311e1f23237626fd4c9c00606bb3d30f")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-maturin@1.14.1:1", type="build")
    depends_on("rust")
