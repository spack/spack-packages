# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIopsBenchmark(PythonPackage):
    """A generic benchmark orchestration framework for automated parametric experiments."""

    homepage = "https://gitlab.inria.fr/lgouveia/iops"
    pypi = "iops_benchmark/iops_benchmark-3.5.8.tar.gz"

    license("BSD-3-Clause")

    version("3.5.8", sha256="04b77c9513702d081fd0af3ba48211dace4bb4425482e51c17684832f2970984")

    depends_on("py-setuptools@61:", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-pandas@2.1:", type=("build", "run"))
    depends_on("py-jinja2@3:", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
