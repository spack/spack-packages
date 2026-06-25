# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAlbumentationsx(PythonPackage):
    """Fast image augmentation library for deep learning and computer vision."""

    homepage = "https://github.com/albumentations-team/AlbumentationsX"
    pypi = "albumentationsx/albumentationsx-2.3.1.tar.gz"

    license("AGPL-3.0-or-later")

    version("2.3.1", sha256="45c43cb86d095e0186f63fa51ff14b47a91adc0eed978d75d1c7321300781d97")

    variant("contrib", default=False, description="Install OpenCV contrib support")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-albucore@0.1.6", type=("build", "run"))
    depends_on("py-numpy@1.24.4:", type=("build", "run"))

    depends_on(
        "opencv@4.13.0:+python3+contrib+imgproc+photo", type=("build", "run"), when="+contrib"
    )

    depends_on("py-pydantic@2.12.4:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))

    depends_on("py-scipy@1.10:", type=("build", "run"))
    depends_on("py-typing-extensions@4.9.0:", type=("build", "run"))
