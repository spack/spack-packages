# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLlguidance(PythonPackage):
    """Bindings for the Low-level Guidance (llguidance) Rust library for use within Guidance."""

    homepage = "https://github.com/guidance-ai/llguidance"
    pypi = "llguidance/llguidance-1.6.1.tar.gz"

    version("1.6.1", sha256="01611f85f834725fb359b568673cfaa5a352423779c097b03aa5ce68f0db3a51")
    version("1.3.0", sha256="861249afd51dc325646834462ea827e57a5c2b2042e108e6aae7059fdad9104d")
    
    depends_on("python@3.10:", type=("build", "run"), when="@1.4.0:")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-maturin@1", type="build")
    depends_on("rust@1.87:", type="build")
