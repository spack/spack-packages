# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTomliW(PythonPackage):
    """A lil' TOML writer."""

    homepage = "https://github.com/hukkin/tomli-w"
    pypi = "tomli_w/tomli_w-1.0.0.tar.gz"

    license("MIT")

    version(
        "1.2.0", sha256="2dd14fac5a47c27be9cd4c976af5a12d87fb1f0b4512f81d69cce3b35ae25021"
    )  # FIXME
    version(
        "1.1.0", sha256="49e847a3a304d516a169a601184932ef0f6b61623fe680f836a2aa7128ed0d33"
    )  # FIXME
    version("1.0.0", sha256="f463434305e0336248cac9c2dc8076b707d8a12d019dd349f5c1e382dd1ae1b9")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-flit-core@3.2.0:3", type="build")
