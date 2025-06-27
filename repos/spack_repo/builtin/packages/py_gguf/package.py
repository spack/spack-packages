# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGguf(PythonPackage):
    """This is a Python package for writing binary files in the GGUF (GGML Universal File) format."""

    pypi = "gguf/gguf-0.17.1.tar.gz"

    license("MIT")

    version(
        "0.17.1",
        sha256="36ad71aad900a3e75fc94ebe96ea6029f03a4e44be7627ef7ad3d03e8c7bcb53",
    )

    depends_on("py-poetry-core", type="build")
    depends_on("py-numpy@1.17:", type=["build", "run"])
    depends_on("py-tqdm@4.27:", type=["build", "run"])
    depends_on("py-pyyaml@5.1:", type=["build", "run"])
