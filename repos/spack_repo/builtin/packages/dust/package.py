# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Dust(Package):
    """du + rust = dust. Like du but more intuitive."""

    homepage = "https://github.com/bootandy/dust"
    url = "https://github.com/bootandy/dust/archive/v0.7.5.tar.gz"

    maintainers("fangohr", "yig")

    license("Apache-2.0")

    version("1.2.4", sha256="2f6768534bd01727234e67f1dd3754c9547aa18c715f6ee52094e881ebac50e3")
    version("1.2.3", sha256="424b26adfbafeac31da269ecb3f189eca09803e60fad90b3ff692cf52e0aeeee")
    version("1.2.2", sha256="e72f539ebe2f30bd85f83f8efd87c70c11e27126eeccd93560d94d2f01e153fe")
    version("1.2.1", sha256="d8ac1a78287a9ea9e6a0e350886dbef8902f5f1dcba9bbc25afafe2ed2ca0a95")
    version("1.2.0", sha256="e879e6bf662e07cff2962b68529dd78c3bafb67541aaa76e8c9d25ecb505b850")
    version("1.1.2", sha256="31da99483ee6110d43ed5e7c56a59f40f33b389e45d09d91fca022b42d442040")
    version("1.1.1", sha256="98cae3e4b32514e51fcc1ed07fdbe6929d4b80942925348cc6e57b308d9c4cb0")
    version("1.1.0", sha256="2429b4ac76ad8520b99e7167dbb70c8e0088b5fad2c79f799e22b7d137d5fc33")
    version("1.0.0", sha256="34b72116ab6db9bdb97bc1e49dadf392a1619838204b44b0a4695539d54ffbe8")
    version("0.9.0", sha256="70efd66e662fcd93bbc6cf2f8c3104a1de7e52090f709e9040a34bdc7c72ea9c")
    version("0.8.6", sha256="feede818e814011207c5bfeaf06dd9fc95825c59ab70942aa9b9314791c5d6b6")
    version("0.7.5", sha256="f892aaf7a0a7852e12d01b2ced6c2484fb6dc5fe7562abdf0c44a2d08aa52618")

    depends_on("rust")

    sanity_check_is_file = [join_path("bin", "dust")]

    def install(self, spec, prefix):
        cargo = which("cargo", required=True)
        cargo("install", "--root", prefix, "--path", ".")

    @run_after("install")
    def check_install(self):
        dust = Executable(join_path(self.prefix.bin, "dust"))
        output = dust("--version", output=str.split)
        assert "Dust " in output

    def test_run(self):
        """check dust can execute (with option '--version')"""
        dust = which(self.prefix.bin.dust, required=True)
        out = dust("--version", output=str.split, error=str.split)
        assert "Dust " in out
