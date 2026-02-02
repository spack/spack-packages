# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-modisco
#
# You can edit this file again by typing:
#
#     spack edit py-modisco
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyModisco(PythonPackage):
    """Algorithm for discovering sequence motifs from
    machine-learning-model-derived importance scores."""

    homepage = "https://github.com/kundajelab/tfmodisco"
    pypi = "modisco/modisco-2.5.2.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("2.5.2", sha256="820433d842803b66bcc8f29ef760edd2e62182a598bcfded6009f679dbbb53d5")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.21.5:", type=("build", "run"))
    depends_on("py-scipy@1.6.2:", type=("build", "run"))
    depends_on("py-numba@0.53.1:", type=("build", "run"))
    depends_on("py-scikit-learn@1.0.2:", type=("build", "run"))
    depends_on("py-leidenalg@0.8.10:", type=("build", "run"))
    depends_on("py-igraph@0.9.11:", type=("build", "run"))
    depends_on("py-tqdm@4.38.0:", type=("build", "run"))
    depends_on("py-pandas@1.4.3:", type=("build", "run"))
    depends_on("py-logomaker@0.8:", type=("build", "run"))
    depends_on("py-h5py@3.7.0:", type=("build", "run"))
    depends_on("py-hdf5plugin", type=("build", "run"))
    depends_on("py-memelite", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))


    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
