# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTensorforge(PythonPackage):
    """A code generator for small (batched) tensor contraction kernels on GPUs"""

    homepage = "https://github.com/SeisSol/TensorForge/blob/master/README.md"
    git = "https://github.com/SeisSol/TensorForge.git"

    maintainers("davschneller", "Thomas-Ulrich")
    license("MIT")

    version("master", branch="master")
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PATH", self.spec.prefix)
        env.prepend_path("PYTHONPATH", self.spec.prefix)
