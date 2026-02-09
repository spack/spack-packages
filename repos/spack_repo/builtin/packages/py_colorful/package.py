# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyColorful(PythonPackage):
    """Terminal string styling done right, in Python."""

    homepage = "https://github.com/timofurrer/colorful"
    pypi = "colorful/colorful-0.5.4.tar.gz"

    license("MIT")

    version("0.5.8", sha256="bb16502b198be2f1c42ba3c52c703d5f651d826076817185f0294c1a549a7445")
    version("0.5.4", sha256="86848ad4e2eda60cd2519d8698945d22f6f6551e23e95f3f14dfbb60997807ea")

    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
