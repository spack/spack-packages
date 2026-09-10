# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRsatoolbox(PythonPackage):
    """Representational Similarity Analysis (RSA) in Python."""

    homepage = "https://github.com/rsagroup/rsatoolbox"
    pypi = "rsatoolbox/rsatoolbox-0.0.3.tar.gz"
    git = "https://github.com/rsagroup/rsatoolbox.git"

    license("MIT")

    version("main", branch="main")
    version("0.2.0", sha256="ecdcb50387c4b6330077ec2a3a221696078071319b8a0c32ed8128cd38da6863")
    version("0.1.5", sha256="439839fb20e2efa0c7c975ad305df8995a509ed3426ad0384ebfff20663fd58b")

    depends_on("python@3.8:", type=("build", "run"), when="@0.1.5:")

    depends_on("py-setuptools@68:", type="build", when="@0.1.5:")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm+toml@8.0:", type="build", when="@0.1.5:")
    depends_on("py-cython@3", type="build", when="@0.0.5:")
    depends_on("py-twine@4.0.1:", type="build", when="@0.1.5:")

    depends_on("py-numpy@1.21.2:", type=("build", "run"))
    depends_on("py-scipy@1.10.1:", type=("build", "run"), when="@0.2:")
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scikit-image", type=("build", "run"))
    depends_on("py-pandas", when="@0.0.4:", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-networkx@3:", type=("build", "run"), when="@0.2:")

    conflicts("^py-matplotlib@3.9.1")
