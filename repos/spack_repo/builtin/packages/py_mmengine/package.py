# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMmengine(PythonPackage):
    """MMEngine is a foundational python library for deep learning
    models based on PyTorch.
    """

    homepage = "https://mmengine.readthedocs.io/en/latest/"
    url = "https://github.com/open-mmlab/mmengine/archive/v0.10.7.tar.gz"

    license("Apache-2.0")

    version("0.10.7", sha256="ccc32b78d230220b6b0e1f5ceb44835b54c2848548b8ee344feecd4aa98cf56f")

    depends_on("cxx", type="build")  # generated

    depends_on("python@3.6:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")

    depends_on("py-addict", type=("build", "run"))
    depends_on("py-numpy@1.11.1:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-regex", type=("build", "run"), when="platform=win32")
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-termcolor", type=("build", "run"))
    depends_on("py-yapf", type=("build", "run"))
