# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDebugpy(PythonPackage):
    """An implementation of the Debug Adapter Protocol for Python."""

    homepage = "https://github.com/microsoft/debugpy/"
    pypi = "debugpy/debugpy-1.8.15.tar.gz"

    # 'debugpy._vendored' requires additional dependencies, Windows-specific
    skip_modules = ["debugpy._vendored"]

    license("MIT")

    version("1.8.20", sha256="55bc8701714969f1ab89a6d5f2f3d40c36f91b2cbe2f65d98bf8196f6a6a2c33")
    version("1.8.15", sha256="58d7a20b7773ab5ee6bdfb2e6cf622fdf1e40c9d5aef2857d85391526719ac00")
    version("1.6.7", sha256="c4c2f0810fa25323abfdfa36cbbbb24e5c3b1a42cb762782de64439c575d67f2")
    version("1.6.6", sha256="b9c2130e1c632540fbf9c2c88341493797ddf58016e7cba02e311de9b0a96b67")
    version("1.6.3", sha256="e8922090514a890eec99cfb991bab872dd2e353ebb793164d5f01c362b9a40bf")
    version("1.5.1", sha256="d2b09e91fbd1efa4f4fda121d49af89501beda50c18ed7499712c71a4bf3452e")
    version("1.4.1", sha256="889316de0b8ff3732927cb058cfbd3371e4cd0002ecc170d34c755ad289c867c")

    depends_on("py-setuptools", type="build")

    def url_for_version(self, version):
        if version >= Version("1.8.10"):
            extention = "tar.gz"
        else:
            extention = "zip"
        return f"https://files.pythonhosted.org/packages/source/t/types-setuptools/debugpy-{version}.{extention}"
