# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGguf(PythonPackage):
    """Read and write ML models in GGUF for GGML."""

    homepage = "https://github.com/ggml-org/llama.cpp"
    pypi = "gguf/gguf-0.18.0.tar.gz"

    version("0.18.0", sha256="b4659093d5d0dccdb5902a904d54b327f4052879fe5e90946ad5fce9f8018c2e")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-poetry-core@1:", type="build")
    depends_on("py-numpy@1.17:", type=("build", "run"))
    depends_on("py-tqdm@4.27:", type=("build", "run"))
    depends_on("py-pyyaml@5.1:", type=("build", "run"))
    depends_on("py-requests@2.25:", type=("build", "run"))
    depends_on("py-pyyaml@5.1:", type=("build", "run"))
    depends_on("py-sentencepiece@0.1.98:0.2", type=("build", "run"))
