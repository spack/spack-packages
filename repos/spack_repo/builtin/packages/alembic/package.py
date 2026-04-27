# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Alembic(CMakePackage):
    """Alembic is an open computer graphics interchange
    framework. Alembic distills complex, animated scenes into a
    non-procedural, application-independent set of baked
    geometric results."""

    homepage = "https://www.alembic.io"
    url = "https://github.com/alembic/alembic/archive/1.7.16.tar.gz"

    license("BSD-3-Clause")

    version("1.8.10", sha256="06c9172faf29e9fdebb7be99621ca18b32b474f8e481238a159c87d16b298553")
    version("1.8.9", sha256="8c59c10813feee917d262c71af77d6fa3db1acaf7c5fecfd4104167077403955")
    version("1.8.8", sha256="ba1f34544608ef7d3f68cafea946ec9cc84792ddf9cda3e8d5590821df71f6c6")
    version("1.8.7", sha256="6de0b97cd14dcfb7b2d0d788c951b6da3c5b336c47322ea881d64f18575c33da")
    version("1.8.6", sha256="c572ebdea3a5f0ce13774dd1fceb5b5815265cd1b29d142cf8c144b03c131c8c")
    version("1.8.5", sha256="180a12f08d391cd89f021f279dbe3b5423b1db751a9898540c8059a45825c2e9")
    version("1.7.16", sha256="2529586c89459af34d27a36ab114ad1d43dafd44061e65cfcfc73b7457379e7c")

    variant("python", default=False, description="Python support")
    variant("hdf5", default=False, description="HDF5 support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@2.8.11:", type="build")
    depends_on("openexr@2.2.0:")
    depends_on("hdf5@1.8.9:", when="+hdf5")
    depends_on("boost@1.55:")
    depends_on("zlib-api")
    depends_on("py-ilmbase", when="+python")

    def cmake_args(self):
        args = [self.define_from_variant("USE_HDF5", "hdf5")]

        if self.spec.satisfies("+python") and self.spec["python"].satisfies("@3:"):
            args.append("-DPython_ADDITIONAL_VERSIONS=3")

        return args
