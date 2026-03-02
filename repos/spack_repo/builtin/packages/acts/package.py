# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


# Submodules are only required for ODD
def submodules(package):
    submodules = []
    if package is None or package.spec.satisfies("+odd"):
        submodules.append("thirdparty/OpenDataDetector")
    return submodules


class Acts(CMakePackage, CudaPackage):
    """
    A Common Tracking Software (Acts)

    This project contains an experiment-independent set of track reconstruction
    tools. The main philosophy is to provide high-level track reconstruction
    modules that can be used for any tracking detector. The description of the
    tracking detector's geometry is optimized for efficient navigation and
    quick extrapolation of tracks. Converters for several common geometry
    description languages exist. Having a highly performant, yet largely
    customizable implementation of track reconstruction algorithms was a
    primary objective for the design of this toolset. Additionally, the
    applicability to real-life HEP experiments plays major role in the
    development process. Apart from algorithmic code, this project also
    provides an event data model for the description of track parameters and
    measurements.

    Key features of this project include: tracking geometry description which
    can be constructed from ROOT, DD4Hep, or GDML input, simple and efficient
    event data model, performant and highly flexible algorithms for track
    propagation and fitting, basic seed finding algorithms.
    """

    homepage = "https://acts.web.cern.ch/ACTS/"
    git = "https://github.com/acts-project/acts.git"
    list_url = "https://github.com/acts-project/acts/releases/"
    maintainers("wdconinc", "stephenswat")

    tags = ["hep"]

    license("MPL-2.0")

    # Supported Acts versions
    version("main", branch="main")
    version("45.3.0", commit="d1323a298569942d98ff46ee413031ebd604290d")
    version("45.2.0", commit="c476557b74ccc8369fe1ef2c1f2e27cca4a356b6")
    version("45.1.1", commit="da50efc7b15cad8fdc5e194719c72d7d8b706823")
    version("45.1.0", commit="061a9d87b0fc07b554ec0b3849e875cf964f8323")
    version("45.0.0", commit="92ab57740f8e875555ea28f542844ac1eb5db65b")
    version("44.4.0", commit="a05c35a14b39a461925d11de12ccd2da5e38b3d1")
    version("44.3.0", commit="d4c630145d5050dd2edc58f1de0c872caff23dd8")
    version("44.2.0", commit="c3d440eb1e441fcd15995b8af87ea1497e0cc126")
    version("44.1.0", commit="9c79dd801e4ab1e2485c3198cc6b987ec1369e5b", submodules=submodules)
    version("44.0.1", commit="404f40aaa6211231b6c6726a364b08134a2e3fa4", submodules=submodules)
    version("44.0.0", commit="d5d65c794d3676034f37d89e555c131b5b7ad807", submodules=submodules)
    # NOTE: Versions between 39.2.0 and 44.0.0 are not available via Spack,
    # as they cannot be built without downloading third-party dependencies
    # from remote, non-Spack sources.
    version("39.2.0", commit="94cf48783efd713f38106b18211d1c59f4e8cdec", submodules=submodules)
    version("39.1.0", commit="09225b0d0bba24d57a696e347e3027b39404bb75", submodules=submodules)
    version("39.0.0", commit="b055202e2fbdd509bc186eb4782714bc46f38f3f", submodules=submodules)
    version("38.2.0", commit="9cb8f4494656553fd9b85955938b79b2fac4c9b0", submodules=submodules)
    version("38.1.0", commit="8a20c88808f10bf4fcdfd7c6e077f23614c3ab90", submodules=submodules)
    version("38.0.0", commit="0a6b5155e29e3b755bf351b8a76067fff9b4214b", submodules=submodules)

    # Variants that affect the core Acts library
    variant(
        "benchmarks", default=False, description="Build the performance benchmarks", when="@0.16:"
    )
    _cxxstd_values = (
        conditional("14", when="@:0.8.1"),
        conditional("17", when="@:35"),
        conditional("20", when="@24:"),
    )
    _cxxstd_common = {
        "values": _cxxstd_values,
        "multi": False,
        "description": "Use the specified C++ standard when building.",
    }
    variant("cxxstd", default="17", when="@:35", **_cxxstd_common)
    variant("cxxstd", default="20", when="@36:", **_cxxstd_common)
    variant("examples", default=False, description="Build the examples", when="@0.23:")
    with when("+examples"):
        requires("+digitization", when="@:16")
        requires("+identification", when="@:34")
        requires("+root")
        requires("+fatras")
        requires("+json")
    variant("integration_tests", default=False, description="Build the integration tests")
    variant("unit_tests", default=False, description="Build the unit tests")
    variant(
        "log_failure_threshold",
        default="MAX",
        description="Log level above which examples should auto-crash",
    )
    _scalar_values = ["float", "double"]
    variant(
        "scalar",
        default="double",
        values=_scalar_values,
        multi=False,
        sticky=True,
        description="Scalar type to use throughout Acts.",
    )

    # Variants that enable / disable Acts plugins
    variant("alignment", default=False, description="Build the alignment package", when="@13:")
    variant(
        "autodiff",
        default=False,
        description="Build the auto-differentiation plugin",
        when="@1.2:32",
    )
    variant("dd4hep", default=False, description="Build the DD4hep plugin", when="+root")
    variant(
        "digitization",
        default=False,
        description="Build the geometric digitization plugin",
        when="@:16",
    )
    variant("edm4hep", default=False, description="Build EDM4hep plugin", when="@25:")
    variant("gnn", default=False, description="Build the GNN plugin", when="@44:")
    variant(
        "fatras",
        default=False,
        description="Build the FAst TRAcking Simulation package",
        when="@0.16:",
    )
    variant("fatras_geant4", default=False, description="Build Geant4 Fatras package")
    variant("geomodel", default=False, description="Build GeoModel plugin", when="@33:")
    variant(
        "identification", default=False, description="Build the Identification plugin", when="@:34"
    )
    variant("json", default=False, description="Build the Json plugin")
    variant("legacy", default=False, description="Build the Legacy package")
    variant("mlpack", default=False, description="Build MLpack plugin", when="@25:31")
    variant("onnx", default=False, description="Build ONNX plugin")
    variant(
        "torch",
        default=False,
        description="Build the torch based parts of the GNN plugin",
        when="@44:",
    )
    requires("+gnn", when="+torch")
    variant("odd", default=False, description="Build the Open Data Detector", when="@19.1:")
    variant("podio", default=False, description="Build Podio plugin", when="@30.3:")
    variant(
        "profilecpu",
        default=False,
        description="Enable CPU profiling using gperftools",
        when="@19.3:",
    )
    variant(
        "profilemem",
        default=False,
        description="Enable memory profiling using gperftools",
        when="@19.3:",
    )
    variant("sycl", default=False, description="Build the SyCL plugin", when="@1:34")

    # The TGeo and ROOT variants are synonyms, and the goal is to slowly phase
    # out the TGeo name. The plan for this is as follow. First, we use both
    # names as synonyms, ensuring that both must be true at the same time. We
    # also enforce that nothing explicitly relies on the TGeo naming anymore,
    # and we use ROOT instead. We then "deprecate" the TGeo naming by
    # eliminating it in ACTS release 45. Finally, we retain the TGeo naming
    # until version 44 of ACTS is removed due to deprecation.
    variant("tgeo", default=False, description="Build the TGeo plugin", when="@:44")
    requires("+identification", when="@:34 +tgeo")
    variant("root", default=False, description="Build the ROOT plugin")
    requires("+identification", when="@:34 +root")
    # Establish a mutual implication between the tgeo and root variants; if
    # one is enabled, so must be the other.
    with when("@:44"):
        conflicts("~root", when="+tgeo")
        conflicts("+root", when="~tgeo")

    variant("traccc", default=False, description="Build the Traccc plugin", when="@35.1:")
    requires("+svg", when="+traccc")
    requires("+json", when="+traccc")

    # Variants that only affect Acts examples for now
    variant(
        "binaries",
        default=False,
        description="Build the examples binaries",
        when="@23:32 +examples",
    )
    variant(
        "edm4hep",
        default=False,
        description="Build the EDM4hep examples",
        when="@19.4.0:24 +examples",
    )
    variant(
        "geant4",
        default=False,
        description="Build the Geant4-based examples",
        when="@0.23: +examples",
    )
    variant(
        "hepmc3",
        default=False,
        description="Build the HepMC3-based examples",
        when="@0.23: +examples",
    )
    variant(
        "pythia8",
        default=False,
        description="Build the Pythia8-based examples",
        when="@0.23: +examples",
    )
    variant(
        "python",
        default=False,
        description="Build python bindings for the examples",
        when="@14: +examples",
    )
    variant("svg", default=False, description="Build ActSVG display plugin", when="@20.1:")
    variant(
        "tbb",
        default=True,
        description="Build the examples with Threading Building Blocks library",
        when="@19.8:19,20.1:37.2 +examples",
    )
    variant("analysis", default=False, description="Build analysis applications in the examples")

    # Build dependencies
    depends_on("c", type="build", when="+dd4hep")  # DD4hep requires C
    depends_on("cxx", type="build")
    depends_on("acts-dd4hep", when="@19 +dd4hep")
    with when("+svg"):
        depends_on("actsvg@0.4.20:", when="@20.1:")
        depends_on("actsvg@0.4.28:", when="@23.2:")
        depends_on("actsvg@0.4.29:", when="@23.4:")
        depends_on("actsvg@0.4.30:", when="@23.5:")
        depends_on("actsvg@0.4.33:", when="@25:27")
        depends_on("actsvg@0.4.35:", when="@28:")
        depends_on("actsvg@0.4.39:", when="@32:")
        depends_on("actsvg@0.4.40:", when="@32.1:")
        depends_on(
            "actsvg@0.4.51:", when="@37:"
        )  # https://github.com/acts-project/actsvg/issues/94
        depends_on("actsvg@0.4.56:", when="@41.1:")
        # TODO: This should be when-constrained when the issue is fixed in ACTS.
        depends_on("actsvg@:0.4.56")
    # The version number of algebra plugins was not correct before v0.28.0.
    depends_on("acts-algebra-plugins @0.28:", when="+traccc")
    depends_on("autodiff @0.6:", when="@17: +autodiff")
    depends_on("autodiff @0.5.11:0.5.99", when="@1.2:16 +autodiff")
    depends_on("boost @1.62:1.69 +program_options +test", when="@:0.10.3")
    depends_on("boost @1.71: +filesystem +program_options +test", when="@0.10.4:")
    depends_on("boost @1.77: +filesystem +program_options +test", when="@42:")
    depends_on("boost @1.78: +filesystem +program_options +test", when="@45:")
    depends_on("cmake @3.14:", type="build")
    depends_on("covfie @0.10:", when="+traccc")
    depends_on("covfie @0.13.0:", when="+traccc @42:")
    depends_on("cuda @12:", when="+traccc")
    depends_on("dd4hep @1.11: +dddetectors +ddrec", when="+dd4hep")
    depends_on("dd4hep @1.21: +dddetectors +ddrec", when="@20: +dd4hep")
    depends_on("dd4hep @1.26: +dddetectors +ddrec", when="@42: +dd4hep")
    depends_on("dd4hep +ddg4", when="+dd4hep +geant4 +examples")
    depends_on("detray @0.72.1:", when="+traccc")
    depends_on("detray @0.75.3:", when="@37: +traccc")
    depends_on("detray @0.101.0:", when="@42.1: +traccc")
    depends_on("edm4hep @0.4.1:", when="+edm4hep")
    depends_on("edm4hep @0.7:", when="@25: +edm4hep")
    depends_on("edm4hep @0.10.5:", when="@42: +edm4hep")
    depends_on("edm4hep @:0", when="@:44 +edm4hep")
    depends_on("eigen @3.3.7:3", when="@15.1:")
    depends_on("eigen @3.3.7:3.3", when="@:15.0")
    depends_on("eigen @3.4:3", when="@36.1:")
    depends_on("geant4", when="+fatras_geant4")
    depends_on("geant4", when="+geant4")
    depends_on("geomodel +geomodelg4", when="+geomodel")
    depends_on("geomodel @4.6.0:", when="+geomodel")
    depends_on("geomodel @6.3.0:", when="+geomodel @36.1:")
    depends_on("geomodel @6.8.0:", when="+geomodel @43.1:")
    depends_on("git-lfs", when="@12.0.0:")
    depends_on("gperftools", when="+profilecpu")
    depends_on("gperftools", when="+profilemem")
    depends_on("hepmc3 @3.2.1:", when="+hepmc3")
    depends_on("hepmc3 @3.2.4:", when="@42: +hepmc3")
    depends_on("heppdt", when="+hepmc3 @:4.0")
    depends_on("intel-tbb @2020.1:", when="+examples +tbb")
    depends_on("intel-tbb @2020.1:", when="+examples @37.3:")
    depends_on("mlpack@3.1.1:", when="+mlpack")
    depends_on("nlohmann-json @3.9.1:", when="@0.14: +json")
    depends_on("nlohmann-json @3.10.5:", when="@37: +json")
    depends_on("nlohmann-json @3.11.3:", when="@45: +json")
    depends_on("torch-scatter", when="+gnn")
    depends_on("torch-scatter +cuda", when="+cuda")
    depends_on("podio @0.6:", when="@25: +edm4hep")
    depends_on("podio @0.16:", when="@30.3: +edm4hep")
    depends_on("podio @:0", when="@:35 +edm4hep")
    depends_on("podio @:1.4", when="@:44.1 +edm4hep +examples")
    depends_on("podio @0.16:", when="+podio")
    depends_on("podio @:0", when="@:35 +podio")
    # TODO: Clarify version on next release
    depends_on("podio @:1.4.1", when="@:44.1.0")
    depends_on("pythia8", when="+pythia8")
    depends_on("python", when="+python")
    depends_on("python@3.8:", when="+python @19.11:19")
    depends_on("python@3.8:", when="+python @21:")
    # NOTE: Python and many of the Python packages we depend on are build
    # dependencies only, but marking them as such allows Spack to pick up
    # different Python versions for e.g. the ACTS build and the numpy
    # installation which, in turn, causes the ACTS build to fail. Until a more
    # robust solution is available we pretend that these packages are also
    # run- and link-time dependencies.
    depends_on("python@3.12:", when="@44:")
    depends_on("py-numpy @2.2", when="@44:")
    depends_on("py-onnxruntime@:1.12", when="+onnx @:23.2")
    depends_on("py-onnxruntime@1.12:", when="+onnx @23.3:")
    depends_on("py-particle @0.24", when="@44:")
    depends_on("py-pybind11 @2.6.2:", when="+python @18:")
    depends_on("py-pybind11 @2.13.1:", when="+python @36:")
    depends_on("py-pybind11 @3.0.1:", when="+python @45.3:")
    depends_on("py-pytest", when="+python +unit_tests")
    depends_on("py-setuptools", when="@44:44.1.0")
    depends_on("py-sympy @1.13", when="@44:")
    # TODO: Clarify version on next release
    depends_on("py-hatchling", when="@44.1.1:")
    depends_on("py-torch", when="+gnn +torch")

    with when("+root"):
        depends_on("root @6.10:")
        depends_on("root @6.20:", when="@0.8.1:")
        depends_on("root @6.28:", when="@42:")

    depends_on("sycl", when="+sycl")
    depends_on("vecmem@0.4: +sycl", when="+sycl")
    depends_on("vecmem@1.17.0:", when="@42: +traccc")

    # ACTS imposes requirements on the C++ standard values used by ROOT
    for _cxxstd in _cxxstd_values:
        for _v in _cxxstd:
            depends_on(f"geant4 cxxstd={_v.value}", when=f"cxxstd={_v.value} +geant4")
            depends_on(f"geant4 cxxstd={_v.value}", when=f"cxxstd={_v.value} +fatras_geant4")
            depends_on(f"root cxxstd={_v.value}", when=f"cxxstd={_v.value} +root")

    # When the traccc plugin is enabled, detray should match the Acts scalars
    with when("+traccc"):
        for _scalar in _scalar_values:
            depends_on(f"detray scalar={_scalar}", when=f"scalar={_scalar}")

    # ACTS has been using C++17 for a while, which precludes use of old GCC
    conflicts("%gcc@:7", when="@0.23:")
    # When using C++20, disable gcc 9 and lower.
    conflicts("%gcc@:9", when="cxxstd=20")
    # See https://github.com/acts-project/acts/pull/3362
    conflicts("^geant4@11.3:", when="@:35")
    # See https://github.com/acts-project/acts/pull/3512
    conflicts("^boost@1.85.0")
    # See https://github.com/acts-project/acts/pull/3921
    conflicts("^edm4hep@0.99:", when="@:37")
    # See https://github.com/acts-project/acts/pull/4631
    conflicts("+gnn ~cuda", when="@:44.0")

    # The ODD package is fetched via the internet by the build system, which
    # cannot be disabled.
    conflicts("+odd", when="@44.2.0:")

    def cmake_args(self):
        spec = self.spec

        def cmake_variant(cmake_label, spack_variant):
            enabled = spec.satisfies("+" + spack_variant)
            return f"-DACTS_BUILD_{cmake_label}={enabled}"

        def enable_cmake_variant(cmake_label, spack_variant):
            enabled = spec.satisfies(spack_variant)
            return f"-DACTS_ENABLE_{cmake_label}={enabled}"

        def example_cmake_variant(cmake_label, spack_variant, type="BUILD"):
            enabled = spec.satisfies("+examples +" + spack_variant)
            return f"-DACTS_{type}_EXAMPLES_{cmake_label}={enabled}"

        def plugin_label(plugin_name):
            if spec.satisfies("@0.33:"):
                return "PLUGIN_" + plugin_name
            else:
                return plugin_name + "_PLUGIN"

        def plugin_cmake_variant(plugin_name, spack_variant):
            return cmake_variant(plugin_label(plugin_name), spack_variant)

        integration_tests_label = "INTEGRATIONTESTS"
        unit_tests_label = "UNITTESTS"
        legacy_plugin_label = "LEGACY_PLUGIN"
        if spec.satisfies("@:0.15"):
            integration_tests_label = "INTEGRATION_TESTS"
            unit_tests_label = "TESTS"
        if spec.satisfies("@:0.32"):
            legacy_plugin_label = "LEGACY"

        args = [
            cmake_variant("ALIGNMENT", "alignment"),
            cmake_variant("ANALYSIS_APPS", "analysis"),
            plugin_cmake_variant("AUTODIFF", "autodiff"),
            cmake_variant("BENCHMARKS", "benchmarks"),
            example_cmake_variant("BINARIES", "binaries"),
            plugin_cmake_variant("CUDA", "cuda"),
            plugin_cmake_variant("DD4HEP", "dd4hep"),
            example_cmake_variant("DD4HEP", "dd4hep"),
            plugin_cmake_variant("DIGITIZATION", "digitization"),
            plugin_cmake_variant("EDM4HEP", "edm4hep"),
            example_cmake_variant("EDM4HEP", "edm4hep"),
            cmake_variant("EXAMPLES", "examples"),
            cmake_variant("FATRAS", "fatras"),
            cmake_variant("FATRAS_GEANT4", "fatras_geant4"),
            example_cmake_variant("GEANT4", "geant4"),
            plugin_cmake_variant("GEANT4", "geant4"),
            plugin_cmake_variant("GEOMODEL", "geomodel"),
            plugin_cmake_variant("GNN", "gnn"),
            example_cmake_variant("HEPMC3", "hepmc3"),
            plugin_cmake_variant("IDENTIFICATION", "identification"),
            cmake_variant(integration_tests_label, "integration_tests"),
            plugin_cmake_variant("JSON", "json"),
            cmake_variant(legacy_plugin_label, "legacy"),
            plugin_cmake_variant("MLPACK", "mlpack"),
            cmake_variant("ODD", "odd"),
            plugin_cmake_variant("ONNX", "onnx"),
            enable_cmake_variant("CPU_PROFILING", "profilecpu"),
            enable_cmake_variant("MEMORY_PROFILING", "profilemem"),
            plugin_cmake_variant("PODIO", "podio"),
            example_cmake_variant("PYTHIA8", "pythia8"),
            example_cmake_variant("PYTHON_BINDINGS", "python"),
            self.define_from_variant("ACTS_CUSTOM_SCALARTYPE", "scalar"),
            plugin_cmake_variant("ACTSVG", "svg"),
            plugin_cmake_variant("SYCL", "sycl"),
            plugin_cmake_variant("TGEO", "root"),
            example_cmake_variant("TBB", "tbb", "USE"),
            plugin_cmake_variant("TRACCC", "traccc"),
            cmake_variant(unit_tests_label, "unit_tests"),
        ]

        log_failure_threshold = spec.variants["log_failure_threshold"].value
        args.append(f"-DACTS_LOG_FAILURE_THRESHOLD={log_failure_threshold}")
        if spec.satisfies("@19.4.0:"):
            args.append("-DACTS_ENABLE_LOG_FAILURE_THRESHOLD=ON")

        # Use dependencies provided by spack
        if spec.satisfies("@20.3:"):
            args.append("-DACTS_USE_SYSTEM_LIBS=ON")
            if spec.satisfies("@35.1:36.0"):
                args.append("-DACTS_USE_SYSTEM_DFELIBS=OFF")
        else:
            if spec.satisfies("+autodiff"):
                args.append("-DACTS_USE_SYSTEM_AUTODIFF=ON")

            if spec.satisfies("@19:20.2 +dd4hep"):
                args.append("-DACTS_USE_SYSTEM_ACTSDD4HEP=ON")

            if spec.satisfies("@0.33: +json"):
                args.append("-DACTS_USE_SYSTEM_NLOHMANN_JSON=ON")
            elif spec.satisfies("@0.14.0:0.32 +json"):
                args.append("-DACTS_USE_BUNDLED_NLOHMANN_JSON=OFF")

            if spec.satisfies("@18: +python"):
                args.append("-DACTS_USE_SYSTEM_PYBIND11=ON")

            if spec.satisfies("@20.1: +svg"):
                args.append("-DACTS_USE_SYSTEM_ACTSVG=ON")

            if spec.satisfies("@14: +vecmem"):
                args.append("-DACTS_USE_SYSTEM_VECMEM=ON")

        if spec.satisfies("+cuda"):
            cuda_arch = spec.variants["cuda_arch"].value
            if cuda_arch != "none":
                args.append(f"-DCUDA_FLAGS=-arch=sm_{cuda_arch[0]}")
                arch_str = ";".join(self.spec.variants["cuda_arch"].value)
                args.append(self.define("CMAKE_CUDA_ARCHITECTURES", arch_str))

        if spec.satisfies("+gnn"):
            args.append(self.define("ACTS_GNN_ENABLE_ONNX", self.spec.satisfies("+onnx")))
            args.append(self.define("ACTS_GNN_ENABLE_TORCH", self.spec.satisfies("+torch")))

        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))

        return args
