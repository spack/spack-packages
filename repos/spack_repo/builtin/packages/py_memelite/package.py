# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMemelite(PythonPackage):
    """The tools in the MEME suite are foundational for many sequence-based
    analyses; MEME itself for discovering repeating patterns in sequences, FIMO
    for scanning these patterns against long sequences, and Tomtom for scoring
    these patterns against each other."""

    homepage = "https://github.com/jmschrei/memesuite-lite"
    pypi = "memelite/memelite-0.2.0.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("0.2.0", sha256="f028a7751369d6d1d88d736e3ac0a8ef1dfdc917618a3a6f958bdc9f380ed5d0")

    depends_on("python@3:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.14.2:2.0.1", type=("build", "run"))
    # https://github.com/jmschrei/memesuite-lite/issues/1
    depends_on("py-numba@0.60.0:", type=("build", "run"))
    depends_on("py-pandas@1.3.3:", type=("build", "run"))
    depends_on("py-pyfaidx@0.7.2.1:", type=("build", "run"))
    depends_on("py-tqdm@4.64.1:", type=("build", "run"))
