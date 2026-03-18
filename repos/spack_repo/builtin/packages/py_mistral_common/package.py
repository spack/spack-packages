# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMistralCommon(PythonPackage):
    """Mistral-common is a library of common utilities for Mistral AI."""

    homepage = "https://github.com/mistral-ai/mistral-common"
    pypi = "mistral_common/mistral_common-1.10.0.tar.gz"

    license("Apache-2.0", checked_by="thomas-bouvier")

    version("1.10.0", sha256="e456ff101edbdfc094039ec6c26f7d0f73356729798d628a6e6e96c3917147bc")

    variant("image", default=False, description="Enable image support")
    variant("opencv", default=False, description="Enable OpenCV support", when="+image")

    conflicts("~opencv", when="+image")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-pydantic@2.12:2", when="^python@3.14:", type=("build", "run"))
    depends_on("py-pydantic@2.7:2", when="^python@:3.13", type=("build", "run"))
    depends_on("py-jsonschema@4.21.1:", type=("build", "run"))
    depends_on("py-typing-extensions@4.11.0:", type=("build", "run"))
    depends_on("py-tiktoken@0.12.0:", when="^python@3.14:", type=("build", "run"))
    depends_on("py-titkoken@0.7.0:", when="^python@:3.13", type=("build", "run"))
    depends_on("pil@10.3.0:", type=("build", "run"))
    depends_on("py-requests@2:", type=("build", "run"))
    depends_on("py-numpy@1.25:", when="^python@3.13:", type=("build", "run"))
    depends_on("py-numpy@1.25:2.3", when="^python@:3.12", type=("build", "run"))
    depends_on("py-pydantic-extra-types@2.10.5: +pycountry", type=("build", "run"))

    depends_on("py-opencv-python@4: +headless", when="+opencv", type=("build", "run"))
