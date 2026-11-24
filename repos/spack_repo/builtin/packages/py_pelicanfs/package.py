# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPelicanfs(PythonPackage):
    """An FSSpec Implementation using the Pelican System."""

    homepage = "https://github.com/PelicanPlatform/pelicanfs"
    pypi = "pelicanfs/pelicanfs-1.3.1.tar.gz"
    git = "https://github.com/PelicanPlatform/pelicanfs.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("1.3.1", sha256="fc650efbaf2863eb072aab8624452a63f304dad472934402f862ad05e5b7a958")

    depends_on("python@3.11:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@61:")

    with default_args(type=("build", "run")):
        depends_on("py-aiohttp@3.9.4:3")
        depends_on("py-aiowebdav2")
        depends_on("py-cachetools@5.3:5")
        depends_on("py-fsspec@2024.3.1:")
        depends_on("py-igwn-auth-utils")
        depends_on("py-pywinpty", when="platform=windows")
