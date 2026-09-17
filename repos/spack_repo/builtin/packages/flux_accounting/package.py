# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class FluxAccounting(AutotoolsPackage):
    """Bank/accounting interface for the Flux resource manager"""

    homepage = "https://github.com/flux-framework/flux-accounting"
    url = "https://github.com/flux-framework/flux-accounting/releases/download/v0.1.0/flux-accounting-0.1.0.tar.gz"
    git = "https://github.com/flux-framework/flux-accounting.git"

    maintainers("sam-maloney")

    license("LGPL-3.0-only")

    version("main", branch="main")
    version("0.61.0", sha256="e542871141ed7f63c513bbec6ee7e1f3521cb82f8cb796cf022c5d60f41a3c36")
    version("0.60.0", sha256="fbeba425cc40377abc9e7486866ecd4372d7a494b2d5a0aeafc4103e141b34ef")
    version("0.59.1", sha256="8f47d7b019711bc33985d75dd576de3a6defdc6ef53e4beaff6254e3185dcdac")
    version("0.59.0", sha256="a49fc39848ac9329ab6232fd64a1f1e50022520bb20117b89415616b5b2f267e")
    version("0.58.0", sha256="3cc82933b9d3c4a40678e6f234da9e8227afdc0736a329139570cf29c498b765")
    version("0.57.2", sha256="8a75cb5b44149687ae120fb788061fcc20c3e286b96277af74bed747e3ecd2ad")
    version("0.57.1", sha256="8cfb8c2c5455601dcc3e0f2856cd0dba5acdf0e4b093a1f20a0d5bcacb9d7285")
    version("0.57.0", sha256="9cecd797f528c24893827abbbaf1af21e8a010c36e238bae45ecb6f1650c2e8b")
    version("0.56.0", sha256="c9e7dabd32215d00d67cda873425f3ea0f820468351df7ba3e2072e40d80d4e0")
    version("0.55.0", sha256="06c57d6a0c21be6c1c330fd934ab8324740e13a8bfb22f64fb701e6b14d11892")
    version("0.54.0", sha256="46f446581c631b089ecc264b239f54da97c66f98d8a636b24342af659788e474")
    version("0.53.0", sha256="96a175d090b7348a1caf511bee5d359cd13f7f9118f37e23a5077ec030bf3a76")
    version("0.52.0", sha256="37b38aa64d25da0ac0301b32a348150f4065cf7d1236f9a247706f7d8c5611e5")
    version("0.51.0", sha256="695bcdd5b309a868d5a2bcb3edca539a82f23d28c7cb7d1c78a74a68fe20bb81")
    version("0.50.0", sha256="7d680eac41392914cad91e62c0cb71db4c9cd62eb155b342d64fd2ee2335cff9")
    version("0.49.0", sha256="384f499215083223f751a363c1bf06d3bafd3f5a21a4360a9ecd8ec7009c3e2b")
    version("0.48.0", sha256="44e1e7091e10dedf64af5e7dc279e49d9034cdfefff141ac3d014f64a233f71a")
    version("0.47.0", sha256="2e998b8d60c4779ccad56931e3c606f0c6a5933b9162da4e1539ebf4e429237f")
    version("0.46.0", sha256="552604291bee427d0e5b126045fcdaf49e8c9aac478c5022971e88b4b1447665")

    variant("docs", default=False, description="Build flux manpages and docs")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build")

    # Need autotools when building on master:
    depends_on("autoconf", type="build", when="@master")
    depends_on("automake", type="build", when="@master")
    depends_on("libtool", type="build", when="@master")

    depends_on("flux-core +security")
    depends_on("flux-core@0.81: +security", when="@0.54.0:")
    depends_on("jansson@2.10:")
    depends_on("sqlite")

    depends_on("py-docutils@0.11.0:", type="build", when="+docs")
    depends_on("py-sphinx@1.6.7:", type="build", when="+docs")
    depends_on("py-sphinx-rtd-theme", type="build", when="+docs")

    # Testing Dependencies
    depends_on("jq", type="test")
    depends_on("lua", type="test")
    depends_on("valgrind", type="test")
    depends_on("which", type="test")

    def setup(self):
        pass

    @when("@master")
    def setup(self):
        with working_dir(self.stage.source_path):
            # Allow git-describe to get last tag so flux-version works:
            git = which("git", required=True)
            # When using spack develop, this will already be unshallow
            try:
                git("fetch", "--unshallow")
                git("config", "remote.origin.fetch", "+refs/heads/*:refs/remotes/origin/*")
                git("fetch", "origin")
            except ProcessError:
                git("fetch")

    def autoreconf(self, spec, prefix):
        self.setup()
        if not os.path.exists("configure"):
            # Bootstrap with autotools
            bash = which("bash", required=True)
            bash("./autogen.sh")

    def configure_args(self):
        args = []
        if "+docs" not in self.spec:
            args.append("--enable-docs=no")
        return args
