# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTensorflowDatasets(PythonPackage):
    """tensorflow/datasets is a library of datasets ready to use with
    TensorFlow."""

    homepage = "https://github.com/tensorflow/datasets"
    pypi = "tensorflow-datasets/tensorflow-datasets-4.4.0.tar.gz"

    license("Apache-2.0")

    version("4.9.10", sha256="c681c9b0e5de2acbec79ece2ad41712dfda3f1bfdb3ffc34d5c0afd786eba0f6")
    version("4.4.0", sha256="3e95a61dec1fdb7b05dabc0dbed1b531e13d6c6fd362411423d0a775e5e9b960")

    with default_args(type="build"):
        depends_on("py-setuptools")
        # setup.py imports pkg_resources
        depends_on("py-setuptools@:81", when="@:4.4")
        depends_on("py-packaging", when="@4.9:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@4.9:")
        depends_on("python@3.6:")
        depends_on("py-absl-py")
        depends_on("py-array-record@0.5:", when="@4.9: platform=linux")
        depends_on("py-dm-tree", when="@4.9:")
        depends_on("py-etils@1.9.1:+epath+epy+enp+etree", when="@4.9: ^python@3.11:")
        depends_on("py-etils@1.6:+epath+epy+enp+etree", when="@4.9:")
        depends_on("py-immutabledict", when="@4.9:")
        depends_on("py-numpy")
        depends_on("py-promise")
        depends_on("py-protobuf@3.20:", when="@4.9:")
        depends_on("py-protobuf@3.12.2:")
        depends_on("py-psutil", when="@4.9:")
        depends_on("py-pyarrow", when="@4.9:")
        depends_on("py-requests@2.19.0:")
        depends_on("py-simple-parsing", when="@4.9:")
        depends_on("py-tensorflow-metadata")
        depends_on("py-termcolor")
        depends_on("py-toml", when="@4.9:")
        depends_on("py-tqdm")
        depends_on("py-wrapt", when="@4.9:")

        # Historical dependencies
        depends_on("py-attrs@18.1.0:", when="@:4.4")
        depends_on("py-dill", when="@:4.4")
        depends_on("py-future", when="@:4.4")
        depends_on("py-six", when="@:4.4")
        depends_on("py-typing-extensions", when="@:4.4 ^python@:3.7")
        depends_on("py-importlib-resources", when="@:4.4 ^python@:3.8")
