# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class ClingoBootstrapPgo(Package):
    """Resources for profile-guided optimization for clingo-bootstrap"""

    homepage = "https://github.com/spack/spack-clingo-pgo"
    git = "https://github.com/spack/spack-clingo-pgo.git"

    maintainers("haampie")

    version("1.0.0", commit="64bec625ae06b32b7f5f01bccf9d27d0432a018f")

    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)
        install_tree("share", prefix.share)
