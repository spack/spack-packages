# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScverseMisc(PythonPackage):
    """Miscellaneous utility code used by scverse packages"""

    homepage = "https://github.com/scverse/scverse-misc"
    pypi = "scverse_misc/scverse_misc-0.1.6.tar.gz"

    license("BSD-3-Clause")

    version("0.1.8", sha256="1a96d1ea0e6f4baf0d1d4cc1688727613bac5227f91268d19c0e0aa1202792ec")
    version("0.1.6", sha256="2310c2a0d2159311f1b44759cbd2f83b543362556396d93cb70cff01647ec835")

    variant("settings", default=False, description="Adds pydantic-settings support")

    depends_on("python@3.12:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-hatch-vcs")

    with default_args(type=("build", "run")):
        depends_on("py-session-info2")
        depends_on("py-typing-extensions", when="^python@:3.12")

        depends_on("py-pydantic-settings", when="+settings")
        depends_on("py-python-dotenv", when="+settings")
