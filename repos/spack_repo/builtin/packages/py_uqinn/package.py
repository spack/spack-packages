# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUqinn(PythonPackage):
    """Quantification of Uncertainties in Neural Networks (QUiNN) is a
    python library centered around various probabilistic wrappers over
    PyTorch modules in order to provide uncertainty estimation in Neural
    Network (NN) predictions."""

    homepage = "https://github.com/sandialabs/quinn"
    pypi = "uqinn/uqinn-1.0.0.tar.gz"

    maintainers("ksargsyan", "odiazib", "gregvw")

    license("BSD-3-Clause", checked_by="gregvw")

    version("1.0.0", sha256="07c6a5a81bc14af2679e9510f438ef1bbb85eba00c4fdd993fcb1f018f511cac")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
