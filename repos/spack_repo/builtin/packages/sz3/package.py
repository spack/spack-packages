# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Sz3(CMakePackage):
    """SZ3 is the next generation of the SZ compressor framework"""

    homepage = "https://github.com/szcompressor/SZ3"
    git = "https://github.com/szcompressor/SZ3"

    maintainers("disheng222", "robertu94")
    tags = ["e4s"]

    version("master")
    version("3.4.0", commit="592df793eb596d952242aa9fec9cbe5e68782aae")
    version("3.2.0", commit="b3dab4018425803a55d8073dc55dade7fa46b7b4")
    version("3.1.8", commit="e308ebf8528c233286874b920c72c0a6c0218fb2")
    version("3.1.7", commit="c49fd17f2d908835c41000c1286c510046c0480e")
    version("3.1.5.4", commit="4c6ddf628f27d36b28d1bbda02174359cd05573d")
    version("3.1.5.1", commit="5736a63b917e439dd62248b4ff6234e96726af5d")
    version("3.1.3.1", commit="323cb17b412d657c4be681b52c34beaf933fe7af")
    version("3.1.3", commit="695dff8dc326f3b165f6676d810f46add088a585")

    variant("hdf5", default=False, description="enable hdf5 filter support")
    variant("mdz", default=True, description="build mdz executable")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.19:", type="build", when="@3.4:")

    depends_on("zstd")
    depends_on("gsl", when="@:3.3")
    depends_on("pkgconfig")
    depends_on("hdf5", when="+hdf5")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if "+hdf5" in self.spec:
            if self.spec.satisfies("@3.4:"):
                env.prepend_path("HDF5_PLUGIN_PATH", self.prefix.lib.plugin)
            else:
                env.prepend_path("HDF5_PLUGIN_PATH", self.prefix.lib64)

    def cmake_args(self):
        args = [
            "-DSZ3_USE_BUNDLED_ZSTD=OFF",
            "-DSZ3_DEBUG_TIMINGS=OFF",
            self.define_from_variant("BUILD_MDZ", "mdz"),
            self.define_from_variant("BUILD_H5Z_FILTER", "hdf5"),
        ]
        if self.spec.satisfies("@3.4: +hdf5"):
            # 3.4 installs a copy of the filter in its own directory for HDF5_PLUGIN_PATH
            args.append(self.define("H5Z_SZ3_PLUGIN_INSTALL_DIR", "lib/plugin"))
        return args

    def test_sz3_smoke_test(self):
        """Run sz3 smoke test"""
        if self.spec.satisfies("@:3.1.6"):
            raise SkipTest("Package must be installed as version 3.1.7 or later")
        exe = which(self.prefix.bin.sz3_smoke_test, required=True)
        exe()

    def test_mdz_smoke_test(self):
        """Run mdz smoke test"""
        if self.spec.satisfies("@:3.1.6"):
            raise SkipTest("Package must be installed as version 3.1.7 or later")
        if "+mdz" not in self.spec:
            raise SkipTest("Package must be installed with '+mdz'")
        exe = which(self.prefix.bin.mdz_smoke_test, required=True)
        exe()
