# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import shlex

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Nim(Package):
    """Nim is a statically typed compiled systems programming language.
    It combines successful concepts from mature languages like Python,
    Ada and Modula.
    """

    homepage = "https://nim-lang.org/"
    url = "https://nim-lang.org/download/nim-2.2.10.tar.xz"
    git = "https://github.com/nim-lang/Nim.git"

    license("MIT", checked_by="Buldram")

    maintainers("Buldram")

    version("develop", branch="devel")
    version("2.2.10", sha256="7957b7ed004206bcf10bcc4f3b4744153878e62f2431552a9a8e9d3f40e8d5d5")
    version("2.2.8", sha256="114191afa083c5059dcbe5ce88dbe4f42542cff04e2c3017668ee438bc0b8cfc")
    version("2.2.6", sha256="657b0e3d5def788148d2a87fa6123fa755b2d92cad31ef60fd261e451785528b")
    version("2.2.4", sha256="f82b419750fcce561f3f897a0486b180186845d76fb5d99f248ce166108189c7")
    version("2.2.2", sha256="7fcc9b87ac9c0ba5a489fdc26e2d8480ce96a3ca622100d6267ef92135fd8a1f")
    version("2.2.0", sha256="ce9842849c9760e487ecdd1cdadf7c0f2844cafae605401c7c72ae257644893c")
    version("2.0.16", sha256="b2e70c6c011b5507093090a8887fa252773208fd047ee38f8562e2569e5c378a")
    version("2.0.14", sha256="d420b955833294b7861e3fb65021dac26d1c19c528c4d6e139ccd379e2c15a43")
    version("2.0.12", sha256="c4887949c5eb8d7f9a9f56f0aeb2bf2140fabf0aee0f0580a319e2a09815733a")
    version("2.0.4", sha256="71526bd07439dc8e378fa1a6eb407eda1298f1f3d4df4476dca0e3ca3cbe3f09")
    version("1.6.20", sha256="ffed047504d1fcaf610f0dd7cf3e027be91a292b0c9c51161504c2f3b984ffb9")

    variant(
        "sqlite", default=False, when="@:1.7.3", description="Install SQLite for std/db_sqlite"
    )

    depends_on("c", type="build")
    depends_on("gmake", type="build")
    depends_on("pcre", type="link")
    depends_on("openssl", type="link")
    depends_on("sqlite@3:", type="link", when="+sqlite")

    resource(
        name="csources_v2",
        git="https://github.com/nim-lang/csources_v2.git",
        commit="86742fb02c6606ab01a532a0085784effb2e753e",
        when="@develop",
    )

    phases = ["build", "install"]

    def patch(self):
        # Hardcode dependency dynamic library paths into wrapper modules using rpath
        def append_rpath(path, libdirs):
            """Add a pragma at the end of the file which passes
            rpath with libdirs to the linker when the module is used."""

            with open(path, "a") as f:
                scope = False
                for path in filter_system_paths(libdirs):
                    quoted_path = shlex.quote(path)
                    if '"""' in quoted_path:
                        raise InstallError(f'Quoted dependency path {quoted_path} contains """')

                    if not scope:
                        f.write("\nwhen not defined(vcc):\n")  # TODO: Implement for msvc
                        scope = True

                    f.write(f'  {{.passl: """-Xlinker -rpath -Xlinker {quoted_path}""".}}\n')

        append_rpath("lib/wrappers/pcre.nim", self.spec["pcre"].libs.directories)
        append_rpath("lib/wrappers/openssl.nim", self.spec["openssl"].libs.directories)
        if self.spec.satisfies("+sqlite"):
            append_rpath("lib/wrappers/sqlite3.nim", self.spec["sqlite"].libs.directories)

        # Musl defines SysThread as a struct *pthread_t rather than an unsigned long as glibc does.
        if self.spec.satisfies("^[virtuals=libc] musl"):
            if self.spec.satisfies("@1.9.3:"):
                pthreadModule = "lib/std/private/threadtypes.nim"
            else:
                pthreadModule = "lib/system/threadlocalstorage.nim"

            filter_file(
                'header: "<sys/types.h>" .} = distinct culong',
                'header: "<sys/types.h>" .} = pointer',
                pthreadModule,
                string=True,
            )

    def build(self, spec, prefix):
        if spec.satisfies("@develop"):
            with working_dir("csources_v2"):
                make()
        else:
            make()

        nim = Executable(join_path("bin", "nim"))
        # Separate nimcache allows parallel compilation of different versions of the Nim compiler
        nim_flags = ["--skipUserCfg", "--skipParentCfg", "--nimcache:nimcache"]
        nim("c", *nim_flags, "koch")

        koch = Executable("./koch")
        koch("boot", "-d:release", *nim_flags)
        koch("tools", *nim_flags)

        if spec.satisfies("@develop"):
            koch("geninstall")

        filter_file("1/nim", "1", "install.sh")

    def install(self, spec, prefix):
        Executable("./install.sh")(prefix)
        install_tree("bin", prefix.bin)
        install_tree("dist", prefix.dist)
