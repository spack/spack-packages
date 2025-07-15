# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage


class Sedacs(PythonPackage, CudaPackage):
    """Scalable Ecosystem, Driver, and Analyzer for Complex Chemistry Simulations (SEDACS) enables massively parallel atomistic simulations that can 
    seamlessly integrate with a diverse range of available and emerging quantum chemistry codes at different levels of theory.

    Supporting ab initio, semiempirical quantum mechanics, and coarse-grained flexible charge equilibration models, this is a unified 
    framework to simulate and analyze the quantum molecular dynamics of complex chemical systems and materials.
    """
    
    homepage = "https://github.com/lanl/sedacs"
    git = "https://github.com/lanl/sedacs.git"

    version('main', branch='main')

    maintainers("finkeljos", "cnegre")

    tags = ["lanl"]

    license("BSD 3-Clause")

    # python dependencies
    depends_on('python@3.10:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-wheel', type='build')
    depends_on('py-scikit-build-core', type='build')
    depends_on('py-numpy@1:', type=('build', 'run'))
    depends_on('py-torch@2:', type=('build', 'run'))
    depends_on('py-scipy@1:', type=('build', 'run'))

    # mpi
    variant("mpi", default=True, description="Build with mpi")
    depends_on('mpi',when="+mpi")
    depends_on('py-mpi4py',when="+mpi")
     
    # gpu/ai-hardware library
    variant("gpulib", default=False, description="Build with GPU, AI-hardware library support.")
    depends_on('cmake',when="+gpulib")
    depends_on('nvhpc',when="+gpulib")
    conflicts(
        "cuda_arch=none", when="+gpulib",  msg="sedacs: Please select a CUDA arch value"
    )

    # build latte with qmd-progress and other branch/variant restrictions
    variant("latte", default=False, description="Make latte available as a sedacs engine")
    depends_on('latte@lattepy+interface+progress',when="+latte") 
    depends_on('qmd-progress@master~benchmarks',when="+latte") 

    # build system
    build_system = 'pyproject'
    build_backend = 'scikit_build_core.build'


def setup_build_environment(self, env):
    env.set('GPU_ARCH', self.spec.variants['cuda_arch'].value)

