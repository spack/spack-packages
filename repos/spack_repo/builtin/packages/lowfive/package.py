# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Lowfive(CMakePackage):
    """HDF5 VOL Plugin for In Situ Data Transport."""

    homepage = "https://github.com/diatomic/LowFive.git"
    url      = "https://github.com/diatomic/LowFive.git"
    git      = "https://github.com/diatomic/LowFive.git"

    version('master', branch='master')

    variant("examples", default=False, description="Install the examples")
    variant("auto_load", default=True, description="Set LowFive environment variables")
    variant("python", default=True, description="Install Python bindings")
    variant("caliper", default=False, description="Enable profiling with Caliper")

    # https://github.com/spack/spack/releases/tag/v1.0.0#languages-are-virtual-dependencies
    depends_on("c", type="build")  
    depends_on("cxx", type="build")  
    depends_on("fortran", type="build")  

    depends_on('mpi')
    depends_on('hdf5+mpi+hl@1.14', type='link')

    extends("python", when="+python")       # brings pylowfive into PYTHONPATH
    depends_on("py-mpi4py", when="+python", type=("build", "run"))

    depends_on('caliper~adiak', when="+caliper")

    def cmake_args(self):
        args = ['-DCMAKE_C_COMPILER=%s' % self.spec['mpi'].mpicc,
                '-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx,
                '-DBUILD_SHARED_LIBS=false',
                self.define_from_variant('lowfive_install_examples', 'examples'),
                self.define_from_variant('lowfive_python', 'python'),
                self.define_from_variant('lowfive_caliper', 'caliper'),
        ]

        if self.spec.satisfies("+python"):
            args += [self.define("PYTHON_EXECUTABLE", self.spec["python"].command.path)]

        return args


    def setup_run_environment(self, env):
        if "+auto_load" in self.spec:
            env.set('HDF5_VOL_CONNECTOR', "lowfive under_vol=0;under_info={};")
            env.set('HDF5_PLUGIN_PATH', self.prefix.lib)
