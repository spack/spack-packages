# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Charliecloud(AutotoolsPackage):
    """Lightweight user-defined software stacks for HPC."""

    maintainers("j-ogas", "reidpr", "loshak")
    homepage = "https://charliecloud.io/"
    url = "https://gitlab.com/charliecloud/charliecloud/-/archive/v0.42/main-v0.42.tar.gz"
    git = "https://gitlab.com/charliecloud/charliecloud.git"

    tags = ["e4s"]

    license("Apache-2.0")

    version("main", branch="main")
    version("0.42", sha256="be98c025f58336a7b6e6d79804ef89dd489c5dcc5ad8faccb551ea0065dcd13a")
    version("0.41", sha256="065cc50f8b7893f8a0e28d9d06e2e3640d0d8139d10ad59fe941aea1e33dfdc6")
    version("0.40", sha256="dcad81136d1fed905be6e573a7bf191ea655ae7827f7980bbe6559942f2affdd")
    version("0.39", sha256="38503b507119a970ac288df7181aefe6cd1a125b9d509f5cb162dacea7143fd1")
    version("0.38", sha256="1a3766d57ff4db9c65fd5c561bbaac52476c9a19fa10c1554190912a03429b7a")
    version("0.37", sha256="1fd8e7cd1dd09a001aead5e105e3234792c1a1e9e30417f495ab3f422ade7397")
    version("0.36", sha256="b6b1a085d8ff82abc6d625ab990af3925c84fa08ec837828b383f329bd0b8e72")
    version("0.35", sha256="042f5be5ed8eda95f45230b4647510780142a50adb4e748be57e8dd8926b310e")

    variant("docs", default=False, description="Build man pages and html docs")
    variant("squashfuse", default=True, description="Build with squashfuse support")
    variant("cdi", default=True, description="Build with CDI support", when="@0.40:")

    depends_on("c", type="build")  # generated
    depends_on("bdw-gc", type=("build", "link"))
    depends_on("bdw-gc@8:", type=("build", "link"), when="@0.40:")

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

    with when("+cdi"):
        # Require cjson for CDI support
        depends_on("cjson", type="build", when="@0.40:")

    def url_for_version(self, version):
        if version >= Version("0.39"):
            url_fmt = "https://gitlab.com/charliecloud/main/-/archive/v{0}/main-v{0}.tar.gz"
        else:
            url_fmt = "https://github.com/hpc/charliecloud/releases/download/v{0}/charliecloud-{0}.tar.gz"
        return url_fmt.format(version)

    @property
    def force_autoreconf(self):
        return self.spec.satisfies("@0.39:")

    def autoreconf(self, spec, prefix):
        which("bash")("autogen.sh")

    def configure_args(self):
        args = ["--with-python=/usr/bin/env python3"]

        if self.spec.satisfies("+docs"):
            sphinx_bin = f"{self.spec['py-sphinx'].prefix.bin}"
            args.append("--enable-html")
            args.append(f"--with-sphinx-build={sphinx_bin.join('sphinx-build')}")
        else:
            args.append("--disable-html")

        if self.spec.satisfies("+squashfuse"):
            if self.spec.satisfies("@:0.39"):
                args.append(f"--with-libsquashfuse={self.spec['squashfuse'].prefix}")
            else:
                # Version 0.40+ uses a new syntax for squashfuse
                args.append(f"--with-squashfuse-include={self.spec['squashfuse'].prefix}/include")
                args.append(f"--with-squashfuse-lib={self.spec['squashfuse'].prefix}/lib")
        else:
            if self.spec.satisfies("@:0.39"):
                args.append("--with-libsquashfuse=no")
            else:
                args.append("--with-squashfuse=no")

        if "+cdi" in self.spec and self.spec.satisfies("@0.40:"):
            cjson_spec = self.spec["cjson"]
            args.append("--with-json=yes")
            args.append(f"--with-json-include={cjson_spec.prefix.include}")
            args.append(f"--with-json-lib={cjson_spec.libs.directories[0]}")

        return args

    # libexec/charliecloud/sotest/bin/sotest misses an rpath, but shouldn't be problematic.
    unresolved_libraries = ["libsotest.so.*"]
