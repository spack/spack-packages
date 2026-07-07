# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.octave import OctavePackage
from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *


class OctaveSymbolic(OctavePackage, SourceforgePackage):
    """Adds symbolic calculation features to GNU Octave.
    These include common Computer Algebra System tools such as algebraic operations,
    calculus, equation solving, Fourier and Laplace transforms, variable precision
    arithmetic and other features.
    Compatibility with other symbolic toolboxes is intended."""

    homepage = "https://octave.sourceforge.io/symbolic/"
    sourceforge_mirror_path = "octave/symbolic-2.9.0.tar.gz"

    license("GPL-3.0-only")

    version("3.2.2", sha256="8eb492408ec5aafe4e196ec5bdbd2298e0ac068d2b754948f34b9082b9126b37")
    version("2.9.0", sha256="089ec44a0a49417a8b78797e87f338da6a6e227509f3080724996483d39b23cb")

    depends_on("cxx", type="build")
    extends("octave@4.2.0:")
