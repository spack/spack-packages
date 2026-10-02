# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyknos(PythonPackage):
    """Conditional density estimation with neural networks."""

    homepage = "https://github.com/sbi-dev/pyknos"
    pypi = "pyknos/pyknos-0.16.0.tar.gz"

    license("Apache-2.0")

    version("0.16.0", sha256="4e1db834d8a5fd847882a081937732fea6798668b72293ae052765e7bfc371c3")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-matplotlib")
        depends_on("py-nflows@0.14")
        depends_on("py-numpy")
        depends_on("py-tensorboard")
        depends_on("py-torch")
        depends_on("py-tqdm")
