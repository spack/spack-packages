# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyKeyValueShared(PythonPackage):
    """Shared Key-Value."""

    homepage = "https://github.com/strawgate/py-key-value"
    pypi = "py_key_value_shared/py_key_value_shared-0.3.0.tar.gz"

    version("0.3.0", sha256="8fdd786cf96c3e900102945f92aa1473138ebe960ef49da1c833790160c28a4b")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-uv-build@0.8.2:0.8", type="build")

    depends_on("py-typing-extensions@4.15:", type=("build", "run"))
    depends_on("py-beartype@0.20:", type=("build", "run"))
