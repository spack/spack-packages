# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySuperqt(PythonPackage):
    """Missing widgets and components for PyQt/PySide"""

    homepage = "https://pyapp-kit.github.io/superqt/"
    pypi = "superqt/superqt-0.6.1.tar.gz"

    license("BSD-3-Clause", checked_by="A-N-Other")

    version("0.7.8", sha256="799c76d780ad9ca289a6a87d481686e28d85e47e2383d1579f57a02b572392a8")
    version("0.7.6", sha256="822fdba71dc391929c9d3db839f78ca2a861e2f2876926f969a288dfb2a9787e")
    version("0.6.1", sha256="f1a9e0499c4bbcef34b6f895eb57cd41301b3799242cd030029238124184dade")

    variant("iconify", default=False, description="Use Iconify icons keys")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-packaging")
        depends_on("py-pygments@2.4:")
        depends_on("py-qtpy@2.4:", when="@0.7.6:")
        depends_on("py-qtpy@1.1:")
        depends_on("py-typing-extensions@4.5:", when="@0.7.6:")
        depends_on("py-typing-extensions@3.7.4.3:", when="@0.6.1")
        depends_on("py-pyconify", when="+iconify")

    conflicts("^py-typing-extensions@3.10.0.0")
