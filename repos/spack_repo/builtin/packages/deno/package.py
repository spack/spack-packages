# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Deno(PythonPackage):
    """Python redistribution of Deno binaries.

    Deno: A modern runtime for JavaScript and TypeScript.
    """

    homepage = "https://deno.com/"
    pypi = "deno/deno-2.9.7.tar.gz"

    license("MIT")

    version("2.9.7", sha256="79f4b7acdd9a37e98a4d1e0ca08d71c4e55f6c0cb13bd1e0946fa9b5497be2d9")
    version("2.8.1", sha256="fb65e568bef30b1a7e63f033713f1a6792a8456e339febdb7d638c6bb2c4c008")

    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "linux" and machine == "x86_64":
        version(
            "2.4.2",
            sha256="d84778633215b7cb93cf7690860d6241f632b087bd2a19de12cd410e6b2e157a",
            url="https://dl.deno.land/release/2.4.2/deno-x86_64-unknown-linux-gnu.zip",
            deprecated=True,
        )
    elif system == "linux" and machine == "aarch64":
        version(
            "2.4.2",
            sha256="4a3218e3ca99f2abbc41d20691bca7942d18ebcb01db6b4389cbb91eabf1055f",
            url="https://dl.deno.land/release/2.4.2/deno-aarch64-unknown-linux-gnu.zip",
            deprecated=True,
        )
    elif system == "darwin" and machine == "x86_64":
        version(
            "2.4.2",
            sha256="fa47eb72b8d1f3499a7fb3e6c7bbcd3b1e6407112bb03fafd40aa8038a54b93e",
            url="https://dl.deno.land/release/2.4.2/deno-x86_64-apple-darwin.zip",
            deprecated=True,
        )
    elif system == "darwin" and machine == "arm64":
        version(
            "2.4.2",
            sha256="732f3ce50dc64a63972ca4efb48679299c01663ce918f710d695a68ce5f4c936",
            url="https://dl.deno.land/release/2.4.2/deno-aarch64-apple-darwin.zip",
            deprecated=True,
        )

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-hatchling", type="build")

    @when("@2.4.2")
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("deno", prefix.bin)

    @when("@2.4.3:")
    def patch(self):
        # Instead of using sysconfig.get_path to find deno, the spack deno
        # prefix should be used.
        filter_file(
            r"(def find_deno_bin.*\n)",
            r"\1" + f'    return "{prefix.bin.deno}"\n',
            "src/deno/_find_deno.py",
        )
