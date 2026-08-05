# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvtx(PythonPackage):
    """PyNVTX - Python code annotation library."""

    homepage = "https://github.com/NVIDIA/nvtx"
    pypi = "nvtx/nvtx-0.2.10.tar.gz"

    license("Apache-2.0")
    maintainers("LydDeb")

    version("0.2.15", sha256="2287d3be05b85661deb386f878d1f536c2e532774aa9ec7a50c434942ed81ae5")
    version("0.2.10", sha256="58b89cd69079fda1ceef8441eec5c5c189d6a1ff94c090a3afe03aedd0bbd140")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")
    depends_on("nvtx", when="@0.2.10")

    # Starting with version 0.2.11, the include directory is packaged in the sources.
    @when("@0.2.10")
    def setup_build_environment(self, env):
        env.set("NVTX_PREFIX", self.spec["nvtx"].prefix.include)
