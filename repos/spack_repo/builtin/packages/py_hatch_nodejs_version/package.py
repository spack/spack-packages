# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHatchNodejsVersion(PythonPackage):
    """Hatch plugin for versioning from a package.json file."""

    homepage = "https://github.com/agoose77/hatch-nodejs-version"
    pypi = "hatch_nodejs_version/hatch_nodejs_version-0.3.1.tar.gz"

    license("MIT")

    version("0.4.0", sha256="2428ea398dd053f019d2b7ac949dd6b690ca8e826b6d433ad13c5b6c475ae91b")
    version("0.3.2", sha256="8a7828d817b71e50bbbbb01c9bfc0b329657b7900c56846489b9c958de15b54c")
    version("0.3.1", sha256="0e55fd713d92c5c1ccfee778efecaa780fd8bcd276d4ca7aff9f6791f6f76d9c")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@0.4:")
        depends_on("python@3.7:")

        depends_on("py-hatchling@0.21:")
