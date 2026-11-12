# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMneIcalabel(PythonPackage):
    """MNE-ICALabel: Automatic labeling of ICA components from MEG, EEG and
    iEEG data with MNE."""

    homepage = "https://github.com/mne-tools/mne-icalabel"
    pypi = "mne_icalabel/mne_icalabel-0.10.0.tar.gz"

    license("BSD-3-Clause")

    version("0.10.0", sha256="6cad9b1fb3df7fa6b3199c0fa434c8db24bff28903698ceeeb46a149f1be6f3f")

    with default_args(type="build"):
        depends_on("py-setuptools@77:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")

        depends_on("py-mne@1.2:")
        depends_on("py-numpy@1.21:")
        depends_on("py-packaging")
        depends_on("py-pooch")
        depends_on("py-psutil")
        depends_on("py-scipy@1.4:")
