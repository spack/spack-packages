# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBiosppy(PythonPackage):
    """A toolbox for biosignal processing written in Python."""

    homepage = "https://github.com/scientisst/BioSPPy"
    pypi = "biosppy/biosppy-2.2.3.tar.gz"

    license("BSD-3-Clause")

    version("2.2.4", sha256="0b52eb27a410fe24c01bd15dd4a85149d20ac0026f73e03b9c61bf99577dcca5")
    version("2.2.3", sha256="2c4b84c98c71e3e84b43bf09a855414c31f534a8aed84e59fb05bbc3c36d9aa9")

    depends_on("py-setuptools", type="build")

    # version contraint from requirement.txt
    depends_on("py-bidict@0.13.1:", type=("build", "run"))
    depends_on("py-h5py@2.7.1:", type=("build", "run"))
    depends_on("py-matplotlib@2.1.2:", type=("build", "run"))
    depends_on("py-numpy@1.22:", type=("build", "run"))
    depends_on("py-scikit-learn@0.19.1:", type=("build", "run"))
    depends_on("py-scipy@1.2:", type=("build", "run"))
    depends_on("py-shortuuid@0.5:", type=("build", "run"))
    depends_on("py-six@1.11:", type=("build", "run"))
    depends_on("py-joblib@0.11:", type=("build", "run"))
    depends_on("py-opencv-python", type=("build", "run"))
    depends_on("py-pywavelets@1.4.1:", type=("build", "run"))
    depends_on("py-mock", type=("build", "run"))

    # from errors when importing
    depends_on("py-peakutils", type=("build", "run"))
