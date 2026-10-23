# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJunitXml(PythonPackage):
    """Creates JUnit XML test result documents that can be read by tools
    such as Jenkins"""

    homepage = "https://github.com/kyrus/python-junit-xml"
    pypi = "junit-xml/junit-xml-1.7.tar.gz"

    license("MIT")

    version("1.9", sha256="de16a051990d4e25a3982b2dd9e89d671067548718866416faec14d9de56db9f")
    version("1.8", sha256="602f1c480a19d64edb452bf7632f76b5f2cb92c1938c6e071dcda8ff9541dc21")
    version("1.7", sha256="5bc851b53e3e2153dcc62278ce2aa796a8ae9208f1dec36d1507b5af445ce355")

    depends_on("py-setuptools", type="build")
    depends_on("py-six", type=("build", "run"))
