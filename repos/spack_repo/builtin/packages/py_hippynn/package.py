# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHippynn(PythonPackage):
    """python library for atomistic machine learning"""

    homepage = "https://lanl.github.io/hippynn/"
    pypi = "hippynn/hippynn-0.1.3.tar.gz"

    license("BSD-3-Clause")

    version("0.1.3", sha256="87e10de2e0db01280ac9001720e5c2e4feeed6f3487f98763af2c2126e1bcd4a")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@64:", type="build")
    depends_on("py-versioneer+toml", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-torch@2:", type=("build", "run"))

    depends_on("py-ase", type="run")
    depends_on("py-numba", type="run")
    depends_on("py-matplotlib", type="run")
    depends_on("py-tqdm", type="run")
    depends_on("py-graphviz", type="run")
    depends_on("py-h5py", type="run")
    depends_on("py-lightning", type="run")
    depends_on("py-scipy", type="run")
    depends_on("py-opt-einsum", type="run")
