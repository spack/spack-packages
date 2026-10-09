# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Centrifuge(MakefilePackage):
    """Classifier for metagenomic sequences."""

    homepage = "https://ccb.jhu.edu/software/centrifuge/index.shtml"
    url = "https://github.com/DaehwanKimLab/centrifuge/archive/refs/tags/v1.0.4.tar.gz"

    version("1.0.4.1", sha256="638cc6701688bfdf81173d65fa95332139e11b215b2d25c030f8ae873c34e5cc")
    version("1.0.4", sha256="929daed0f84739f7636cc1ea2757527e83373f107107ffeb5937a403ba5201bc")

    depends_on("cxx", type="build")  # generated

    def flag_handler(self, name, flags):
        if name == "cxxflags" and self.spec.satisfies("target=aarch64:"):
            flags.append("-fsigned-char")
        return (flags, None, None)

    # Adds arm compilation support
    patch(
        "https://patch-diff.githubusercontent.com/raw/DaehwanKimLab/centrifuge/pull/291.patch?full_index=1",
        sha256="2e09ccfdd1812b2f2de6b00a265e20f89569b7fcae3d54e3124344b5ea5a40f0",
        when="target=aarch64:",
    )

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        make("install", "prefix=" + prefix)
