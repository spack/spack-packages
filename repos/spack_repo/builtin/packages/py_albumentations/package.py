# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAlbumentations(PythonPackage):
    """albumentations is a fast image augmentation library and
    easy to use wrapper around other libraries."""

    homepage = "https://github.com/albu/albumentations"
    pypi = "albumentations/albumentations-1.1.0.tar.gz"

    license("MIT")

    version("2.0.8", sha256="4da95e658e490de3c34af8fcdffed09e36aa8a4edd06ca9f9e7e3ea0b0b16856")
    version("1.3.1", sha256="a6a38388fe546c568071e8c82f414498e86c9ed03c08b58e7a88b31cf7a244c6")
    version("1.1.0", sha256="60b067b3093908bcc52adb2aa5d44f57ebdbb8ab57a47b0b42f3dc1d3b1ce824")
    version("0.4.2", sha256="93baec3ca01a61bc81fa80563cdebf35dbae3f86b573e4cbe5c141c94782737f")

    depends_on("python@3.6:", type=("build", "run"), when="@1.1.0:")
    depends_on("python@3.7:", type=("build", "run"), when="@1.3.1:")
    depends_on("python@3.9:", type=("build", "run"), when="@2.0.8:")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@45:", type="build", when="@2.0.8:")
    depends_on("py-numpy@1.11.1:", type=("build", "run"))
    depends_on("py-numpy@1.24.4:", type=("build", "run"), when="@2.0.8:")
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scipy@1.1:", when="@1.3.1:", type=("build", "run"))
    depends_on("py-scipy@1.10:", when="@2.0.8:", type=("build", "run"))
    depends_on("py-imgaug@0.2.5:0.2.6", type=("build", "run"), when="@0.4.2")
    depends_on("py-scikit-image@0.16.1:1.18", type=("build", "run"), when="@1.1.0")
    depends_on("py-scikit-image@0.16.1:", type=("build", "run"), when="@1.3.1")
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-qudida@0.0.4:", type=("build", "run"), when="@1.1.0:")
    depends_on("py-typing-extensions@4.9:", type=("build", "run"), when="@2.0.8:^python@:3.9")
    depends_on("py-pydantic@2.9.2:", type=("build", "run"), when="@2.0.8:")
    depends_on("py-albucore@0.0.24", type=("build", "run"), when="@2.0.8:")
    depends_on("opencv@4.1.1:+python3+contrib", type=("build", "run"))
    depends_on("opencv@4.9.0.80:+python3+contrib+photo", type=("build", "run"), when="@2.0.8:")
