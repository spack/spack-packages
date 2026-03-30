# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyKundajelabShap(PythonPackage):
    """Kundaje lab edits to Scott Lundberg's unified approach to explain the
    output of any machine learning model."""

    homepage = "http://github.com/kundajelab/shap"
    pypi = "kundajelab-shap/kundajelab-shap-1.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("1", sha256="0269759677ae8a71544e34168c680588703c2e983a20ff8bce93cd73dc6004ff")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicitly by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1")
        depends_on("py-scipy")
        depends_on("py-scikit-learn")
        depends_on("py-matplotlib")
        depends_on("py-pandas")
        depends_on("py-tqdm@4.25:")
        depends_on("py-ipython")
        depends_on("py-scikit-image")
