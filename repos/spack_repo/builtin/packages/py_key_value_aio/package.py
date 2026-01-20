# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyKeyValueAio(PythonPackage):
    """A pluggable interface for KV Stores."""

    homepage = "https://github.com/strawgate/py-key-value"
    pypi = "py_key_value_aio/py_key_value_aio-0.3.0.tar.gz"

    version("0.3.0", sha256="858e852fcf6d696d231266da66042d3355a7f9871650415feef9fca7a6cd4155")

    variant("memory", default=False, description="Enable memory backend")
    variant("redis", default=False, description="Enable redis backend")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-uv-build@0.8.2:0.8", type="build")

    depends_on("py-key-value-shared@0.3.0", when="@0.3.0", type=("build", "run"))
    depends_on("py-beartype@0.20:", type=("build", "run"))

    depends_on("py-cachetools@5:", when="+memory", type=("build", "run"))
    depends_on("py-redis@4.3:", when="+redis", type=("build", "run"))
