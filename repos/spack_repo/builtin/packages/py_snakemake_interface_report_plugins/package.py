# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakemakeInterfaceReportPlugins(PythonPackage):
    """The interface for Snakemake report plugins."""

    homepage = "https://github.com/snakemake/snakemake-interface-report-plugins"
    pypi = "snakemake_interface_report_plugins/snakemake_interface_report_plugins-1.0.0.tar.gz"

    license("MIT")

    version("1.3.0", sha256="fc9495298bec4e69721ab8afe6d6d88a86966fda2eeb003db56b9a88b86d5934")
    version("1.2.0", sha256="36cff4d50e7763ae0def0a7cf36d85e6c575d7bad1a3ade26b66c9b2b8831c02")
    version("1.1.2", sha256="3d1218c5897345632f138a3f02794dfef7e59e407100c2a87313307a2da63c5b")
    version("1.1.0", sha256="b1ee444b2fca51225cf8a102f8e56633791d01433cd00cf07a1d9713a12313a5")
    version("1.0.0", sha256="02311cdc4bebab2a1c28469b5e6d5c6ac6e9c66998ad4e4b3229f1472127490f")

    depends_on("py-snakemake-interface-common@1.16:1", type=("build", "run"))

    depends_on("python@:3", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
