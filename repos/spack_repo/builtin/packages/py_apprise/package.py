# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyApprise(PythonPackage):
    """Apprise - Push Notifications that work with just about every platform!"""

    homepage = "https://github.com/caronc/apprise"
    pypi = "apprise/apprise-1.9.6.tar.gz"

    version("1.9.6", sha256="4206be9cb5694a3d08dd8e0393bbb9b36212ac3a7769c2633620055e75c6caef")

    license("BSD-2-Clause")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@69:", type="build")

    depends_on("py-requests", type=("build", "run"))
    depends_on("py-requests-oauthlib", type=("build", "run"))
    depends_on("py-click@5:", type=("build", "run"))
    depends_on("py-markdown", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-certifi", type=("build", "run"))
    depends_on("py-tzdata", when="platform=windows", type=("build", "run"))
