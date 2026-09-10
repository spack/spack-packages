# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQutip(PythonPackage):
    """QuTiP: The Quantum Toolbox in Python"""

    homepage = "https://qutip.org/"
    pypi = "qutip/qutip-4.7.0.tar.gz"

    license("BSD-3-Clause")

    version("5.3.1", sha256="056206b40cbe97c3c7e4f85eff11873406669cd72b2db039fa1a3812767395e9")
    version("4.7.1", sha256="9a87178e68b145c2145b526caa943ccc8400a111325ced45bd17f9b893663af2")
    version("4.7.0", sha256="a9dde64457991ef1c5a7d4186b5348a16a71480a610f1c0902e4d656ddc12e31")

    depends_on("cxx", type="build")  # generated

    depends_on("py-setuptools@77.0.3:", type="build", when="@5:")
    depends_on("py-setuptools", type="build")
    depends_on("py-packaging", type=("build", "run"))

    depends_on("py-cython@0.29.20:", type="build")
    depends_on("py-numpy@2:", type=("build", "run"), when="@5:")
    depends_on("py-numpy@1.16.6:", type=("build", "run"), when="@4")
    # https://github.com/qutip/qutip/pull/2421
    depends_on("py-numpy@:1", type=("build", "run"), when="@4")
    depends_on("py-scipy@1.9:1.15,1.8:", type=("build", "run"), when="@5:")
    depends_on("py-scipy@1.0:", type=("build", "run"))
