# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchtoolbox(PythonPackage):
    """This project aims to provide the most frequently used tools to help you
    write more concise and readable PyTorch code."""

    homepage = "https://github.com/PistonY/torch-toolbox"
    pypi = "torchtoolbox/torchtoolbox-0.1.8.2.tar.gz"

    license("BSD-3-Clause", checked_by="alex391")

    version("0.1.8.2", sha256="31f92dd93f3115a8e336d9e3db5945bafa9dbb1323f3d7e47bb7fff968c87203")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-lmdb", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("opencv +python3", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-tensorboard", type=("build", "run"))
    depends_on("py-prettytable", type=("build", "run"))
    depends_on("py-transformers", type=("build", "run"))
