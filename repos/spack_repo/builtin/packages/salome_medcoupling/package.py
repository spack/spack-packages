# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#
# Important feature: a version of salome-medcoupling depand on
# a specific version of salome-med package

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SalomeMedcoupling(CMakePackage):
    """salome-medcoupling is a part of SALOME platform to manipulate meshes and
    fields in memory, and uses MED format for files."""

    maintainers("franciskloss")

    homepage = "https://docs.salome-platform.org/latest/dev/MEDCoupling/developer/index.html"
    git = "https://github.com/SalomePlatform/medcoupling.git"

    license("LGPL-2.1-or-later")

    version("9.15.0", sha256="4ec97fc881f12e71965ea73422319aac6f69319c5c688eb165329dce826cbbb8")
    version("9.14.0", sha256="d4699b564fe1a113663649b9ff1c353314509763a5aca756569e6f4de8940049")
    version("9.13.0", sha256="54d010df0d8a66c7cf7b39a40e28aac16bc0bc20faf97c5190d0a2df4941e15e")
    version("9.12.0", sha256="b668b9b2883b456e3edf6f9f1ef3749f8c8cc5279ae212c388e53f69eed66db7")
    version("9.11.0", sha256="11d86030f7552a3b91fe0769784b42e9794b754e88c8b50405b75d130f1cb45a")

    def url_for_version(self, version):
        url = "https://github.com/SalomePlatform/medcoupling/archive/refs/tags/V{0}.tar.gz"
        return url.format(version.underscored)

    variant("static", default=False, description="Enable static library build")
    variant("mpi", default=False, description="Enable MPI")
    variant("int64", default=False, description="Use 64 bits indices")
    variant("partitioner", default=False, description="Enable partitioner")
    variant("metis", default=False, when="+partitioner", description="Enable Metis")
    variant("scotch", default=False, when="+partitioner", description="Enable Scotch")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # See https://github.com/SalomePlatform/sat_salome/blob/master/applications for the
    # dependencies and their version used for official releases

    depends_on("cmake@2.8.11:3", type="build")

    depends_on("rpc")
    depends_on("libxml2@2.9.1:")
    depends_on("cppunit", type="test")
    depends_on("python@3.6.5:", when="@:9.12")
    depends_on("python@3.9.14:", when="@9.13:")
    depends_on("py-scipy@0.19.1:1.14", type=("build", "run"))
    depends_on("py-numpy@1.15.1:1", type=("build", "run"))
    depends_on("boost+python+numpy@1.58.0:", when="@:9.12")
    depends_on("boost+python+numpy@1.71.0:", when="@9.13:")
    depends_on("swig@3.0.12:", when="@:9.10", type="build")
    depends_on("swig@4.0.2:", when="@9.11:", type="build")

    depends_on("metis@5.1.0:", when="+metis")
    depends_on("scotch@6.0.4:", when="@:9.12 +scotch")
    depends_on("scotch@6.1.2:", when="@9.13: +scotch")
    depends_on("mpi", when="+mpi")

    for _min_ver in range(11, 16):
        _ver = f"9.{_min_ver}.0"
        depends_on(f"salome-configuration@{_ver}", when=f"@{_ver}")

    for _mpi_variant in ("~mpi", "+mpi"):
        for _static_variant, _shared_variant in (("~static", "+shared"), ("+static", "~shared")):
            for _int64_variant in ("~int64", "+int64"):
                depends_on(
                    f"med@4.2.0{_mpi_variant}{_shared_variant}{_int64_variant}",
                    when=f"@9.15.0:{_mpi_variant}{_static_variant}{_int64_variant}",
                )
                depends_on(
                    f"med@4.1.1{_mpi_variant}{_shared_variant}{_int64_variant}",
                    when=f"@9.11.0:9.14.0{_mpi_variant}{_static_variant}{_int64_variant}",
                )

    def check(self):
        pass

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if "+metis" in self.spec:
            env.set("METIS_ROOT_DIR", self.spec["metis"].prefix)

        if "+scotch" in self.spec:
            env.set("SCOTCH_ROOT_DIR", self.spec["scotch"].prefix)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        python_ver = self.spec["python"].version.up_to(2)
        env.prepend_path(
            "PYTHONPATH", join_path(self.prefix.lib, f"python{python_ver}", "site-packages")
        )

    def cmake_args(self):
        args = [
            self.define_from_variant("MEDCOUPLING_BUILD_STATIC", "static"),
            self.define_from_variant("MEDCOUPLING_USE_MPI", "mpi"),
            self.define_from_variant("SALOME_USE_MPI", "mpi"),
            self.define_from_variant("MEDCOUPLING_USE_64BIT_IDS", "int64"),
            self.define_from_variant("MEDCOUPLING_ENABLE_PARTITIONER", "partitioner"),
            self.define_from_variant("MEDCOUPLING_PARTITIONER_METIS", "metis"),
            self.define_from_variant("MEDCOUPLING_PARTITIONER_SCOTCH", "scotch"),
            self.define("MEDCOUPLING_BUILD_TESTS", self.run_tests),
            self.define("MEDCOUPLING_BUILD_DOC", False),
            self.define("MEDCOUPLING_ENABLE_PYTHON", True),
            self.define("MEDCOUPLING_ENABLE_RENUMBER", False),
            self.define("MEDCOUPLING_PARTITIONER_PARMETIS", False),
            self.define("MEDCOUPLING_PARTITIONER_PTSCOTCH", False),
            self.define("MEDCOUPLING_MICROMED", False),
        ]
        return args
