# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Colima(MakefilePackage):
    """Container runtimes on MacOS (and Linux) with minimal setup."""

    homepage = "https://github.com/abiosoft/colima/blob/main/README.md"
    url = "https://github.com/abiosoft/colima/archive/refs/tags/v0.9.1.tar.gz"
    git = "https://github.com/abiosoft/colima"

    maintainers = ["becker33"]

    version("0.9.1", sha256="1fe95da6dbe584783e2ae521759aaacd3ba52bd6c44632f95b5adc0d97345460")
    version("0.9.0", sha256="c4a0f15f971d876ab4a725df802c7888abc73b9384c9df295c7e4ac888d276c5")
    version("0.8.4", sha256="e02f3abf3ad7911fe4665b1c3291f03677edc0efa93e8d37b337d76149a7202b")
    version("0.8.3", sha256="2c0f670f2e3124d1e81894bc3c0bea90f25cc675bb293e70e8ff25f47c8db35e")
    version("0.8.2", sha256="c076bc9bf984f42d7f3b47b09cec9859f5fc715a0410d5e2e8263cc9cb05b864")
    version("0.8.1", sha256="9af9e1de6adc3590d852857e10c2846a167c331c40b6704fe71ac97b8bcda6ab")
    version("0.8.0", sha256="0040a1832a1e89cbffec9311382344546cb5965384bede079325dac8b2cbf4f0")
    version("0.7.6", sha256="97a3130023e00b5e1a73a24167e958e7135f69a742ab555993a0d6033f31b60e")
    version("0.7.5", sha256="88e37091e64d632ec44e5284665e5adc6506000acb13102fa2bbc67790770a3d")
    version("0.7.4", sha256="3e6d265378c1cfa17c8c041bcb1115e8ab02654756c327be258aff2276f2cf10")

    depends_on("go")
    depends_on("openssl", type="build")

    def edit(self, spec, prefix):
        filter_file(r"/usr/local/bin", prefix.bin, "Makefile", string=True)
