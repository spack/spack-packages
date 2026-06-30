from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Eventanalysis(CMakePackage):
    """An event-based data processing framework for HEP."""

    homepage = "https://baltig.infn.it/mori/EventAnalysis/"
    git = "https://baltig.infn.it/mori/EventAnalysis.git"

    license("GPL-3.0-only")

    version("1.4.1", tag="1.4.1", commit="bfe463ad1bdb0294b02bd10bb5aa7d1b45f8ba1e")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20"),
        multi=False,
        description="Force a specific C++ standard",
    )
    variant("root", default=True, description="Enables Root I/O")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.13:", type="build")

    depends_on("root", when="+root")

    def cmake_args(self):
        args = []
        args.append(self.define("DISABLE_ROOT", "~root" in self.spec))
        return args
