# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBidskit(PythonPackage):
    """Tools for DICOM to BIDS conversion."""

    homepage = "https://github.com/jmtyszka/bidskit"
    pypi = "bidskit/bidskit-2022.10.13.tar.gz"

    license("MIT")

    version("2025.11.7", sha256="fc478bc5eb5b4808aa4ff2df2d5def54dbf8411313e16a2a2f639adbf0965a56")
    version("2025.1.30", sha256="91daa1041b07b029da2e720b91270be9ab39c42ccbb6e8d8bb302441ea1a1bf5")
    version("2023.9.7", sha256="029d9aecbbcb2df733858ceb3e6d5dd5013c36e431e40fb522a580adc7b667a5")
    version("2023.2.16", sha256="b2e4e3246d43a6f00af6c0391ec8fecc59405241de1ea9ca68eb4d8128d62c7b")
    version(
        "2022.10.13", sha256="576b92cef187032c73f64e2e6a5b0be0c06771442048a33c55e224b3df0aae3a"
    )

    depends_on("python@3.10:3", type=("build", "run"), when="@2024.11.7:")
    depends_on("python@3.7:3", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-poetry-core@2", when="@2025.11.7:")

    with default_args(type=("build", "run")):
        # ignore upper version limits, because it works with newer versions as well
        depends_on("py-pydicom@2.3.1:", when="@2025.1.30:")
        depends_on("py-pydicom@2.2:")
        depends_on("py-numpy@2.2.4:", when="@2025.11.7:")
        depends_on("py-numpy@1.26.3:", when="@2025.1.30:")
        depends_on("py-numpy@1.21:")

    # still a dependency in newer versions, otherwise bidskit will throw an error message
    depends_on("py-pybids@0.15:", type=("build", "run"))

    # version requirement comes from error message when using bidskit
    depends_on("dcm2niix@1.0.20220720:", type=("build", "run"))

    # Historical dependencies
    depends_on("py-setuptools@72.1:", type=("build", "run"), when="@2025.1.30")
    depends_on("py-setuptools", type="build", when="@:2025.1.30")
