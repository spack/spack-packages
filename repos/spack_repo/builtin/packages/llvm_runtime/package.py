# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os
from collections import OrderedDict

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class LlvmRuntime(Package):
    """Package for LLVM compiler runtime libraries."""

    homepage = "https://llvm.org/"
    has_code = False

    tags = ["runtime"]

    skip_version_audit = ["platform=linux", "platform=darwin"]

    license("Apache-2.0 WITH LLVM-exception")

    depends_on("llvm+clang libcxx=runtime", type="build")

    def install(self, spec, prefix):
        llvm = spec["llvm"]

        if spec.platform == "linux" or spec.platform == "darwin":
            libraries = self._find_libraries(llvm.prefix)
        else:
            raise InstallError(f"unsupported platform: {spec.platform}")

        if not libraries:
            tty.warn("Could not detect any shared LLVM runtime libraries")
            return

        mkdirp(prefix.lib)

        for library in libraries:
            install(library, prefix.lib)

    def _find_libraries(self, llvm_prefix):
        """Find shared LLVM C++ runtime libraries"""
        libraries = []

        for dirname in ("lib", "lib64"):
            libdir = join_path(llvm_prefix, dirname)
            if os.path.isdir(libdir):
                for pattern in (
                    "libc++.so.1",
                    "libc++.so.1.*",
                    "libc++.1.dylib",
                    "libc++abi.so.1",
                    "libc++abi.so.1.*",
                    "libc++abi.1.dylib",
                    "libunwind.so.1",
                    "libunwind.so.1.*",
                    "libunwind.1.dylib",
                ):
                    libraries.extend(glob.glob(join_path(libdir, pattern)))

        return list(OrderedDict.fromkeys(os.path.realpath(p) for p in libraries))
