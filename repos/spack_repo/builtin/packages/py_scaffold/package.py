# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class PyScaffold(PythonPackage, CudaPackage, ROCmPackage):
    """Scale-Free Fractal benchmark"""

    git = "https://github.com/LBANN/ScaFFold.git"

    version("main", branch="main")

    maintainers("michaelmckinsey1")
    license("Apache-2.0")

    variant("mpi", default=True, description="MPI support")
    variant("caliper", default=False, description="Build with Caliper support enabled.")

    depends_on("python@3.11", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("mpi")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("caliper+python", when="+caliper", type=("build", "run"))
    depends_on("adiak+python", when="+caliper", type=("build", "run"))

    def setup_run_environment(self, env):
        super().setup_run_environment(env)

        if self.spec.satisfies("+caliper"):
            if self.spec.satisfies("+rocm"):
                # Need to set this to libcaliper.so to avoid rocprofiler context error
                env.set(
                    "ROCP_TOOL_LIBRARIES",
                    os.path.join(self.spec["caliper"].prefix, "lib64", "libcaliper.so"),
                )
