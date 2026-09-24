# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Fabtests(AutotoolsPackage):
    """Fabtests provides a set of runtime analysis tools and examples that use
    libfabric."""

    homepage = "https://libfabric.org"
    url = "https://github.com/ofiwg/libfabric/releases/download/v1.9.1/fabtests-1.9.1.tar.bz2"
    maintainers("kgerheiser")

    license("GPL-2.0-only")

    version("2.6.0", sha256="79ddab1290fcd62c76735ce7c25a277cb322de91d5e1b696b6e01a8824c62b7d")
    version("2.5.1", sha256="005fded6a91dbb929ca41dc35ec6c043bf6f82de055eed8413fa6de172a56346")
    version("2.5.0", sha256="d0902946f421e490cc33452d4131ad94f7ea919a07cffb674dab063fc5552182")
    version("2.4.0", sha256="2caff4517c36df3a4df89d0ba4c0869f1e5e01c458153fd0ba0767da2d0759d7")
    version("2.3.1", sha256="d19d526e26e4620ae4fdc13f89d3e79b39df5fca643787c8b2e62151152ee4fd")
    version("2.3.0", sha256="18c17bff50257735356ed059211ae3345f2313e993a1951b2d5e283f1da520fd")
    version("2.2.0", sha256="2e4c79fbacea2e2aa776bdae7310bc8e0c8b02671ebcc8325d3bee0b27aabe5c")
    version("2.1.0", sha256="60f024a5c5e5c956db7af07229a40e5c64f3ea37d84b9c142c1a23c3248c08cc")
    version("2.0.0", sha256="121ac305750e78bce744594c103bb72a6669c701a2419bec1da6a409c15e48de")
    version("1.22.0", sha256="140ad1d9fa6e03c13d0ce62fe4c158777a218825f9837b121aa75e1edb869e44")
    version("1.21.1", sha256="3d9eacdfb64066609593a615af5cfd440ee1cbc71ade394d09aaade38698f3ea")
    version("1.21.0", sha256="d022a186d37bd6ccb52303e0588c28e29f0f56c25a384c37acb16c881ba99e64")
    version("1.20.2", sha256="624beb02ffc8e325834545810566330f2a1204d5c6ad015ba095303121cb8ae6")
    version("1.20.1", sha256="687884b6fd3046f46e2f878e19e76e4506b50950bd2f59a731618b89d02a5436")
    version("1.20.0", sha256="61d483452163b39d81dcb9f578e5d9007817e0496235bc2aac1e82b7737fd65e")
    version("1.19.1", sha256="57b11f2e0e3cd77b104d63f0ecb453161fa8a17bc4f7ca2d7a17a7a34f7fb85c")
    version("1.19.0", sha256="82d714020df9258cfdd659c51f2be8f4507cbe157c7f03c992c70fc528d8d837")
    version("1.18.2", sha256="3d85486ff80151defdb66414a851a9a9a2d4adc6cf696e2b8e4bb3ce340512c2")
    version("1.18.1", sha256="fe9864acc0e17a5b0157b1cc996bb3c578cfa32c87bd43bc17b5e31e24ef63b5")
    version("1.18.0", sha256="9201ba020c3cf2f07dbf16d9837b565031f2eab664efd02f2e4345443983ae3e")
    version("1.17.1", sha256="efc89c6c2412168b7b8fdd495c2f46d9074205363959e80e4c8d452ba97d4c0d")
    version("1.17.0", sha256="5d3cf28de32549822cbb155329fe7ce0f88423157e1210a76b23c498c848ce2a")
    version("1.16.1", sha256="0e5def832ac9438ba7c50b8198f0089b568935fcc13d1ccb50a5f8a1dcf4ec30")
    version("1.16.0", sha256="c428ec353f64b073fb17ac0061aab76b9cc8c41614adb772d00575f3e486884d")
    version("1.15.2", sha256="9afdc992bedf3f47c068824ba3408156c890b5cb2587964ec2ad9f658102db63")
    version("1.9.1", sha256="6f8ced2c6b3514759a0e177c8b2a19125e4ef0714d4cc0fe0386b33bd6cd5585")
    version("1.9.0", sha256="60cc21db7092334904cbdafd142b2403572976018a22218e7c453195caef366e")
    version("1.8.1", sha256="e9005d8fe73ca3849c872649c29811846bd72a62f897ecab73a08c7a9514f37b")
    # old releases, published in a separate repository
    version("1.6.2", sha256="37405c6202f5b1aa81f8ea211237a2d87937f06254fa3ed44a9b69ac73b234e8")
    version("1.6.1", sha256="d357466b868fdaf1560d89ffac4c4e93a679486f1b4221315644d8d3e21174bf")
    version("1.6.0", sha256="dc3eeccccb005205017f5af60681ede15782ce202a0103450a6d56a7ff515a67")
    version("1.5.3", sha256="3835b3bf86cd00d23df0ddba8bf317e4a195e8d5c3c2baa918b373d548f77f29")
    version("1.5.0", sha256="1dddd446c3f1df346899f9a8636f1b4265de5b863103ae24876e9f0c1e40a69d")
    version("1.4.2", sha256="3b78d0ca1b223ff21b7f5b3627e67e358e3c18b700f86b017e2233fee7e88c2e")

    depends_on("c", type="build")  # generated

    for v in (
        "2.6.0",
        "2.5.1",
        "2.5.0",
        "2.4.0",
        "2.3.1",
        "2.3.0",
        "2.2.0",
        "2.1.0",
        "2.0.0",
        "1.22.0",
        "1.21.1",
        "1.21.0",
        "1.20.2",
        "1.20.1",
        "1.20.0",
        "1.19.1",
        "1.19.0",
        "1.18.2",
        "1.18.1",
        "1.18.0",
        "1.17.1",
        "1.17.0",
        "1.16.1",
        "1.16.0",
        "1.15.2",
        "1.9.1",
        "1.9.0",
        "1.8.1",
        "1.6.2",
        "1.6.1",
        "1.6.0",
        "1.5.3",
        "1.5.0",
        "1.4.2",
    ):
        depends_on(f"libfabric@{v}", when=f"@{v}")

    def url_for_version(self, version):
        if version >= Version("1.8.1"):
            url = "https://github.com/ofiwg/libfabric/releases/download/v{0}/fabtests-{0}.tar.bz2"
        else:
            url = "https://github.com/ofiwg/fabtests/releases/download/v{0}/fabtests-{0}.tar.gz"
        return url.format(version.dotted)
