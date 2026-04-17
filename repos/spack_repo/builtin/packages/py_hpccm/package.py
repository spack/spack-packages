# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHpccm(PythonPackage):
    """HPC Container Maker (HPCCM - pronounced H-P-see-M) is an open source
    tool to make it easier to generate container specification files."""

    homepage = "https://github.com/NVIDIA/hpc-container-maker"
    pypi = "hpccm/hpccm-19.2.0.tar.gz"

    license("Apache-2.0")

    version("26.1.0", sha256="f0757993c18df8619d9722c082ffa6edfec07a99d46b4be38f7ee10dfd26fc8b")
    version("19.2.0", sha256="c60eec914a802b0a76596cfd5fdf7122d3f8665fcef06ef928323f5dfb5219a6")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
