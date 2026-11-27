# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNcpi(PythonPackage):
    """Neural circuit parameter inference from electrophysiological data."""

    homepage = "https://github.com/necolab-ugr/ncpi"
    git = "https://github.com/necolab-ugr/ncpi.git"
    import_modules = ["ncpi"]

    maintainers("pablomc88", "AlejandroOrozcoValero")

    license("GPL-3.0-only")

    version("1.0.0b2", commit="1534b126cfa9ec02f8c01f995445d76b494e7b57")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-wheel", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-arviz@:0.21")
        depends_on("py-flask")
        depends_on("py-matplotlib")
        depends_on("py-numpy")
        depends_on("py-packaging")
        depends_on("py-pandas")
        depends_on("py-pycatch22")
        depends_on("py-requests")
        depends_on("py-sbi@0.26.0")
        depends_on("py-scikit-learn@1.5.0")
        depends_on("py-scipy")
        depends_on("py-specparam")
        depends_on("py-torch@2.10.0")
        depends_on("py-tqdm")
