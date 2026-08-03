from spack.package import *
from spack_repo.builtin.build_systems.makefile import MakefilePackage


class Lunum(MakefilePackage):
    """Numeric arrays for Lua."""

    homepage = "https://github.com/jzrake/lunum"
    git = "https://github.com/jzrake/lunum.git"
    parallel = False

    version("0.5.3", tag="v0.5.3")

    patch("lunum-0.5.3-source-fixes.patch")

    depends_on("c", type="build")
    depends_on("lua-lang@5.1:", type=("build", "link", "run"))

    @property
    def build_targets(self):
        return [
            "CC={0}".format(spack_cc),
            "LUA_HOME={0}".format(self.spec["lua-lang"].prefix),
            "INSTALL_TOP={0}".format(self.prefix),
        ]

    @property
    def install_targets(self):
        return self.build_targets + ["install"]
