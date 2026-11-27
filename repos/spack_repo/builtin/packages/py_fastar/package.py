# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFastar(PythonPackage):
    """High-level bindings for the Rust tar crate."""

    homepage = "https://github.com/DoctorJohn/fastar"
    pypi = "fastar/fastar-0.12.0.tar.gz"

    license("MIT")

    version("0.12.0", sha256="bba71522eae6a7627a5514ffdd4ac9645ef27d82e23931d79fd974bb49c3f2ad")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-maturin@1.14.1:1", type="build")
    depends_on("rust", type="build")
