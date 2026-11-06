# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEnlighten(PythonPackage):
    """Enlighten Progress Bar is a console progress bar library for Python."""

    homepage = "https://github.com/Rockhopper-Technologies/enlighten"
    pypi = "enlighten/enlighten-1.14.1.tar.gz"

    supplier = "Avram Lubkin <avylove@rockhopper.net>"

    license("MPL-2.0", checked_by="mr-c")

    version("1.14.1", sha256="85c35412a9a4f3886b3337d41f813441fab9a30d9f5b5f0c015bd078a4411473")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-blessed@1.17.7:")
        depends_on("py-prefixed@0.3.2:")
