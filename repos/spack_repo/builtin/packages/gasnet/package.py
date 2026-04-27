# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re
import warnings
from pathlib import Path

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Gasnet(Package, CudaPackage, ROCmPackage):
    """GASNet is a language-independent, networking middleware layer that
    provides network-independent, high-performance communication primitives
    including Remote Memory Access (RMA) and Active Messages (AM). It has been
    used to implement parallel programming models and libraries including UPC,
    UPC++, multi-image Fortran, Legion, Chapel, and many others. The interface is
    primarily intended as a compilation target and for use by runtime library
    writers (as opposed to end users), and the primary goals are high
    performance, interface portability, and expressiveness.

    ***NOTICE***: The Spack built version of GASNet is generally considered
    UNSUITABLE FOR PRODUCTION USE by its authors.  The RECOMMENDED way to build
    GASNet is as an embedded library as configured by the higher-level client
    runtime package (UPC++, Chapel, etc), including system-specific configuration.

    Despite this recommendation, this Spack package is a best effort to allow
    supporting a range of platforms. For optimal performance and more
    fine-grained control on a particular target platform, HPC admins can provide an
    external build.

    Note on variant defaults:
    Many variants default to "auto" to respect GASNet's carefully tuned
    configure-time auto-detection. The configure script's defaults were
    chosen over time to balance the needs of multiple clients and target
    systems. Explicit variant settings override this auto-detection.
    """

    homepage = "https://gasnet.lbl.gov"
    url = "https://gasnet.lbl.gov/EX/GASNet-2024.5.0.tar.gz"
    git = "https://bitbucket.org/berkeleylab/gasnet.git"

    license("BSD-3-Clause-LBNL")

    maintainers("PHHargrove", "bonachea", "rbberger")

    tags = ["e4s", "ecp"]
    executables = ["^gasnet_trace$"]

    version("develop", branch="develop")
    version("main", branch="stable")
    version("master", branch="master")

    # commit hash e2fdec corresponds to tag gex-2025.2.0-snapshot
    version("2025.2.0-snapshot", commit="e2fdece76d86d7b4fa090fbff9b46eb98ce97177")

    # Versions fetched from git require a Bootstrap step
    bootstrap_version = "@master:,2025.2.0-snapshot"

    version("2025.8.0", sha256="bd5919099477d1d2f59c247d006e9d1ac017c9190c974f5e069667418e5bf48d")
    version("2024.5.0", sha256="f945e80f71d340664766b66290496d230e021df5e5cd88f404d101258446daa9")
    version("2023.9.0", sha256="2d9f15a794e10683579ce494cd458b0dd97e2d3327c4d17e1fea79bd95576ce6")
    version(
        "2023.3.0",
        deprecated=True,
        sha256="e1fa783d38a503cf2efa7662be591ca5c2bb98d19ac72a9bc6da457329a9a14f",
    )
    # Do NOT add older versions here.
    # GASNet-EX releases over 2 years old are not supported.

    # The optional network backends:
    variant(
        "conduits",
        values=any_combination_of("smp", "mpi", "ibv", "udp", "ofi", "ucx").with_default("smp"),
        description="The hardware-dependent network backends to enable.\n"
        + "(smp) = SMP conduit for single-node operation\n"
        + "(ibv) = Native InfiniBand verbs conduit\n"
        + "(ofi) = OFI conduit over libfabric, for HPE Cray Slingshot and Intel Omni-Path\n"
        + "(udp) = Portable UDP conduit, for Ethernet networks\n"
        + "(mpi) = Low-performance/portable MPI conduit\n"
        + "(ucx) = EXPERIMENTAL UCX conduit for Mellanox IB/RoCE ConnectX-5+\n"
        + "For detailed recommendations, consult https://gasnet.lbl.gov",
    )

    # ============================================================
    # Threading support variants
    # ============================================================

    variant(
        "pthreads",
        default="auto",
        values=("auto", "on", "off"),
        description="Enable use of pthreads (required for PAR/PARSYNC modes)",
    )

    variant(
        "threadmode",
        default="auto",
        values=("auto", "seq", "par", "parsync"),
        description="support threaded GASNet clients",
        multi=True,
    )
    conflicts("threadmode=auto", when="threadmode=seq")
    conflicts("threadmode=auto", when="threadmode=par")
    conflicts("threadmode=auto", when="threadmode=parsync")

    # ============================================================
    # Memory and system variants
    # ============================================================

    variant(
        "pshm",
        default="auto",
        values=("auto", "on", "off"),
        description="Enable/disable inter-process shared memory support",
    )

    variant(
        "pmi",
        default="auto",
        values=("auto", "none", "x", "1", "2", "cray"),
        description="PMI version (auto-detected when needed by conduit)",
    )

    variant("debug", default=False, description="Enable library debugging mode")
    variant(
        "mpi_compat", default=False, description="Enable/disable MPI compatibility in all conduits"
    )
    variant(
        "segment",
        default="fast",
        values=("fast", "large", "everything"),
        description="Build GASNet in the FAST/LARGE/EVERYTHING shared segment configuration",
    )

    with when("conduits=ofi"):
        variant(
            "ofi_provider",
            default="auto",
            values=("auto", "generic", "cxi", "psm2", "verbs", "gni", "efa", "sockets", "udp"),
            description="Statically configure ofi-conduit for the given provider",
        )
        variant(
            "ofi_spawner",
            default="auto",
            values=("auto", "ssh", "mpi", "pmi"),
            description="ofi job spawner",
        )

    with when("conduits=ibv"):
        variant(
            "ibv_max_hcas",
            default="1",
            values=lambda x: x.isdigit() and int(x) > 0,
            description="Maximum number of IBV HCAs to open",
        )
        variant(
            "ibv_spawner",
            default="auto",
            values=("auto", "ssh", "mpi", "pmi"),
            description="ibv job spawner",
        )

    with when("conduits=ucx"):
        variant(
            "ucx_spawner",
            default="auto",
            values=("auto", "ssh", "mpi", "pmi"),
            description="ucx job spawner",
        )

    variant(
        "cuda",
        default=False,
        description="Enables support for the CUDA memory kind in some conduits.\n"
        + "NOTE: Requires CUDA Driver library be present on the build system",
    )

    variant(
        "rocm",
        default=False,
        description="Enables support for the ROCm/HIP memory kind in some conduits",
    )

    variant(
        "level_zero",
        default=False,
        description="Enables *experimental* support for the Level Zero "
        + "memory kind on Intel GPUs in some conduits",
        when="@2023.9.0:",
    )

    variant(
        "pic", default=False, description="Produce position-independent code (for shared libs)"
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")

    depends_on("mpi", when="+mpi_compat")
    depends_on("mpi", when="conduits=mpi")

    depends_on("libfabric", when="conduits=ofi")

    depends_on("pmix", when="pmi=x")
    depends_on("cray-pmi", when="pmi=cray")

    depends_on("autoconf@2.69", type="build", when=bootstrap_version)
    depends_on("automake@1.16:", type="build", when=bootstrap_version)

    conflicts("^hip@:4.4.0", when="+rocm")

    conflicts("^hip@6:", when="@:2024.4+rocm")  # Bug 4686

    depends_on("oneapi-level-zero@1.8.0:", when="+level_zero")

    # ============================================================
    # Conflicts
    # ============================================================

    conflicts("threadmode=par", when="pthreads=off", msg="PAR mode requires pthreads")
    conflicts("threadmode=parsync", when="pthreads=off", msg="PARSYNC mode requires pthreads")
    conflicts(
        "pshm=on", when="segment=everything", msg="PSHM not compatible with SEGMENT_EVERYTHING"
    )
    conflicts(
        "conduits=ucx",
        when="segment=everything",
        msg="UCX conduit not compatible with SEGMENT_EVERYTHING",
    )

    def enable_or_disable(self, option_name, value):
        if value:
            return [f"--enable-{option_name}"]
        return [f"--disable-{option_name}"]

    def enable_disable_or_auto(self, option_name, variant_name=None):
        """Helper for variants with 'auto', 'on', 'off' values.

        Returns configure flags for the given option.
        'auto' returns [], 'on' returns ['--enable-{option_name}'],
        'off' returns ['--disable-{option_name}'].

        Args:
            option_name: The configure option name (e.g., 'pthreads')
            variant_name: The variant name (e.g., 'pthreads'). If None, uses option_name.
        """
        if variant_name is None:
            variant_name = option_name

        value = self.spec.variants[variant_name].value

        if value == "on":
            return [f"--enable-{option_name}"]
        elif value == "off":
            return [f"--disable-{option_name}"]
        return []  # auto

    def install(self, spec, prefix):
        if spec.satisfies(self.bootstrap_version):
            bootstrapsh = Executable("./Bootstrap")
            bootstrapsh()
            # Record git-describe when fetched from git:
            try:
                git = which("git", required=True)
                git("describe", "--long", "--always", output="version.git")
            except ProcessError:
                warnings.warn("Omitting version stamp due to git error")

        # The GASNet-EX library has a highly multi-dimensional configure space,
        # to accomodate the varying behavioral requirements of each client runtime.
        # The library's ABI/link compatibility is strongly dependent on these
        # client-specific build-time settings, and that variability is deliberately NOT
        # encoded in the variants of this package. The recommended way to build/deploy
        # GASNet is as an EMBEDDED library within the build of the client package
        # (eg. Berkeley UPC, UPC++, Legion, etc), some of which provide build-time
        # selection of the GASNet library sources. This spack package provides
        # the GASNet-EX sources, for use by appropriate client packages.
        install_tree(self.stage.source_path, prefix + "/src")

        if not spec.satisfies("conduits=none"):
            options = [f"--prefix={prefix}", "--disable-auto-conduit-detect", "--enable-rpath"]

            flags = {"cflags": [], "cxxflags": [], "mpi-cflags": []}

            if spec.satisfies("+pic"):
                flags["cflags"].append(self.compiler.cc_pic_flag)
                flags["mpi-cflags"].append(self.compiler.cc_pic_flag)
                flags["cxxflags"].append(self.compiler.cxx_pic_flag)

            for key, value in sorted(flags.items()):
                if value:
                    options.append(f"--with-{key}={' '.join(value)}")

            options += self.enable_or_disable("debug", spec.satisfies("+debug"))
            if not spec.satisfies("threadmode=auto"):
                options += self.enable_or_disable("seq", spec.satisfies("threadmode=seq"))
                options += self.enable_or_disable("par", spec.satisfies("threadmode=par"))
                options += self.enable_or_disable("parsync", spec.satisfies("threadmode=parsync"))
            options += self.enable_or_disable("mpi-compat", spec.satisfies("+mpi_compat"))

            options += self.enable_disable_or_auto("pthreads")
            options += self.enable_disable_or_auto("pshm")

            # PMI
            pmi_val = spec.variants["pmi"].value
            if pmi_val == "none":
                options.append("--disable-pmi")
            elif pmi_val != "auto":
                options.append("--enable-pmi")
                options.append(f"--with-pmi-version={pmi_val}")
                if pmi_val == "x":
                    options.append(f"--with-pmi-home={spec['pmix'].prefix}")
                elif pmi_val == "cray":
                    options.append(f"--with-pmi-home={spec['cray-pmi'].prefix}")
            # else: "auto" - let configure and conduits auto-detect PMI needs

            # ============================================================
            # Segment configuration
            # ============================================================

            options.append(f"--enable-segment-{spec.variants['segment'].value}")

            # ============================================================
            # GPU support (CUDA, ROCm, Level Zero)
            # ============================================================

            if spec.satisfies("+cuda"):
                options.append("--enable-kind-cuda-uva")
                options.append("--with-cuda-home=" + spec["cuda"].prefix)

            if spec.satisfies("+rocm"):
                options.append("--enable-kind-hip")
                options.append("--with-hip-home=" + spec["hip"].prefix)

            if spec.satisfies("+level_zero"):
                options.append("--enable-kind-ze")
                options.append("--with-ze-home=" + spec["oneapi-level-zero"].prefix)

            # ============================================================
            # Conduits
            # ============================================================

            for c in spec.variants["conduits"].value:
                options.append(f"--enable-{c}")

            if spec.satisfies("conduits=mpi") or spec.satisfies("+mpi_compat"):
                options.append(f"--with-mpi-cc={spec['mpi'].mpicc}")

            if spec.satisfies("conduits=ibv"):
                options.append(f"--with-ibv-max-hcas={spec.variants['ibv_max_hcas'].value}")
                if not spec.satisfies("ibv_spawner=auto"):
                    options.append(f"--with-ibv-spawner={spec.variants['ibv_spawner'].value}")

            if spec.satisfies("conduits=ofi"):
                if not spec.satisfies("ofi_provider=auto"):
                    options.append(f"--with-ofi-provider={spec.variants['ofi_provider'].value}")
                if not spec.satisfies("ofi_spawner=auto"):
                    options.append(f"--with-ofi-spawner={spec.variants['ofi_spawner'].value}")

            if spec.satisfies("conduits=ucx"):
                if not spec.satisfies("ucx_spawner=auto"):
                    options.append(f"--with-ucx-spawner={spec.variants['ucx_spawner'].value}")

            configure(*options)
            make()
            make("install")

            for c in spec.variants["conduits"].value:
                testdir = join_path(self.prefix.tests, c)
                mkdirp(testdir)
                make("-C", f"{c}-conduit", "testgasnet")
                make("-C", f"{c}-conduit", "testtools")
                install(f"{c}-conduit/testgasnet", testdir)
                install(f"{c}-conduit/testtools", prefix.tests)

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):
        if self.spec.satisfies("conduits=smp"):
            make("-C", "smp-conduit", "run-tests")
        self.test_testtools()

    def _setup_test_env(self):
        """Set up key stand-alone test environment variables."""
        os.environ["GASNET_VERBOSEENV"] = "1"  # include diagnostic info

        # The following are not technically relevant to test_testtools
        os.environ["GASNET_SPAWN_VERBOSE"] = "1"  # include spawning diagnostics
        if "GASNET_SSH_SERVERS" not in os.environ:
            os.environ["GASNET_SSH_SERVERS"] = "localhost " * 4

    def test_testtools(self):
        """run testtools and check output"""
        if self.spec.satisfies("conduits=none"):
            raise SkipTest("Test requires conduit libraries")

        testtools_path = join_path(self.prefix.tests, "testtools")
        assert os.path.exists(testtools_path), "Test requires testtools"

        self._setup_test_env()
        testtools = which(testtools_path, required=True)
        out = testtools(output=str.split, error=str.split)
        assert "Done." in out

    def test_testgasnet(self):
        """run testgasnet and check output"""
        if self.spec.satisfies("conduits=none"):
            raise SkipTest("Test requires conduit libraries")

        self._setup_test_env()
        ranks = "4"
        spawner = {
            "smp": ["env", "GASNET_PSHM_NODES=" + ranks],
            "mpi": [join_path(self.prefix.bin, "gasnetrun_mpi"), "-n", ranks],
            "ibv": [join_path(self.prefix.bin, "gasnetrun_ibv"), "-n", ranks],
            "ofi": [join_path(self.prefix.bin, "gasnetrun_ofi"), "-n", ranks],
            "ucx": [join_path(self.prefix.bin, "gasnetrun_ucx"), "-n", ranks],
            "udp": [join_path(self.prefix.bin, "amudprun"), "-spawn", "L", "-np", ranks],
        }

        expected = "done."
        for c in self.spec.variants["conduits"].value:
            os.environ["GASNET_SUPERNODE_MAXSIZE"] = "0" if (c == "smp") else "1"
            test = join_path(self.prefix.tests, c, "testgasnet")

            with test_part(
                self,
                "test_testgasnet_{0}".format(c),
                purpose="run {0}-conduit/testgasnet".format(c),
            ):
                exe = which(spawner[c][0], required=True)

                args = spawner[c][1:] + [test]
                out = exe(*args, output=str.split, error=str.split)
                assert expected in out

    @classmethod
    def determine_version(cls, exe):
        prefix = Path(exe).parent.parent
        config = prefix / "include" / "gasnet_config.h"
        if config.exists():
            with open(config, "r") as f:
                for line in f:
                    if line.startswith("#define GASNETI_RELEASE_VERSION"):
                        return line.split()[2]
        return None

    @classmethod
    def determine_variants(cls, exes, version):
        results = []
        for exe in exes:
            variants = []
            prefix = Path(exe).parent.parent
            config = prefix / "include" / "gasnet_config.h"
            lib_dir = prefix / "lib"

            if config.exists():
                flags = {"threadmode": set()}
                conduits = []

                with open(config, "r") as f:
                    for line in f:
                        if line.startswith("#define GASNETI_CONDUITS"):
                            m = re.search(r'"([^"]*)"', line)
                            conduits = m.group(1).split() if m else []
                            variants.append(f"conduits={','.join(conduits)}")
                        elif line.startswith("#define GASNET_SEGMENT_FAST 1"):
                            variants.append("segment=fast")
                        elif line.startswith("#define GASNET_SEGMENT_LARGE 1"):
                            variants.append("segment=large")
                        elif line.startswith("#define GASNET_SEGMENT_EVERYTHING 1"):
                            variants.append("segment=everything")
                        elif line.startswith("#define GASNETI_MK_CLASS_CUDA_UVA_ENABLED 1"):
                            flags["cuda"] = True
                        elif line.startswith("#define GASNETI_MK_CLASS_HIP_ENABLED 1"):
                            flags["rocm"] = True
                        elif line.startswith("#define GASNETI_MK_CLASS_ZE_ENABLED 1"):
                            flags["level_zero"] = True
                        elif line.startswith("#define GASNETI_PSHM_ENABLED 1"):
                            flags["pshm"] = True
                        elif line.startswith("#define HAVE_PTHREAD_H 1"):
                            flags["pthreads"] = True
                        elif line.startswith("#define GASNET_DEBUG 1"):
                            flags["debug"] = True

                # Detect threading modes by checking for library files
                # Check any conduit (use first one found) for mode-specific libraries
                if lib_dir.exists() and conduits:
                    for conduit in conduits:
                        if (lib_dir / f"libgasnet-{conduit}-seq.a").exists():
                            flags["threadmode"].add("seq")
                        if (lib_dir / f"libgasnet-{conduit}-par.a").exists():
                            flags["threadmode"].add("par")
                        if (lib_dir / f"libgasnet-{conduit}-parsync.a").exists():
                            flags["threadmode"].add("parsync")

                # Add auto/on/off variants
                variants.append("pshm=on" if flags.get("pshm") else "pshm=off")
                variants.append("pthreads=on" if flags.get("pthreads") else "pthreads=off")
                variants.append(f"threadmode={','.join(flags['threadmode'])}")

                # Add boolean variants
                variants.append("+debug" if flags.get("debug") else "~debug")
                variants.append("+cuda" if flags.get("cuda") else "~cuda")
                variants.append("+rocm" if flags.get("rocm") else "~rocm")
                variants.append("+level_zero" if flags.get("level_zero") else "~level_zero")

            results.append(" ".join(variants))
        return results
