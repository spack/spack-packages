# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.sip import SIPPackage

from spack.package import *


class PyPyqt6(SIPPackage):
    """PyQt6 is a comprehensive set of Python bindings for Qt v6."""

    homepage = "https://www.riverbankcomputing.com/software/pyqt/"
    url = "https://files.pythonhosted.org/packages/source/P/PyQt6/pyqt6-6.9.1.tar.gz"
    list_url = "https://pypi.org/simple/PyQt6/"

    license("GPL-3.0-or-later")

    version("6.11.0", sha256="45dd60aa69976de1918b5ced6b4e7b6a25abd2a919ecef5fd5826ecc76718889")
    version("6.10.0", sha256="710ecfd720d9a03b2c684881ae37f528e11d17e8f1bf96431d00a6a73f308e36")
    version("6.9.1", sha256="50642be03fb40f1c2111a09a1f5a0f79813e039c15e78267e6faaf8a96c1c3a6")
    version("6.7.0", sha256="3d31b2c59dc378ee26e16586d9469842483588142fc377280aad22aaf2fa6235")
    version("6.6.1", sha256="9f158aa29d205142c56f0f35d07784b8df0be28378d20a97bcda8bd64ffd0379")
    version("6.5.2", sha256="1487ee7350f9ffb66d60ab4176519252c2b371762cbe8f8340fd951f63801280")
    version("6.5.1", sha256="e166a0568c27bcc8db00271a5043936226690b6a4a74ce0a5caeb408040a97c3")

    with default_args(type="build"):
        depends_on("cxx")

        # pyproject.toml
        depends_on("py-sip@6.15:6", when="@6.10:")
        depends_on("py-sip@6.13.1:6", when="@6.10:")
        depends_on("py-sip@6.12:6", when="@6.9.1:")
        depends_on("py-sip@6.8:6", when="@6.7:")
        depends_on("py-sip@6.5:6", when="@:6.6")
        depends_on("py-pyqt-builder@1.19:1", when="@6.10:")
        depends_on("py-pyqt-builder@1.17:1", when="@6.8:")
        depends_on("py-pyqt-builder@1.15:1")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@6.11:")
        depends_on("python@3.9:", when="@6.8:")
        depends_on("python@3.8:", when="@6.7:")

        # PKG-INFO
        depends_on("py-pyqt6-sip@13.11:13", when="@6.11:")
        depends_on("py-pyqt6-sip@13.8:13", when="@6.7.1:")
        depends_on("py-pyqt6-sip@13.6:13", when="@6.5.3:6.7.2")
        depends_on("py-pyqt6-sip@13.4:13", when="@:6.5.2")

    # README
    depends_on("qt-base@6+gui+accessibility")

    def url_for_version(self, version):
        if version >= Version("6.8.1"):
            name = "pyqt6"
        else:
            name = "PyQt6"
        return f"https://files.pythonhosted.org/packages/source/P/PyQt6/{name}-{version}.tar.gz"

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Detected system locale encoding (US-ASCII, locale "C") is not UTF-8.
        # Qt shall use a UTF-8 locale ("UTF-8") instead. If this causes problems,
        # reconfigure your locale. See the locale(1) manual for more information.
        env.set("LC_ALL", "en_US.UTF-8")

    def configure_args(self):
        # https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html
        return ["--confirm-license", "--no-make", "--qmake", self.spec["qt-base"].prefix.bin.qmake]
