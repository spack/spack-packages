# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Charliecloud(AutotoolsPackage):
    """Lightweight user-defined software stacks for HPC."""

    maintainers("j-ogas", "reidpr")
    homepage = "https://hpc.github.io/charliecloud"
    url = "https://github.com/hpc/charliecloud/releases/download/v0.18/charliecloud-0.18.tar.gz"
    git = "https://github.com/hpc/charliecloud.git"

    tags = ["e4s"]

    license("Apache-2.0")

    version("master", branch="master")
    version("0.38", sha256="1a3766d57ff4db9c65fd5c561bbaac52476c9a19fa10c1554190912a03429b7a")
    version("0.37", sha256="1fd8e7cd1dd09a001aead5e105e3234792c1a1e9e30417f495ab3f422ade7397")
    version("0.36", sha256="b6b1a085d8ff82abc6d625ab990af3925c84fa08ec837828b383f329bd0b8e72")
    version("0.35", sha256="042f5be5ed8eda95f45230b4647510780142a50adb4e748be57e8dd8926b310e")

    variant("docs", default=False, description="Build man pages and html docs")
    variant("squashfuse", default=True, description="Build with squashfuse support")

    depends_on("c", type="build")  # generated

    # Autoconf.
    depends_on("m4", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    # pkg-config is required for 0.36 regardless of variant.
    depends_on("pkgconfig", type="build", when="@0.36")

    # Image manipulation.
    depends_on("python@3.6:", type="run")
    depends_on("py-requests", type="run")
    depends_on("git@2.28.1:", type="run")  # build cache

    # Man page and html docs.
    depends_on("rsync", type="build", when="+docs")
    depends_on("py-sphinx", type="build", when="+docs")
    depends_on("py-sphinx-rtd-theme", type="build", when="+docs")

    # Bash automated testing harness (bats).
    depends_on("bats@1.10.0:")

    # Require pip and wheel for git checkout builds (master).
    depends_on("py-pip@21.1.2:", type="build", when="@master")
    depends_on("py-wheel", type="build", when="@master")

    # See https://github.com/spack/spack/pull/16049.
    conflicts("platform=darwin", msg="This package does not build on macOS")

    # Squashfuse support. For why this is so messy, see:
    # https://github.com/hpc/charliecloud/issues/1696
    # https://github.com/hpc/charliecloud/pull/1697
    # https://github.com/hpc/charliecloud/pull/1784
    #
    # FIXME: the current variant and dependencies reflect
    # Charliecloud's automatic mount/un-mounting requirements. A more manual
    # approach with squashfuse could implemented in a different variant.
    with when("+squashfuse"):
        depends_on("libfuse@3:", type=("build", "run", "link"))
        depends_on("pkgconfig", type="build", when="@0.37:")
        depends_on("squashfuse@0.1.105:0.2.0,0.4.0:", type="link", when="@0.36:")
        depends_on("squashfuse@0.1.105:0.2.0,0.4.0", type="link", when="@0.35")

    def autoreconf(self, spec, prefix):
        which("bash")("autogen.sh")

    def configure_args(self):
        args = [f"--with-python={self.spec['python'].command.path}"]

        if self.spec.satisfies("+docs"):
            sphinx_bin = f"{self.spec['py-sphinx'].prefix.bin}"
            args.append("--enable-html")
            args.append(f"--with-sphinx-build={sphinx_bin.join('sphinx-build')}")
        else:
            args.append("--disable-html")

        if self.spec.satisfies("+squashfuse"):
            args.append(f"--with-libsquashfuse={self.spec['squashfuse'].prefix}")
        else:
            args.append("--with-libsquashfuse=no")

        return args

    # libexec/charliecloud/sotest/bin/sotest misses an rpath, but shouldn't be problematic.
    unresolved_libraries = ["libsotest.so.*"]
