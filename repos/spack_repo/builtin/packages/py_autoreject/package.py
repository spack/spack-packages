# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAutoreject(PythonPackage):
    """Automated rejection and repair of epochs in M/EEG."""

    homepage = "http://autoreject.github.io"
    pypi = "autoreject/autoreject-0.4.3.tar.gz"
    git = "https://github.com/autoreject/autoreject.git"

    license("BSD-3-Clause")

    version("0.4.3", sha256="bd977ea3c88dc68550fbd5dbb98515b3b811907ba78afe8e412632edde6c8fc5")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.20.2:", type=("build", "run"))
    depends_on("py-scipy@1.6.3:", type=("build", "run"))
    depends_on("py-mne+hdf5@1:", type=("build", "run"))
    depends_on("py-scikit-learn@0.24.2:", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-matplotlib@3.4:", type=("build", "run"))
