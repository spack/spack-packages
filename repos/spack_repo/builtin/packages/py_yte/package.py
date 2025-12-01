# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyYte(PythonPackage):
    """A YAML template engine with Python expressions."""

    homepage = "https://yte-template-engine.github.io"
    pypi = "yte/yte-1.5.1.tar.gz"
    git = "https://github.com/yte-template-engine/yte.git"

    maintainers("charmoniumQ")

    license("MIT")

    version("1.9.4", sha256="86a47e6d722cec9419a7ac88be57d0d6c4ce28f02860393b71a66f2c674069f6")
    version("1.8.1", sha256="6eefbdceae56e156ba9881ecb63f3c9217cfe5d5cc6f85fdb061c266a8eff112")
    version("1.7.0", sha256="d9cadcb597128490356a8260842fd71bf3145fa4ee633ecc4023f53a6b3f646d")
    version("1.6.0", sha256="d901d4cc0ead79c1c72a8fe9960fb4102d1c6d29d3c5e344f0ce7b6f64cf01e8")
    version("1.5.7", sha256="1e22a74e7c4d1aa70c54fe79d23938cb249d08c0804ad764ab97d5c587cbbad2")
    version("1.5.1", sha256="6d0b315b78af83276d78f5f67c107c84238f772a76d74f4fc77905b46f3731f5")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"), when="@1.9.2:")

    depends_on("py-poetry-core@1:", type="build", when="@:1.8")
    depends_on("py-uv", type="build", when="@1.9:")

    depends_on("py-argparse-dataclass@1", type=("build", "run"))
    depends_on("py-argparse-dataclass@2", type=("build", "run"), when="@1.9.2:")
    depends_on("py-dpath@2", type=("build", "run"))
    depends_on("py-dpath@2.1:", type=("build", "run"), when="@1.5.2:")
    depends_on("py-pyyaml@6", type=("build", "run"))

    # Historical dependencies
    depends_on("py-plac@1.3.4:1", type=("build", "run"), when="@:1.8")
