# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDotmatch(PythonPackage):
    """Known-target short-DNA assignment from FASTQ."""

    homepage = "https://github.com/dnncha/dotmatch"
    pypi = "dotmatch/dotmatch-0.2.2.tar.gz"

    license("Apache-2.0")

    version("0.2.2", sha256="c441aaafb6b29db51560d3fc68c52a8ad01ed0f08158a89544c1d9366f12fce8")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-tomli", when="^python@:3.10", type="run")
