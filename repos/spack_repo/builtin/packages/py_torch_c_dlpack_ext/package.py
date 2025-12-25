# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchCDlpackExt(PythonPackage):
    """torch c dlpack ext"""

    homepage = "https://pypi.org/project/torch-c-dlpack-ext/"
    pypi = "torch-c-dlpack-ext/torch_c_dlpack_ext-0.1.4.tar.gz"

    license("Apache-2.0")

    version("0.1.4", sha256="ad292d17e285ab9523940e51e87d21ffce4982ce8beb46fb18b5c2b4760a1a10")

    depends_on("py-torch")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("cmake")
        depends_on("ninja")
        depends_on("py-setuptools@61.0:")
        depends_on("py-apache-tvm-ffi@0.1.1:")
        depends_on("py-pybind11")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("CPLUS_INCLUDE_PATH", self.spec["py-pybind11"].prefix.include)
