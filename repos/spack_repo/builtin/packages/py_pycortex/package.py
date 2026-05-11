# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPycortex(PythonPackage):
    """Python Cortical mapping software for fMRI data."""

    # When pycortex is started it creates a user config file (on linux located
    # in ~/.config/pycortex) which can be problematic when reinstalling a newer
    # version with spack due to hardscoded absolute paths of the pycortex module

    homepage = "https://github.com/gallantlab/pycortex"
    pypi = "pycortex/pycortex-1.2.2.tar.gz"

    license("BSD-2-Clause")

    version("1.3.1", sha256="2d4eef825cde211a33b5cdb51fd974674042834653f8fd163b8e3b20e061af60")
    version("1.2.2", sha256="ac46ed6a1dc727c3126c2b5d7916fc0ac21a6510c32a5edcd3b8cfb7b2128414")

    with default_args(type="build"):
        depends_on("c")

        depends_on("py-setuptools@64:", when="@1.2.13:")
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm@8:", when="@1.2.13:")
        depends_on("py-build", when="@1.2.9:")

    with default_args(type=("build", "run")):
        # from requirements.txt
        depends_on("py-setuptools", when="@1.2.9:")
        depends_on("py-future")
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-tornado@4.3:")
        depends_on("py-shapely")
        depends_on("py-lxml")
        depends_on("py-html5lib")
        depends_on("py-h5py")
        depends_on("py-numexpr")
        depends_on("py-cython", when="@1.2.11:")
        depends_on("py-cython@:2", when="@:1.2.10")
        depends_on("py-matplotlib")
        depends_on("pil")
        depends_on("py-nibabel@2.1:", when="@1.2.6:")
        depends_on("py-nibabel")
        depends_on("py-networkx@2.1:")
        depends_on("py-imageio")
        depends_on("py-looseversion", when="@1.2.10:")
        depends_on("py-mda-xdrlib", when="@1.2.11:")
        depends_on("py-typing-extensions", when="@1.3: ^python@:3.10")

        # Historical dependencies
        depends_on("py-wget", when="@:1.2.8")

    # inkscape is not in spack
    # TODO remove this patch and add inkscape dependency once it is in
    def patch(self):
        # remove inkscape dependency
        filter_file(
            "from .testing_utils import INKSCAPE_VERSION", "", "cortex/utils.py", string=True
        )
        filter_file("open_inkscape=True", "open_inkscape=False", "cortex/utils.py", string=True)
        filter_file(
            "from .testing_utils import INKSCAPE_VERSION",
            "INKSCAPE_VERSION = None",
            "cortex/svgoverlay.py",
            string=True,
        )
