# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.python import PythonExtension

from spack.package import *


class KratosMultiphysics(CMakePackage, PythonExtension):
    """KRATOS Multiphysics ("Kratos") is a framework for building parallel,
    multi-disciplinary simulation software, aiming at modularity, extensibility,
    and high performance. Kratos is written in C++ and counts with an extensive
    Python interface."""

    homepage = "https://github.com/KratosMultiphysics/Kratos"
    url = "https://github.com/KratosMultiphysics/Kratos/archive/refs/tags/v10.4.3.tar.gz"
    git = "https://github.com/KratosMultiphysics/Kratos.git"

    maintainers("loumalouomega", "pooyandadvand", "riccardorossi")

    license("BSD-4-Clause", checked_by="loumalouomega")

    version("master", branch="master")
    version("10.4.3", sha256="fd6b1b5495e40540b73b3ef2a44e3d0aade0fc98d3543005b07cd497121c9984")
    version("10.4.2", sha256="b2b8d2f007e6e3f9dbecfb411c13b59e35e269c2a15c64c6c409c984ea555308")
    version("10.4.0", sha256="8af64defa11b71c461141c073b0760a095392f3f0013cd149855f231f5f288b5")
    version("10.3.0", sha256="04a9f9dd64dd1b61c422fea24abcfebeba6da9bea17f7713dd740e281f70ede1")
    version("10.2.3", sha256="8e6ae39d7b3fd8ae02d4a3488d8828ec2104dfad2f7c7539603b51c2f10e6176")
    version("10.1", sha256="0fe6b77b35676578701a67bd07e55d79439a5a3a5615f94e566bab0443b0e733")
    version("10.0", sha256="9f21ea6ad094550687f87fa4e88bc2b2b73142c0ba23e1cab856cc2eaae52094")
    version("9.5", sha256="5b94bc7913dccb1131c2fc51c638dc06ea275f2a43dd466164b554c3d76e3da6")

    # Map from the (snake_case) variant value to the on-disk directory name
    # under `applications/`. Every in-tree application is exposed except
    # KaHIPApplication, which ships without a CMakeLists.txt and cannot be
    # built. Kratos auto-resolves inter-application dependencies at configure
    # time (cmake_modules/KratosDependencies.cmake), so only the user-selected
    # applications need to be listed in KRATOS_APPLICATIONS.
    application_dirs = {
        "cable_net": "CableNetApplication",
        "chimera": "ChimeraApplication",
        "co_simulation": "CoSimulationApplication",
        "compressible_potential_flow": "CompressiblePotentialFlowApplication",
        "constitutive_laws": "ConstitutiveLawsApplication",
        "contact_mechanics": "ContactMechanicsApplication",
        "contact_structural_mechanics": "ContactStructuralMechanicsApplication",
        "convection_diffusion": "ConvectionDiffusionApplication",
        "dam": "DamApplication",
        "delaunay_meshing": "DelaunayMeshingApplication",
        "dem": "DEMApplication",
        "dem_structures_coupling": "DemStructuresCouplingApplication",
        "droplet_dynamics": "DropletDynamicsApplication",
        "fem_to_dem": "FemToDemApplication",
        "fluid_dynamics": "FluidDynamicsApplication",
        "fluid_dynamics_biomedical": "FluidDynamicsBiomedicalApplication",
        "fluid_dynamics_hydraulics": "FluidDynamicsHydraulicsApplication",
        "free_surface": "FreeSurfaceApplication",
        "fsi": "FSIApplication",
        "geo_mechanics": "GeoMechanicsApplication",
        "hdf5": "HDF5Application",
        "iga": "IgaApplication",
        "linear_solvers": "LinearSolversApplication",
        "mapping": "MappingApplication",
        "med": "MedApplication",
        "mesh_moving": "MeshMovingApplication",
        "meshing": "MeshingApplication",
        "metis": "MetisApplication",
        "mpm": "MPMApplication",
        "optimization": "OptimizationApplication",
        "pfem": "PfemApplication",
        "pfem2": "PFEM2Application",
        "pfem_fluid_dynamics": "PfemFluidDynamicsApplication",
        "pfem_solid_mechanics": "PfemSolidMechanicsApplication",
        "poromechanics": "PoromechanicsApplication",
        "rans": "RANSApplication",
        "rom": "RomApplication",
        "shallow_water": "ShallowWaterApplication",
        "shape_optimization": "ShapeOptimizationApplication",
        "solid_mechanics": "SolidMechanicsApplication",
        "statistics": "StatisticsApplication",
        "structural_mechanics": "StructuralMechanicsApplication",
        "swimming_dem": "SwimmingDEMApplication",
        "system_identification": "SystemIdentificationApplication",
        "thermal_dem": "ThermalDEMApplication",
        "topology_optimization": "TopologyOptimizationApplication",
        "trilinos": "TrilinosApplication",
        "wind_engineering": "WindEngineeringApplication",
    }

    # Applications whose (possibly auto-added) DelaunayMeshingApplication
    # dependency hard-fails at configure time unless the non-free Triangle
    # TPL is enabled.
    _triangle_apps = (
        "delaunay_meshing",
        "pfem",
        "pfem_fluid_dynamics",
        "pfem_solid_mechanics",
        "contact_mechanics",
        "fem_to_dem",
        "thermal_dem",
    )

    # Kratos defines its own build-type list (see CMakeLists.txt). Override the
    # CMakePackage default so the custom types are accepted and Release is used.
    variant(
        "build_type",
        default="Release",
        description="CMake build type",
        values=("Release", "RelWithDebInfo", "Debug", "FullDebug", "Custom"),
    )

    variant(
        "applications",
        values=any_combination_of(*sorted(application_dirs)).with_default(
            "linear_solvers,structural_mechanics,fluid_dynamics,iga"
        ),
        description="Kratos applications to compile (any combination)",
    )

    variant("mpi", default=False, description="Build with MPI (distributed memory) support")
    variant(
        "shared_memory",
        default="openmp",
        values=("openmp", "cxx11", "none"),
        multi=False,
        description="Shared-memory parallelization backend",
    )
    variant("mkl", default=False, description="Use Intel MKL solvers in LinearSolversApplication")
    variant(
        "suitesparse",
        default=False,
        description="Use SuiteSparse solvers in LinearSolversApplication",
    )
    variant("mmg", default=False, description="Enable MMG remeshing in MeshingApplication")
    variant("parmmg", default=False, description="Enable ParMMG parallel remeshing (needs +mmg)")
    variant("tbb", default=False, description="Use Intel TBB")
    variant(
        "tetgen",
        default=False,
        description="Enable the non-free TetGen TPL (extra license restrictions)",
    )
    variant(
        "triangle",
        default=False,
        description="Enable the non-free Triangle TPL (extra license restrictions)",
    )
    # TetGen/Triangle licenses restrict redistribution, so binaries built
    # against them must not be pushed to public build caches/mirrors.
    redistribute(binary=False, when="+tetgen")
    redistribute(binary=False, when="+triangle")
    # Both testing and benchmarks FetchContent-download googletest/benchmark at
    # configure time, so +cpp_tests / +benchmark need network access.
    variant("benchmark", default=False, description="Build the C++ (Google) benchmarks")
    variant("cpp_tests", default=False, description="Build the C++ (GTest) unit tests")
    variant("stubs", default=True, description="Generate Python stub (.pyi) files for IDE hinting")
    # Not exposed on purpose: USE_CUDA (only runs find_package(CUDA), no code
    # uses it), KRATOS_NO_TRY_CATCH, KRATOS_ENABLE_PROFILING, KRATOS_USE_PCH
    # and KRATOS_COLORED_OUTPUT (debug/developer/cosmetic switches).

    # The MKL / SuiteSparse solvers live inside LinearSolversApplication.
    requires(
        "applications=linear_solvers",
        when="+mkl",
        msg="+mkl requires the LinearSolversApplication (applications=linear_solvers)",
    )
    requires(
        "applications=linear_solvers",
        when="+suitesparse",
        msg="+suitesparse requires the LinearSolversApplication (applications=linear_solvers)",
    )
    # MMG/ParMMG support is consumed by the MeshingApplication.
    requires(
        "applications=meshing",
        when="+mmg",
        msg="+mmg requires the MeshingApplication (applications=meshing)",
    )
    requires("+mmg", when="+parmmg", msg="+parmmg requires MMG (+mmg)")
    requires("+mpi", when="+parmmg", msg="+parmmg requires MPI (+mpi)")
    # The Trilinos and Metis applications are the MPI-parallel backends.
    requires(
        "+mpi", when="applications=trilinos", msg="The TrilinosApplication requires MPI (+mpi)"
    )
    requires("+mpi", when="applications=metis", msg="The MetisApplication requires MPI (+mpi)")
    # DelaunayMeshingApplication (auto-added by the Pfem family, ContactMechanics,
    # FemToDem and ThermalDEM) fails to configure without the Triangle TPL.
    for _app in _triangle_apps:
        requires(
            "+triangle",
            when=f"applications={_app}",
            msg=f"applications={_app} needs the non-free Triangle TPL (+triangle)",
        )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # CMake floor is 3.15, but Python stub generation needs >= 3.20.
    depends_on("cmake@3.15:", type="build")
    depends_on("cmake@3.20:", type="build", when="+stubs")
    depends_on("ninja", type="build")

    # Python interface (numpy is a hard runtime requirement, see pyproject.toml).
    extends("python")
    depends_on("python@3.8:", type=("build", "link", "run"))
    depends_on("py-numpy@1.20:", type=("build", "run"))

    # Boost is used header-only; >= 1.70 unlocks the ublas move-semantics path.
    depends_on("boost@1.70:")

    # zlib is needed by the bundled gidpost; let Kratos find it in the system.
    depends_on("zlib-api")

    depends_on("mpi", when="+mpi")

    # HDF5Application: the serial/parallel HDF5 flavor must match USE_MPI,
    # a mismatch is a configure-time fatal error in both directions.
    with when("applications=hdf5"):
        depends_on("hdf5@1.8:")
        depends_on("hdf5+mpi", when="+mpi")
        depends_on("hdf5~mpi", when="~mpi")

    # TrilinosApplication needs the Epetra stack (Epetra/Teuchos mandatory;
    # Amesos/AztecOO/Ifpack/ML wanted). Those variants were removed from the
    # trilinos package in v17, hence the version bound.
    depends_on(
        "trilinos@:16 +mpi +amesos +aztec +epetra +epetraext +ifpack +ml",
        when="applications=trilinos",
    )
    depends_on("metis", when="applications=metis")

    # MedApplication (MED file I/O), needs a MED library built on HDF5.
    depends_on("med", when="applications=med")
    depends_on("hdf5", when="applications=med")

    # Optional solver / meshing backends. Kratos globs and installs the MMG
    # shared libraries, so +shared is required.
    depends_on("mmg+shared", when="+mmg")
    depends_on("parmmg", when="+parmmg")
    depends_on("tbb", when="+tbb")
    depends_on("intel-oneapi-mkl", when="+mkl")
    depends_on("suite-sparse", when="+suitesparse")

    # Eigen3, Spectra, pybind11, json, amgcl, nanoflann, triangle, etc. are
    # vendored in the source tree, so they are intentionally *not* declared
    # as dependencies.

    # Kratos needs the TetGen *sources* (USE_TETGEN_NONFREE_TPL_PATH must
    # contain tetgen.h/tetgen.cxx), which the spack tetgen package does not
    # install, so fetch them as a resource instead.
    resource(
        name="tetgen",
        url="http://www.tetgen.org/1.5/src/tetgen1.6.0.tar.gz",
        sha256="87b5e61ebd3a471fc4f2cdd7124c2b11dd6639f4feb1f941a5d2f5110d05ce39",
        when="+tetgen",
        placement="tetgen-src",
    )

    # Compiler floors enforced by the Kratos CMake (C++20).
    conflicts("%gcc@:9", msg="Kratos requires GCC >= 10 for C++20 support")
    conflicts("%clang@:11", msg="Kratos requires Clang >= 12")
    conflicts("%apple-clang@:11", msg="Kratos requires apple-clang >= 12")
    conflicts("%intel@:17", msg="Kratos requires the Intel compiler >= 18")

    def selected_applications(self):
        """Return the list of on-disk application directory names selected via
        the ``applications`` variant (empty entries filtered out)."""
        selected = self.spec.variants["applications"].value
        # Multi-valued variants come back as a tuple; "none"/empty are filtered.
        return [self.application_dirs[key] for key in selected if key in self.application_dirs]

    def setup_build_environment(self, env):
        # Kratos reads the application list and the Python interpreter from the
        # environment at configure time (see the root CMakeLists.txt), mirroring
        # scripts/standard_configure.sh.
        app_paths = [
            join_path(self.stage.source_path, "applications", app_dir)
            for app_dir in self.selected_applications()
        ]
        if app_paths:
            # Trailing ';' matches Kratos' own add_app helper.
            env.set("KRATOS_APPLICATIONS", ";".join(app_paths) + ";")

        env.set("PYTHON_EXECUTABLE", self.spec["python"].command.path)
        env.set("BOOST_ROOT", self.spec["boost"].prefix)

        if self.spec.satisfies("+mkl"):
            # LinearSolversApplication fatal-errors if MKLROOT is unset.
            env.set("MKLROOT", self.spec["intel-oneapi-mkl"].package.component_prefix)

    def cmake_args(self):
        spec = self.spec

        shared_memory = {"openmp": "OpenMP", "cxx11": "C++11", "none": "None"}[
            spec.variants["shared_memory"].value
        ]

        args = [
            self.define_from_variant("USE_MPI", "mpi"),
            self.define_from_variant("USE_EIGEN_MKL", "mkl"),
            self.define_from_variant("USE_EIGEN_SUITESPARSE", "suitesparse"),
            self.define_from_variant("KRATOS_BUILD_TESTING", "cpp_tests"),
            self.define_from_variant("KRATOS_BUILD_BENCHMARK", "benchmark"),
            self.define_from_variant("KRATOS_GENERATE_PYTHON_STUBS", "stubs"),
            self.define_from_variant("KRATOS_USE_TBB", "tbb"),
            self.define("KRATOS_SHARED_MEMORY_PARALLELIZATION", shared_memory),
            # Allow configuring against deprecated minimum CMake policies that
            # some bundled third-party CMake files still rely on (matches
            # scripts/standard_configure.sh).
            self.define("CMAKE_POLICY_VERSION_MINIMUM", "3.5"),
        ]

        # Non-free TPLs (off by default for licensing reasons).
        if spec.satisfies("+triangle"):
            args.append(self.define("USE_TRIANGLE_NONFREE_TPL", True))
        if spec.satisfies("+tetgen"):
            args.append(self.define("USE_TETGEN_NONFREE_TPL", True))
            args.append(
                self.define(
                    "USE_TETGEN_NONFREE_TPL_PATH",
                    join_path(self.stage.source_path, "tetgen-src"),
                )
            )

        # MMG/ParMMG remeshing backends.
        if spec.satisfies("+mmg"):
            args.append(self.define("INCLUDE_MMG", True))
            args.append(self.define("MMG_ROOT", spec["mmg"].prefix))
        if spec.satisfies("+parmmg"):
            args.append(self.define("INCLUDE_PMMG", True))
            args.append(self.define("PMMG_ROOT", spec["parmmg"].prefix))

        # Point the bundled Find modules at the spack prefixes.
        if spec.satisfies("applications=metis"):
            args.append(self.define("METIS_ROOT_DIR", spec["metis"].prefix))
        if spec.satisfies("applications=med"):
            args.append(self.define("MED_ROOT", spec["med"].prefix))

        return args

    # Kratos installs the `KratosMultiphysics` Python package at the prefix
    # root (not in site-packages) and its shared objects under <prefix>/libs.
    import_modules = ["KratosMultiphysics"]

    @run_after("install")
    def check_install(self):
        python = self.spec["python"].command
        python.add_default_env("PYTHONPATH", self.prefix)
        python("-c", "import KratosMultiphysics")

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix)
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "libs"))

    def setup_dependent_run_environment(self, env, dependent_spec):
        env.prepend_path("PYTHONPATH", self.prefix)
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "libs"))
