# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.lua import LuaPackage

from spack.package import *


class LuaLuaposix(LuaPackage):
    """Lua POSIX bindings, including ncurses"""

    homepage = "https://github.com/luaposix/luaposix"
    url = "https://github.com/luaposix/luaposix/archive/refs/tags/v36.3.tar.gz"

    license("MIT")

    version("36.3", sha256="82cd9a96c41a4a3205c050206f0564ff4456f773a8f9ffc9235ff8f1907ca5e6")
    version("36.1", sha256="5e48e8ea5adfd8958bcdbaba132f5766473afedecc5c14ae3593464a5463a616")
    version("35.0", sha256="a4edf2f715feff65acb009e8d1689e57ec665eb79bc36a6649fae55eafd56809")
    version("33.4.0", sha256="e66262f5b7fe1c32c65f17a5ef5ffb31c4d1877019b4870a5d373e2ab6526a21")
    version("33.2.1", sha256="4fb34dfea67f4cf3194cdecc6614c9aea67edc3c4093d34137669ea869c358e1")

    def url_for_version(self, version):
        if version >= Version("35.0"):
            return f"https://github.com/luaposix/luaposix/archive/refs/tags/v{version}.tar.gz"
        return f"https://github.com/luaposix/luaposix/archive/release-v{version}.tar.gz"

    depends_on("c", type="build")
    depends_on("lua-lang@:5.4", when="@35.0:")
    depends_on("lua-lang@:5.3", when="@33.2:34")
    depends_on("lua-lang@:5.2", when="@:33.1")
    depends_on("lua-lang@5.1:")
    depends_on("lua-bit32", when="^lua-lang@5.1")
    depends_on("libxcrypt", when="platform=linux")
