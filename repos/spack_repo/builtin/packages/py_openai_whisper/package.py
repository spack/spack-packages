# Copyright Spack Project Developers. See COPYRIGHT file for details.
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpenaiWhisper(PythonPackage):
    """Robust Speech Recognition via Large-Scale Weak Supervision"""

    homepage = "https://github.com/openai/whisper"
    pypi = "openai-whisper/openai_whisper-20250625.tar.gz"
    git = "https://github.com/openai/whisper.git"

    license("MIT")

    version("20250625", sha256="37a91a3921809d9f44748ffc73c0a55c9f366c85a3ef5c2ae0cc09540432eb96")

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-setuptools@61.2:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numba")
        depends_on("py-numpy")
        depends_on("py-torch")
        depends_on("py-tqdm")
        depends_on("py-more-itertools")
        depends_on("py-tiktoken")
        depends_on("py-triton@2.0.0:2", when="platform=linux target=x86_64:")
