# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeeplift(PythonPackage):
    """DeepLIFT: Deep Learning Important FeaTures

    DeepLIFT implements the methods in "Learning Important Features Through
    Propagating Activation Differences" by Shrikumar, Greenside & Kundaje, as
    well as other commonly-used methods such as gradients, gradient-times-input
    (equivalent to a version of Layerwise Relevance Propagation for ReLU
    networks), guided backprop and integrated gradients."""

    homepage = "https://github.com/kundajelab/deeplift"
    pypi = "deeplift/deeplift-0.6.13.0.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("0.6.13.0", sha256="354ac5a00630b2df0856e8c948262e38c7eb83a719f71d6b5bf8ec4b064cb432")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.9:1")
        depends_on("py-tensorflow@1.7:")
        # Keras is not listed in requirements/setup.py but referred to in code
        depends_on("py-keras@2.2:")
