# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class _4cMultiphysics(CMakePackage):
    """4C is a parallel multiphysics research code."""

    homepage = "https://www.4c-multiphysics.org/"
    url = "https://github.com/4C-multiphysics/4C/archive/refs/tags/v2025.3.0.tar.gz"
    git = "https://github.com/4C-multiphysics/4C.git"

    maintainers(
        "bgoderbauer",
        "c-p-schmidt",
        "georghammerl",
        "isteinbrecher",
        "lauraengelhardt",
        "mayrmt",
        "rjoussen",
    )
    license("LGPL-3.0-or-later")

    version("main", branch="main")
    version("2026.2.0", sha256="57e05128934e06b67d5ae3c2d3402f80d1ddfc3975b1557670e5b1d3399a6c0b")
    version("2026.1.0", sha256="9d95607a0b7668c9712392c81863b6327b8922745705b62e07f605f1d6932646")
    version("2025.3.0", sha256="31088a9392bf55eb8c1b5a3b8426e8ae2b367327cef01f8f34aff55cb1153180")

    # Keep these sources private to 4C until maintained packages are available
    # in the builtin repository. FetchContent consumes the staged source trees.
    resource(
        name="ryml",
        git="https://github.com/biojppm/rapidyaml.git",
        commit="47ec2fa184209687c20fd5bc05621e1cb1200311",
        submodules=True,
        destination="spack-resources",
        placement="ryml",
    )
    resource(
        name="mirco",
        url="https://github.com/imcs-compsim/MIRCO/archive/b9d0c4ba27ff8463a3d2b17163fead8800b2650c.tar.gz",
        sha256="b3a16a0aeed5fcd778c8757d81af9070ec4964a5206f87b6257a402aa3fc4bfd",
        destination="spack-resources",
        placement="mirco",
        when="+mirco",
    )

    variant("shared", default=True, description="Build shared libraries")
    variant("qhull", default=True, description="Enable Qhull support")
    variant("vtk", default=False, description="Enable VTK support")
    variant("gmsh", default=False, description="Enable Gmsh support")
    variant("dealii", default=False, description="Enable deal.II support")
    variant("arborx", default=False, description="Enable ArborX support")
    variant("fftw", default=False, description="Enable FFTW support")
    variant("mirco", default=False, description="Enable MIRCO support")
    variant("backtrace", default=False, description="Enable libbacktrace support")

    patch("identify-release-dealii.patch", when="+dealii")
    patch("link-installed-arborx.patch", when="+arborx")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.30:", type="build")
    depends_on("ninja", type="build")
    requires("platform=linux")

    depends_on("mpi")
    depends_on("hdf5+mpi+hl")
    # Trilinos pulls in Fortran dependencies through MUMPS. A Fortran-capable
    # compiler must therefore be registered even though 4C has no Fortran sources.
    depends_on(
        "trilinos@16.2.1+mpi+amesos+amesos2+belos+epetra+epetraext"
        "+ifpack+ifpack2+intrepid2+isorropia+ml+muelu+nox+sacado+shards+stratimikos"
        "+teko+thyra+tpetra+zoltan+zoltan2+explicit_template_instantiation"
        "+mumps+superlu-dist+suite-sparse+exodus gotype=int",
        patches=[patch("trilinos-iocgns-extern-c-linkage.patch")],
    )
    # deal.II 9.6.2 uses bundled Boost 1.84. Keep 4C's compiled Boost.Graph
    # library and headers ABI-compatible with the deal.II headers.
    depends_on("boost@1.84.0+graph")
    depends_on("cln")
    depends_on("zlib-api")
    depends_on("cli11@2.6.1")
    depends_on("magic-enum@0.9.7")

    # 4C uses Qhull's deprecated non-reentrant libqhull API.
    depends_on("qhull@2019.1", when="+qhull")
    depends_on("vtk@9:+shared", when="+vtk")
    depends_on("gmsh@4.15.1+shared~cgns~fltk~med", when="+gmsh")
    depends_on(
        "dealii@9.6.2+trilinos+mpi~adol-c",
        patches=[
            patch("dealii-force-bundled-boost.patch"),
            patch("dealii-use-cxx20.patch"),
            patch("dealii-petsc-3.25-domain-flags.patch"),
        ],
        when="+dealii",
    )
    depends_on("arborx@2.0.1+mpi", when="+arborx")
    depends_on("fftw", when="+fftw")
    depends_on("libbacktrace", when="+backtrace")

    generator("ninja")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define_from_variant("FOUR_C_BUILD_SHARED_LIBS", "shared"),
            self.define("FOUR_C_ENABLE_DEVELOPER_MODE", False),
            self.define("FOUR_C_ENABLE_METADATA_GENERATION", False),
            self.define("FETCHCONTENT_TRY_FIND_PACKAGE_MODE", "ALWAYS"),
            self.define("FOUR_C_HDF5_ROOT", spec["hdf5"].prefix),
            self.define("FOUR_C_MPI_ROOT", spec["mpi"].prefix),
            self.define("FOUR_C_TRILINOS_ROOT", spec["trilinos"].prefix),
            self.define("FOUR_C_BOOST_ROOT", spec["boost"].prefix),
            self.define("FOUR_C_CLN_ROOT", spec["cln"].prefix),
            self.define(
                "FETCHCONTENT_SOURCE_DIR_RYML",
                join_path(self.stage.source_path, "spack-resources", "ryml"),
            ),
            self.define("FOUR_C_MAGIC_ENUM_ROOT", spec["magic-enum"].prefix),
            self.define("FOUR_C_ZLIB_ROOT", spec["zlib-api"].prefix),
            self.define("FOUR_C_CLI11_ROOT", spec["cli11"].prefix),
            self.define_from_variant("FOUR_C_WITH_QHULL", "qhull"),
            self.define_from_variant("FOUR_C_WITH_VTK", "vtk"),
            self.define_from_variant("FOUR_C_WITH_GMSH", "gmsh"),
            self.define_from_variant("FOUR_C_WITH_DEAL_II", "dealii"),
            self.define_from_variant("FOUR_C_WITH_ARBORX", "arborx"),
            self.define_from_variant("FOUR_C_WITH_FFTW", "fftw"),
            self.define_from_variant("FOUR_C_WITH_MIRCO", "mirco"),
            self.define_from_variant("FOUR_C_WITH_BACKTRACE", "backtrace"),
            self.define("FOUR_C_WITH_PYTHON", False),
            self.define("FOUR_C_WITH_PYBIND11", False),
            self.define("FOUR_C_ENABLE_PYTHON_BINDINGS", False),
        ]

        roots = {
            "qhull": ("FOUR_C_QHULL_ROOT", "qhull"),
            "vtk": ("FOUR_C_VTK_ROOT", "vtk"),
            "gmsh": ("FOUR_C_GMSH_ROOT", "gmsh"),
            "dealii": ("FOUR_C_DEAL_II_ROOT", "dealii"),
            "arborx": ("FOUR_C_ARBORX_ROOT", "arborx"),
            "fftw": ("FOUR_C_FFTW_ROOT", "fftw"),
            "backtrace": ("FOUR_C_BACKTRACE_ROOT", "libbacktrace"),
        }
        for variant, (variable, dependency) in roots.items():
            if "+" + variant in spec:
                args.append(self.define(variable, spec[dependency].prefix))

        if "+arborx" in spec:
            args.append(self.define("FOUR_C_ARBORX_FIND_INSTALLED", True))
        if "+mirco" in spec:
            args.append(
                self.define(
                    "FETCHCONTENT_SOURCE_DIR_MIRCO",
                    join_path(self.stage.source_path, "spack-resources", "mirco"),
                )
            )

        return args
