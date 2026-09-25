# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNir(PythonPackage):
    """Neuromorphic Intermediate Representation"""

    homepage = "https://github.com/neuromorphs/nir"
    pypi = "nir/nir-1.0.4.tar.gz"

    license("BSD-3-Clause")

    version("1.0.8", sha256="8567513d84d975f8df444e50b5875fc7271b7bc61fcf85c5556178df35db089f")
    version("1.0.4", sha256="2f864b089cf1daf4147ab6613f24d515d8181e5479940efedb76faff743ad62c")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@1.0.8:")

    depends_on("py-setuptools@60:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
