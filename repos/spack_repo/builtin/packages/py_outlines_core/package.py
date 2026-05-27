# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOutlinesCore(PythonPackage):
    """Faster structured generation."""

    homepage = "https://docs.rs/outlines-core/latest/outlines_core/"
    pypi = "outlines_core/outlines_core-0.2.11.tar.gz"

    version("0.2.11", sha256="dfce56f717ff5083e54cbcfdb66cad243365437fccbb5509adaa7e31e030f1d8")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-maturin@1", type="build")
    depends_on("rust@1.85:", type="build")
