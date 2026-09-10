# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNeurokit2(PythonPackage):
    """The Python Toolbox for Neurophysiological Signal Processing.

    This package is the continuation of NeuroKit 1. It's a user-friendly
    package providing easy access to advanced biosignal processing routines.
    Researchers and clinicians without extensive knowledge of programming or
    biomedical signal processing can analyze physiological data with only two
    lines of code.
    """

    homepage = "https://github.com/neuropsychology/NeuroKit"
    pypi = "neurokit2/neurokit2-0.1.2.tar.gz"

    license("MIT")

    version("0.2.13", sha256="e0a3831e939444855c8350f01322d3ecece1faf8a290c179d730697930f10046")
    version("0.2.12", sha256="f1ca66136a397ce31bc9df8319a3fd04c544950b6e43080d13ea83e89492ca7c")
    version("0.2.4", sha256="4699704f6890ae3510d5abf1deec86a59d793d31cda51b627f6eae65360d298f")
    version("0.2.2", sha256="0c33b060f9ac5ec8a6a0e23261fdbc36a98cb48e06142a1653fd12698806a952")
    version("0.1.5", sha256="4df48c0ce8971e32e32f36c2263986b00fd83da5eadaaa98e4bb5ab6bcd930e5")
    version("0.1.4.1", sha256="226bb04bb369d8bb87d99831f0a93cd8d0ed96fdc500f63de0b3550082876f6e")
    version("0.1.2", sha256="5ef40037c2d7078ecb713ab0b77b850267babf133856b59595de9613f29787bc")

    depends_on("python@3.10:", type=("build", "run"), when="@0.2.13:")

    with default_args(type="build"):
        depends_on("py-hatchling", when="@0.2.13:")
        depends_on("py-hatch-vcs", when="@0.2.13:")

    with default_args(type=("build", "run")):
        depends_on("py-requests", when="@0.2.8:")
        depends_on("py-numpy@2:", when="@0.2.13")
        depends_on("py-numpy")
        depends_on("py-pandas@:2")
        depends_on("py-scipy")
        depends_on("py-scikit-learn@1:", when="@0.2:")
        depends_on("py-scikit-learn")
        depends_on("py-matplotlib@3.5:", when="@0.2.11:")
        depends_on("py-matplotlib")
        depends_on("py-pywavelets@1.4:", when="@0.2.12:")
        depends_on("py-setuptools@:81", when="@0.2.13:")

    # Historical dependencies
    depends_on("py-setuptools@40.6.0:", type="build", when="@:0.2.12")
    depends_on("py-pytest-runner", type="build", when="@:0.2.12")
