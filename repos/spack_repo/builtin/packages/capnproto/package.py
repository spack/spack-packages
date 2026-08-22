# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Capnproto(AutotoolsPackage):
    """Cap'n'Proto is an insanely fast data interchange
    format and capability-based RPC system
    """

    homepage = "https://capnproto.org"
    url = "https://github.com/capnproto/capnproto/archive/refs/tags/v0.8.0.tar.gz"
    git = "https://github.com/capnproto/capnproto"

    maintainers("alexrobomind")

    license("MIT")

    version("master", branch="master")

    version("1.5.0", sha256="d5ebdf858e9885c33d4b3f765006d68bd66e9b002bf4d607ff4317ef9c1aac6a")
    version("1.4.0", sha256="d14a9149b79c055fee9d5aa778defe8e8cee0d2a11f0729865cd30dcc345eef2")
    version("1.3.0", sha256="01ab2ba7f52fcc3c51a10e22935aae56f3bc5e99b726b7e507fe6700cb12147d")
    version("1.2.0", sha256="763ecaa78e900101bc40c1c3397991413ff26996415b891ca9c310987fbdf3fb")
    version("1.1.0", sha256="c0a0d78a07e821f7bae26c7fcac20a9202eb3d639a673b2606b76092a1f35b6b")
    version("1.0.2", sha256="3cfd0ed58080d78b3a3381305489f2175cdaf1ef1cb55425d8fc8246a76bdff3")
    version("0.10.4", sha256="c6f25940688c87ddb24e0c4e475c3213d9b044aad2ba305439cc8c224f559da6")
    version("0.10.2", sha256="756262841fa66260c9969e900701cc86720c2548584fb96c8153348fd7edfe69")
    version("0.10.0", sha256="0e46a72d086830762c001116c0a146098fbdce3cd40665a0ffd4742962d42bfd")
    version("0.9.1", sha256="daf49f794560f715e2f4651c842aaece2d065d4216834c5c3d3254962e35b535")
    version("0.9.0", sha256="a156efe56b42957ea2d118340d96509af2e40c7ef8f3f8c136df48001a5eb2ac")
    version("0.8.0", sha256="6d8b43a7ec2a764b4dfe4139a7cdd070ad9057f106898050d9f4db3754b98820")
    version("0.7.0", sha256="76c7114a3d142ad08b7208b3964a26e72a6320ee81331d3f0b87569fc9c47a28")
    version("0.6.1", sha256="85210424c09693d8fe158c1970a2bca37af3a0424f02b263f566a1b8a5451a2d")
    version("0.6.0", sha256="3b73a3dc39592a30b1bb6d00dff930e5fb277c774a1d40bf6a1aa7758c5fec74")
    version("0.5.3.1", sha256="e9af9ccfcb6d61be2dca1daf75e90daea32cf6f4c7c24a19919815ce527d9ac8")
    version("0.5.3", sha256="13c66dc1ce2a038562cddeaf48f71f0bb0e15a1d1a1775efa80dff3cdebeea6c")
    version("0.5.2", sha256="bd8aa7c45120c3bc5e1857d72006171b78a4b698af54dd1e3bfc966b54faedaf")
    version("0.5.1.2", sha256="e76c2b55e2b6fe8b6db8df46a348c36e7056e95507359118e54db60d746ff244")
    version("0.5.1.1", sha256="caf308e92683b278bc6c568d4fb5558eca78180cac1eb4a3db15d435bf25116f")
    version("0.4.1.2", sha256="6376c1910e9bc9d09dc46d53b063c5bdcb5cdf066a8210e9fffe299fb863f0d9")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    depends_on("zlib-api", when="+zlib")
    depends_on("openssl", when="+tls")

    depends_on("autoconf", type="build", when="build_system=autotools")
    depends_on("automake", type="build", when="build_system=autotools")
    depends_on("libtool", type="build", when="build_system=autotools")

    variant("zlib", default=True, description="Enable compression")
    variant("tls", default=False, description="Enable TLS support")

    configure_directory = "c++"

    def configure_args(self):
        args = []

        if self.spec.satisfies("+tls"):
            args.append("--with-openssl")
        else:
            args.append("--without-openssl")

        if self.spec.satisfies("+zlib"):
            args.append("--with-zlib")
        else:
            args.append("--without-zlib")

        return args

    def patch(self):
        # The master branch has version versions of type '0.11-dev', which is incompatible with
        # CMake's find_package call.
        # Therefore, these are patched to the respective release-type versions.
        if self.version == Version("master"):
            filter_file(
                "set\\(VERSION 0\\.(\\d*)\\-dev\\)", "set(VERSION 0.\\1)", "c++/CMakeLists.txt"
            )
            filter_file(
                (
                    "AC_INIT\\(\\[Capn Proto\\],\\[0\\.(\\d*)\\-dev\\],"
                    "\\[capnproto@googlegroups\\.com\\],\\[capnproto\\-c\\+\\+\\]\\)"
                ),
                "AC_INIT([Capn Proto],[0.\\1],[capnproto@googlegroups.com],[capnproto-c++])",
                "c++/configure.ac",
            )
