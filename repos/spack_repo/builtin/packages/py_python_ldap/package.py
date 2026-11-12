# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonLdap(PythonPackage):
    """python-ldap provides an object-oriented API to access LDAP directory
    servers from Python programs.
    """

    homepage = "https://www.python-ldap.org/en/python-ldap-3.2.0/"
    pypi = "python-ldap/python-ldap-3.2.0.tar.gz"

    license("MIT")

    # Note: 3.4.6 is skipped intentionally: it has no sdist on PyPI and its
    # artifacts contained unintended files (see the 3.4.7 release notes)
    version("3.4.7", sha256="bacd9fb680d20263d8570ade1cf234d90d281149a8beb4f079dd8f33f7613dc8")
    version("3.4.5", sha256="b2f6ef1c37fe2c6a5a85212efe71311ee21847766a7d45fcb711f3b270a5f79a")
    version("3.4.4", sha256="7edb0accec4e037797705f3a05cbf36a9fde50d08c8f67f2aef99a2628fab828")
    version("3.4.3", sha256="ab26c519a0ef2a443a2a10391fa3c5cb52d7871323399db949ebfaa9f25ee2a0")
    version("3.4.2", sha256="b16470a0983aaf09a00ffb8f40b69a2446f3d0be639a229256bce381fcb268f7")
    version("3.4.0", sha256="60464c8fc25e71e0fd40449a24eae482dcd0fb7fcf823e7de627a6525b3e0d12")
    version("3.3.1", sha256="4711cacf013e298754abd70058ccc995758177fb425f1c2d30e71adfc1d00aa5")
    version("3.3.0", sha256="de04939485b53ee5d9a6855562d415b73060c52e681644386de4d5bd18e3f540")
    version("3.2.0", sha256="7d1c4b15375a533564aad3d3deade789221e450052b21ebb9720fb822eccdb8e")
    version("3.1.0", sha256="41975e79406502c092732c57ef0c2c2eb318d91e8e765f81f5d4ab6c1db727c5")
    version("3.0.0", sha256="86746b912a2cd37a54b06c694f021b0c8556d4caeab75ef50435ada152e2fbe1")

    depends_on("c", type="build")  # generated

    # See https://github.com/python-ldap/python-ldap/issues/432
    depends_on("openldap+client_only @:2.4", type=("build", "link", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))
    depends_on("python@3.6:", when="@3.4.0:", type=("build", "run"))
    # distutils was removed from the stdlib in Python 3.12; releases before
    # 3.4.4 still import it during the wheel build
    depends_on("python@:3.11", when="@:3.4.3", type=("build", "run"))
    depends_on("py-pyasn1@0.3.7:", type=("build", "run"))
    depends_on("py-pyasn1-modules@0.1.5:", type=("build", "run"))
    depends_on("cyrus-sasl", type="link", when="^openldap+sasl")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/p/{0}/{0}-{1}.tar.gz"
        # PEP 625: sdist filename uses an underscore since 3.4.5
        name = "python_ldap" if version >= Version("3.4.5") else "python-ldap"
        return url.format(name, version)

    def patch(self):
        if self.spec.satisfies("^openldap~sasl"):
            filter_file("HAVE_SASL ", "", "setup.cfg")

        # "optimize = 1" in the [install] section makes setuptools byte-compile
        # via a subprocess that imports distutils, removed in Python 3.12.
        # Byte-compilation at install time is unnecessary, so drop it.
        if self.spec.satisfies("^python@3.12:"):
            filter_file("^(compile|optimize) = 1$", "", "setup.cfg")
