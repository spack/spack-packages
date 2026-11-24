# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPcpp(PythonPackage):
    """A C99 preprocessor written in pure Python"""

    homepage = "https://github.com/ned14/pcpp"
    pypi = "pcpp/pcpp-1.30.tar.gz"

    license("MIT")

    maintainers("pearzt")

    version("1.30", sha256="5af9fbce55f136d7931ae915fae03c34030a3b36c496e72d9636cedc8e2543a1")

    depends_on("py-setuptools", type="build")
