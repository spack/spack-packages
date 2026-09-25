# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySbi(PythonPackage):
    """Simulation-based inference."""

    homepage = "https://github.com/sbi-dev/sbi"
    pypi = "sbi/sbi-0.24.0.tar.gz"

    license("Apache-2.0")

    version("0.24.0", sha256="86a436bf6ccdfeb04085085e8db07aed2e86dd32c3dc88c5f2c0385fd7c46396")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@65:", type="build")
    depends_on("py-wheel", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-arviz")
        depends_on("py-joblib@1:")
        depends_on("py-matplotlib")
        depends_on("py-notebook@:6.4.12")
        depends_on("py-numpy")
        depends_on("py-pillow")
        depends_on("py-pyknos@0.16:")
        depends_on("py-pymc@5:")
        depends_on("py-pyro-ppl@1.3.1:")
        depends_on("py-scikit-learn")
        depends_on("py-scipy")
        depends_on("py-tensorboard")
        depends_on("py-torch@1.13:2.5")
        depends_on("py-tqdm")
        depends_on("py-zuko@1.2:")
