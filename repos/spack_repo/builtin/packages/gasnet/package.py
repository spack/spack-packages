# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import warnings

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Gasnet(AutotoolsPackage, CudaPackage, ROCmPackage):
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
    """

    homepage = "https://gasnet.lbl.gov"
    url = "https://gasnet.lbl.gov/EX/GASNet-2024.5.0.tar.gz"
    git = "https://bitbucket.org/berkeleylab/gasnet.git"

    maintainers("PHHargrove", "bonachea", "rbberger")

    tags = ["e4s", "ecp"]

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

    variant("debug", default=False, description="Enable library debugging mode")

    variant("seq", default=True, description="support SEQ-mode single-threaded GASNet clients")
    variant("par", default=False, description="support PAR-mode pthreaded GASNet clients")
    variant("parsync", default=False, description="support PARSYNC-mode pthreaded GASNet clients")

    variant("pshm", default=True, description="Enable/disable inter-process shared memory support")
    variant("pthreads", default=False, description="enable use of pthreads")
    variant(
        "mpi_compat", default=False, description="Enable/disable MPI compatibility in all conduits"
    )

    variant(
        "pmi", default="none", values=("none", "x", "1", "2", "cray"), description="PMI version"
    )
    variant(
        "segment",
        default="off",
        values=("off", "fast", "large", "everything"),
        description="Build GASNet in the FAST/LARGE/EVERYTHING shared segment configuration",
    )

    with when("conduits=ofi"):
        variant(
            "ofi_provider",
            default="auto",
            values=("auto", "cxi"),
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
            values=(str(x) for x in range(9)),
            description="Maximum number of IBV HCAs to open",
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

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
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

    @run_before("configure")
    def bootstrap(self):
        if self.spec.satisfies(self.bootstrap_version):
            bootstrapsh = Executable("./Bootstrap")
            bootstrapsh()
            # Record git-describe when fetched from git:
            try:
                git = which("git")
                git("describe", "--long", "--always", output="version.git")
            except ProcessError:
                warnings.warn("Omitting version stamp due to git error")

    def configure_args(self):
        spec = self.spec
        options = ["--disable-auto-conduit-detect", "--enable-rpath"]
        options += self.enable_or_disable("debug")
        options += self.enable_or_disable("par")
        options += self.enable_or_disable("seq")
        options += self.enable_or_disable("parsync")
        options += self.enable_or_disable("pshm")
        options += self.enable_or_disable("pthreads")
        options += self.enable_or_disable("mpi-compat", variant="mpi_compat")

        if not spec.satisfies("pmi=none"):
            options.append("--enable-pmi")
            options.append(f"--with-pmi-version={spec.variants['pmi'].value}")

            if spec.satisfies("pmi=x"):
                options.append(f"--with-pmi-home={spec['pmix'].prefix}")
            elif spec.satisfies("pmi=cray"):
                options.append(f"--with-pmi-home={spec['cray-pmi'].prefix}")
        else:
            options.append("--disable-pmi")

        if spec.satisfies("+cuda"):
            options.append("--enable-kind-cuda-uva")
            options.append("--with-cuda-home=" + spec["cuda"].prefix)

        if spec.satisfies("+rocm"):
            options.append("--enable-kind-hip")
            options.append("--with-hip-home=" + spec["hip"].prefix)

        if spec.satisfies("+level_zero"):
            options.append("--enable-kind-ze")
            options.append("--with-ze-home=" + spec["oneapi-level-zero"].prefix)

        for c in spec.variants["conduits"].value:
            options.append("--enable-" + c)

        if spec.satisfies("conduits=mpi") or spec.satisfies("+mpi_compat"):
            options.append(f"--with-mpi-cc={spec['mpi'].mpicc}")

        if spec.satisfies("conduits=ibv"):
            options.append(f"--with-ibv-max-hcas={spec.variants['ibv_max_hcas'].value}")

        if spec.satisfies("conduits=ofi"):
            if not spec.satisfies("ofi_provider=auto"):
                options.append(f"--with-ofi-provider={spec.variants['ofi_provider'].value}")
            if not spec.satisfies("ofi_spawner=auto"):
                options.append(f"--with-ofi-spawner={spec.variants['ofi_spawner'].value}")
        return options

    @run_after("build")
    def build_tests(self):
        if not self.spec.satisfies("conduits=none"):
            for c in self.spec.variants["conduits"].value:
                make("-C", c + "-conduit", "testgasnet-par")
                make("-C", c + "-conduit", "testtools-par")

    @run_after("install")
    def install_source(self):
        install_tree(self.stage.source_path, self.prefix + "/src")

    @run_after("install")
    def install_tests(self):
        if not self.spec.satisfies("conduits=none"):
            for c in self.spec.variants["conduits"].value:
                testdir = join_path(self.prefix.tests, c)
                mkdirp(testdir)
                install(c + "-conduit/testgasnet", testdir)
                install(c + "-conduit/testtools", prefix.tests)

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
