# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWerkzeug(PythonPackage):
    """The Swiss Army knife of Python web development"""

    homepage = "https://palletsprojects.com/p/werkzeug"
    pypi = "werkzeug/werkzeug-3.0.0.tar.gz"
    git = "https://github.com/pallets/werkzeug.git"

    license("BSD-3-Clause", checked_by="wdconinc")

    version("3.1.3", sha256="60723ce945c19328679790e3282cc758aa4a6040e4bb330f53d30fa546d44746")
    version("3.0.4", sha256="34f2371506b250df4d4f84bfe7b0921e4762525762bbd936614909fe25cd7306")
    version("3.0.0", sha256="3ffff4dcc32db52ef3cc94dff3000a3c2846890f3a5a51800a27b909c5e770f0")

    depends_on("py-flit-core@:3", type="build")
    depends_on("py-markupsafe@2.1.1:", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/w/werkzeug/werkzeug-{}.tar.gz"
        return url.format(version)
