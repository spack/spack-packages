# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCylcRose(PythonPackage):
    """A Cylc plugin providing support for the Rose rose-suite.conf file."""

    homepage = "https://cylc.github.io/cylc-doc/latest/html/plugins/cylc-rose.html"
    pypi = "cylc-rose/cylc_rose-1.5.1.tar.gz"
    git = "https://github.com/cylc/cylc-rose.git"

    maintainers("LydDeb", "climbfuji")

    license("GPL-3.0-only")

    version("1.5.1", sha256="280449bc8d2bc0426468b13c0f0602e8ca231c690ece5444af5bd55f6be60284")
    with default_args(deprecated=True):
        version("1.4.2", sha256="d215e2b58fabde66a82f131088b8a3e5add7fab82b226a0b7aa3cc2079ff62e9")
        version("1.3.0", sha256="017072b69d7a50fa6d309a911d2428743b07c095f308529b36b1b787ebe7ab88")

    depends_on("py-setuptools", type="build")
    depends_on("py-metomi-isodatetime", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))

    with when("@1.3.0"):
        depends_on("py-metomi-rose@2.1", type=("build", "run"))
        depends_on("py-cylc-flow@8.2", type=("build", "run"))

    with when("@1.4.2"):
        depends_on("py-metomi-rose@2.3", type=("build", "run"))
        depends_on("py-cylc-flow@8.3.5:8.3", type=("build", "run"))
        depends_on("py-ansimarkup", type=("build", "run"))

    with when("@1.5.1"):
        depends_on("py-metomi-rose@2.4", type=("build", "run"))
        depends_on("py-cylc-flow@8.4", type=("build", "run"))
        depends_on("py-ansimarkup", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/c/cylc-rose/{0}-{1}.tar.gz"
        if version >= Version("1.4"):
            prefix = "cylc_rose"
        else:
            prefix = "cylc-rose"
        return url.format(prefix, version)
