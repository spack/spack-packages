# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gbl(CMakePackage):
    deprecated(
        reason="rename",
        msg="The gbl package has been renamed to generalbrokenlines. "
            "Please use generalbrokenlines instead."
    )