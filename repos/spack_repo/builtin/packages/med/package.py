# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Med(CMakePackage):
    """The MED file format is a specialization of the HDF5 standard."""

    homepage = "https://docs.salome-platform.org/latest/dev/MEDCoupling/med-file.html"
    url = "https://files.salome-platform.org/Salome/medfile/med-4.1.1.tar.gz"

    maintainers("likask")

    license("LGPL-3.0-only")

    version("6.0.1", sha256="f8f1edc6874bc48d8f3e4e8be1cf7379ed318726d8abc6804e85e821555b1fa8")
    version(
        "5.0.0",
        sha256="267e76d0c67ec51c10e3199484ec1508baa8d5ed845c628adf660529dce7a3d4",
        url="https://files.salome-platform.org/Salome/medfile/med-5.0.0.tar.bz2",
    )
    version("4.2.0", sha256="87c840638f439626b7b3054f655b93a3b9cc8de2177389b09193b646c3095a65")
    version("4.1.1", sha256="a082b705d1aafe95d3a231d12c57f0b71df554c253e190acca8d26fc775fb1e6")

    variant("api23", default=True, description="Enable API2.3")
    variant("mpi", default=True, description="Enable MPI")
    variant("shared", default=False, description="Builds a shared version of the library")
    variant("fortran", default=False, description="Enable Fortran support")
    variant("int64", default=False, description="Use 64-bit integers as indices.")
    variant("doc", default=False, description="Install documentation")
    variant("python", default=False, description="Build Python bindings")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("hdf5@1.10.2:1.10.7", when="@4")
    depends_on("hdf5@1.12.1:1.12", when="@5")
    depends_on("hdf5@1.14", when="@6")

    depends_on("hdf5~mpi", when="~mpi")
    depends_on("hdf5+mpi", when="+mpi")
    depends_on("mpi", when="+mpi")

    depends_on("doxygen", type="build", when="+doc")

    depends_on("swig", type="build", when="+python")
    depends_on("python", when="+python")
    conflicts("~shared", when="+python", msg="Python bindings require shared libraries")

    def patch(self):
        # resembles FindSalomeHDF5.patch as in salome-configuration
        # see https://cmake.org/cmake/help/latest/prop_tgt/IMPORTED_LINK_INTERFACE_LIBRARIES.html
        filter_file(
            "GET_PROPERTY(_lib_lst TARGET hdf5-shared PROPERTY IMPORTED_LINK_INTERFACE_LIBRARIES_NOCONFIG)",  # noqa: E501
            "#GET_PROPERTY(_lib_lst TARGET hdf5-shared PROPERTY IMPORTED_LINK_INTERFACE_LIBRARIES_NOCONFIG)",  # noqa: E501
            "config/cmake_files/FindMedfileHDF5.cmake",
            string=True,
        )

    def cmake_args(self):
        spec = self.spec

        options = [
            self.define("HDF5_ROOT_DIR", spec["hdf5"].prefix),
            self.define("MEDFILE_BUILD_TESTS", self.run_tests),
            self.define_from_variant("MEDFILE_BUILD_PYTHON", "python"),
            self.define_from_variant("MEDFILE_INSTALL_DOC", "doc"),
        ]
        if "~fortran" in spec:
            options.append("-DCMAKE_Fortran_COMPILER=")

        if "+int64" in spec:
            options.append("-DMED_MEDINT_TYPE=long")

        if "+api23" in spec:
            options.extend(
                [
                    "-DCMAKE_CXX_FLAGS:STRING=-DMED_API_23=1",
                    "-DCMAKE_C_FLAGS:STRING=-DMED_API_23=1",
                    "-DMED_API_23=1",
                ]
            )

        if "+shared" in spec:
            options.extend(["-DMEDFILE_BUILD_SHARED_LIBS=ON", "-DMEDFILE_BUILD_STATIC_LIBS=OFF"])
        else:
            options.extend(["-DMEDFILE_BUILD_SHARED_LIBS=OFF", "-DMEDFILE_BUILD_STATIC_LIBS=ON"])

        if "+mpi" in spec:
            options.extend(["-DMEDFILE_USE_MPI=YES", "-DMPI_ROOT_DIR=%s" % spec["mpi"].prefix])

        if "+python" in spec and spec["python"].version >= Version("3.9"):
            options.extend(["-DCMAKE_CXX_FLAGS=-DPyEval_CallObject=PyObject_CallObject"])

        return options
