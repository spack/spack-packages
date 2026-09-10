# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyYte(PythonPackage):
    """A YAML template engine with Python expressions."""

    homepage = "https://yte-template-engine.github.io"
    pypi = "yte/yte-1.5.1.tar.gz"

    maintainers("charmoniumQ")

    license("MIT")

    version("1.5.7", sha256="1e22a74e7c4d1aa70c54fe79d23938cb249d08c0804ad764ab97d5c587cbbad2")
    version("1.5.1", sha256="6d0b315b78af83276d78f5f67c107c84238f772a76d74f4fc77905b46f3731f5")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-poetry-core@1:", type="build")

    depends_on("py-dpath@2", type=("build", "run"))
    depends_on("py-dpath@2.1:2", type=("build", "run"), when="@1.5.2:")
    depends_on("py-plac@1.3.4:1", type=("build", "run"))
    depends_on("py-pyyaml@6", type=("build", "run"))
