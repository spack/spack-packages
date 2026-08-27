# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Hmpi(Package):
    """HMPI wrapper for HPCKit - provides mpi virtual package."""

    homepage = "https://www.hikunpeng.com/developer/hpc/hpckit-download"

    license("UNKNOWN", checked_by="github_user1")

    version(
        "25.1.0",
        url="https://mirrors.huaweicloud.com/kunpeng/archive/HPC/HPCKit/HPCKit_25.1.0_Linux-aarch64.tar.gz",
        sha256="e58a43cebf0cea071ee69c0106a7edaaec9a6fb7022f13d091a0bd43bf85e2d5",
    )

    depends_on("hpckit@25.1.0", when="@25.1.0:")

    provides("mpi")

    variant(
        "compiler_variant",
        default="gcc",
        values=("gcc", "bisheng"),
        multi=False,
        description="Compiler variant for HMPI",
    )

    def _get_hmpi_prefix(self):
        """Get HMPI prefix from the hpckit dependency."""
        hpckit_prefix = self.spec["hpckit"].prefix
        compiler_var = self.spec.variants["compiler_variant"].value
        return os.path.join(
            hpckit_prefix,
            "HPCKit",
            str(self.spec["hpckit"].version),
            "hmpi",
            compiler_var,
            "release",
            "hmpi",
        )

    def _get_hucx_prefix(self):
        """Get HUCX prefix from the hpckit dependency."""
        hpckit_prefix = self.spec["hpckit"].prefix
        compiler_var = self.spec.variants["compiler_variant"].value
        return os.path.join(
            hpckit_prefix,
            "HPCKit",
            str(self.spec["hpckit"].version),
            "hmpi",
            compiler_var,
            "release",
            "hucx",
        )

    def _get_xucg_prefix(self):
        """Get XUCG prefix from the hpckit dependency."""
        hpckit_prefix = self.spec["hpckit"].prefix
        compiler_var = self.spec.variants["compiler_variant"].value
        return os.path.join(
            hpckit_prefix,
            "HPCKit",
            str(self.spec["hpckit"].version),
            "hmpi",
            compiler_var,
            "release",
            "xucg",
        )

    def _mpi_bin(self, name):
        return os.path.join(self._get_hmpi_prefix(), "bin", name)

    @property
    def libs(self):
        lib_dir = os.path.join(self._get_hmpi_prefix(), "lib")
        if os.path.isdir(lib_dir):
            libs = find_libraries(["libmpi"], lib_dir, shared=True, recursive=False)
            if libs:
                return libs
        return LibraryList([])

    @property
    def headers(self):
        include_dir = os.path.join(self._get_hmpi_prefix(), "include")
        return find_headers(["mpi"], include_dir, recursive=False)

    def setup_run_environment(self, env):
        hmpi = self._get_hmpi_prefix()
        hucx = self._get_hucx_prefix()
        xucg = self._get_xucg_prefix()

        bin_dir = os.path.join(hmpi, "bin")
        if os.path.isdir(bin_dir):
            env.prepend_path("PATH", bin_dir)

        for lib_dir in [
            os.path.join(hmpi, "lib"),
            os.path.join(hucx, "lib"),
            os.path.join(xucg, "lib"),
        ]:
            if os.path.isdir(lib_dir):
                env.prepend_path("LD_LIBRARY_PATH", lib_dir)

        for include_dir in [
            os.path.join(hmpi, "include"),
            os.path.join(hucx, "include"),
            os.path.join(xucg, "include"),
        ]:
            if os.path.isdir(include_dir):
                env.prepend_path("CPATH", include_dir)
                env.prepend_path("INCLUDE", include_dir)

        env.set("MPICC", self._mpi_bin("mpicc"))
        env.set("MPICXX", self._mpi_bin("mpic++"))
        env.set("MPIF77", self._mpi_bin("mpif77"))
        env.set("MPIF90", self._mpi_bin("mpif90"))
        env.set("MPIFC", self._mpi_bin("mpifort"))
        env.set("OPAL_PREFIX", hmpi)

    def setup_dependent_package(self, module, dependent_spec):
        spec = self.spec
        spec.mpicc = self._mpi_bin("mpicc")
        spec.mpicxx = self._mpi_bin("mpic++")
        spec.mpif77 = self._mpi_bin("mpif77")
        spec.mpif90 = self._mpi_bin("mpif90")
        spec.mpifc = self._mpi_bin("mpifort")

    def setup_dependent_build_environment(self, env, dependent_spec):
        hmpi = self._get_hmpi_prefix()
        hucx = self._get_hucx_prefix()
        xucg = self._get_xucg_prefix()

        for lib_dir in [
            os.path.join(hmpi, "lib"),
            os.path.join(hucx, "lib"),
            os.path.join(xucg, "lib"),
        ]:
            if os.path.isdir(lib_dir):
                env.prepend_path("LD_LIBRARY_PATH", lib_dir)
                env.prepend_path("LIBRARY_PATH", lib_dir)

        bin_dir = os.path.join(hmpi, "bin")
        if os.path.isdir(bin_dir):
            env.prepend_path("PATH", bin_dir)

        for include_dir in [
            os.path.join(hmpi, "include"),
            os.path.join(hucx, "include"),
            os.path.join(xucg, "include"),
        ]:
            if os.path.isdir(include_dir):
                env.prepend_path("CPATH", include_dir)
                env.prepend_path("INCLUDE", include_dir)

        env.set("OPAL_PREFIX", hmpi)

    def install(self, spec, prefix):
        mkdirp(prefix)
        with open(os.path.join(prefix, ".spack_wrapper"), "w") as f:
            f.write("This is a wrapper package for hpckit\n")
