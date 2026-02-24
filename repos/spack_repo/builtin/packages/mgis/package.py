# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mgis(CMakePackage):
    """
    The MFrontGenericInterfaceSupport project (MGIS) provides helper
    functions for various solvers to interact with behaviour written
    using MFront generic interface.

    MGIS is written in C++.
    Bindings are provided for C and fortran (2003).
    A FEniCS binding is also available.
    """

    homepage = "https://thelfer.github.io/mgis/web/index.html"
    url = "https://github.com/thelfer/MFrontGenericInterfaceSupport/archive/MFrontGenericInterfaceSupport-1.2.tar.gz"
    git = "https://github.com/thelfer/MFrontGenericInterfaceSupport.git"
    maintainers("thelfer")

    license("LGPL-3.0-only")

    # development branches
    version("master", branch="master")
    version("rliv-3.1", branch="rliv-3.1")
    version("rliv-3.0", branch="rliv-3.0")
    version("rliv-2.2", branch="rliv-2.2")
    version("rliv-2.1", branch="rliv-2.1")
    version("rliv-2.0", branch="rliv-2.0")
    version("rliv-1.2", branch="rliv-1.2")
    version("rliv-1.1", branch="rliv-1.1")
    version("rliv-1.0", branch="rliv-1.0")

    # released version
    version(
        "3.1.0",
        sha256="61afae1a367dbb150b24ca85f042efb15a77184a54a746f11c08d9b7cb9e94f3",
        url="https://github.com/thelfer/MFrontGenericInterfaceSupport/archive/MFrontGenericInterfaceSupport-3.1.tar.gz",
    )
    version("3.0.2", sha256="189b53789d4e2af3a69970880f5b1e90ff596ad3a71109ace69b2026333a8641")
    version("2.2.2", sha256="cd31a51939c5e15c880563ec738cf6801aa9142d5d2783607eb1400e992ef504")
    version("2.1.1", sha256="3fb5500cdb855543403028e28b6418913b3067ab2509d254022a234ea59ed4a8")
    version("2.0.1", sha256="9850aa177d4a6e43faa1434968d2daad65aab2a9b7d64fa4eea51bd25c3d2c5c")
    version("1.2.3", sha256="250bca538ad0806f0d3d3a0ee7410344de2c92f8d038a49f486acb69fa81362d")
    version("1.1.2", sha256="49b6a115f6ca758c1b29aa49e7f9940c36102edc2478c338de5f9fa6a13c0e95")
    version("1.0.1", sha256="6102621455bc5d9b1591cd33e93b2e15a9572d2ce59ca6dfa30ba57ae1265c08")

    with default_args(deprecated=True):

        version("3.0.1", sha256="fb9a7f5008a43c70bdb1c4b80f32f7fd3e4274c912b93c36af7011d3c4f93039")
        version(
            "3.0.0",
            sha256="dae915201fd20848b69745dabda1a334eb242d823af600825b8b010ddc597640",
            url="https://github.com/thelfer/MFrontGenericInterfaceSupport/archive/MFrontGenericInterfaceSupport-3.0.tar.gz",
        )
        version("2.2.1", sha256="a0e6af65f5fd2237f39306354ef786eadb0c6bc6868c23e2681e04a83e629ad2")
        version("2.2.0", sha256="b3776d7b3a534ca626525a42b97665f7660ae2b28ea57b3f53fd7e8538da1ceb")
        version("2.1.0", sha256="f5b556aab130da0c423f395fe4c35d6bf509dd8fc958242f2e37ea788464aea9")
        version(
            "2.0.0",
            sha256="cb427d77f2c79423e969815b948a8b44da33a4370d1760e8c1e22a569f3585e2",
            url="https://github.com/thelfer/MFrontGenericInterfaceSupport/archive/MFrontGenericInterfaceSupport-2.0.tar.gz",
        )
        version("1.2.2", sha256="dc24e85cc90ec656ed707eef3d511317ad800915014d9e4e9cf8818b406586d5")
        version("1.2.1", sha256="a2d7cae3a24546adcf1d1bf7f13f012170d359370f5b6b2c1730b19eb507601d")
        version("1.2.0", sha256="ed82ab91cbe17c00ef36578dbfcb4d1817d4c956619b7cccbea3e3f1a3b31940")
        version("1.1.0", sha256="06593d7a052678deaee87ef60b2213db7545c5be9823f261d3388b3978a0b7a5")
        version(
            "1.0.0",
            sha256="279c98da00fa6855edf29c2b8f8bad6e7732298dc62ef67d028d6bbeaac043b3",
            url="https://github.com/thelfer/MFrontGenericInterfaceSupport/archive/MFrontGenericInterfaceSupport-1.0.tar.gz",
        )

    # variants
    variant("c", default=True, description="Enables c bindings")
    variant("fortran", default=True, description="Enables fortran bindings")
    variant("python", default=True, description="Enables python bindings")
    variant("static", default=False, description="Enables static libraries")

    with when("@3.1:,rliv-3.1"):
        variant("openmp", default=False, description="Enables openmp support")
        variant("mgis-function", default=True, description="Enables MGIS/Function")
        variant(
            "exception",
            default=False,
            description="use exceptions to report contract violation and error reporting",
        )

    with when("@3.1:"):
        depends_on("py-pybind11", when="+python", type=("build", "link", "run"))

    # dependencies
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("tfel@5.1.0", when="@3.1.0")
    depends_on("tfel@5.0.2", when="@3.0.2")
    depends_on("tfel@5.0.1", when="@3.0.1")
    depends_on("tfel@5.0.0", when="@3.0.0")
    depends_on("tfel@4.2.4", when="@2.2.2")
    depends_on("tfel@4.2.3", when="@2.2.1")
    depends_on("tfel@4.2.0", when="@2.2.0")
    depends_on("tfel@4.1.5", when="@2.1.1")
    depends_on("tfel@4.1.0", when="@2.1.0")
    depends_on("tfel@4.0.5", when="@2.0.1")
    depends_on("tfel@4.0.0", when="@2.0.0")
    depends_on("tfel@3.4.9", when="@1.2.3")
    depends_on("tfel@3.4.3", when="@1.2.2")
    depends_on("tfel@3.4.1", when="@1.2.1")
    depends_on("tfel@3.4.0", when="@1.2.0")
    depends_on("tfel@3.3.8", when="@1.1.2")
    depends_on("tfel@3.3.0", when="@1.1.0")
    depends_on("tfel@3.2.1", when="@1.0.1")
    depends_on("tfel@3.2.0", when="@1.0.0")
    depends_on("tfel@rliv-5.1", when="@rliv-3.1")
    depends_on("tfel@rliv-5.0", when="@rliv-3.0")
    depends_on("tfel@rliv-4.2", when="@rliv-2.2")
    depends_on("tfel@rliv-4.1", when="@rliv-2.1")
    depends_on("tfel@rliv-4.0", when="@rliv-2.0")
    depends_on("tfel@rliv-3.4", when="@rliv-1.2")
    depends_on("tfel@rliv-3.3", when="@rliv-1.1")
    depends_on("tfel@rliv-3.2", when="@rliv-1.0")
    depends_on("tfel@master", when="@master")

    depends_on("py-numpy", when="+python", type=("build", "link", "run"))

    with when("@3.1:"):
        depends_on("py-pybind11", when="+python", type=("build", "link", "run"))

    with when("@1.0:3.0.99"):
        depends_on(
            "boost+python+numpy+exception+container", when="+python", type=("build", "link", "run")
        )

    with when("@rliv-1.0:rliv-3.0"):
        depends_on(
            "boost+python+numpy+exception+container", when="+python", type=("build", "link", "run")
        )

    extends("python", when="+python")

    def cmake_args(self):
        args = []

        args.append("-DUSE_EXTERNAL_COMPILER_FLAGS=ON")
        args.append("-Denable-website=OFF")
        args.append("-Denable-doxygen-doc=OFF")
        args.append("-DTFEL_DIR={0}/share/tfel/cmake".format(self.spec["tfel"].prefix))
        args.append("-Denable-parallel-stl-algorithms=OFF")
        args.append(self.define_from_variant("enable-openmp", "openmp"))
        args.append(self.define_from_variant("enable-exception", "exception"))
        args.append(self.define_from_variant("enable-mgis-function", "mgis-function"))

        for i in ["c", "fortran", "python"]:
            args.append(self.define_from_variant(f"enable-{i}-bindings", f"{i}"))

        if "+static" in self.spec:
            args.append("-Denable-static=ON")

        if not self.spec.satisfies("+python"):
            return args

        # adding path to python
        python = self.spec["python"]
        args.append("-DPYTHON_LIBRARY={0}".format(python.libs[0]))
        args.append("-DPYTHON_INCLUDE_DIR={0}".format(python.headers.directories[0]))
        args.append("-DPython_ADDITIONAL_VERSIONS={0}".format(python.version.up_to(2)))

        if "py-pybind11" in self.spec:
            args.append("-Dpybind11_DIR={0}".format(self.spec["py-pybind11"].prefix))

        if "boost" in self.spec:
            # adding path to boost
            args.append("-DBOOST_ROOT={0}".format(self.spec["boost"].prefix))

        return args

    def check(self):
        """skip target 'test' which doesn't build the test programs used by tests"""
        with working_dir(self.build_directory):
            if self.generator == "Unix Makefiles":
                self._if_make_target_execute("check")
            elif self.generator == "Ninja":
                self._if_ninja_target_execute("check")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Requested by some users whose build system do not rely on RPATH
        env.append_path("LD_LIBRARY_PATH", self.prefix.lib)
