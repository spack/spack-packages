# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPercevalInterop(PythonPackage):
    """Interoperability packages between Perceval and other quantum computing frameworks."""

    homepage = "https://github.com/Quandela/Perceval_Interop"
    pypi = "perceval_interop/perceval_interop-1.2.5.tar.gz"

    supplier = "Organization: quandela"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("1.2.5", sha256="c2a836f49ef03dfb38e66187995b17d208cacbe5171f0e712642629984d57185")

    depends_on("python@:3.14", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-scmver")

    with default_args(type=("build", "run")):
        depends_on("py-perceval-quandela")
