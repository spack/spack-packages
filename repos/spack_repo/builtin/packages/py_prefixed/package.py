# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPrefixed(PythonPackage):
    """Prefixed alternative numeric library."""

    homepage = "https://github.com/Rockhopper-Technologies/prefixed"
    pypi = "prefixed/prefixed-0.9.0.tar.gz"

    supplier = "Avram Lubkin <avylove@rockhopper.net>"

    license("MPL-2", checked_by="mr-c")

    version("0.9.0", sha256="164403fa9ebc83280bbc4705f4b243a28837e164310b4e65c38ccab1ebafeeb3")

    with default_args(type="build"):
        depends_on("py-setuptools")
