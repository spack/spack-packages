# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Kpblas(Package):
    """KML BLAS wrapper for HPCKit - provides blas virtual package."""

    homepage = "https://www.hikunpeng.com/developer/hpc/hpckit-download"

    license("UNKNOWN", checked_by="github_user1")

    version(
        "25.1.0",
        url="https://mirrors.huaweicloud.com/kunpeng/archive/HPC/HPCKit/HPCKit_25.1.0_Linux-aarch64.tar.gz",
        sha256="e58a43cebf0cea071ee69c0106a7edaaec9a6fb7022f13d091a0bd43bf85e2d5",
    )

    depends_on("hpckit@25.1.0", when="@25.1.0:")

    variant(
        "compiler_variant",
        default="gcc",
        values=("gcc", "bisheng"),
        multi=False,
        description="Compiler variant for KML libraries",
    )

    variant(
        "kblas_mode",
        default="multi",
        values=("multi", "locking", "nolocking"),
        multi=False,
        description="KML BLAS threading mode",
    )

    provides("blas")

    @staticmethod
    def _parse_cpuinfo():
        """Parse /proc/cpuinfo and return (implementer, part) strings."""
        implementer = ""
        part = ""
        try:
            with open("/proc/cpuinfo", "r") as fh:
                for line in fh:
                    if line.startswith("CPU implementer"):
                        implementer = line.split(":")[-1].strip()
                    elif line.startswith("CPU part"):
                        part = line.split(":")[-1].strip()
                    if implementer and part:
                        break
        except OSError:
            pass
        return implementer, part

    _ISA_MAP = {
        "0x48-0xd02": "sve",
        "0x48-0xd03": "sve",
        "0x48-0xd06": "sve",
        "0x48-0xd22": "sme",
    }

    @classmethod
    def _detect_isa(cls):
        """Detect ISA subdirectory based on CPU type."""
        implementer, part = cls._parse_cpuinfo()
        cputype = "{0}-{1}".format(implementer, part)
        return cls._ISA_MAP.get(cputype, "neon")

    def _get_kml_prefix(self):
        """Get KML prefix from the hpckit dependency."""
        hpckit_prefix = self.spec["hpckit"].prefix
        compiler_var = self.spec.variants["compiler_variant"].value
        return os.path.join(
            hpckit_prefix, "HPCKit", str(self.spec["hpckit"].version), "kml", compiler_var
        )

    def _lib_dirs(self):
        """Return candidate BLAS library directories in priority order."""
        kml = self._get_kml_prefix()
        mode = self.spec.variants["kblas_mode"].value
        isa = self._detect_isa()
        return [
            os.path.join(kml, "lib", isa, "kblas", mode),
            os.path.join(kml, "lib", isa, "kblas"),
            os.path.join(kml, "lib", isa),
            os.path.join(kml, "lib"),
        ]

    @property
    def libs(self):
        for lib_dir in self._lib_dirs():
            if os.path.isdir(lib_dir):
                libs = find_libraries(["libkblas"], lib_dir, shared=True, recursive=False)
                if libs:
                    return libs
        return LibraryList([])

    @property
    def headers(self):
        include_dir = os.path.join(self._get_kml_prefix(), "include")
        return find_headers(["kblas"], include_dir, recursive=False)

    def setup_run_environment(self, env):
        for lib_dir in self._lib_dirs():
            if os.path.isdir(lib_dir):
                env.prepend_path("LD_LIBRARY_PATH", lib_dir)

        include_dir = os.path.join(self._get_kml_prefix(), "include")
        if os.path.isdir(include_dir):
            env.prepend_path("CPATH", include_dir)
            env.prepend_path("INCLUDE", include_dir)

    def setup_dependent_package(self, module, dependent_spec):
        self.spec.blas_libs = self.libs

    def setup_dependent_build_environment(self, env, dependent_spec):
        for lib_dir in self._lib_dirs():
            if os.path.isdir(lib_dir):
                env.prepend_path("LD_LIBRARY_PATH", lib_dir)
                env.prepend_path("LIBRARY_PATH", lib_dir)

        include_dir = os.path.join(self._get_kml_prefix(), "include")
        if os.path.isdir(include_dir):
            env.prepend_path("CPATH", include_dir)
            env.prepend_path("INCLUDE", include_dir)

    def install(self, spec, prefix):
        # Wrapper 包不需要实际安装，只创建标记文件
        mkdirp(prefix)
        with open(os.path.join(prefix, ".spack_wrapper"), "w") as f:
            f.write("This is a wrapper package for hpckit\n")
