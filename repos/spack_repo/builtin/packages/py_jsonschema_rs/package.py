# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJsonschemaRs(PythonPackage):
    """A high-performance JSON Schema validator for Python."""

    homepage = "https://github.com/Stranger6667/jsonschema/tree/master/crates/jsonschema-py"
    pypi = "jsonschema_rs/jsonschema_rs-0.61.2.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("0.61.2", sha256="8ea236493450c013f095d5d4d9d3b8e56fa0153fb305107f9a7134ea16bcf56b")

    with default_args(type="build"):
        depends_on("py-maturin@1.0:1")
        depends_on("rust@1.85:")

    depends_on("python@3.10:", type=("build", "run"))
