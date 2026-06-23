# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Topaz(PythonPackage):
    """topaz: Pipeline for particle picking in cryo-electron microscopy images using
    convolutional neural networks trained from positive and unlabeled examples. Also
    featuring micrograph and tomogram denoising with DNNs."""

    homepage = "https://topaz-em.readthedocs.io/"
    pypi = "topaz-em/topaz_em-0.3.7.tar.gz"

    license("GPL-3.0-or-later")

    version("0.3.18", sha256="a68a426bea0c0999a714f868694d7a5f07cfb0456098e99ac3e7b33865abcd7b")
    version("0.3.7", sha256="ae3c0d6ccb1e8ad2e4926421442b8cb33a4d01d1ee1dff83174949a9f91cc8a9")
    version(
        "0.2.5",
        sha256="002a6eb775598b6c4df0225f3a488bfe6a6da9246e8ca42eb4e7d58f694c25cc",
        url="https://files.pythonhosted.org/packages/source/t/topaz-em/topaz-em-0.2.5.tar.gz",
    )

    depends_on("py-setuptools", type="build")
    with default_args(type=("build", "run")):
        depends_on("python@3")
        depends_on("python@3.8:3.12", when="@0.3.7:")
        depends_on("py-torch@1:2.3.1", when="@:0.3.7")
        depends_on("py-torch@1:", when="@0.3.18:")
        depends_on("py-torchvision")
        depends_on("py-numpy@1.11:")
        depends_on("py-pandas@0.20.3:")
        depends_on("py-scikit-learn@0.19.0:")
        depends_on("py-scipy@0.17.0:")
        depends_on("py-pillow@6.2.0:")
        depends_on("py-future")
        depends_on("py-tqdm@4.65.0:", when="@0.3.7:")
        depends_on("py-h5py@3.7.0:", when="@0.3.7:")
