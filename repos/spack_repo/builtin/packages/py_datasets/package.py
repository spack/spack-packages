# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDatasets(PythonPackage):
    """Datasets is a lightweight library providing two main
    features: one-line dataloaders for many public datasets and
    efficient data pre-processing."""

    homepage = "https://github.com/huggingface/datasets"
    pypi = "datasets/datasets-1.8.0.tar.gz"

    maintainers("thomas-bouvier")

    license("Apache-2.0")

    version("3.2.0", sha256="9a6e1a356052866b5dbdd9c9eedb000bf3fc43d986e3584d9b028f4976937229")
    version("2.20.0", sha256="3c4dbcd27e0f642b9d41d20ff2efa721a5e04b32b2ca4009e0fc9139e324553f")
    version("2.8.0", sha256="a843b69593914071f921fc1086fde939f30a63415a34cdda5db3c0acdd58aff2")
    version("1.8.0", sha256="d57c32bb29e453ee7f3eb0bbca3660ab4dd2d0e4648efcfa987432624cab29d3")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-filelock", when="@2.20:")
        depends_on("py-numpy@1.17:")
        depends_on("py-pyarrow@15:", when="@2.20:")
        depends_on("py-pyarrow@6:", when="@2.8")
        depends_on("py-pyarrow@1:3", when="@1.8")
        depends_on("py-dill@0.3.0:0.3.8", when="@2.20:")
        depends_on("py-dill@:0.3.6", when="@:2.8")
        depends_on("py-pandas")
        depends_on("py-requests@2.32.2:", when="@2.20:")
        depends_on("py-requests@2.19:")
        depends_on("py-tqdm@4.66.3:", when="@2.20:")
        depends_on("py-tqdm@4.62.1:", when="@2.8")
        depends_on("py-tqdm@4.27:4.49", when="@1.8")
        depends_on("py-xxhash")
        depends_on("py-multiprocess@:0.70.16", when="@3.2:")
        depends_on("py-multiprocess")
        depends_on("py-fsspec@2023.1:2024.9.0+http", when="@3.2:")
        depends_on("py-fsspec@2023.1:2024.5.0+http", when="@2.20")
        depends_on("py-fsspec@2021.11.1:+http", when="@2.8")
        depends_on("py-fsspec", when="@1.8")
        depends_on("py-aiohttp", when="@2.8:")
        depends_on("py-huggingface-hub@0.23:", when="@3.2:")
        depends_on("py-huggingface-hub@0.21.2:", when="@2.20")
        depends_on("py-huggingface-hub@0.2:0", when="@2.8")
        depends_on("py-huggingface-hub@0.0", when="@1.8")
        depends_on("py-packaging")
        depends_on("py-pyyaml@5.1:", when="@2.8:")

        # Historical dependencies
        # depends_on("py-pyarrow-hotfix", when="@2.20")  # only for pyarrow < 14.0.1
        depends_on("py-responses@:0.18", when="@2.8")
