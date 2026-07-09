# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakemakeStoragePluginPelican(PythonPackage):
    """A Snakemake Storage Plugin for Pelican Federations."""

    homepage = "https://github.com/PelicanPlatform/snakemake-storage-plugin-pelican"
    pypi = "snakemake_storage_plugin_pelican/snakemake_storage_plugin_pelican-0.1.1.tar.gz"
    git = "https://github.com/PelicanPlatform/snakemake-storage-plugin-pelican.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("0.1.1", sha256="a2b436dedaed0cae1edfb0d2d6c32085239eb0c2ec15bed86419d465b7bb5cb5")

    depends_on("python@3.12:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-poetry-core@2")

    with default_args(type=("build", "run")):
        depends_on("py-snakemake-interface-common@1.21:1")
        depends_on("py-snakemake-interface-storage-plugins@4.2.1:4")
        depends_on("py-pelicanfs@1.2.3:")
