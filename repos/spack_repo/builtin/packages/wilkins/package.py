# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Wilkins(CMakePackage):
    """A workflow system for triple convergence of HPC, Big Data, and AI applications."""

    homepage = "https://github.com/orcunyildiz/wilkins"
    url      = "https://github.com/orcunyildiz/wilkins.git"
    git      = "https://github.com/orcunyildiz/wilkins.git"

    maintainers("orcunyildiz")

    license("BSD-3-Clause")

    version('master', branch='master')

    # https://github.com/spack/spack/releases/tag/v1.0.0#languages-are-virtual-dependencies
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    
    depends_on('mpi')
    depends_on('lowfive')
    depends_on('hdf5+mpi+hl@1.14', type='link')
    depends_on('henson@master+python+mpi-wrappers')

    extends("python")
    depends_on("py-mpi4py", type=("build", "run"))

    def cmake_args(self):
        args = [
          self.define("CMAKE_C_COMPILER", self.spec['mpi'].mpicc),
          self.define("CMAKE_CXX_COMPILER", self.spec['mpi'].mpicxx),
          self.define("PYTHON_EXECUTABLE", self.spec["python"].command.path)
        ]

        return args
