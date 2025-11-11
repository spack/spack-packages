# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNh3(PythonPackage):
    """Python binding to Ammonia HTML sanitizer Rust crate."""

    homepage = "https://github.com/messense/nh3"
    pypi = "nh3/nh3-0.3.0.tar.gz"

    license("MIT")

    version("0.3.0", sha256="d8ba24cb31525492ea71b6aac11a4adac91d828aadeff7c4586541bf5dc34d2f")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-maturin@1", type="build")
