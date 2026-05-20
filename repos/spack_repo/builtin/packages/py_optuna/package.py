# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOptuna(PythonPackage):
    """Optuna is an automatic hyperparameter optimization software framework,
    particularly designed for machine learning. It features an imperative,
    define-by-run style user API. Thanks to our define-by-run API, the code
    written with Optuna enjoys high modularity, and the user of Optuna can
    dynamically construct the search spaces for the hyperparameters."""

    homepage = "https://optuna.org/"
    pypi = "optuna/optuna-3.2.0.tar.gz"

    maintainers("eugeneswalker")

    license("MIT")

    version("4.8.0", sha256="6f7043e9f8ecb5e607af86a7eb00fb5ec2be26c3b08c201209a73d36aff37a38")
    version("3.2.0", sha256="683d8693643a761a41d251a6b8e13263b24acacf9fc46a9233d5f6aa3ce5c683")

    depends_on("py-setuptools@61.1:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@4.8:")
        depends_on("python@3.7:")
        depends_on("py-alembic@1.5:")
        depends_on("py-cmaes@0.9.1:", when="@3.2")
        depends_on("py-colorlog")
        depends_on("py-numpy")
        depends_on("py-packaging@20:")
        depends_on("py-pyyaml")
        depends_on("py-tqdm")
        depends_on("py-sqlalchemy@1.4.2:", when="@4.8:")
        depends_on("py-sqlalchemy@1.3:")
