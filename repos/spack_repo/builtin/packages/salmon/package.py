# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Salmon(CMakePackage):
    """Salmon is a tool for quantifying the expression of transcripts using
    RNA-seq data."""

    homepage = "https://combine-lab.github.io/salmon/"
    url = "https://github.com/COMBINE-lab/salmon/archive/v0.8.2.tar.gz"
    maintainers("snehring")

    license("GPL-3.0-only")

    version("1.11.4", sha256="9410904fa787f1f9aca635626fcdca08f3af9b02f820963f9439e80fb56d23b8")
    version("1.10.3", sha256="a053fba63598efc4ade3684aa2c8e8e2294186927d4fcdf1041c36edc2aa0871")
    version("1.10.2", sha256="976989182160fef3afb4429ee8b85d8dd39ed6ca212bb14d6a65cde0e985fb98")
    version("1.9.0", sha256="450d953a5c43fe63fd745733f478d3fbaf24d926cb52731fd38ee21c4990d613")
    version("1.4.0", sha256="6d3e25387450710f0aa779a1e9aaa9b4dec842324ff8551d66962d7c7606e71d")
    version("0.14.1", sha256="05289170e69b5f291a8403b40d6b9bff54cc38825e9f721c210192b51a19273e")
    version("0.12.0", sha256="91ebd1efc5b0b4c12ec6babecf3c0b79f7102e42b8895ca07c8c8fea869fefa3")
    version("0.9.1", sha256="3a32c28d217f8f0af411c77c04144b1fa4e6fd3c2f676661cc875123e4f53520")
    version("0.8.2", sha256="299168e873e71e9b07d63a84ae0b0c41b0876d1ad1d434b326a5be2dce7c4b91")

    variant(
        "build_type",
        default="RELEASE",
        description="CMake build type",
        values=("DEBUG", "RELEASE"),
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # 1.8.0 relies on tbb provided config, earlier versions make
    # assumptions about the layout of tbb files that are not true in
    # 2021.1 and later
    conflicts("^intel-tbb@2021.1:", when="@:1.7.0")
    conflicts("^intel-oneapi-tbb@2021.1:", when="@:1.7.0")
    depends_on("tbb")
    depends_on("intel-tbb@2021.4.0:", when="@1.11: %tbb=intel-tbb")
    depends_on("intel-oneapi-tbb@2021.4.0:", when="@1.11: %tbb=intel-oneapi-tbb")
    depends_on(
        "boost@1.66.0:"
        "+program_options+exception+filesystem+system+chrono+serialization"
        "+random+graph+timer+iostreams+math+thread+container",
        when="@:0.14.1",
    )
    depends_on(
        "boost@1.72.0:1.88"
        "+program_options+exception+filesystem+system+chrono+serialization"
        "+random+graph+timer+iostreams+math+thread+container",
        when="@1.4.0:1.10.3",
    )
    depends_on("boost@1.72.0:+atomic+filesystem+timer+chrono+program_options", when="@1.11.4:")
    depends_on("cereal")
    depends_on("jemalloc", when="@:1.10")
    depends_on("xz")
    depends_on("zlib-api", when="@:1.10")
    # it's explicitly looking for zlib-ng.h files, not normal compat includes
    depends_on("zlib-ng~compat", when="@1.11:")
    depends_on("bzip2")
    depends_on("libdivsufsort", when="@:1.10")
    depends_on("staden-io-lib~curl", when="@:1.10")
    # docs suggest libdeflate is slightly faster
    depends_on("staden-io-lib~curl+libdeflate~shared@1.15:", when="@1.10.3")
    depends_on("libgff")
    depends_on("pkgconfig")
    depends_on("curl", when="@0.14.1:")
    depends_on("htslib", when="@1.10.2:")
    depends_on("mimalloc", when="@1.11:")
    depends_on("catch2", type="test", when="@1.11:")
    # probably just for tests, but cmake looks anyway
    depends_on("python@3:", type="build", when="@1.11:")

    patch("fix_hts.patch", when="@1.10.2")

    conflicts("%gcc@:5.1", when="@0.14.1:")

    # SalmonDependencies.camke
    resource(
        name="pufferfish",
        git="https://github.com/COMBINE-lab/pufferfish.git",
        commit="ace68c1c022816ba8c50a1a07c5d08f2abd597d6",
        submodules=True,
        placement="pufferfish",
        when="@1.11.4",
    )
    resource(
        name="fqfeeder",
        git="https://github.com/rob-p/FQFeeder.git",
        commit="f5b08d1002351c192b69048ac9f6cf4c7c116265",
        placement="fqfeeder",
        when="@1.11.4",
    )

    for ver, repo, checksum in [
        (
            "1.10.3",
            "pufferfish",
            "52b6699de0d33814b73edb3455175568c2330d8014be017dce7b564e54134860",
        ),
        (
            "1.10.2",
            "pufferfish",
            "f225b74833f71dcf767a565345224357fb091f90ce79717abc836814d9ccd101",
        ),
        (
            "1.9.0",
            "pufferfish",
            "2a862daeff95a19c9b188bc26a5d02fc0ecc5b9c9ae5523a67c9d14e62551c5d",
        ),
        (
            "1.4.0",
            "pufferfish",
            "059207e8d3134060ed70595e53f4189954c9e5edfaa6361b46304f55d1b71bc7",
        ),
        ("0.14.1", "RapMap", "fabac2f360513b803aa3567415eddcd97261ab8a23d4f600af5f98ee8ffd944b"),
        ("0.12.0", "RapMap", "05102c0bbc8a0c0056a01cd0e8788fa5b504aee58ac226ab8c0e3ffec8019790"),
        ("0.9.1", "RapMap", "8975e5a1ed61ed9354ba776272927545f417ecdce95823e71ba1e7b61de7d380"),
        ("0.8.2", "RapMap", "1691f4bca2b604f05f36772ae45faf0842ab4809843df770bd10366a5cfd6822"),
    ]:
        resource(
            name=repo,
            url=f"https://github.com/COMBINE-lab/{repo}/archive/salmon-v{ver}.zip",
            sha256=checksum,
            placement="external",
            expand=False,
            when=f"@{ver}",
        )

    # `%gcc13:` requires `<cstdint>` to be manually included. Fixed upstream,
    # so we patch to allow building of previous salmon versions
    patch(
        "https://github.com/COMBINE-lab/salmon/commit/ffb2a11.patch?full_index=1",
        sha256="5ed3512bae665c1d72002911ab9ee6d213f10df63019ebd9e8e0ecde03823a73",
        when="@:1.10.1%gcc@13:",
        level=1,
    )

    def patch(self):
        # remove static linking to libstdc++
        filter_file("-static-libstdc++", "", "CMakeLists.txt", string=True)
        if self.spec.satisfies("@0.8.2:0.9.1"):
            filter_file(
                "${FAST_MALLOC_LIB}",
                "${FAST_MALLOC_LIB}\n${CMAKE_DL_LIBS}",
                "src/CMakeLists.txt",
                string=True,
            )

        if self.spec.satisfies("@:0.14.1"):
            filter_file("curl -k.*", "", "scripts/fetchRapMap.sh")
            symlink("./salmon-v{0}.zip".format(self.version), "./external/rapmap.zip")

        if self.spec.satisfies("@1.4.0:1.10"):
            filter_file("curl -k.*", "", "scripts/fetchPufferfish.sh")
            symlink("./salmon-v{0}.zip".format(self.version), "./external/pufferfish.zip")
            # Fix issues related to lto-wrapper during install
            filter_file(
                "INTERPROCEDURAL_OPTIMIZATION True",
                "INTERPROCEDURAL_OPTIMIZATION False",
                "src/CMakeLists.txt",
                string=True,
            )
            filter_file("curl -k.*", "", "scripts/fetchPufferfish.sh")

        if self.spec.satisfies("@1.10.3"):
            findstadenio_module = join_path("cmake", "Modules", "Findlibstadenio.cmake")
            filter_file("PACKAGE_VERSION", "IOLIB_VERSION", findstadenio_module, string=True)
            filter_file("io_lib_config.h", "version.h", findstadenio_module, string=True)

        # filter file to remove boost_system dep if boost @1.69:
        # (or 1.89: when they removed the stub)
        if self.spec.satisfies("@1.11.4:"):
            if self.spec.satisfies("%boost@1.89:"):
                filter_file(
                    r"(^set\(_salmon_boost_components.*)( system)(.*\)$)",
                    r"\1\3",
                    join_path("cmake", "SalmonDependencies.cmake"),
                )
            # tbbmalloc isn't identified as a target without adding it here
            filter_file(
                r"(find_package\(TBB 2021.4 QUIET CONFIG COMPONENTS) (tbb)\)",
                r"\1 \2 tbbmalloc)",
                join_path("cmake", "SalmonDependencies.cmake"),
            )

    def cmake_args(self):
        if self.spec.satisfies("@:1.10.3"):
            args = ["-DBOOST_ROOT=%s" % self.spec["boost"].prefix]
        if self.spec.satisfies("@1.11:"):
            args = [
                self.define("SALMON_USE_SYSTEM_DEPS", True),
                self.define("SALMON_FETCH_MISSING_DEPS", False),
                self.define("SALMON_USE_HTSLIB", True),
                self.define("USE_SHARED_LIBS", True),
                self.define(
                    "SALMON_PUFFERFISH_SOURCE_DIR", join_path(self.stage.source_path, "pufferfish")
                ),
                self.define(
                    "SALMON_FQFEEDER_SOURCE_DIR", join_path(self.stage.source_path, "fqfeeder")
                ),
                self.define("SALMON_ENABLE_TESTS", self.run_tests),
                self.define("SALMON_ENABLE_BENCHMARKS", self.run_tests),
            ]
        return args

    @when("@1.11.4:")
    def check(self):
        with working_dir(self.build_directory):
            make("unitTests")
            make("benchmark_smoke")
