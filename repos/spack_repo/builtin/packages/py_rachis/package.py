# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRachis(PythonPackage):
    """Rachis Framework (Formerly Known as QIIME 2 Framework (Q2F))"""

    homepage = "https://qiime2.org/"
    pypi = "rachis/rachis-2026.1.0.tar.gz"

    license("BSD-3-Clause")

    version("2026.1.0", sha256="692449dd06025902943c2ec3810dbb03683dee5e92e138f4d1b0c419972f7511")

    depends_on("python@3.10:3.11", type=("build", "run"))
    depends_on("py-setuptools@80.9:80", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-appdirs@1.4.4:1")
        depends_on("py-bibtexparser@1.4.3:1")
        depends_on("py-decorator@4.4.2:4.4")
        depends_on("py-dill@0.4")
        depends_on("py-flufl-lock@9")
        depends_on("py-networkx@3.1:4")
        depends_on("py-numpy@1.26:2")
        depends_on("py-pandas@2.2:2")
        depends_on("py-parsl@2026:")
        depends_on("py-psutil@7.1.3:7")
        depends_on("py-python-dateutil@2.9.0.post0:2")
        depends_on("py-pyyaml@6.0.3:6")
        depends_on("py-tomlkit@0.13.3:0.13")
        depends_on("py-tzlocal@5.3.1:5")
        depends_on("py-lxml@6.0.2:6")
