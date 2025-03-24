# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class HemepureGpu(CMakePackage):
    """HemeLB is a high performance lattice-Boltzmann solver optimized for
    simulating blood flow through sparse geometries, such as those found in the
    human vasculature. It is routinely deployed on powerful supercomputers,
    scaling to hundreds of thousands of cores even for complex geometries.
    HemeLB has traditionally been used to model cerebral bloodflow and vascular
    remodelling in retinas, but is now being applied to simulating the fully
    coupled human arterial and venous trees.

    HemePure is a optimized verion of HemeLB with improved memory, compilation
    and scaling"""

    homepage = "https://github.com/izacharo/HemePure_GPU_BSD"
    url      = "https://github.com/izacharo/HemePure_GPU_BSD"
    git      = "https://github.com/izacharo/HemePure_GPU_BSD.git"

    maintainers("nicolin", "connoraird")
    license("BSD-3-Clause", checked_by="connoraird")

    version('main', branch='main')

    depends_on('cmake@3.18:')
    depends_on('openmpi@4.1:')
    depends_on('boost@1.86:+mpi')
    depends_on('tinyxml')
    depends_on('libtirpc')
    depends_on('parmetis')
    depends_on('ctemplate')
    depends_on('cuda@12.0:')

    # Post Processing 
    variant('gmyplus', default=False, description='Use GMY+ format')
    variant('parmetis', default=False, description='Use ParMETIS')

    # Solver Compute  
    variant('simd', default='auto', description='Use SIMD instrinsics', values=('sse3', 'avx2', 'avx512', 'auto', 'off'))
    variant('mpi_call', default=False, description='Use standard MPI functions when reading blocks')
    variant('mpi_win',  default=False, description='Use MPI Domain Split to help load large domains')
    variant('big_mpi',  default=False, description='Use Domain Split to help load large domains')
    variant('cuda_arch', default='89', description='CUDA architecture')

    # Solver BC Vel or Pressure
    variant('pressure_bc', default=False, description='Use Pressure Boundary Conditions')
    variant('wall_boundary', default='SIMPLEBOUNCEBACK', description='Boundary conditions at walls', values=('SIMPLEBOUNCEBACK'))
    variant('inlet_boundary', default='LADDIOLET', description='Boundary conditions at inlets', values=('NASHZEROTHORDERPRESSUREIOLET', 'LADDIOLET'))
    variant('wall_inlet_boundary', default='LADDIOLETSBB', description='Boundary conditions at wall-inlet corners', values=('NASHZEROTHORDERPRESSURESBB','LADDIOLETSBB'))
    variant('outlet_boundary', default='NASHZEROTHORDERPRESSUREIOLET', description='Boundary conditions at outlets', values=('NASHZEROTHORDERPRESSUREIOLET', 'LADDIOLET'))
    variant('wall_outlet_boundary', default='NASHZEROTHORDERPRESSURESBB', description='Boundary conditions at wall-outlet corners', values=('NASHZEROTHORDERPRESSURESBB'))

    # Lagranian Tracking
    variant('tracer', default=True, description='Use particles as tracers')
    variant('velocity_weight', default=False, description='Use velocity weights file')


    root_cmakelists_dir = 'src'
    def setup_build_environment(self, env):
        env.prepend_path('CPATH', self.spec['libtirpc'].prefix.include.tirpc)
        env.append_flags('LDFLAGS', '-ltirpc')

    def cmake_args(self):
        args = []

        args.append("-DCMAKE_C_COMPILER=%s" % self.spec['mpi'].mpicc)
        args.append("-DCMAKE_CXX_COMPILER=%s" % self.spec['mpi'].mpicxx)
        args.append("-DCMAKE_CXX_EXTENSIONS=OFF")
        args.append("-DCMAKE_BUILD_TYPE=Release")
        args.append("-DHEMELB_COMPUTE_ARCHITECTURE=NEUTRAL")

        args.append("-DHEMELB_GPU_BACKEND=CUDA")
        args.append("-DHEMELB_CUDA_AWARE_MPI=ON")
        args.append("-DCMAKE_CUDA_ARCHITECTURES=%s" % self.spec.variants['cuda_arch'].value)

        args.append("-DHEMELB_USE_MPI_PARALLEL_IO=ON")
        args.append("-DHEMELB_USE_VELOCITY_WEIGHTS_FILE=ON")

        if '+pressure_bc' in self.spec:
            args.append("-DHEMELB_INLET_BOUNDARY=NASHZEROTHORDERPRESSUREIOLET")
            args.append("-DHEMELB_WALL_INLET_BOUNDARY=NASHZEROTHORDERPRESSURESBB")
        else:
             args.append("-DHEMELB_INLET_BOUNDARY=LADDIOLET")
             args.append("-DHEMELB_WALL_INLET_BOUNDARY=LADDIOLETSBB")


        args.append("-DHEMELB_OUTLET_BOUNDARY=NASHZEROTHORDERPRESSUREIOLET")
        args.append("-DHEMELB_WALL_OUTLET_BOUNDARY=NASHZEROTHORDERPRESSURESBB")
        args.append("-DHEMELB_WALL_BOUNDARY=SIMPLEBOUNCEBACK")

        args.append("-DHEMELB_LOG_LEVEL=Info")
        return args

    def build(self, pkg, prefix):
        mkdirp('buildHemeGPU')
        cmake('src', *self.cmake_args())
        make()


