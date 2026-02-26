# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class RocmGdb(AutotoolsPackage):
    """This is ROCmgdb, the ROCm source-level debugger for Linux,
    based on GDB, the GNU source-level debugger."""

    homepage = "https://github.com/ROCm/ROCgdb"
    url = "https://github.com/ROCm/ROCgdb/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]
    executables = ["rocgdb"]

    license("LGPL-2.0-or-later")

    maintainers("srekolam", "renjithravindrankannath")

    version("7.2.0", sha256="0648c00a4098af9edddbdb05832f0afd03c0027359213ad4d6b211951ec672d1")
    version("7.1.1", sha256="4369b0dc0bea6c371872d517c43867fdfba3f12af7d5ae3900d4a4311bd49e30")
    version("7.1.0", sha256="33833597801680b76639b0cc97113da17ab3cad3167bf06419e838c9e2ae8113")
    version("7.0.2", sha256="1b06122860b9036ecdab4ba2ff2f3cab4707ad01941513aa23543962308c0e9e")
    version("7.0.0", sha256="a65824bb2f8d67eab9e3823da06638b4c015ba3342400159eed76ca2e7c48b25")
    version("6.4.3", sha256="7cb8a1c3554284b735232c2fa917315ac72421f11cc8156476003f0c3f1c3086")
    version("6.4.2", sha256="787128a11805891b2ecef3014bc36cc33e08e008e6e882982a410c60efd0335e")
    version("6.4.1", sha256="e8f80ed022af7ce9b4f59ebb352d6b2b5af7b6a4179023b24f89215e65bc4527")
    version("6.4.0", sha256="ef32529b2e3799dd8ab15647701063fcdcadd6d043a0d376a98c3ca10813817a")
    version("6.3.3", sha256="51678b588f65f92f50c2336707322cf4973fa96d03e268ec5956ac1a9f2ebaa3")
    version("6.3.2", sha256="85b03c1fb99f55272f4732dff58e8ba0a1add454a79d2b9d471df200366d0c7e")
    version("6.3.1", sha256="954236518491ba547f849be7c86e71ff95ef24535f66acabfd45040e11c25d7b")
    version("6.3.0", sha256="4a41ffbc4f7a5970181ee0aae07f0ea4cda278870cd60a562b25001f1365e29f")
    version("6.2.4", sha256="061d00f3d02ca64094008c5da185712712ccd3a922f6e126d5f203cdae2b9e04")
    version("6.2.1", sha256="bed312c3fbb9982166538036bb9fd4a75053117c65ba80e34dbdae629a8fe6e4")
    version("6.2.0", sha256="753fd4f34d49fb0297b01dca2dd7cdf12cd039caa622a5f2d153362d27a8659c")
    version("6.1.2", sha256="19208de18d503e1da79dc0c9085221072a68e299f110dc836204364fa1b532cc")
    version("6.1.1", sha256="3d982abc130a286d227948aca5783f2e4507ef4275be21dad0914e37217ba19e")
    version("6.1.0", sha256="e90d855ca4c1478acf143d45ff0811e7ecd068711db155de6d5f3593cdef6230")
    version("6.0.2", sha256="69b7c3d63435e7d99088980498c68422e52b69244d10a3a62541633e733286e0")
    version("6.0.0", sha256="0db4ab32ca729e69688cdb238df274ce5cf58b5cb2538584662cca4358708c2b")
    version("5.7.1", sha256="5cd150b5796aea9d77efd43b89d30a34fa4125338179eb87c6053abcac9f3c62")
    version("5.7.0", sha256="94fba57b2f17b593de61f7593b404fabc00b054d38567be57d12cf7654b7969a")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3:", type="build")
    depends_on("texinfo", type="build")
    depends_on("bison", type="build")
    depends_on("flex@2.6.4:", type="build")
    depends_on("libunwind", type="build")
    depends_on("expat", type=("build", "link"))
    depends_on("python", type=("build", "link"))
    depends_on("zlib-api", type="link")
    depends_on("babeltrace@1.2.4", type="link")
    depends_on("gmp", type=("build", "link"))
    depends_on("mpfr", type=("build", "link"))
    depends_on("pkgconfig", type="build")

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
    ]:
        depends_on(f"rocm-dbgapi@{ver}", type="link", when=f"@{ver}")
        depends_on(f"comgr@{ver}", type="link", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    build_directory = "spack-build"

    def configure_args(self):
        # Generic options to compile GCC
        options = [
            # Distributor options
            "--program-prefix=roc",
            "--enable-64-bit-bfd",
            "--with-bugurl=https://github.com/ROCm/ROCgdb/issues",
            "--with-pkgversion=-ROCm",
            "--enable-targets=x86_64-linux-gnu,amdgcn-amd-amdhsa",
            "--disable-ld",
            "--disable-gas",
            "--disable-gdbserver",
            "--disable-sim",
            "--enable-tui",
            "--disable-gdbtk",
            "--disable-shared",
            "--with-expat",
            "--with-system-zlib",
            "--without-guile",
            "--with-babeltrace",
            "--with-lzma",
            "--with-python",
            "--with-rocm-dbgapi={0}".format(self.spec["rocm-dbgapi"].prefix),
            "--disable-gprofng",
        ]
        return options

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"rocm-rel-(\d+)\.(\d+)", output)
        if match:
            ver = "{0}.{1}".format(int(match.group(1)), int(match.group(2)))
        else:
            ver = None
        return ver
