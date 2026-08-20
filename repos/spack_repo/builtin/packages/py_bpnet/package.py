# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBpnet(PythonPackage):
    """BPNet is a python package with a CLI to train and interpret
    base-resolution deep neural networks trained on functional genomics data
    such as ChIP-nexus or ChIP-seq. This is the improved version of the repo
    associated the BPNet paper."""

    homepage = "https://github.com/kundajelab/bpnet"
    pypi = "bpnet/bpnet-2.0.0.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("2.0.0", sha256="ea39cfb0e5ac9d22cc25a7db3461119765cac3fe23eff09eaa352e506ea5e86d")

    depends_on("python@3", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-tensorflow")  # Officially lists 2.4.1 which is ancient
        depends_on("py-tensorflow-probability@0.12.2")
        # Officially pinned to 0.18.0, but that gives conflicting python requirements
        depends_on("py-pysam@0.18.0:")
        depends_on("py-py2bit@0.3.0")
        depends_on("py-tqdm")
        depends_on("py-scikit-learn")
        depends_on("py-scipy")
        depends_on("py-deepdish")
        depends_on("py-pandas")
        depends_on("py-matplotlib")
        depends_on("py-plotly")
        depends_on("py-deeptools")
        depends_on("py-pyfaidx")
        depends_on("py-deeplift")
        depends_on("py-hdf5plugin")
        depends_on("py-kundajelab-shap")
