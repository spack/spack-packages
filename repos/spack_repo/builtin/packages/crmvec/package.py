# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import json

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Crmvec(MakefilePackage):
    """Correctly rounded vector math for Linux programs. libmvec.so.1 is a
    drop-in for glibc's vector math library (and, on aarch64, for SLEEF's
    libsleefgnuabi.so.3) whose results are CORE-MATH's correctly rounded ones;
    libcrpreload.so provides CORE-MATH's scalar functions under the C library's
    names for LD_PRELOAD. The libraries install to lib/crmvec and are used
    through crmvec-run, crmvec-stamp or pkg-config, never system-wide."""

    homepage = "https://github.com/anun333/crmvec"
    url = "https://github.com/anun333/crmvec/archive/refs/tags/v0.12.2.tar.gz"

    test_requires_compiler = True

    maintainers("anun333")

    license("MIT", checked_by="anun333")

    version("0.12.2", sha256="174de208c2e7bf2d866e88152fe8448989b6138eb13153d25efd0384acb07ec3")

    depends_on("c", type="build")
    # the aarch64 rules use grouped targets (GNU make 4.3)
    depends_on("gmake@4.3:", type="build", when="target=aarch64:")
    # the x86 intrinsics on aarch64; header-only, and the compiler wrapper adds -I
    # only for a link dependency
    depends_on("simde", type="link", when="target=aarch64:")
    # make check runs mpfrcheck, and checks f16check against MPFR, with MPFR 4.2 or later
    depends_on("mpfr@4.2:", type="test")

    requires("platform=linux", msg="crmvec is a drop-in for glibc's libmvec and libm")
    requires(
        "target=x86_64:",
        "target=aarch64:",
        policy="one_of",
        msg="crmvec builds for x86_64 and aarch64",
    )
    requires("%gcc", msg="crmvec builds with GCC (crmvec.c refuses clang on x86_64)")
    # __bf16 arithmetic needs GCC 13 (the Makefile's cc-check stops an older one)
    conflicts("%gcc@:12", msg="crmvec needs GCC 13 or newer")

    build_targets = ["lib"]

    sanity_check_is_file = [
        "bin/crmvec-run",
        "bin/crmvec-stamp",
        "include/crmvec.h",
        "lib/crmvec/libmvec.so.1",
        "lib/crmvec/libcrpreload.so",
        "lib/pkgconfig/crmvec.pc",
    ]

    @property
    def install_targets(self):
        return ["install", f"PREFIX={self.prefix}"]

    def check(self):
        # The compiler wrapper adds no -I or -L for a test dependency, so MPFR's
        # are passed here; mpfr.h includes gmp.h, a dependency of mpfr's
        mpfr = self.spec["mpfr"]
        headers = mpfr.headers
        if "gmp" in mpfr:
            headers += mpfr["gmp"].headers
        rpaths = " ".join(f"-Wl,-rpath,{d}" for d in mpfr.libs.directories)
        make("check", f"CFLAGS=-O2 {headers.include_flags} {mpfr.libs.search_flags} {rpaths}")

    def test_version(self):
        """check that crmvec-run and crmvec-stamp report the version"""
        for tool in ["crmvec-run", "crmvec-stamp"]:
            exe = which(join_path(self.prefix.bin, tool), required=True)
            out = exe("--version", output=str.split, error=str.split)
            assert f"{tool} {self.spec.version}" in out

    def test_smoke(self):
        """build a program against the library, run it with libcrpreload.so and stamp the run"""
        lib_dir = join_path(self.prefix.lib, "crmvec")
        src = join_path(self.test_suite.current_test_data_dir, "crmvec_smoke.c")
        cc = which(self.spec["c"].package.cc, required=True)
        cc(
            f"-I{self.prefix.include}",
            src,
            "-o",
            "crmvec_smoke",
            f"-L{lib_dir}",
            f"-Wl,-rpath,{lib_dir}",
            "-lmvec",
        )
        expected = f"{self.spec.version} 3c00 4170 1 1024"

        smoke = which("./crmvec_smoke", required=True)
        out = smoke(output=str.split, error=str.split)
        assert expected in out

        crmvec_run = which(join_path(self.prefix.bin, "crmvec-run"), required=True)
        mkdirp("stamp")
        out = crmvec_run(
            "--libm", "--stamp", "stamp", "./crmvec_smoke", output=str.split, error=str.split
        )
        assert expected in out
        assert "cannot be preloaded" not in out
        with open(join_path("stamp", "crmvec-libm.json")) as f:
            stamp = json.load(f)
        assert stamp["Version"] == str(self.spec.version)
        assert "libcrpreload.so" in stamp["ScalarMath"]
