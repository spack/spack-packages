# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHfXet(PythonPackage):
    """Fast transfer of large files with the Hugging Face Hub."""

    homepage = "https://github.com/huggingface/xet-core"
    pypi = "hf-xet/hf_xet-1.1.5.tar.gz"

    license("Apache-2.0")

    version("1.4.3", sha256="8ddedb73c8c08928c793df2f3401ec26f95be7f7e516a7bee2fbb546f6676113")
    version("1.1.5", sha256="69ebbcfd9ec44fdc2af73441619eeb06b94ee34511bbcf57cd423820090f5694")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")

        # https://github.com/huggingface/xet-core/blob/v1.1.5/hf_xet/pyproject.toml
        depends_on("py-maturin@1.7:1")
        depends_on("rust")

    conflicts("py-maturin@1.13:", when="@:1.1")
