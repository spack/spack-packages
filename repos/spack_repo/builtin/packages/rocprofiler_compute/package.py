# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RocprofilerCompute(CMakePackage):
    """Advanced Profiling and Analytics for AMD Hardware"""

    homepage = "https://github.com/ROCm/rocm-systems"
    git = "https://github.com/ROCm/rocm-systems.git"

    tags = ["rocm"]
    maintainers("afzpatel", "srekolam", "renjithravindrankannath")
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/rocprofiler-compute/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-systems/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="201f19174eafbace2f7abf0d1178ebb17db878191276aba6d23f0e1758b0e10f")
    version("7.2.0", sha256="728ea7e9bf16e6ed217a0fd1a8c9afaba2dae2e7908fa4e27201e67c803c5638")
    version("7.1.1", sha256="cf5d577edc1bed185f9c424868ec42952ccd2f9c2679e6daeb3bc788536cf182")
    version("7.1.0", sha256="11a65dac6e4099b4f2bb438320ef8206bb130a8a31bba52e90b594cdc235969b")
    version("7.0.2", sha256="b56ab5c57883e2c3d75b7cc584279eb91157de195722f90c09cad51701ef4650")
    version("7.0.0", sha256="0ef46ee668b6ee6936911ecd70947abb4e501ced1c4f87d8001a6e35b9781705")
    version("6.4.3", sha256="d5005322dbfdd0feccd619d8fb6665f8631d74be1d6345be8726eff76829747b")
    version("6.4.2", sha256="0a0c5cbcc6d54881c58899d2f0db7feaa0d5665bf13e19f0715cb22f54b11187")
    version("6.4.1", sha256="a48837861dad010516f579ba627b1cf49469c56d74787f7b0883c5198de6e2a7")
    version("6.4.0", sha256="484a8974ebf973fa00241bf3665eac790b3c317aa36b794cc2998f892b3036fc")
    version("6.3.3", sha256="0f563874f71b593cbdcdf0eea58b08c7437f1abf807f0886a3a30afa9e7f4953")
    version("6.3.2", sha256="317f19acfa6e6780923e6c8144c3c223b523c382588df528b6df001fae38d13d")

    depends_on("python@3.8:")
    depends_on("py-pip", type="run")
    depends_on("py-astunparse@1.6.2", type=("build", "run"))  # wants exact version
    depends_on("py-colorlover", type=("build", "run"))
    depends_on("py-pyyaml")
    depends_on("py-matplotlib")
    depends_on("py-pandas@1.4.3:")
    depends_on("py-numpy@1.17.5:")
    depends_on("py-pymongo")
    depends_on("py-tabulate")
    depends_on("py-tqdm")
    depends_on("py-kaleido")
    depends_on("py-plotille")
    depends_on("py-dash-svg", type=("build", "run"))
    depends_on("py-dash", type=("build", "run"))
    depends_on("py-dash@3:", type=("build", "run"), when="@7.0:")
    depends_on("py-dash-bootstrap-components", type=("build", "run"))
    depends_on("py-textual", when="@7.0:")
    depends_on("py-textual-plotext", when="@7.0:")
    depends_on("py-sqlalchemy@2.0.42:", when="@7.1:")
    depends_on("py-textual-fspicker@0.4.3:", when="@7.2:")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:7.1"):
            return "."
        else:
            return "projects/rocprofiler-compute"

    def cmake_args(self):
        args = [self.define("ENABLE_TESTS", self.run_tests)]
        return args

    @run_before("cmake")
    def before_cmake(self):
        if self.spec.satisfies("@:7.1"):
            touch(join_path(self.stage.source_path, "VERSION.sha"))
