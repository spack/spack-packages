# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyId(PythonPackage):
    """id is a Python tool for generating OIDC identities."""

    homepage = "https://pypi.org/project/id/"
    pypi = "id/id-1.5.0.tar.gz"
    git = "https://github.com/di/id.git"

    license("Apache-2.0", checked_by="RobertMaaskant")

    version("1.6.1", sha256="d0732d624fb46fd4e7bc4e5152f00214450953b9e772c182c1c22964def1a069")
    version("1.5.0", sha256="292cb8a49eacbbdbce97244f47a97b4c62540169c976552e497fd57df0734c1d")

    depends_on("py-flit-core@3.2:3", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@1.6:")
        depends_on("python@3.8:")

        depends_on("py-urllib3@2:", when="@1.6:")

        # Historical dependencies
        depends_on("py-requests", when="@:1.5")
