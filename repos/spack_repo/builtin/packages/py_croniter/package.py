# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCroniter(PythonPackage):
    """croniter provides iteration for datetime object with cron like format."""

    homepage = "https://github.com/kiorky/croniter"
    pypi = "croniter/croniter-1.3.8.tar.gz"

    license("MIT")

    version("6.2.4", sha256="fc124f751b1b04805c2a04b061898b436b45ab2320b045e1e052ea895de65189")
    version("1.3.8", sha256="32a5ec04e97ec0837bcdf013767abd2e71cceeefd3c2e14c804098ce51ad6cd9")

    depends_on("py-setuptools", type="build")
    # The following build dependencies are relaxed compared to upstream
    depends_on("py-hatchling@1.30.1:", type="build")
    depends_on("py-packaging@26.2:", type="build")
    depends_on("py-pathspec@1.1.1:", type="build")
    depends_on("py-pluggy@1.6.0:", type="build")
    depends_on("py-trove-classifiers@2026.3.1.19:", type="build")

    depends_on("py-python-dateutil", type=("build", "run"))
