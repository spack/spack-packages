# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScikitBio(PythonPackage):
    """Data structures, algorithms and educational resources for bioinformatics."""

    homepage = "https://scikit.bio/"
    pypi = "scikit-bio/scikit_bio-0.7.3.tar.gz"
    url = "https://files.pythonhosted.org/packages/f1/b7/9a349408f2edb09be83a2d105a0c1ecbfcb52d794abfeb601a12a3cc5093/scikit_bio-0.7.3.tar.gz"

    license("BSD-3-Clause", checked_by="V-Karch")

    version("0.7.3", sha256="2492ebf2f6432d24c1030a0cd96d7708c2b57bc31b097a5ec838881792401ec5")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))

    depends_on("py-requests@2.20.0:", type=("build", "run"))
    depends_on("py-decorator@3.4.2:", type=("build", "run"))
    depends_on("py-natsort@4.0.3:", type=("build", "run"))
    depends_on("py-numpy@2.0:", type=("build", "run"))
    depends_on("py-pandas@1.5.0:", type=("build", "run"))
    depends_on("py-scipy@1.9.0:", type=("build", "run"))
    depends_on("py-h5py@3.6.0:", type=("build", "run"))
    depends_on("py-biom-format@2.1.16:", type=("build", "run"))
    depends_on("py-statsmodels@0.14.0:", type=("build", "run"))
    depends_on("py-patsy@0.5.0:", type=("build", "run"))
    depends_on("py-array-api-compat@1.3:", type=("build", "run"))
