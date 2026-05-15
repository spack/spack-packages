# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonXmpToolkit(PythonPackage):
    """Python XMP Toolkit for working with metadata."""

    homepage = "https://github.com/python-xmp-toolkit/python-xmp-toolkit"
    pypi = "python_xmp_toolkit/python_xmp_toolkit-2.1.0.tar.gz"

    license("BSD-3-Clause")

    version("2.1.0", sha256="ca0aa2c60d418dd2558767db59953ab5954fb5b87dc0b50cecd60566b0b4e2da")
    version("2.0.1", sha256="f8d912946ff9fd46ed5c7c355aa5d4ea193328b3f200909ef32d9a28a1419a38")

    with default_args(type="build"):
        depends_on("py-flit-core@3.2:3", when="@2.1:")

        # Historical dependencies
        depends_on("py-setuptools", when="@2.0")

    with default_args(type=("build", "run")):
        depends_on("py-pytz")
        depends_on("exempi@2.2.0:")

        # needed for ld used in ctypes.util.find_library to find exempi
        depends_on("binutils")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.spec["exempi"].prefix.lib)

    def url_for_version(self, version):
        if self.spec.satisfies("@2.1:"):
            name = "python_xmp_toolkit"
        else:
            name = "python-xmp-toolkit"
        return f"https://files.pythonhosted.org/packages/source/{name[0]}/{name}/{name}-{version}.tar.gz"
