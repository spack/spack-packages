# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNirtorch(PythonPackage):
    """Neuromorphic Intermediate Representation"""

    homepage = "https://github.com/neuromorphs/NIRTorch"
    pypi = "nirtorch/nirtorch-2.0.2.tar.gz"

    license("BSD-3-Clause")

    version("2.6", sha256="6ed4afaf2eef0b125a8355fddb5adadcee17695083f25f93eac4d29143bd6701")
    version("2.0.2", sha256="ba09d6fd428eecc427eb9b1f7e17dbe3c82bff3a9dd8edd7ac754846ab0596c6")

    depends_on("py-setuptools@60:", type="build")
    depends_on("py-setuptools-scm@8.0:", type="build")

    depends_on("py-torch", type=("build", "run"))
    depends_on("py-nir", type=("build", "run"))
    depends_on("py-nir@1.0.6:", type=("build", "run"), when="@2.6:")
