# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatomicTorch(PythonPackage):
    """Torchscript bindings for metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    url = "https://github.com/metatensor/metatomic/releases/download/metatomic-torch-v0.1.2/metatomic_torch-0.1.2.tar.gz"
    git = "https://github.com/metatensor/metatomic.git"
    pypi = "metatomic-torch/metatomic-torch-0.1.2.tar.gz"

    import_modules = ["metatomic.torch"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.3", sha256="60a4b651cf6e15f175879af74d18215d45cc4fd5e42a61242a180e2014fe9fd2")
    version("0.1.2", sha256="0d793b16b3d6eee915c89e9b1a385143ec2dbb6dc451bed8feee3a2445b3f63e")
    version("0.1.1", sha256="5b2ea0da270399a315d15551ae09fe80750fc1ef10fcca07fac73bd97bbab9aa")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-vesin", type=("run", "build"))
    depends_on("py-torch@2.1:", type=("build", "run"))
    depends_on("py-metatensor-torch@0.7", type=("build", "run"))
    # >=0.3.0 and <0.4.0
    depends_on("py-metatensor-operations@0.3", type=("build", "run"))
    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    # CMakeLists.txt
    depends_on("cmake@3.16:", type="build")
