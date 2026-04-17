# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCodechecker(PythonPackage):
    """CodeChecker is a static analysis infrastructure built on the LLVM/Clang
    Static Analyzer toolchain, replacing scan-build in a Linux or macOS (OS X)
    development environment."""

    homepage = "https://github.com/Ericsson/codechecker"
    pypi = "codechecker/codechecker-6.26.2.tar.gz"

    license("Apache-2.0")

    version("6.26.2", sha256="6e73eb32e7c61dd1a13ec566b80dec8a7625e211fdd419f1b652da6aaa290249")

    depends_on("cxx")
    depends_on("c")
    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-setuptools@70.2.0:", type="build")

    depends_on("llvm +clang", type=("build", "run"))
    depends_on("gcc@13:", type=("build", "run"))
    depends_on("cppcheck@1.80:", type=("build", "run"))

    # https://github.com/Ericsson/codechecker/blob/v6.26.2/analyzer/requirements.txt
    depends_on("py-lxml@5.3.0:", type=("build", "run"))
    depends_on("py-portalocker@3.1.1:", type=("build", "run"))
    depends_on("py-psutil@5.9.8:", type=("build", "run"))
    depends_on("py-pyyaml@6.0.1:", type=("build", "run"))
    depends_on("py-sarif-tools@3.0.4:", type=("build", "run"))
    depends_on("py-multiprocess@0.70.15:", type=("build", "run"))
    depends_on("py-types-pyyaml@6.0.12.12:", type=("build", "run"))

    # https://github.com/Ericsson/codechecker/blob/v6.26.2/web/requirements.txt
    # some are duplicates of those above
    depends_on("py-authlib@1.3.1:", type=("build", "run"))
    depends_on("py-requests@2.32.4:", type=("build", "run"))
    depends_on("py-sqlalchemy@1.4.54:1", type=("build", "run"))
    depends_on("py-alembic@1.5.5:", type=("build", "run"))
    depends_on("thrift +python", type=("build", "run"))
    # https://github.com/Ericsson/codechecker/issues/4437
    depends_on("thrift@0.22: +python", type=("build", "run"), when="^python@3.12:")
    depends_on("py-gitpython@3.1.41:", type=("build", "run"))

    depends_on("node-js@16:", type=("build", "run"))
