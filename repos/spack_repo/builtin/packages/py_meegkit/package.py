# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMeegkit(PythonPackage):
    """M/EEG denoising in Python."""

    homepage = "https://nbara.github.io/python-meegkit"
    pypi = "meegkit/meegkit-0.2.0.tar.gz"
    git = "https://github.com/nbara/python-meegkit.git"

    license("BSD-3-Clause")

    version("0.2.0", sha256="0df5783a9b03b23c196c3be36f448be2badd37e00e88e075bf3b2a0e3a0c9397")

    with default_args(type="build"):
        depends_on("py-setuptools@62:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")

        # from requirements.txt
        depends_on("py-numpy@1.20:")
        depends_on("py-scipy")
        depends_on("py-matplotlib")
        depends_on("py-scikit-learn")
        depends_on("py-pandas")
        depends_on("py-joblib")
        depends_on("py-tqdm")
        depends_on("py-statsmodels")
        depends_on("py-pyriemann@0.12:")
