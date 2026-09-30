# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


def debian_patch(name, sha256, **kwargs):
    """Patch from the debian/patches series of Debian's csh source package."""
    url = f"https://sources.debian.org/data/main/c/csh/20240808-4/debian/patches/{name}"
    patch(url, sha256=sha256, **kwargs)


class Csh(MakefilePackage):
    """The original BSD C shell: OpenBSD's csh(1), via Debian's csh source package.

    This is plain csh, without tcsh extensions.
    """

    homepage = "https://tracker.debian.org/pkg/csh"
    url = "https://deb.debian.org/debian/pool/main/c/csh/csh_20240808.orig.tar.xz"

    maintainers("tgamblin")

    license("BSD-3-Clause")

    version("20240808", sha256="df916baa73c264516177c6667cc0a061f6eb9743f862b625f17067d74a3f4d1c")

    depends_on("c", type="build")
    depends_on("libbsd", when="platform=linux")

    # Debian's patches, applied in series order. glibc portability patches are
    # linux-only; the arithmetic fix and pledge(2) removal (an OpenBSD-only
    # syscall) apply everywhere.
    with when("platform=linux"):
        debian_patch(
            "02_libbsd.diff",
            sha256="bdb992adcbf17794b7d5cd2912c4d92c22b612d6234e7e27ddc2715e4e92ebff",
        )
        debian_patch(
            "03_maxpathlen.diff",
            sha256="418cd4c77faf52f62765287e5513eaef97e475d9cfb6d434953bf2001b4b61b2",
        )
        debian_patch(
            "04_fpurge.diff",
            sha256="a3acaa94c88eb02878f98fa034780380732fec3b278552ed40a208cfc21bea24",
        )
        debian_patch(
            "06_time_h_for_time_t.diff",
            sha256="8eb5fc09dee920fd3042d87ab51ba3946699e36dfb00b8a257ca01730b92907c",
        )
        debian_patch(
            "07_funopen.diff",
            sha256="28d5e49a1470ea9b4160ae3695207abfb00c6b1f7446c467bc34b35403664a0b",
        )
        debian_patch(
            "08_glob.diff",
            sha256="db0e90b343560a52cd27425b8757796b137887fe51b12e7b1f428ae7cc5cc3cd",
        )
        debian_patch(
            "09_sys_signame.diff",
            sha256="f8b105923f58bf29b986da51cc9278491a3545fdeb30bd8c4ed88e1a4605ccfd",
        )
    debian_patch(
        "13_fix_arithmetic_precedence.diff",
        sha256="20343669212e4ee64aeb56b61a4d064d5640e0f62fd78df1f3b57d7943196dd5",
    )
    with when("platform=linux"):
        debian_patch(
            "15_glibc-strsignal.diff",
            sha256="1fb4aa794b15197d4a8e731974ac2c244e6de21b16487d51b3179972b5e77f9b",
        )
        debian_patch(
            "16_missing_tiocstat.diff",
            sha256="03357ae8ccac6274550222e43223d01f18dc9a05e56ad0ba0846663a3eb0ec7f",
        )
    debian_patch(
        "17_no_pledge.diff",
        sha256="0ef230820c3a10ee03b6e5a45be281ed818bb3541668273baecf09152512ddeb",
    )
    with when("platform=linux"):
        debian_patch(
            "18_g++-14.diff",
            sha256="bbdc19b94f8ffad7600e7386018b3321bc4ebd70c0bd327ddc3512eeb86ee538",
        )

    # use in-tree xmalloc/xreallocarray in Debian's glob code instead of publib
    patch("no-publib.patch", when="platform=linux")

    # closefrom(3) needs libbsd's declaration before glibc 2.34
    patch("linux-closefrom.patch", when="platform=linux")

    # shims for OpenBSD-isms missing from Darwin libc
    patch("macos-compat.patch", when="platform=darwin")

    sanity_check_is_file = [join_path("bin", "csh")]

    def edit(self, spec, prefix):
        # upstream's BSD Makefile requires bsd.prog.mk; GNU make prefers
        # GNUmakefile, so ours takes over without touching the original
        copy(join_path(self.package_dir, "GNUmakefile"), "GNUmakefile")

    @property
    def install_targets(self):
        return ["install", f"PREFIX={self.prefix}"]

    def test_run(self):
        """run a simple csh script"""
        csh = Executable(self.prefix.bin.csh)
        out = csh("-f", "-c", "set x = (a b c); echo $x[2-]:q", output=str)
        assert "b c" in out
