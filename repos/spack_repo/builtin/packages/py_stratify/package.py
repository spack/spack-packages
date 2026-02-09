# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyStratify(PythonPackage):
    """Vectorized interpolators that are especially useful for
    Nd vertical interpolation/stratification of atmospheric and
    oceanographic datasets.
    """

    homepage = "https://github.com/SciTools-incubator/python-stratify"
    pypi = "stratify/stratify-0.1.tar.gz"

    license("BSD-3-Clause")

    version("0.1.1", sha256="29f5afc9a94719ccce277032b9db5b778f605d914917b43f031f752070e91e78")
    version("0.1", sha256="5426f3b66e45e1010952d426e5a7be42cd45fe65f1cd73a98fee1eb7c110c6ee")

    depends_on("c", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
