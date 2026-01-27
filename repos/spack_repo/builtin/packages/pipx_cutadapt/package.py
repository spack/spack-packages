# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.pipx import PipxPackage

from spack.package import *


class PipxCutadapt(PipxPackage):
    """Cutadapt finds and removes adapter sequences, primers, poly-A tails and
    other types of unwanted sequence from your high-throughput sequencing
    reads."""

    homepage = "https://cutadapt.readthedocs.io"
    pypi = "cutadapt/cutadapt-4.4.tar.gz"
    git = "https://github.com/marcelm/cutadapt.git"

    maintainers("ebagrenrut")

    license("MIT")

    version("5.2", sha256="2394deead42ecae5fe0fdf369e35f3e2afed770e14059582272779c2e8295d3c")
    version("4.9", sha256="da3b45775b07334d2e2580a7b154d19ea7e872f0da813bb1ac2a4da712bfc223")
    version("4.4", sha256="4554157c673022e1c433fcd6e3b803008fef60c8e71c01215e4aa04b0f09fe83")

    depends_on("c", type="build")

    depends_on("python@3.9:", when="@5:")
    depends_on("python@3.8:", when="@4.7:4")
    depends_on("python@3.7:", when="@4:4.6")
    depends_on("python@3.6:")
