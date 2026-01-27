# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.pipx import PipxPackage

from spack.package import *


class PipxMypy(PipxPackage):
    """Optional static typing for Python."""

    homepage = "http://www.mypy-lang.org/"
    pypi = "mypy/mypy-1.11.1.tar.gz"
    git = "https://github.com/python/mypy.git"

    maintainers("ebagrenrut")

    license("MIT")

    version("1.19.1", sha256="19d88bb05303fe63f71dd2c6270daca27cb9401c4ca8255fe50d1d920e0eb9ba")
    version("1.18.2", sha256="06a398102a5f203d7477b2923dda3634c36727fa5c237d8f859ef90c42a9924b")
    version("1.15.0", sha256="404534629d51d3efea5c800ee7c42b72a6554d6c400e6a79eafe15d11341fd43")
    version("1.14.1", sha256="7ec88144fe9b510e8475ec2f5f251992690fcf89ccb4500b214b4226abcd32d6")
    version("1.11.1", sha256="f404a0b069709f18bbdb702eb3dcfe51910602995de00bd39cea3050b5772d08")
    version("1.3.0", sha256="e1f4d16e296f5135624b34e8fb741eb0eadedca90862405b1f1fde2040b9bd11")

    depends_on("python@3.9:", when="@1.15.0:")
    depends_on("python@3.8:", when="@1.5.0:")
    depends_on("python@3.7:")
