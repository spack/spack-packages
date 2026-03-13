# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Meshoptimizer(CMakePackage):
    """A mesh optimization library that makes meshes smaller and faster to render."""

    homepage = "https://meshoptimizer.org"
    url = "https://github.com/zeux/meshoptimizer/archive/refs/tags/v1.0.tar.gz"

    license("MIT", checked_by="cmelone")

    version("1.0", sha256="30d1c3651986b2074e847b17223a7269c9612ab7f148b944250f81214fed4993")

    variant("shared", default=False, description="Build shared libraries")
    variant("gltfpack", default=False, description="Build gltfpack")
    variant(
        "stable_exports", default=False, description="Only export stable APIs from shared library"
    )

    depends_on("cmake@3.5:", type="build")

    def cmake_args(self):
        return [
            self.define_from_variant("MESHOPT_BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("MESHOPT_BUILD_GLTFPACK", "gltfpack"),
            self.define_from_variant("MESHOPT_STABLE_EXPORTS", "stable_exports"),
        ]
