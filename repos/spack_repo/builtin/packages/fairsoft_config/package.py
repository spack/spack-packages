# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *

class FairsoftConfig(CMakePackage):
    """Legacy fairsoft-config script"""

    homepage = 'https://github.com/FairRootGroup/fairsoft-config'
    git = 'https://github.com/FairRootGroup/fairsoft-config'
    maintainers('dennisklein', 'fuhlig1', 'jezwilkinson')

    version('develop')
    version('may25')

    variant('cxxstd',
            default='17',
            values=('17', '20'),
            multi=False,
            description='C++ standard reported')

    depends_on('cmake@3:', type='build')
    depends_on('root', type=('build', 'link', 'run'))

    def cmake_args(self):
        args = []
        args.append('-DFAIRSOFT_VERSION=%s' % self.version)
        args.append('-DCMAKE_CXX_STANDARD=%s' %
                    self.spec.variants['cxxstd'].value)
        return args
