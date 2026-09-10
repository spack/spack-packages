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

    version("0.3.10", sha256="4487cbc90730a48cfb64f811d99e14b6faed6d738420cd5f93f59f48e6930bfb")
    version("0.2.6", sha256="50817aaeaa9f4163cb1e76f5bdf84207fa05ce728b23fd779479b3462e5430ac")

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@0.3:")
        depends_on("python@3.8:")

        depends_on("py-fsspec@2024.5.0:", when="@0.3:")
        depends_on("py-fsspec@2022.1.0:")
        depends_on("py-pathlib-abc@0.5.1:0.5", when="@0.3.4:")

    conflicts("py-fsspec@2024.3.1", when="@0.2.6")
