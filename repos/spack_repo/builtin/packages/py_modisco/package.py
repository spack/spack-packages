# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
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

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.21.5:")
        depends_on("py-scipy@1.6.2:")
        depends_on("py-numba@0.53.1:")
        depends_on("py-scikit-learn@1.0.2:")
        depends_on("py-leidenalg@0.8.10:")
        depends_on("py-igraph@0.9.11:")
        depends_on("py-tqdm@4.38.0:")
        depends_on("py-pandas@1.4.3:")
        depends_on("py-logomaker@0.8:")
        depends_on("py-h5py@3.7.0:")
        depends_on("py-hdf5plugin")
        depends_on("py-memelite")
        depends_on("py-jinja2")
