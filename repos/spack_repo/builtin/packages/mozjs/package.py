# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Mozjs(AutotoolsPackage):
    """SpiderMonkey is Mozilla’s JavaScript and WebAssembly Engine, used in Firefox, Servo and
    various other projects. It is written in C++, Rust and JavaScript. You can embed it into C++
    and Rust projects, and it can be run as a stand-alone shell."""

    homepage = "https://spidermonkey.dev/"
    url = "https://ftp.mozilla.org/pub/firefox/releases/128.1.0esr/source/firefox-128.1.0esr.source.tar.xz"

    maintainers("KineticTheory")

    license("MPL-2.0")

    version("140.7.0", sha256="608a739071726f30236f7100ec5e30e1b8ec342d4e91e715948c287909cb1529")
    version("140.3.1", sha256="0b43b3a1c4f40765d96eb2094d38838f5d01b7280ad8b9b0a17612bed9c36735")
    version("128.1.0", sha256="ccdab622a395622abc6d80040a11715ad81a614f601db6672c05b98ac91fd9b5")
    version("115.28.0", sha256="91b52505f91ec8bc1ba93afc50c59a845a5f6a57fac4967df04d54906a14181a")

    conflicts("platform=darwin", msg="Darwin is not currently supported.")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("curl", type="build")
    depends_on("llvm", type="build")
    depends_on("python@:3.13", type="build")
    depends_on("py-pip", type="build")
    depends_on("rust", type="build")
    depends_on("cbindgen@0.27:", type="build", when="@140:")
    depends_on("cbindgen", type="build")
    depends_on("zlib-api")

    configure_directory = "js/src"
    build_directory = "spack-build"

    def configure_args(self):
        args = ["--disable-jemalloc", "--with-intl-api", "--enable-optimize"]
        return args

    def url_for_version(self, version):
        return f"https://ftp.mozilla.org/pub/firefox/releases/{version}esr/source/firefox-{version}esr.source.tar.xz"
