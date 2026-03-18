# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMneBids(PythonPackage):
    """MNE-BIDS: Organizing MEG, EEG, and iEEG data according to the BIDS
    specification and facilitating their analysis with MNE-Python."""

    homepage = "https://mne.tools/mne-bids"
    pypi = "mne_bids/mne_bids-0.15.0.tar.gz"
    git = "https://github.com/mne-tools/mne-bids"

    license("BSD-3-Clause")

    version("0.17.0", sha256="e6415bce905d6721eb175f8eab269309cb4b75081f43c782da860a89553ab4bb")
    version("0.15.0", sha256="8a3ac7fb586ba2be70eb687c67ae060b42693078c56232180b27161124c22f72")

    variant("full", default=False, description="Enable full functionality.")

    depends_on("python@3.10:", type=("build", "run"), when="@0.16:")
    depends_on("python@3.9:", type=("build", "run"))
    # although 0.17 needs py-hatchling==1.26.3 to build according to
    # pyproject.toml, it also builds fine with other versions
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-mne@1.8:", type=("build", "run"), when="@0.17:")
    depends_on("py-mne@1.5:", type=("build", "run"))
    depends_on("py-numpy@1.23:", type=("build", "run"), when="@0.17:")
    depends_on("py-numpy@1.21.2:", type=("build", "run"))
    depends_on("py-scipy@1.9:", type=("build", "run"), when="@0.17:")
    depends_on("py-scipy@1.7.1:", type=("build", "run"))

    with when("+full"):
        depends_on("py-defusedxml", type=("build", "run"))
        depends_on("py-edfio@0.2.1:", type=("build", "run"))
        depends_on("py-eeglabio@0.0.2:", type=("build", "run"))
        depends_on("py-matplotlib@3.6:", type=("build", "run"), when="@0.17:")
        depends_on("py-matplotlib@3.5:", type=("build", "run"))
        depends_on("py-nibabel@3.2.1:", type=("build", "run"))
        depends_on("py-pandas@1.3.2:", type=("build", "run"))
        depends_on("py-pybv@0.7.5:", type=("build", "run"))
        depends_on("py-pymatreader", type=("build", "run"))
        depends_on("py-pymatreader@0.0.30:", type=("build", "run"), when="@:0.15")

        # Historical dependencies
        depends_on("py-edflib-python@1.0.6:", type=("build", "run"), when="@:0.15")
