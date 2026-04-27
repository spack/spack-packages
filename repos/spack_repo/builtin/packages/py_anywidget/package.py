# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAnywidget(PythonPackage):
    """custom jupyter widgets made easy."""

    homepage = "https://github.com/manzt/anywidget"
    pypi = "anywidget/anywidget-0.9.18.tar.gz"

    license("MIT")

    version("0.9.21", sha256="b8d0172029ac426573053c416c6a587838661612208bb390fa0607862e594b27")
    version("0.9.18", sha256="262cf459b517a7d044d6fbc84b953e9c83f026790b2dd3ce90f21a7f8eded00f")

    depends_on("py-hatchling", type="build")
    # from [tool.hatch.build.hooks.jupyter-builder]
    depends_on("py-hatch-jupyter-builder@0.5:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-ipywidgets@7.6:")
        depends_on("py-typing-extensions@4.2:")
        depends_on("py-psygnal@0.8.1:")
