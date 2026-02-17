# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakemakeInterfaceSchedulerPlugins(PythonPackage):
    """Scheduler plugin interface for snakemake."""

    homepage = "https://github.com/snakemake/snakemake-interface-scheduler-plugins"
    pypi = (
        "snakemake_interface_scheduler_plugins/snakemake_interface_scheduler_plugins-2.0.2.tar.gz"
    )

    license("MIT")

    version("2.0.2", sha256="2797e8fa9019d983132c2b403f14d6fcd3c5ad4c8d8a66b984b4740a71cacc46")

    depends_on("python@3.11:", type=("build", "run"))

    depends_on("py-hatchling", type="build")

    depends_on("py-snakemake-interface-common@1.20.1:1", type=("build", "run"))
