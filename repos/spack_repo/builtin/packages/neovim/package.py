# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Neovim(CMakePackage):
    """Neovim: Vim-fork focused on extensibility and usability"""

    homepage = "https://neovim.io"
    git = "https://github.com/neovim/neovim.git"
    url = "https://github.com/neovim/neovim/archive/v0.4.3.tar.gz"

    maintainers("albestro", "trws")

    license("Apache-2.0 AND Vim")

    version("master", branch="master")
    version("stable", tag="stable")
    version("0.11.6", sha256="d1c8e3f484ed1e231fd5f48f53b7345b628e52263d5eef489bb8b73ca8d90fca")
    version("0.11.5", sha256="c63450dfb42bb0115cd5e959f81c77989e1c8fd020d5e3f1e6d897154ce8b771")
    version("0.11.4", sha256="83cf9543bedab8bec8c11cd50ccd9a4bf1570420a914b9a28f83ad100ca6d524")
    version("0.11.3", sha256="7f1ce3cc9fe6c93337e22a4bc16bee71e041218cc9177078bd288c4a435dbef0")
    version("0.11.2", sha256="324759a1bcd1a80b32a7eae1516ee761ec3e566d08284a24c4c7ca59079aabfa")
    version("0.10.1", sha256="edce96e79903adfcb3c41e9a8238511946325ea9568fde177a70a614501af689")
    version("0.11.1", sha256="ffe7f9a7633ed895ff6adb1039af7516cd6453715c8889ad844b6fa39c3df443")
    version("0.11.0", sha256="6826c4812e96995d29a98586d44fbee7c9b2045485d50d174becd6d5242b3319")
    version("0.10.4", sha256="10413265a915133f8a853dc757571334ada6e4f0aa15f4c4cc8cc48341186ca2")
    version("0.10.3", sha256="39fab47d241da7b9418823cc563c689d522c1c4b2def04036393834f3f1ca94c")
    version("0.10.2", sha256="546cb2da9fffbb7e913261344bbf4cf1622721f6c5a67aa77609e976e78b8e89")
    version("0.10.0", sha256="372ea2584b0ea2a5a765844d95206bda9e4a57eaa1a2412a9a0726bab750f828")
    version("0.9.5", sha256="fe74369fc30a32ec7a086b1013acd0eacd674e7570eb1acc520a66180c9e9719")
    version("0.9.4", sha256="148356027ee8d586adebb6513a94d76accc79da9597109ace5c445b09d383093")
    version("0.9.2", sha256="06b8518bad4237a28a67a4fbc16ec32581f35f216b27f4c98347acee7f5fb369")
    version("0.9.1", sha256="8db17c2a1f4776dcda00e59489ea0d98ba82f7d1a8ea03281d640e58d8a3a00e")
    version("0.9.0", sha256="39d79107c54d2f3babcad2cd157c399241c04f6e75e98c18e8afaf2bb5e82937")
    version("0.8.3", sha256="adf45ff160e1d89f519b6114732eba03485ae469beb27919b0f7a4f6b44233c1")
    version("0.8.2", sha256="c516c8db73e1b12917a6b2e991b344d0914c057cef8266bce61a2100a28ffcc9")
    version("0.8.0", sha256="505e3dfb71e2f73495c737c034a416911c260c0ba9fd2092c6be296655be4d18")
    version("0.7.2", sha256="ccab8ca02a0c292de9ea14b39f84f90b635a69282de38a6b4ccc8565bc65d096")
    version("0.7.0", sha256="792a9c55d5d5f4a5148d475847267df309d65fb20f05523f21c1319ea8a6c7df")
    version("0.6.1", sha256="dd882c21a52e5999f656cae3f336b5fc702d52addd4d9b5cd3dc39cfff35e864")
    version("0.6.0", sha256="2cfd600cfa5bb57564cc22ffbbbcb2c91531053fc3de992df33656614384fa4c")
    version("0.5.1", sha256="aa449795e5cc69bdd2eeed7095f20b9c086c6ecfcde0ab62ab97a9d04243ec84")

    variant(
        "no_luajit",
        default=False,
        description="use lua rather than luajit as lua language provider",
    )

    depends_on("c", type="build")  # generated

    # depend on virtual, lua-luajit-openresty preferred
    depends_on("lua-lang")
    depends_on("luajit", when="~no_luajit")
    depends_on("lua-lang@5.1", when="+no_luajit")

    # dependencies to allow regular lua to work
    depends_on("lua-ffi", when="^[virtuals=lua-lang] lua", type=("link", "run"))
    depends_on("lua-bitlib", when="^[virtuals=lua-lang] lua", type=("link", "run"))

    # base dependencies
    depends_on("cmake@3.0:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("gettext")
    depends_on("gperf", type="link")
    depends_on("jemalloc", type="link", when="platform=linux")
    depends_on("lua-lpeg")
    depends_on("lua-mpack", when="@:0.10")
    depends_on("iconv", type="link")
    depends_on("libuv@1.42:", type="link")
    depends_on("libluv@1.30.0:", type="link")
    depends_on("libtermkey@0.18:", type="link", when="@:0.9")
    depends_on("libvterm@0.1:", type="link", when="@:0.10")
    depends_on("unibilium@2.0:", type="link")
    depends_on("msgpack-c@1.0.0:", type="link", when="@:0.10")
    depends_on("tree-sitter")

    # versions
    with when("@0.6:"):
        depends_on("cmake@3.10:", type="build")
        depends_on("gperf@3.1:", type="link")
        conflicts("^libiconv@:1.14")
        depends_on("libtermkey@0.22:", type="link", when="@:0.9")
        depends_on("libvterm@0.1.4:", type="link", when="@:0.10")
        depends_on("msgpack-c@3.0.0:", type="link", when="@:0.10")
    with when("@0.7:"):
        depends_on("gettext@0.20.1:")
        depends_on("libluv@1.43.0:", type="link")
        depends_on("libuv@1.44.1:", type="link")
        depends_on("tree-sitter@0.20.6:")
    with when("@0.8:"):
        depends_on("libvterm@0.3:", type="link", when="@:0.10")
    with when("@0.9:"):
        depends_on("tree-sitter@0.20.8", when="@0.9")
    with when("@0.10:"):
        depends_on("cmake@3.13:", type="build")
        depends_on("libvterm@0.3.3:", type="link", when="@:0.10")
        depends_on("tree-sitter@0.20.9", when="@0.10")
    with when("@0.11:"):
        depends_on("cmake@3.16:", type="build")
        depends_on("utf8proc@2.10.0", type="link")

    # Support for `libvterm@0.2:` has been added in neovim@0.8.0
    # term: Add support for libvterm >= 0.2 (https://github.com/neovim/neovim/releases/tag/v0.8.0)
    # https://github.com/neovim/neovim/issues/16217#issuecomment-958590493
    conflicts("libvterm@0.2:", when="@:0.7")

    # ts_parser_timeout_micros and ts_parser_set_timeout_micros not anymore in API
    # https://github.com/neovim/neovim/pull/33141
    # https://github.com/tree-sitter/tree-sitter/pull/4814
    conflicts("tree-sitter@0.26:", when="@:0.11.6")

    @when("^lua")
    def cmake_args(self):
        return [
            self.define("PREFER_LUA", True),
            self.define("LPEG_LIBRARY", self.spec["lua-lpeg"].libs),
        ]
