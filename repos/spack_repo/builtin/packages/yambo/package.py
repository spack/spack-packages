# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack.package import *


class Yambo(AutotoolsPackage,CudaPackage):
    """YAMBO is an open-source code released within the GPL licence.

    YAMBO implements Many-Body Perturbation Theory (MBPT) methods
    (such as GW and BSE) and Time-Dependent Density Functional Theory
    (TDDFT), which allows for accurate prediction of fundamental
    properties as band gaps of semiconductors, band alignments, defect
    quasi-particle energies, optics and out-of-equilibrium properties
    of materials.

    The code resorts to previously computed electronic structure,
    usually at the Density Functional Theory (DFT) level and for this
    reason it is interfaced with two of the most used planewave DFT
    codes used in scientific community, Quantum ESPRESSO and Abinit.
    """

    homepage = "http://www.yambo-code.eu"
    url = "https://github.com/yambo-code/yambo/archive/5.3.0.tar.gz"
    git = "https://github.com/yambo-code/yambo.git"

    maintainers = ['nicspalla']

    version('5.3.0', sha256='97b6867c28af6ea690bb02446745e817adcedf95bcd568f132ef3510abbb1cfe')
    version('5.2.4', sha256='7c3f2602389fc29a0d8570c2fe85fe3768d390cfcbb2d371e83e75c6c951d5fc')
    version('5.2.3', sha256='a6168d1fa820af857ac51217bd6ad26dda4cc89c07e035bd7dc230038ae1ab9c')
    version('5.2.2', sha256='2ddd6356830ce9302e304b7627cff3aa973846cf893f91742b4390d0b53d63d4')
    version('5.2.1', sha256='0ac362854313927d75bbf87be98ff58447f3805f79724c38dc79df07f03a7046')
    version('5.2.0', sha256='eb41e83df716eb87261cf130ffe7f930e7dc2e123343d47b73d5a3c69fea7316')
    version('5.1.4', sha256='f2dfa1b4cb6a28bd54efb56a9333f51e6da9bd248d92ca3f6e945cb9ac9fe82c')
    version('5.1.3', sha256='eb12297990030e785a58db6b9c9f0e34809eb2f095082e0aeca89eeaaf14ff37')
    version('5.1.2', sha256='9625d8a96bd9a3ff3713ebe53228d5ac9be0a98adecbe2a2bad67234c0e26a2e')
    version('5.1.1', sha256='c85036ca60507e627c47b6c6aee8241830349e88110e1ce9132ef03ab2c4e9f6')
    version('5.0.4', sha256='1841ded51cc31a4293fa79252d7ce893d998acea7ccc836e321c3edba19eae8a')
    version('5.0.3', sha256='7a5a5f3939bdb6438a3f41a3d26fff0ea6f77339e4daf6a5d850cf2a51da4414')
    version('5.0.2', sha256='a2cc0f880dd915b47efa0d5dd88cb94edffbebaff37a252183efb9e23dbd3fab')
    version('5.0.1', sha256='bbdbd08f7219d575a0f479ff05dac1f1a7b25f7e20f2165abf1b2cf28aedae92')
    version('5.0.0', sha256='b1cbc0b3805538f892b2b8691901c4cc794e75e056a4bd9ad9cf585899cf0aa9')
    version('4.5.3', sha256='04f89b5445d35443325c071784376c7b5c25cc900d1fdcc92971a441f8c05985')
    version('4.5.2', sha256='0b4f8b82c1d37fce472228bdffb6f6f44b86104d170677a5d55e77a2db832cf0')
    version('4.5.1', sha256='6ef202535e38f334a69bd75bd24ff8403b0a4c6b8c60a28b69d4b1c5808aeff5')
    version('4.5.0', sha256='c68b2c79acc31b3d48e7edb46e4049c1108d60feee80bf4fcdc4afe4b12b6928')
    version('4.4.1', sha256='2daf80f394a861301a9bbad559aaf58de283ce60395c9875e9f7d7fa57fcf16d')
    version('4.3.3', sha256='790fa1147044c7f33f0e8d336ccb48089b48d5b894c956779f543e0c7e77de19')

    # Workaround for this https://github.com/yambo-code/yambo-devel/issues/619
    # patch('hdf5.patch', sha256='b9362020b0a29abec535afd7d782b8bb643678fe9215815ca8dc9e4941cb169f', when='@4.3:5.0.99')
    # See https://github.com/yambo-code/yambo-devel/issues/643
    patch('s_psi.patch', sha256='981a0783a9a2c21a89faa358eaf277213837ed712c936152842f8cf7620f52cd', when='@:5.1.99 %gcc@12.0.0:')
    # See https://github.com/yambo-code/yambo/issues/190
    patch('cuda_runtime.patch', sha256='bfd5ade95ef5ca9502c7ad1b375e4517fbf77a32bf97041fd580bb36304fd755', when='@5.3.0+cuda')

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("tar", type="build")
    
    # MPI + OpenMP parallelism
    variant('mpi', default=True, description='Enable MPI support')
    variant('openmp', default=True, description='Enable OpenMP support')

    # Linear Algebra and Parallel I/O
    variant('slepc', default=False, description='Activate support for linear algebra with SLEPc and PETSc')
    with when('+mpi'):
        variant('scalapack', default=False, description='Activate support for parallel linear algebra with SCALAPACK')
        variant('parallel_io', default=True, when='@4.4.0:', description='Activate the HDF5 parallel I/O')

    # Other variants
    variant('dp', default=False, description='Enable double precision')
    variant('time', default=False, description='Activate time profiling of specific sections')
    variant('memory', default=False, description='Activate memory profiling of specific sections')
    variant('ph', default=False, description='Compile Electron-phonon coupling project executables: yambo_ph ypp_ph')
    variant('rt', default=False, description='Compile Real-time dynamics project executables: yambo_rt ypp_rt')
    variant('sc', default=False, description='Compile Self-consistent (COHSEX, HF, DFT) project executables: yambo_sc ypp_sc')
    variant('nl', default=False, description='Compile Non-linear optics project executables: yambo_nl ypp_nl')

    with when('+mpi'):
        depends_on('mpi')

    # Linar Algebra
    depends_on('blas')
    depends_on('lapack')

    with when('+scalapack'):
        depends_on('scalapack')
    conflicts('+scalapack', when='~mpi', msg="Parallel linear algebra available only with +mpi")

    with when('+slepc'):
        depends_on('petsc+complex~superlu-dist~hypre~metis')
        depends_on('petsc+mpi', when='+mpi')
        depends_on('petsc~mpi', when='~mpi')
        depends_on('petsc+double', when='+dp')
        depends_on('petsc~double', when='~dp')
        depends_on('petsc~cuda', when='@:5.2.0')
        depends_on('petsc@:3.20.5', when='@:5.2.99')
        depends_on('petsc@:3.22.2', when='@:5.3.0')
        depends_on('slepc~arpack')
        depends_on('slepc~cuda', when='@:5.2.0')

    # FFTW dependecies
    depends_on('fftw-api@3')
    with when("+mpi"):
        depends_on('fftw +mpi', when='^[virtuals=fftw-api] fftw')
    with when("~mpi"):
        depends_on('fftw ~mpi', when='^[virtuals=fftw-api] fftw')

    # HDF5 and NetCDF dependecies
    with when("+parallel_io"):
        depends_on('hdf5+fortran+hl+mpi')
        depends_on('netcdf-c+mpi')
    with when("~parallel_io"):
        depends_on('hdf5+fortran+hl~mpi')
        depends_on('netcdf-c~mpi')
    depends_on('hdf5@:1.12.3', when='@:5.2.99')
    conflicts('hdf5+mpi', when='@:4.4.0', msg="Parallel I/O available from version 4.4.1")
    depends_on('netcdf-fortran')

    # LIBXC dependecies
    depends_on('libxc@2.0.3:3.0.0~cuda', when='@:5.0.99')
    depends_on('libxc@5.0.0:6.2.2~cuda', when='@5.1.0:')

    # GPU variants and dependecies
    with when('+cuda'):
        variant('cuda_rt', values=str, default='none', when='%nvhpc',
            description='Specify the CUDA runtime version (e.g. "11.8") only if you want the secondary version installed with the NVHPC SDK.')
    conflicts('cuda_rt=none', when='@:5.2.99 +cuda', msg='CUDA runtime version is required')
    variant('cuda-fortran', default=False, description='Build with CUDA-Fortran')
    with when('+cuda-fortran'):
        conflicts('~cuda',
                  msg="CUDA required when +cuda-fortran")
        conflicts('cuda_arch=none',
                  msg="CUDA architecture is required when +cuda")
        conflicts('@:4.5.3',
                  msg="CUDA-Fortran available only from version 5.0.0")
        conflicts('%gcc',
                  msg="CUDA-Fortran available only with NV or PGI compilers")
        conflicts('%intel',
                  msg="CUDA-Fortran available only with NV or PGI compilers")
        conflicts('%oneapi',
                  msg="CUDA-Fortran available only with NV or PGI compilers")

    # DeviceXlib
    with when('@5.3.0:'):
        depends_on('devicexlib@0.8.6: ~cuda-fortran~openacc~openmp5', when='~cuda-fortran')
        depends_on('devicexlib@0.8.6: +cuda-fortran+cuda', when='+cuda-fortran+cuda')
    
    with when("+openmp"):
        depends_on("openblas threads=openmp", when="^[virtuals=lapack] openblas")
        depends_on("intel-oneapi-mkl threads=openmp", when="^[virtuals=lapack] intel-oneapi-mkl")
        depends_on("fftw +openmp", when="^[virtuals=fftw-api] fftw")
        depends_on("petsc +openmp", when="^[virtuals=petsc] petsc")

    # IOTK external resource
    resource(
        name='iotk',
        url='https://github.com/yambo-code/yambo-libraries/raw/master/external/iotk-y1.2.2.tar.gz',
        sha256='64af6a4b98f3b62fcec603e4e1b00ef994f95a0efa53ab6593ebcfe6de1739ef',
        placement={'iotk-y1.2.2.tar.gz': 'lib/archive/iotk-y1.2.2.tar.gz'},
        expand=False
    )

    # Yambo Driver external resource
    resource(
        name='Ydriver',
        url='https://github.com/yambo-code/yambo-libraries/raw/master/external/Ydriver-0.0.2.tar.gz',
        sha256='63984c3eb2d28320b320f1d9b3a2c1efcd3c9505a10d887c8bbd54513442202c',
        placement={'Ydriver-0.0.2.tar.gz': 'lib/archive/Ydriver-0.0.2.tar.gz'},
        when='@5.0.0:5.0.99',
        expand=False
    )
    resource(
        name='Ydriver',
        url='https://github.com/yambo-code/yambo-libraries/raw/master/external/Ydriver-1.1.0.tar.gz',
        sha256='6c316d613f5a41ddd15efad7ba97e4712f87d7e56c073ba5458caf424afcb97a',
        placement={'Ydriver-1.1.0.tar.gz': 'lib/archive/Ydriver-1.1.0.tar.gz'},
        when='@5.1.0:5.1.99',
        expand=False
    )
    resource(
        name='Ydriver',
        url='https://github.com/yambo-code/Ydriver/archive/refs/tags/1.2.0.tar.gz',
        sha256='0f29a44e9c4b49d3f6be3f159a7ef415932b2ae2f2fdba163af60a0673befe6e',
        placement={'1.2.0.tar.gz': 'lib/archive/Ydriver-1.2.0.tar.gz'},
        when='@5.2.0:5.2.3',
        expand=False
    )
    resource(
        name='Ydriver',
        url='https://github.com/yambo-code/Ydriver/archive/refs/tags/1.4.2.tar.gz',
        sha256='c242f0700a224325ff59326767614a561b02ce16ddb2ce6c13ddd2d5901cc3e4',
        placement={'1.4.2.tar.gz': 'lib/archive/Ydriver-1.4.2.tar.gz'},
        when='@5.2.4',
        expand=False
    )

    sanity_check_is_file = ["bin/yambo", "bin/ypp", "bin/a2y", "bin/c2y", "bin/p2y"]

    @property
    def build_targets(self):
        spec = self.spec
        if '+ph' in spec and '+rt' in spec and '+sc' in spec and '+nl' in spec:
            return ['all']
        bt = ['core']
        if '+ph' in spec:
            bt.append('ph-project')
        if '+rt' in spec:
            bt.append('rt-project')
        if '+sc' in spec:
            bt.append('sc-project')
        if '+nl' in spec:
            bt.append('nl-project')
        return bt

    @run_before('configure')
    def filter_configure(self):
        spec = self.spec
        # The configure in the package has the string 'cat config/report'
        # hard-coded, which causes a failure at configure time due to the
        # current working directory in Spack. Fix this by using the absolute
        # path to the file.
        report_abspath = join_path(self.build_directory, 'config', 'report')
        filter_file('cat config/report', 'cat '+report_abspath, 'configure')
        # fix petsc bad recognition
        filter_file('#include <petsc/finclude/petscvec.h90>', '#include <petsc/finclude/petscvec.h>', 'configure')
        # fix hdf5 bad linking and include flags
        filter_file('.+try_HDF5_LIBS=..h5pfc -show .+', '#', 'configure')
        filter_file('.+try_hdf5_incdir=..h5pfc -show .+', '#', 'configure')
        filter_file('.+try_HDF5_LIBS=..h5fc -show .+', '#', 'configure')
        filter_file('.+try_hdf5_incdir=..h5fc -show .+', '#', 'configure')

    @run_before('configure')
    def filter_linking_issue(self):
        # fix linking issues with intel-oneapi-compilers
        spec = self.spec
        if '@5.1.2:' in spec and '%intel-oneapi-compilers' in spec:
            filter_file('libs="-lint_modules $libs $llocal $lPLA $lIO $lextlibs -lm"', 
                        r'libs="-lint_modules $libs $llocal $lSL $lPLA $lIO $lextlibs -lm"', 
                        'sbin/compilation/libraries.sh',
                        string=True)
            filter_file('$libs $llocal', 
                        r'-Wl,--start-group $libs $llocal', 
                        'sbin/compilation/libraries.sh',
                        string=True)
            filter_file('$lextlibs', 
                        r'$lextlibs -Wl,--end-group', 
                        'sbin/compilation/libraries.sh',
                        string=True)
            filter_file('libs=" "', 'libs=" -l_Y_tddft "', 'sbin/compilation/libraries.sh', string=True)

    @run_before('configure')
    def filter_oneapi(self):
        spec = self.spec
        # fix oneapi ifx issues
        if ('%oneapi' in spec or '%intel-oneapi-compilers' in spec) and '@5.0.0:5.2.99' in spec:
            filter_file('*ifort*', '*ifx*', 'configure', string=True)
            filter_file('2021', '2023', 'configure')
            filter_file('FC="$(fc)"', 'FC=mpiifort', 'lib/iotk/Makefile.loc', string=True)
            filter_file('#include <stdlib.h>',
                        '#if defined _ypp || defined _a2y || defined _p2y || defined _c2y || defined _e2y || defined _eph2y\n #include <yambo_driver.h>\n#endif',
                        'lib/yambo/Ydriver/src/main/options_maker.c',
                        string=True)

    @run_before('configure')
    def filter_time(self):
        spec = self.spec
        # To always have the times written in seconds in the report, useful for benchmarking
        if '+time' in spec and '@5.0.0:' in spec:
            filter_file('total_time(i_c)<600.', 'total_time(i_c)<604800.', 'src/timing/TIMING_clock_write.F', string=True)
            filter_file("ch='            [Time-Profile]: '//trim(time_string(total_time))",
                        "write (ch,'(a,f11.4,a)') '            [Time-Profile]: ',total_time,'s'",
                        'src/modules/mod_timing.F', string=True)
    
    def enable_or_disable_time(self, activated):
        return '--enable-time-profile' if activated else '--disable-time-profile'

    def enable_or_disable_memory(self, activated):
        return '--enable-memory-profile' if activated else '--disable-memory-profile'

    def enable_or_disable_openmp(self, activated):
        return '--enable-open-mp' if activated else '--disable-open-mp'

    def enable_or_disable_parallel_io(self, activated):
        return '--enable-hdf5-par-io' if activated else '--disable-hdf5-par-io'

    def setup_build_environment(self, env):
        spec = self.spec
        if spec['mpi'].name == 'openmpi':
            env.set('MPICC', 'mpicc')
            env.set('MPICXX', 'mpicxx')
            env.set('MPIF77', 'mpif77')
            env.set('MPIFC', 'mpif90')
        if spec['mpi'].name == 'fujitsu-mpi':
            env.set('MPICC', 'mpicc')
            env.set('MPICXX', 'mpicxx')
            env.set('MPIF77', 'mpifort')
            env.set('MPIFC', 'mpifort')
        if '%nvhpc' in spec:
            env.set('FC', "nvfortran")
            env.set('CPP', "cpp -E -P")
            env.set('FPP', "nvfortran -Mpreprocess -E")
            env.set('F90SUFFIX', ".f90")
            env.unset('CUDA_HOME')
        if '%intel' in spec:
            env.set('FPP', "ifort -E -free -P")
            env.set('FC', "ifort")
            env.set('F77', "ifort")
            env.set('CC', "icc")
            env.set('CPP', "icc -E -ansi")
            if 'intel' in spec['mpi'].name:
                env.set('MPICC', 'mpiicc')
                env.set('MPICXX', 'mpiicpc')
                env.set('MPIF77', 'mpiifort')
                env.set('MPIFC', 'mpiifort')
        if '%oneapi' in spec:
            env.set('FC', "ifx")
            env.set('F77', "ifx")
            env.set('CC', "icx")
            env.set('FPP', "ifx -E -free -P")
            env.set('CPP', "icx -E -ansi")
            if 'intel' in spec['mpi'].name:
                if '^intel-oneapi-mpi@2021.10.0' in spec:
                    env.set('MPICC', 'mpiicc -cc=icx')
                    env.set('MPIF77', 'mpiifort -fc=ifx')
                    env.set('MPIFC', 'mpiifort -fc=ifx')
                else:
                    env.set('MPICC', 'mpiicx')
                    env.set('MPIF77', 'mpiifx')
                    env.set('MPIFC', 'mpiifx')

    def configure_args(self):
        spec = self.spec

        args = [
            '--enable-msgs-comps',
            '--disable-keep-objects',
            '--with-editor=none',
            '--enable-keep-src'
        ]

        # There are hard-coded paths that make the build process fail if the
        # target prefix is not the configure directory
        args.append('--prefix={0}'.format(self.stage.source_path))
        if '@:4.5.3' in spec:
            if '%gcc@9.0.0:' in spec:
                args.append('FCFLAGS=-fallow-argument-mismatch')

        # Double precision
        args.extend(self.enable_or_disable('dp'))

        # Application profiling
        args.extend(self.enable_or_disable('time'))
        args.extend(self.enable_or_disable('memory'))

        # MPI + threading
        args.extend(self.enable_or_disable('mpi'))
        args.extend(self.enable_or_disable('openmp'))

        # MKL
        mkl_lines = {
            'intel': '-lmkl_intel_lp64 -lmkl_sequential -lmkl_core',
            'intel_thr': '-lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -liomp5',
            'oneapi': '-lmkl_intel_lp64 -lmkl_sequential -lmkl_core',
            'oneapi_thr': '-lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -liomp5',
            'gcc': '-Wl,--no-as-needed -lmkl_gf_lp64 -lmkl_sequential -lmkl_core',
            'gcc_thr': '-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -lgomp',
            'nvhpc': '-lmkl_intel_lp64 -lmkl_sequential -lmkl_core',
            'nvhpc_thr': '-lmkl_intel_lp64 -lmkl_pgi_thread -lmkl_core -pgf90libs -mp',
        }
        mkl_line=''
        if 'mkl' in spec or 'intel-oneapi-mkl' in spec:
            mkl_line = "-L{0}/lib/intel64 ".format(env['MKLROOT'])
            if '%intel-oneapi-compilers' in spec or '%oneapi' in spec:
                comp = "oneapi"
            elif '%intel' in spec:
                comp = "intel"
            elif '%gcc' in spec:
                comp = "gnu"
            elif '%nvhpc' in spec:
                comp = "nvhpc"
            if "+openmp" in spec:
                comp += "_thr"
            mkl_line += mkl_lines[comp]
            mkl_line += ' -lpthread -lm -ldl'

            # BLAS/LAPACK
            args.append('--with-blas-libs={0}'.format(mkl_line))
            args.append('--with-lapack-libs={0}'.format(mkl_line))
            # FFT
            args.extend([
                '--with-fft-libs={0}'.format(mkl_line),
                '--with-fft-includedir={0}/include/fftw'.format(env['MKLROOT'])
                ])
        else:
            # BLAS/LAPACK
            args.extend([
                '--with-blas-libs={0}'.format(spec['blas'].libs),
                '--with-lapack-libs={0}'.format(spec['lapack'].libs),
            ])
            # FFT
            args.append('--with-fft-path={0}'.format(spec['fftw-api'].prefix))

        # ScaLAPACK
        if '+scalapack' in spec:
            args.append('--enable-par-linalg')
            if ('mkl' in spec or 'intel-oneapi-mkl' in spec) and 'netlib-scalapack' not in spec:
                args.extend([
                    '--with-blacs-libs=-L{0}/lib/intel64 '
                    '-lmkl_blacs_intelmpi_lp64'.format(env['MKLROOT']),
                    '--with-scalapack-libs=-L{0}/lib/intel64 '
                    '-lmkl_scalapack_lp64'.format(env['MKLROOT']),
                ])
            else:
                args.extend([
                    '--with-blacs-libs={0}'.format(spec['scalapack'].libs),
                    '--with-scalapack-libs={0}'.format(spec['scalapack'].libs),
                ])

        # PETSc + SLEPc
        if '+slepc' in spec:
            args.extend([
                '--enable-slepc-linalg',
                '--with-petsc-path={0}'.format(spec['petsc'].prefix),
                '--with-slepc-path={0}'.format(spec['slepc'].prefix),
            ])

        # I/O
        args.extend([
            '--with-netcdf-path={0}'.format(spec['netcdf-c'].prefix),
            '--with-netcdff-path={0}'.format(spec['netcdf-fortran'].prefix),
            '--with-hdf5-path={0}'.format(spec['hdf5'].prefix)
        ])

        # Parallel I/O
        if '@4.4.0:' in spec:
            args.extend(self.enable_or_disable('parallel_io'))

        # Other dependencies
        args.append('--with-libxc-path={0}'.format(spec['libxc'].prefix))
        if '@5.3.0:' in spec:
            args.append('--with-devxlib-path={0}'.format(spec['devicexlib'].home))

        # GPU
        if '+cuda-fortran' in spec: args.append('--enable-cuda-fortran')
        if '+cuda' in spec:
            if '@5.3.0:' in spec:
                args.append('--with-cuda-cc={0}'.format(*spec.variants['cuda_arch'].value))
                if spec.variants['cuda_rt'].value != 'none':
                    args.append('--with-cuda-runtime={0}'.format(spec.variants['cuda_rt'].value))
                # args.append('--with-cuda-path={0}'.format(spec['cuda'].prefix))
            else:
                enable_cuda = '--enable-cuda=cuda{0}.{1}'.format(*spec['cuda'].version)
                enable_cuda += ',cc{0}'.format(*spec.variants['cuda_arch'].value)
                args.append(enable_cuda)
            if '%nvhpc' not in spec:
                args.append('--with-cuda-path={0}'.format(spec['cuda'].home))

        return args

    def install(self, spec, prefix):
        # 'install' target is not present
        install_tree('bin', prefix.bin)

    def build(self, spec, prefix):
        print(f"Using compiler: {spec.compiler.name} {spec.compiler.version}")
        if spec.satisfies('%nvhpc') and spec.compiler.version >= Version('24.11') :
            # Modify the config/setup file that was created by configure
            config_file = join_path(self.stage.source_path, 'config', 'setup')
            # Handle the -Mcuda=A,X pattern
            filter_file( r'-Mcuda=([^,\s]+),([^,\s]+)', r'-cuda -gpu=\1,\2', config_file )
            # Handle the -Mcudalib pattern
            filter_file( r'-Mcudalib=([^,\s][^,\s]*(?:,[^,\s]+)*)', r'-cudalib=\1', config_file )
        # Then proceed with the actual build
        super(Yambo, self).build(spec, prefix)
