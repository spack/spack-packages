# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOlmoearthPretrainMinimal(PythonPackage):
    """Minimal package for loading and initializing OlmoEarth models."""

    homepage = "https://github.com/allenai/olmoearth_pretrain_minimal"
    pypi = "olmoearth_pretrain_minimal/olmoearth_pretrain_minimal-0.0.2.tar.gz"

    maintainers("piperwolters", "adamjstewart")

    license("Apache-2.0")

    version("0.0.2", sha256="832fad5311e9827ebc74093335d774ba03cd0b9b8fba17d6bec5168b14b6c7a7")

    # Enable Python 3.14+ support
    # https://github.com/allenai/olmoearth_pretrain_minimal/pull/3
    patch("python-3.14.patch", when="@0.0.2")

    with default_args(type="build"):
        depends_on("py-setuptools@61:")

    with default_args(type=("build", "run")):
        depends_on("py-einops@0.7:")
        depends_on("py-huggingface-hub")
        depends_on("py-numpy@1.26.4:")
        depends_on("py-torch@2.8:")
        depends_on("py-universal-pathlib@0.2.5:")
