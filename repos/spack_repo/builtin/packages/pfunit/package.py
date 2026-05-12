# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Pfunit(CMakePackage):
    """pFUnit is a unit testing framework enabling JUnit-like testing of
    serial and MPI-parallel software written in Fortran.
    """

    homepage = "https://github.com/Goddard-Fortran-Ecosystem/pFUnit"
    url = "https://github.com/Goddard-Fortran-Ecosystem/pFUnit/releases/download/v4.6.1/pFUnit-v4.6.1.tar"
    git = "https://github.com/Goddard-Fortran-Ecosystem/pFUnit.git"

    maintainers("mathomp4", "tclune")

    license("NASA-1.3", checked_by="mathomp4", when="@:4.16")
    license("Apache-2.0", checked_by="mathomp4", when="@4.17:")

    version("4.18.1", sha256="34654ac27c3498333210cac480d6319d3d8c0230057fd0974f3e3c4d656b8cd9")
    version("4.18.0", sha256="e1beb32e95f487423720b85bbb8314f46af5321f3ed0d06cf0122bc479ecb812")
    version("4.17.1", sha256="de3d3a9d097762e41763035b1e8f39edfce7606c7ccda01839ca6331580ef38c")
    # There was a mistake in the 4.16.0 release. Mark as deprecated.
    version(
        "4.16.0",
        sha256="314381ff08dc99e87a4da5862501053d112babaf73244b1c04b77065d3fd3091",
        deprecated=True,
    )
    version("4.15.0", sha256="8c9cb7f7275802c5169b16dd511209b15ccde3a0e2fb3ed9007a0ab9acf4abb1")
    version("4.14.0", sha256="3f5fcc79cf5f12ed08eb8e49aff23e0826243b14d4b2b2efee91ce823ac1749d")
    version("4.13.0", sha256="f4f894faea5cc591f05e071a2bb16ddf613c3c22f88a6dc3b8149f5c4f159548")
    version("4.12.0", sha256="facbef73b3e225ca552a376d0ec4502881ad0876f706cd0b5cffed8a089b92e4")
    version("4.11.1", sha256="db954ce44e857fe17cf4212f91223d2ab73248de0c3af405e2e1224f92ed8d42")
    version("4.10.0", sha256="ee5e899dfb786bac46e3629b272d120920bafdb7f6a677980fc345f6acda0f99")
    version("4.9.0", sha256="caea019f623d4e02dd3e8442cee88e6087b4c431a2628e9ec2de55b527b51ab6")
    version("4.8.0", sha256="b5c66ab949fd23bee5c3b4d93069254f7ea40decb8d21f622fd6aa45ee68ef10")
    version("4.7.4", sha256="ac850e33ea99c283f503f75293bf238b4b601885d7adba333066e6185dad5c04")
    version("4.7.3", sha256="247239298b55e847417b7830183d7fc62cca93dc92c8ec7c0067784b7ce34544")
    version("4.7.2", sha256="3142a1e56b7d127fdc9589cf6deff8505174129834a6a268d0ce7e296f51ab02")
    version("4.7.1", sha256="64de3eb9f364b57ef6df81ba33400dfd4dcebca6eb5d0e9b7955ed8156e29165")
    version("4.7.0", sha256="5faf52d0ab8589b3cd3ea488b34a65dc931f70c07aaa7bf4f209b18af2b38e4e")
    version("4.6.3", sha256="a43a64c4338be57fdbe1cae1a89e277196f10931bc1f73418a463e05e5e7b2d1")
    version("4.6.2", sha256="fd302a1f7a131b38e18bc31ede69a216e580c640152e5e313f5a1e084669a950")
    version("4.6.1", sha256="19de22ff0542ca900aaf2957407f24d7dadaccd993ea210beaf22032d3095add")
    version("4.6.0", sha256="7c768ea3a2d16d8ef6229b25bd7756721c24a18db779c7422afde0e3e2248d72")
    version("4.5.0", sha256="ae0ed4541f2f4ec7b1d06eed532a49cb4c666394ab92b233911f92ce50f76743")
    version("4.4.1", sha256="6b5d5e19201f56e1ebc984f1cb30dffa0e9e1f14810aab601bd43e85fd3f18ab")
    version("4.4.0", sha256="e51e09b272e0f2598eb94cd1367158049deed1ac3a8779a7b30931e36f8c9752")
    version("4.3.0", sha256="a63d3ccda4a5e44b2afecbf3cc01275f80047602bd8587343a19f17db3e64b1d")
    version("4.2.7", sha256="1412134f812322b0aa5471007c9b7281fbe962e15b9efc9700cac24c9054bd84")
    version("4.2.6", sha256="9604d4c010a56bbb495eafcc9a2061a49572204dd211750b6f7209712c7c4a8a")
    version("4.2.5", sha256="a1f8edece98d6ffc3475465022828ccc9e26e2ecbd0374f4883bef626e33e549")
    version("4.2.3", sha256="9469a945a41649fd136bd75b3c5bae9895fe2d5f36046c24525b73d3d444d32f")
    version("4.2.2", sha256="f837b99585780c065e32249741926c61c8bf8b5b0b170ffc0fbcde105afbbb6a")
    version("4.2.1", sha256="977ac9de453da26700b7d4660f783e2850b6d4c9bbf36a4ffb721dbdeb8eb58c")
    version("4.2.0", sha256="33df62f80cf03827455508b67d53f820ddffa2ec0f1ba999790ff1f87592ce16")
    version("4.1.14", sha256="bada2be8d7e69ca1f16209ba92293fa1c06748b78534d71b24b2c825450a495f")
    version("4.1.13", sha256="f388e08c67c51cbfd9f3a3658baac912b5506d2fc651410cd34a21260c309630")
    version("4.1.12", sha256="7d71b0fb996497fe9a20eb818d02d596cd0d3cded1033a89a9081fbd925c68f2")
    version("4.1.11", sha256="16160bac223aaa3ed2b27e30287d25fdaec3cf6f2c570ebd8d61196e6aa6180f")
    version("4.1.10", sha256="051c35ad9678002943f4a4f2ab532a6b44de86ca414751616f93e69f393f5373")

    variant("mpi", default=False, description="Enable MPI")
    variant("openmp", default=False, description="Enable OpenMP")
    variant("fhamcrest", default=False, description="Enable hamcrest support")
    variant("esmf", default=False, description="Enable esmf support")
    variant("docs", default=False, description="Build docs")

    # pFUnit brought in mpi_f08 support in 4.4.0
    variant(
        "mpi_f08",
        default=False,
        description="Enable MPI Fortran 2008 bindings",
        when="@4.4.0: +mpi",
    )

    # The maximum rank of an array in the Fortran 2008 standard is 15
    max_rank = 15
    allowed_array_ranks = tuple(str(i) for i in range(3, max_rank + 1))

    variant(
        "max_array_rank",
        default="5",
        values=allowed_array_ranks,
        description="Max rank for assertion overloads (higher values may be slower to build)",
    )

    variant(
        "build_type",
        default="Release",
        description="The build type to build",
        values=("Debug", "Release"),
    )

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("doxygen", type="build", when="+docs")

    depends_on("python", type=("build", "run"))
    depends_on("mpi", when="+mpi")
    depends_on("esmf", when="+esmf")
    depends_on("m4", type="build")
    depends_on("fargparse@1.8.0:", when="@4.10.0:")
    depends_on("fargparse")

    depends_on("cmake@3.12:3", type="build", when="@:4.11")
    depends_on("cmake@3.12:", type="build", when="@4.12")
    depends_on("cmake@3.24:", type="build", when="@4.13:")

    # CMake 3.25.0 has an issue with pFUnit
    # https://gitlab.kitware.com/cmake/cmake/-/issues/24203
    conflicts(
        "^cmake@3.25.0", msg="CMake 3.25.0 has a bug with pFUnit. Please use another version."
    )

    conflicts("%gcc@:8.3.9", msg="pFUnit requires GCC 8.4.0 or newer")

    # pfunit only works with the Fujitsu compiler from 4.9.0 onwards
    conflicts(
        "%fj", when="@:4.8.0", msg="pfunit only works with the Fujitsu compiler from 4.9.0 onwards"
    )

    patch("mpi-test.patch", when="+use_comm_world")

    def patch(self):
        # The package tries to put .mod files in directory ./mod;
        # spack needs to put them in a standard location:
        for file in glob.glob("*/CMakeLists.txt"):
            filter_file(r".*/mod($|[^\w].*)", "", file)

    def url_for_version(self, version):
        url_base = "https://github.com/Goddard-Fortran-Ecosystem/pFUnit"
        # Version 4.2.3+ has a v...
        if version >= Version("4.2.3"):
            url = url_base + "/releases/download/v{0}/pFUnit-v{0}.tar"
        # Then version down to 4.0.0 does not
        elif version >= Version("4"):
            url = url_base + "/releases/download/v{0}/pFUnit-{0}.tar"
        # Version 3.3.0 has a v unlike all other 3 releases
        elif version == Version("3.3.0"):
            url = url_base + "/archive/v{0}.tar.gz"
        else:
            url = url_base + "/archive/{0}.tar.gz"

        return url.format(version)

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define("BUILD_SHARED_LIBS", False),
            self.define("CMAKE_Fortran_MODULE_DIRECTORY", spec.prefix.include),
            self.define_from_variant("ENABLE_BUILD_DOXYGEN", "docs"),
            self.define("ENABLE_TESTS", self.run_tests),
            self.define("SKIP_MPI", self.spec.satisfies("~mpi")),
            self.define("SKIP_OPENMP", self.spec.satisfies("~openmp")),
            self.define("SKIP_FHAMCREST", self.spec.satisfies("~fhamcrest")),
            self.define("SKIP_ESMF", self.spec.satisfies("~esmf")),
            self.define_from_variant("MAX_ASSERT_RANK", "max_array_rank"),
        ]

        if spec.satisfies("@:4.2.1") and spec.satisfies("%gcc@5:"):
            # prevents breakage when max_array_rank is larger than default. Note
            # that 4.0.0-4.2.1 still had a 512 limit
            args.append(self.define("CMAKE_Fortran_FLAGS", "-ffree-line-length-none"))

        if spec.satisfies("+mpi"):
            args.extend(
                [
                    self.define("MPI_USE_MPIEXEC", True),
                    self.define("CMAKE_Fortran_COMPILER", spec["mpi"].mpifc),
                ]
            )

        if spec.satisfies("@4.4.0: +mpi"):
            args.append(self.define_from_variant("ENABLE_MPI_F08", "mpi_f08"))

        return args

    def check(self):
        """Searches the CMake-generated Makefile for the target ``test``
        and runs it if found.
        """
        args = ["tests"]
        if self.spec.satisfies("+mpi"):
            args.append("MPI=YES")
        if self.spec.satisfies("+openmp"):
            args.append("OPENMP=YES")
        with working_dir(self.build_directory):
            make(*args)

    def compiler_vendor(self):
        vendors = {
            "%gcc": "GNU",
            "%clang": "GNU",
            "%intel": "Intel",
            "%nag": "NAG",
            "%cce": "Cray",
        }
        for key, value in vendors.items():
            if self.spec.satisfies(key):
                return value
        raise InstallError("Unsupported compiler.")
