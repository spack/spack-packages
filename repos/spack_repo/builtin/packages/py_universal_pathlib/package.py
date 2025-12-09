# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUniversalPathlib(PythonPackage):
    """pathlib api extended to use fsspec backends."""

    homepage = "https://github.com/fsspec/universal_pathlib"
    pypi = "universal_pathlib/universal_pathlib-0.2.6.tar.gz"

    license("MIT")

    version("0.2.6", sha256="50817aaeaa9f4163cb1e76f5bdf84207fa05ce728b23fd779479b3462e5430ac")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@64:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    depends_on("py-fsspec@2022.1.0:", type=("build", "run"))

    conflicts("py-fsspec@2024.3.1")
