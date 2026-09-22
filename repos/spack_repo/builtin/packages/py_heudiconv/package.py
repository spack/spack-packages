# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHeudiconv(PythonPackage):
    """Heuristic DICOM Converter."""

    homepage = "https://heudiconv.readthedocs.io/"
    pypi = "heudiconv/heudiconv-1.3.4.tar.gz"
    git = "https://github.com/nipy/heudiconv.git"

    license("Apache-2.0")

    version("1.5.1", sha256="10ede22a116ced4fde92e79e50af0f4627fa345715eb1a0320c0bef63b3443ca")
    version("1.3.4", sha256="cd3ff1cbd7f41819a11899b819dd1910a35289f0418f1d119933aaabaa8de1aa")

    with default_args(type="build"):
        depends_on("py-setuptools@77.0.3:", when="@1.5.1:")
        depends_on("py-setuptools@46.4:")
        depends_on("py-versioningit@2.3:2")
        depends_on("py-wheel@0.32:0", when="@:1.5.0")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")

        depends_on("py-dcmstack@0.8:")
        depends_on("py-etelemetry")
        depends_on("py-filelock@3.0.12:")
        depends_on("py-nibabel@5.3.1:")
        depends_on("py-nipype@1.2.3:")
        depends_on("py-pydicom@1:")
        depends_on("dcm2niix")
