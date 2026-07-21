# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySimpleSlurm(PythonPackage):
    """A simple Python wrapper for Slurm with flexibility in mind."""

    homepage = "https://github.com/amq92/simple_slurm"
    pypi = "simple-slurm/simple_slurm-0.3.6.tar.gz"

    license("AGPL-3.0")
    maintainers("adamwitmer")

    version("0.3.6", sha256="0f88cac96b39d7d7e34c5a124919cebb41eb8a8ef2ff4fb65c363d940ff8551e")

    depends_on("py-setuptools", type="build")
