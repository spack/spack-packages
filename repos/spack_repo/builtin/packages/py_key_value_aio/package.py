# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyKeyValueAio(PythonPackage):
    """A pluggable interface for KV Stores."""

    homepage = "https://github.com/strawgate/py-key-value"
    pypi = "py_key_value_aio/py_key_value_aio-0.4.4.tar.gz"

    version("0.4.4", sha256="e3012e6243ed7cc09bb05457bd4d03b1ba5c2b1ca8700096b3927db79ffbbe55")

    variant("memory", default=False, description="Enable memory backend")
    variant("redis", default=False, description="Enable redis backend")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-uv-build@0.8.2:0.8", type="build")

    depends_on("py-beartype@0.20:", type=("build", "run"))
    depends_on("py-typing-extensions@4.15:", type=("build", "run"))

    depends_on("py-cachetools@5:", type=("build", "run"), when="+memory")
    depends_on("py-redis@4.3:", type=("build", "run"), when="+redis")
