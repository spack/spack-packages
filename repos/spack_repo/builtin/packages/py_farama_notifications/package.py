# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFaramaNotifications(PythonPackage):
    """Allows for providing notifications on import to all Farama Packages."""

    homepage = "https://github.com/Farama-Foundation/Farama-Notifications"
    pypi = "farama_notifications/farama_notifications-0.0.6.tar.gz"

    license("MIT")

    version("0.0.6", sha256="b19acac4bb41d76e59e03394b5dd165f4761c86fa327f56307a35cbee3b60158")

    depends_on("py-setuptools@42:", type="build")
    depends_on("python@3.8:", type=("build", "run"))
