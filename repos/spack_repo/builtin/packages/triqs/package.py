# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os
from spack.package import *


class Triqs(CMakePackage, PythonExtension):
    """A Toolbox for Research on Interacting Quantum Systems. Supported by the Flatiron Institute."""

    homepage = "https://github.com/TRIQS/triqs"
    url = "https://github.com/TRIQS/triqs/releases/download/3.3.1/triqs-3.3.1.tar.gz"

    license("GPL-3.0", checked_by="V-Karch")

    version("3.3.1", sha256="740efb57c9af39f4086115f8167a55833e84558261e0564c7179d8c17f911539")

    extends("python")

    depends_on("cmake@3.20:", type="build")

    depends_on("mpi", type=("build", "run"))
    depends_on("blas", type=("build", "run"))
    depends_on("lapack", type=("build", "run"))
    depends_on("fftw", type=("build", "run"))
    depends_on("boost@1.7:", type=("build", "run"))

    depends_on("py-numpy@:1", type=("build", "run"))
    depends_on("py-mako", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    def cmake_args(self):
        return [
            self.define("PythonSupport", True),
            self.define("Build_Documentation", False),
            self.define("Build_Tests", self.run_tests),
            self.define("Build_Benchs", False),
            "-Wno-dev"
        ]

    def setup_run_environment(self, env):
        share_dir = self.prefix.share.triqs
        bin_dir = self.prefix.bin
        lib_dir = self.prefix.lib
        python_dir = self.prefix.lib 

        env.prepend_path("PATH", bin_dir)
        env.prepend_path("LD_LIBRARY_PATH", lib_dir)
        env.prepend_path("PYTHONPATH", python_dir)
        env.set("TRIQS_ROOT", self.prefix)
        env.set("TRIQS_SHARE_PATH", share_dir)

    def install(self, spec, prefix):
        super().install(spec, prefix)
        if "+python" in spec:
            python = spec["python"].command
            python("-m", "compileall", prefix)

