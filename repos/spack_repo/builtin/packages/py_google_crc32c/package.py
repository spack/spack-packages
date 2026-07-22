# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGoogleCrc32c(PythonPackage):
    """This package wraps the google/crc32c hardware-based implementation
    of the CRC32C hashing algorithm."""

    homepage = "https://github.com/googleapis/python-crc32c"
    pypi = "google-crc32c/google-crc32c-1.3.0.tar.gz"

    maintainers("marcusboden")

    license("Apache-2.0")

    version("1.8.0", sha256="a428e25fb7691024de47fecfbff7ff957214da51eddded0da0ae0e0f03a2cf79")
    version("1.3.0", sha256="276de6273eb074a35bc598f8efbc00c7869c5cf2e29c90748fccc8c898c244df")

    depends_on("c", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("google-crc32c", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/g/{0}/{0}-{1}.tar.gz"
        if version > Version("1.5.0"):
            name = "google_crc32c"
        else:
            name = "google-crc32c"
        return url.format(name, version)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CRC32C_INSTALL_PREFIX", self.spec["google-crc32c"].prefix)
