# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLlguidance(PythonPackage):
    """Bindings for the Low-level Guidance (llguidance) Rust library for use within Guidance"""

    pypi = "llguidance/llguidance-0.7.30.tar.gz"

    license("MIT")

    version("0.7.30", sha256="e93bf75f2b6e48afb86a5cee23038746975e1654672bf5ba0ae75f7d4d4a2248")

    depends_on("py-maturin@1.0.0:", type="build")
    conflicts("py-maturin ^ rust@1.85.0:")
