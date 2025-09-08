# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Tmalign(Package):
    """TM-align is an algorithm for sequence-order independent protein
    structure comparisons."""

    homepage = "https://zhanggroup.org/TM-align/"
    url = "https://zhanggroup.org/TM-align/TMalign.cpp"

    maintainers("snehring")

    version(
        "20220412",
        sha256="09227c46705ca8cf7c922a6e1672c34d7ed4daba32e5c7c484306808db54117a",
        expand=False,
    )

    variant("fast-math", default=False, description="Enable fast math")

    depends_on("cxx", type="build")

    phases = ["build", "install"]

    def build(self, spec, prefix):
        cxx = Executable(self.compiler.cxx)
        args = ["-O3"]
        if spec.satisfies("+fast-math"):
            args.append("-ffast-math")
        args.extend(["-lm", "-o", "TMalign", "TMalign.cpp"])
        cxx(*args)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("TMalign", prefix.bin)
