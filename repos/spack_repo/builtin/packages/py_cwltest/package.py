# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCwltest(PythonPackage):
    """Common Workflow Language testing framework"""

    homepage = "https://github.com/common-workflow-language/cwltest"
    pypi = "cwltest/cwltest-2.7.20260814150058.tar.gz"

    supplier = "https://www.commonwl.org"

    maintainers("mr-c")

    license("Apache-2.0", checked_by="mr-c")

    version(
        "2.7.20260814150058",
        sha256="8aeeccfcc22be3b5ada5611c63e721c7f3251477959bcdc1e006e2fdbd27b967",
    )

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@61.2:")
        depends_on("py-setuptools-scm@8.0.4:")

    with default_args(type=("build", "run")):
        depends_on("py-schema-salad@5.0.20200220195218:9")
        depends_on("py-junit-xml@1.8:")
