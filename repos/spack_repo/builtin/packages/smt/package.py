# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install smt
#
# You can edit this file again by typing:
#
#     spack edit smt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Smt(CMakePackage):
    """Spherical Mean Technique - microscopic diffusion anisotropy imaging"""

    homepage = "https://github.com/ekaden/smt"
    git = "https://github.com/ekaden/smt.git"
    maintainers = "richardbeare"
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("BSD-2-Clause", checked_by="richardbeare")

    version("0.4", tag="v0.4")

    # FIXME: Add dependencies if required.
    depends_on("cmake", type=("build"))
    def cmake_args(self):
        # FIXME: If not needed delete this function
        args = []
        return args
