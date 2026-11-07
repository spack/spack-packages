# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Sloth(CMakePackage):
    """SLOTH is an HPC multiphase-field, multicomponent framework built on top of
    MFEM by the CEA (French Alternative Energies and Atomic Energy Commission)."""

    homepage = "https://github.com/Collab4Sloth/SLOTH"
    url = "https://github.com/Collab4Sloth/SLOTH/archive/refs/tags/v2.2.0.tar.gz"
    git = "https://github.com/Collab4Sloth/SLOTH.git"

    maintainers("CINTROINI")

    license("LGPL-3.0-or-later", checked_by="CINTROINI")

    version("master", branch="master")
    version("2.2.0", sha256="db91213f055c7549460d6e7ab66978d9dc07a03a2aaa12df12beacb19158b120")

    variant("shared", default=False, description="Build SLOTH as a shared library")
    variant("mumps", default=False, description="Enable the MUMPS direct solver (through MFEM)")
    variant("voro", default=False, description="Enable Voro++ (Voronoi tessellations)")
    variant(
        "bigint",
        default=False,
        description="64-bit global indices (HYPRE +mixedint), for problems with more "
        "than about 2 billion unknowns",
    )
    variant(
        "native",
        default=False,
        description="Optimize for the CPU of the build machine (-march=native and "
        "link-time optimization)",
    )

    depends_on("cxx", type="build")
    depends_on("cmake@3.13:", type="build")
    # SymPy generates the coefficient classes at configure time and at run time
    # (scripts/GenerateCoefficient.py)
    depends_on("python@3:", type=("build", "run"))
    depends_on("py-sympy", type=("build", "run"))

    depends_on("mpi")
    depends_on("mfem@4.9: +mpi")
    # 2.2.0 is tested with MFEM 4.9 only
    depends_on("mfem@4.9", when="@2.2.0")
    depends_on("hypre@3.1: +shared")

    depends_on("mfem+shared", when="+shared")
    depends_on("mfem+mumps", when="+mumps")
    depends_on("mumps", when="+mumps")
    depends_on("voropp", when="+voro")
    # mixedint rather than int64: 64-bit global indices, 32-bit local ones
    depends_on("hypre+mixedint", when="+bigint")

    def cmake_args(self):
        return [
            # MFEM and its third-party libraries are read from MFEM's config.mk
            self.define("MFEM_DIR", self.spec["mfem"].prefix),
            self.define_from_variant("SLOTH_USE_SHARED", "shared"),
            self.define_from_variant("SLOTH_USE_VORO", "voro"),
            self.define_from_variant("SLOTH_NATIVE_ARCH", "native"),
            self.define_from_variant("SLOTH_ENABLE_LTO", "native"),
        ]

    def setup_build_environment(self, env):
        # Fallback used to read the HYPRE version
        env.set("HYPRE_DIR", self.spec["hypre"].prefix)
        # Takes priority over CMAKE_INSTALL_PREFIX in SLOTH's CMakeLists.txt
        env.set("USER_INSTALL_PATH", self.prefix)
        if self.spec.satisfies("+voro"):
            env.set("VORO", self.spec["voropp"].prefix)
