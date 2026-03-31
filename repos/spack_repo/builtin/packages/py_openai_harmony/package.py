# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpenaiHarmony(PythonPackage):
    """OpenAI's response format for its open-weight model series gpt-oss."""

    homepage = "https://github.com/openai/harmony"
    pypi = "openai_harmony/openai_harmony-0.0.8.tar.gz"

    version("0.0.8", sha256="6e43f98e6c242fa2de6f8ea12eab24af63fa2ed3e89c06341fb9d92632c5cbdf")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pydantic@2.11.7:", type=("build", "run"))
    depends_on("py-maturin@1.8:1", type="build")
    depends_on("rust", type="build")
