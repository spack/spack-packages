# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Sniper(CMakePackage):
    """General-purpose software framework for high-energy physics processing.

    SNiPER provides event-loop control, dynamically loadable algorithms and
    services, Python configuration, and optional ROOT integration. It is used
    by experiments including JUNO, STCF, and HERD.
    """

    homepage = "https://sniper-framework.github.io/"
    url = "https://github.com/SNiPER-Framework/sniper/archive/refs/tags/v2.2.3.tar.gz"

    maintainers("guangzhuangzhao")

    license("LGPL-3.0-or-later", checked_by="guangzhuangzhao")

    version(
        "2.2.3",
        sha256="bd2c9f91dd3b938b5416b91511ef27ae456fe055fb5287b82c13b6cbb90826e1",
    )
    version(
        "2.1",
        sha256="8da2f9d251b19d806b17a7c4b87245f134c27efeb1f28ad374bde850862cd568",
    )

    variant(
        "cxxstd",
        default="17",
        values=("11", "14", "17", "20"),
        multi=False,
        description="C++ language standard",
    )
    variant("python", default=True, description="Enable Python bindings and configuration")
    variant("root", default=True, description="Enable ROOT-dependent components")

    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")
    depends_on("boost@1.67:+python", when="+python", type=("build", "link"))
    depends_on("python@3:", when="+python", type=("build", "link", "run"))

    conflicts("+root cxxstd=11", msg="ROOT requires at least C++14")
    conflicts("+root cxxstd=14", msg="Supported ROOT versions require C++17")
    depends_on("root@5.18: cxxstd=17", when="+root cxxstd=17", type=("build", "link", "run"))
    depends_on(
        "root@6.28.04: cxxstd=20",
        when="+root cxxstd=20",
        type=("build", "link", "run"),
    )

    def cmake_args(self):
        # Upstream installs the example scripts only when BUILD_TESTS is enabled.
        # self.run_tests is true only for a direct `spack install --test=root`.
        args = [
            self.define("BUILD_TESTS", self.run_tests),
            self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value),
            self.define_from_variant("USE_PYTHON", "python"),
            self.define_from_variant("USE_ROOT", "root"),
        ]

        if "+python" in self.spec:
            args.extend(
                [
                    self.define("Python3_EXECUTABLE", self.spec["python"].command.path),
                    self.define("USE_PYTHON2", False),
                ]
            )

        return args

    # The upstream CTest definitions run build-tree binaries without the
    # build-tree library and Python paths. The post-install hook below tests an
    # installed example instead, using the environment provided by `spack load`.
    def check(self):
        pass

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def test_hello_world(self):
        """Run the installed HelloWorld example."""
        run_env = EnvironmentModifications()
        self.setup_run_environment(run_env)

        sniper = Executable(join_path(self.prefix.bin, "sniper.exe"))
        sniper.add_default_envmod(run_env)
        extension = "py" if "+python" in self.spec else "json"
        sniper(join_path(self.prefix.share, "SniperExamples", f"run-HelloWorld.{extension}"))

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.set("SNiPER_DIR", self.prefix)
        env.set("SNIPER_INIT_FILE", join_path(self.prefix.share, "sniper", ".init.json"))
        if "+python" in self.spec:
            env.prepend_path("PYTHONPATH", self.prefix.python)
