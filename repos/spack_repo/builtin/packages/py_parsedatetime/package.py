# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyParsedatetime(PythonPackage):
    """Parse human-readable date/time strings."""

    homepage = "https://github.com/bear/parsedatetime"
    pypi = "parsedatetime/parsedatetime-2.5.tar.gz"

    version("2.6", sha256="4cb368fbb18a0b7231f4d76119165451c8d2e35951455dfee97c62a87b04d455")
    version("2.5", sha256="d2e9ddb1e463de871d32088a3f3cea3dc8282b1b2800e081bd0ef86900451667")

    depends_on("py-setuptools", type="build")
