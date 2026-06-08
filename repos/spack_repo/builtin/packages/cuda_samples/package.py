# Copyright Spack Project Developers. See COPYRIGHT file for details.
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
#     spack install cuda-samples
#
# You can edit this file again by typing:
#
#     spack edit cuda-samples
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class CudaSamples(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/NVIDIA/cuda-samples/archive/refs/tags/v13.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("13.0", sha256="63cc9d5d8280c87df3c1f4e2276234a0f42cc497c52b40dd5bdda2836607db79")
    version("12.9", sha256="2e67e1f6bdb15bf11b21e07e988e2f9f60fb054eff51ef01cebdd47229788015")
    version("12.8", sha256="fe82484f9a87334075498f4e023a304cc70f240a285c11678f720f0a1e54a89d")
    version("12.5", sha256="5c40cc096706045b067ec5897f039403014aa7a39b970905698466a2d029b972")
    version("12.4.1", sha256="01bb311cc8f802a0d243700e4abe6a2d402132c9d97ecf2c64f3fbb1006c304c")
    version("12.4", sha256="aa28fa2227768dd31ebbf9cd48b265a0c8810fae03e02c6079c0fa71bbea7319")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
