# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakemakeStoragePluginRucio(PythonPackage):
    """A Snakemake storage plugin that handles files available through Rucio."""

    homepage = "https://github.com/bouweandela/snakemake-storage-plugin-rucio"
    url = "https://github.com/bouweandela/snakemake-storage-plugin-rucio/archive/refs/tags/v0.4.1.tar.gz"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("0.4.1", sha256="2e1ed50402b90ec85fc6f0a79b2dd27ad52cdfb80195f0ced8965af93e1d4742")

    depends_on("python@3.11:3", type=("build", "run"))
    depends_on("py-poetry-core", type="build")

    depends_on("py-rucio-clients@36:", type=("build", "run"))
    depends_on("snakemake@9.5.1:", type=("build", "run"))
    depends_on("py-snakemake-interface-common@1.18:1", type=("build", "run"))
    depends_on("py-snakemake-interface-storage-plugins@4.2.1:", type=("build", "run"))
