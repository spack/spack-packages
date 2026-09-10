# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cosimio(CMakePackage):
    """The CoSimIO is a small library for interprocess communication in
    CoSimulation contexts.  It is designed for exchanging data between
    different solvers or other software tools.  For performing coupled
    simulations it is used in combination with the CoSimulationApplication.
    It is implemented as a detached interface: it follows the interface of
    Kratos but is independent of it, which allows easy integration into
    other codes / solvers.
    """

    tags = ["fem", "finite-elements", "hpc", "cosimulation", "coupling"]

    homepage = "https://github.com/KratosMultiphysics/CoSimIO"
    git = "https://github.com/KratosMultiphysics/CoSimIO.git"
    url = "https://github.com/KratosMultiphysics/CoSimIO/archive/refs/tags/v4.3.1.tar.gz"

    maintainers("loumalouomega", "philbucher", "pooyan-dadvand")

    version("master", branch="master")
    version("4.3.1", sha256="9e57839175c06a3d2e8694f95f718707ae465867958ef3bc6b554f775915082b")
    version("4.3.0", sha256="108a8c0b042f0eb307984accaecb2b6fc1407afd0bd4b36a4c5a98470a757a66")
    version("4.2.0", sha256="0c7e96d689b016eefd86781c0a55ce2383088cd2612aadc9697a839a0fa8d2b3")
    version("4.1.0", sha256="de02c526835d021c851dbbc1f95e4c929b10d0daccbabc80bcdc7503343678fc")
    version("4.0.0", sha256="12f38d1282b41e1ebc1d2c66d799cb7537840495c98638c698215d390403f221")
    version("3.0.0", sha256="02c902c2b28ae71241c4faf33f3e7a44f363b1d9732c53363cd33ffbbbe81eea")

    # -------------------------------------------------------------------------
    # Variants
    # -------------------------------------------------------------------------
    variant("mpi", default=False, description="Enable MPI communication")
    variant("c", default=True, description="Build C API")
    variant("python", default=False, description="Build Python bindings")
    variant("fortran", default=False, description="Build Fortran API")
    variant("testing", default=False, description="Build tests")
    variant("strict", default=False, description="Enable strict compiler warnings")

    # -------------------------------------------------------------------------
    # Conflicts
    # -------------------------------------------------------------------------
    # The Fortran interface is built on top of the C interface.
    conflicts("+fortran", when="~c", msg="+fortran requires +c (the Fortran API wraps the C API)")

    # -------------------------------------------------------------------------
    # Patches
    # -------------------------------------------------------------------------
    def patch(self):
        """Fix Fortran wrapper for gfortran 11+ compatibility (releases <= 4.3.1).

        Two bugs exist in co_sim_io/fortran/co_sim_io.f90:

        1. Fixed-form continuation: FUNCTION declarations spanning two lines use
           a column-6 ``&`` on the continuation line (fixed-form style), but
           gfortran compiles ``.f90`` as free-form where ``&`` must be at the
           **end** of the continued line.  Fix: add trailing ``&`` to the
           FUNCTION declaration line.

        2. Missing ``USE, INTRINSIC :: ISO_C_BINDING`` and ``IMPORT`` inside 15
           INTERFACE block function declarations. gfortran 11+ hard-errors on
           this; gfortran <=10 silently accepted it.
        """
        if not self.spec.satisfies("@:4.3.1 +fortran"):
            return

        fortran_file = join_path(self.stage.source_path, "co_sim_io", "fortran", "co_sim_io.f90")

        # BIND C name -> types to IMPORT in that interface block.
        fixes = {
            "CoSimIO_ImportData_fortran": "CoSimIO_Info",
            "CoSimIO_Element_GetNodeByIndex": "CoSimIO_Node, CoSimIO_Element",
            "CoSimIO_ModelPart_NumberOfNodes": "CoSimIO_ModelPart",
            "CoSimIO_ModelPart_NumberOfLocalNodes": "CoSimIO_ModelPart",
            "CoSimIO_ModelPart_NumberOfGhostNodes": "CoSimIO_ModelPart",
            "CoSimIO_ModelPart_NumberOfElements": "CoSimIO_ModelPart",
            "CoSimIO_ModelPart_GetNodeByIndex": "CoSimIO_Node, CoSimIO_ModelPart",
            "CoSimIO_ModelPart_GetLocalNodeByIndex": "CoSimIO_Node, CoSimIO_ModelPart",
            "CoSimIO_ModelPart_GetGhostNodeByIndex": "CoSimIO_Node, CoSimIO_ModelPart",
            "CoSimIO_ModelPart_GetNodeById": "CoSimIO_Node, CoSimIO_ModelPart",
            "CoSimIO_ModelPart_GetElementByIndex": "CoSimIO_Element, CoSimIO_ModelPart",
            "CoSimIO_ModelPart_GetElementById": "CoSimIO_Element, CoSimIO_ModelPart",
            "CoSimIO_ModelPart_CreateNewNode": "CoSimIO_Node, CoSimIO_ModelPart",
            "CoSimIO_ModelPart_CreateNewGhostNode": "CoSimIO_Node, CoSimIO_ModelPart",
            "CoSimIO_ModelPart_CreateNewElement": (
                "CoSimIO_Element, CoSimIO_ModelPart, CoSimIO_ElementType"
            ),
        }

        with open(fortran_file) as f:
            lines = f.readlines()

        out = []
        i = 0
        while i < len(lines):
            line = lines[i]
            out.append(line)

            # Detect a BIND continuation line: starts (after whitespace) with &
            # and contains one of our target BIND(C, NAME=...) patterns.
            stripped = line.lstrip()
            if stripped.startswith("&") and 'BIND(C, NAME="' in line:
                bind_name = next((n for n in fixes if 'BIND(C, NAME="' + n + '")' in line), None)
                if bind_name is not None:
                    # Fix 1: ensure the preceding FUNCTION line ends with & so
                    # that this is a valid free-form continuation.  If it already
                    # ends with & (idempotent re-run), skip.
                    if len(out) >= 2 and not out[-2].rstrip().endswith("&"):
                        out[-2] = out[-2].rstrip("\n").rstrip() + " &\n"

                    # Fix 2: inject USE/IMPORT after the BIND line if absent.
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if j < len(lines) and "USE, INTRINSIC" not in lines[j]:
                        out.append("                  USE, INTRINSIC :: ISO_C_BINDING\n")
                        out.append("                  IMPORT " + fixes[bind_name] + "\n")

            i += 1

        with open(fortran_file, "w") as f:
            f.writelines(out)

    # -------------------------------------------------------------------------
    # Compilers
    # -------------------------------------------------------------------------
    # When building without MPI (`~mpi`), ensure Spack provides valid
    # compiler wrappers so CMake can find `CC`, `CXX`, and `FC` when the
    # corresponding language APIs are enabled.
    with when("~mpi"):
        depends_on("c", type="build")  # Ensures C compiler is available
        depends_on("cxx", type="build")  # Ensures CXX compiler is available
    # +fortran needs a Fortran compiler regardless of MPI
    with when("+fortran"):
        depends_on("fortran", type="build")  # Ensures Fortran compiler is available

    # -------------------------------------------------------------------------
    # Dependencies
    # -------------------------------------------------------------------------
    depends_on("cmake@3.15:", type="build")

    # MPI: any implementation satisfying the 'mpi' virtual package works
    # (e.g. openmpi, mpich, intel-oneapi-mpi, mvapich2, ...)
    depends_on("mpi", when="+mpi")

    # Python bindings
    with when("+python"):
        depends_on("python@3.6:", type=("build", "link", "run"))
        # pybind11 is vendored under external_libraries/ but the system copy is
        # preferred to avoid duplicating toolchain state.
        depends_on("py-pybind11", type="build")

        extends("python")

    # -------------------------------------------------------------------------
    # CMake arguments
    # -------------------------------------------------------------------------
    def cmake_args(self):
        # Spack already forwards CMAKE_BUILD_TYPE; only set CoSimIO-specific
        # knobs here so we don't override Spack's build-type logic.
        args = [
            self.define_from_variant("CO_SIM_IO_BUILD_C", "c"),
            self.define_from_variant("CO_SIM_IO_BUILD_PYTHON", "python"),
            self.define_from_variant("CO_SIM_IO_BUILD_FORTRAN", "fortran"),
            self.define_from_variant("CO_SIM_IO_BUILD_TESTING", "testing"),
            self.define_from_variant("CO_SIM_IO_BUILD_MPI", "mpi"),
            self.define_from_variant("CO_SIM_IO_STRICT_COMPILER", "strict"),
        ]

        # The top-level CMakeLists declares `LANGUAGES CXX C` (no Fortran).
        # cmake_add_fortran_subdirectory() searches for a Fortran compiler at
        # configure time; without an explicit hint it may not find Spack's FC
        # wrapper.  Passing CMAKE_Fortran_COMPILER directly fixes this for all
        # compilers, including gfortran 10+.
        if "+fortran" in self.spec:
            args.append(self.define("CMAKE_Fortran_COMPILER", self.compiler.fc))

        return args
