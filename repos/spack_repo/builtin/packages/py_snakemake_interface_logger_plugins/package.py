# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakemakeInterfaceLoggerPlugins(PythonPackage):
    """Logger plugin interface for snakemake."""

    homepage = "https://github.com/snakemake/snakemake-interface-logger-plugins"
    pypi = "snakemake_interface_logger_plugins/snakemake_interface_logger_plugins-2.0.0.tar.gz"

    license("MIT")

    version("2.0.0", sha256="0e8ff2af4c55ca140d6ea1c1540e733a4b3944abae48fe0eaf6a707e5797cd17")
    version("1.2.5", sha256="efa63ce156fb85fbdde0bf3e77e3319690b28280313a57c54c683a9e691f41ab")
    version("1.1.0", sha256="8af888a5def0ad58a7b244e34b5edfde4608bbf572cba8c648407ebfbf2cc855")

    depends_on("python@3.11:", type=("build", "run"))

    depends_on("py-hatchling", type="build")

    depends_on("py-snakemake-interface-common@1.17.4:", type=("build", "run"))
