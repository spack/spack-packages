# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyani(PythonPackage):
    """pyani is a Python3 module that provides support for calculating
    average nucleotide identity (ANI) and related measures for whole genome
    comparisons, and rendering relevant graphical summary output. Where
    available, it takes advantage of multicore systems, and can integrate
    with SGE/OGE-type job schedulers for the sequence comparisons."""

    homepage = "https://widdowquinn.github.io/pyani"
    pypi = "pyani/pyani-0.2.7.tar.gz"

    license("MIT")

    version("0.2.9", sha256="0b87870a03cf5ccd8fbab7572778903212a051990f00cf8e4ef5887b36b9ec91")
    version("0.2.7", sha256="dbc6c71c46fbbfeced3f8237b84474221268b51170caf044bec8559987a7deb9")
    version("0.2.6", sha256="e9d899bccfefaabe7bfa17d48eef9c713d321d2d15465f7328c8984807c3dd8d")

    depends_on("python@3.5:")
    depends_on("py-setuptools", type="build")
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))

    # Required for ANI analysis
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    # Required for ANIb analysis
    depends_on("blast-plus~python", type="run")

    # Required for ANIm analysis
    depends_on("mummer", type="run")
