# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchCDlpackExt(PythonPackage):
    """torch c dlpack ext"""

    homepage = "https://pypi.org/project/torch-c-dlpack-ext/"
    pypi = "torch-c-dlpack-ext/torch_c_dlpack_ext-0.1.5.tar.gz"

    license("Apache-2.0")

    version("0.1.5", sha256="d06f0357d575d22a168cc77acb9020fc4bae30968ceb6718a055dcbe92bacabe")

    depends_on("py-torch", type=("build", "link", "run"))

    with default_args(type="build"):
        depends_on("cxx")
        depends_on("py-setuptools@61.0:")
        depends_on("py-apache-tvm-ffi@0.1.1:")
