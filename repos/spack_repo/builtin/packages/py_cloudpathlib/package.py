# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCloudpathlib(PythonPackage):
    """pathlib-style classes for cloud storage services."""

    homepage = "https://github.com/drivendataorg/cloudpathlib"
    pypi = "cloudpathlib/cloudpathlib-0.23.0.tar.gz"

    license("MIT")

    version("0.23.0", sha256="eb38a34c6b8a048ecfd2b2f60917f7cbad4a105b7c979196450c2f541f4d6b4b")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-flit-core@3.2:3", type="build")
    depends_on("py-typing-extensions@4:", type=("build", "run"), when="^python@:3.10")
