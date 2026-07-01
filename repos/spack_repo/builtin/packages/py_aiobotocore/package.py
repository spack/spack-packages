# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAiobotocore(PythonPackage):
    """Async client for amazon services using botocore and aiohttp/asyncio."""

    homepage = "https://aiobotocore.readthedocs.io/en/latest/"
    pypi = "aiobotocore/aiobotocore-1.2.1.tar.gz"

    license("Apache-2.0")

    version("2.26.0", sha256="50567feaf8dfe2b653570b4491f5bc8c6e7fb9622479d66442462c021db4fadc")
    version("2.12.1", sha256="8706b28f16f93c541f6ed50352115a79d8f3499539f8d0bb70aa0f7a5379c1fe")
    version("2.5.0", sha256="6a5b397cddd4f81026aa91a14c7dd2650727425740a5af8ba75127ff663faf67")
    version("2.4.2", sha256="0603b74a582dffa7511ce7548d07dc9b10ec87bc5fb657eb0b34f9bd490958bf")
    version("1.2.1", sha256="58cc422e65fc89f7cb78eca740d241ac8e15f39f6b308cc23152711e8a987d45")

    depends_on("py-setuptools@77:", type="build", when="@2.26:")
    depends_on("py-setuptools", type="build")
    depends_on("py-botocore@1.41", when="@2.26:", type=("build", "run"))
    depends_on("py-botocore@1.34.41:1.34.51", when="@2.12.1", type=("build", "run"))
    depends_on("py-botocore@1.27.59", when="@2.4.2", type=("build", "run"))
    depends_on("py-botocore@1.19.52", when="@1.2.1", type=("build", "run"))
    depends_on("py-botocore@1.29.76", when="@2.5.0", type=("build", "run"))
    depends_on("py-aiohttp@3.9.2:3", when="@2.26:", type=("build", "run"))
    depends_on("py-aiohttp@3.7.4:3", when="@2.12:", type=("build", "run"))
    depends_on("py-aiohttp@3.3.1:", when="@:2.5", type=("build", "run"))
    depends_on("py-wrapt@1.10.10:1", when="@2.12:", type=("build", "run"))
    depends_on("py-wrapt@1.10.10:", when="@:2.5", type=("build", "run"))
    depends_on("py-aioitertools@0.5.1:0", when="@2.12:", type=("build", "run"))
    depends_on("py-aioitertools@0.5.1:", when="@:2.5", type=("build", "run"))
    depends_on("py-python-dateutil@2.1:2", when="@2.26:", type=("build", "run"))
    depends_on("py-multidict@6", when="@2.26:", type=("build", "run"))
    depends_on("py-jmespath@0.7:1", when="@2.26:", type=("build", "run"))
