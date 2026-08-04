# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWxpython(PythonPackage):
    """Cross platform GUI toolkit for Python."""

    homepage = "https://www.wxpython.org/"
    pypi = "wxpython/wxpython-4.0.6.tar.gz"
    git = "https://github.com/wxWidgets/Phoenix.git"

    version("4.2.5", sha256="44e836d1bccd99c38790bb034b6ecf70d9060f6734320560f7c4b0d006144793")
    version("4.2.4", sha256="2eb123979c87bcb329e8a2452269d60ff8f9f651e9bf25c67579e53c4ebbae3c")
    version("4.2.3", sha256="20d6e0c927e27ced85643719bd63e9f7fd501df6e9a8aab1489b039897fd7c01")
    version("4.2.2", sha256="5dbcb0650f67fdc2c5965795a255ffaa3d7b09fb149aa8da2d0d9aa44e38e2ba")
    version("4.1.1", sha256="00e5e3180ac7f2852f342ad341d57c44e7e4326de0b550b9a5c4a8361b6c3528")
    version("4.0.6", sha256="35cc8ae9dd5246e2c9861bb796026bbcb9fb083e4d49650f776622171ecdab37")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("pkgconfig")
        # As of 4.2.4, sdists no longer ship wx/svg/_nanosvg.c
        # https://github.com/wxWidgets/Phoenix/issues/2843
        depends_on("py-cython", when="@4.2.4:")
        depends_on("py-pathlib2")
        depends_on("py-requests")

        depends_on("py-setuptools")
        depends_on("py-setuptools@:75", when="@:4.1")
        # Older 4.2 versions use the old copy_file() function of py-setuptools@:80
        depends_on("py-setuptools@:80", when="@4.2:4.2.4")

    # Versions before 4.2.3 require distutils which is removed in python 3.12
    depends_on("python@:3.11", when="@:4.2.2")
    # See https://www.wxpython.org/news/2022-08-07-wxpython-411-release/
    depends_on("python@:3.9", when="@:4.1")

    # Pre-generated Cython C files fail to build with free-threaded Python
    # https://github.com/wxWidgets/Phoenix/issues/2707
    conflicts("^python+freethreading", when="@:4.2.3")

    depends_on("wxwidgets +gui")
    depends_on("wxwidgets@3.2.6 +gui", when="@4.2.2")
    depends_on("wxwidgets@3.2.7 +gui", when="@4.2.3")
    depends_on("wxwidgets@3.2.8.1 +gui", when="@4.2.4")
    depends_on("wxwidgets@3.2.9 +gui", when="@4.2.5")

    # Needed at runtime
    depends_on("py-numpy", type=("build", "run"))
    depends_on("pil", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/w/wxPython/wxPython-{0}.tar.gz"
        if version >= Version("4.2.3"):
            url = url.lower()
        return url.format(version)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # By default wxWidgets is built as well instead of using spack provided version,
        # this tells it to just build the python extensions
        env.set("WXPYTHON_BUILD_ARGS", "build_py --use_syswx")
