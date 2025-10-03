# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCodechecker(PythonPackage):
    """ FIX ME """

    homepage = "https://github.com/Ericsson/codechecker"
    pypi = "codechecker/codechecker-6.26.2.tar.gz"

    license("Apache-2.0")

    version("6.26.2", sha256="6e73eb32e7c61dd1a13ec566b80dec8a7625e211fdd419f1b652da6aaa290249")

    depends_on("cxx")
    depends_on("c")

    depends_on("py-setuptools@70.2.0:", type="build")

    depends_on("llvm +clang", type=("build", "run"))
    depends_on("gcc@13:", type=("build", "run"))
    depends_on("cppcheck@1.80:", type=("build", "run"))

    # https://github.com/Ericsson/codechecker/blob/v6.26.2/analyzer/requirements.txt
    depends_on("py-lxml@5.3.0", type=("build", "run"))
    depends_on("py-portalocker@3.1.1:", type=("build", "run"))
    depends_on("py-psutil@5.9.8:", type=("build", "run"))
    depends_on("py-pyyaml@6.0.1:", type=("build", "run"))
    depends_on("py-sarif-tools@3.0.4:", type=("build", "run"))
    depends_on("py-multiprocess@0.70.15:", type=("build", "run"))
    # types-PyYAML==6.0.12.12 ??

    # https://github.com/Ericsson/codechecker/blob/v6.26.2/web/requirements.txt

    depends_on("py-authlib", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-sqlalchemy", type=("build", "run"))
    depends_on("py-alembic", type=("build", "run"))
    depends_on("py-gitpython", type=("build", "run"))
    depends_on("thrift +python", type=("build", "run"))
    
    
    depends_on("node-js@16:", type=("build", "run"))
    

    # depends_on("curl")
    # depends_on("git")