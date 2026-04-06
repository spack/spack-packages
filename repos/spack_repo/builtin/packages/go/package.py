# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

# - vanilla CentOS 7, and possibly other systems, fail a test:
#   TestCloneNEWUSERAndRemapRootDisableSetgroups
#
#   The Fix, discussed here: https://github.com/golang/go/issues/16283
#   is to enable "user_namespace".
#
#   On a Digital Ocean image, this can be achieved by updating
#   `/etc/default/grub` so that the `GRUB_CMDLINE_LINUX` variable
#   includes `user_namespace.enable=1`, re-cooking the grub
#   configuration with `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`,
#   and then rebooting.
#
# - on CentOS 7 systems (and possibly others) you need to have the
#   glibc package installed or various static cgo tests fail.
#


class Go(Package):
    """The golang compiler and build environment"""

    homepage = "https://go.dev"
    url = "https://go.dev/dl/go1.20.2.src.tar.gz"
    git = "https://go.googlesource.com/go.git"

    extendable = True
    executables = ["^go$"]
    unresolved_libraries = ["libtiff.so.*"]  # go/src/debug/elf/testdata/libtiffxx.so_
    tags = ["build-tools"]

    maintainers("alecbcs")

    license("BSD-3-Clause")

    version("1.26.1", sha256="3172293d04b209dc1144698e7ba13f0477f6ba8c5ffd0be66c20fdbc9785dfbb")
    version("1.25.8", sha256="e988d4a2446ac7fe3f6daa089a58e9936a52a381355adec1c8983230a8d6c59e")
    version("1.25.7", sha256="178f2832820274b43e177d32f06a3ebb0129e427dd20a5e4c88df2c1763cf10a")
    version("1.25.6", sha256="58cbf771e44d76de6f56d19e33b77d745a1e489340922875e46585b975c2b059")
    version("1.25.5", sha256="22a5fd0a91efcd28a1b0537106b9959b2804b61f59c3758b51e8e5429c1a954f")
    version("1.25.4", sha256="160043b7f17b6d60b50369436917fda8d5034640ba39ae2431c6b95a889cc98c")
    version("1.25.3", sha256="a81a4ba593d0015e10c51e267de3ff07c7ac914dfca037d9517d029517097795")
    version("1.25.2", sha256="3711140cfb87fce8f7a13f7cd860df041e6c12f7610f40cac6ec6fa2b65e96e4")
    version("1.25.1", sha256="d010c109cee94d80efe681eab46bdea491ac906bf46583c32e9f0dbb0bd1a594")
    version("1.24.12", sha256="fba2dd661b7be7b34d6bd17ed92f41c44a5e05953ad81ab34b4ec780e5e7dc41")
    version("1.24.11", sha256="ffdf97766a4c4b135cd53809713978e9ee1a943b2c8e28ad221a5429de30e210")
    version("1.24.10", sha256="34000dcc47a517b78fcf2657ee7d033328a57079fe60c4ed8b7b84260d1d19d3")
    version("1.24.7", sha256="2a8f50db0f88803607c50d7ea8834dcb7bd483c6b428a91e360fdf8624b46464")
    version("1.24.6", sha256="e1cb5582aab588668bc04c07de18688070f6b8c9b2aaf361f821e19bd47cfdbd")
    version("1.24.4", sha256="5a86a83a31f9fa81490b8c5420ac384fd3d95a3e71fba665c7b3f95d1dfef2b4")
    version("1.24.3", sha256="229c08b600b1446798109fae1f569228102c8473caba8104b6418cb5bc032878")
    version("1.24.2", sha256="9dc77ffadc16d837a1bf32d99c624cb4df0647cee7b119edd9e7b1bcc05f2e00")
    version("1.24.1", sha256="8244ebf46c65607db10222b5806aeb31c1fcf8979c1b6b12f60c677e9a3c0656")
    version("1.24.0", sha256="d14120614acb29d12bcab72bd689f257eb4be9e0b6f88a8fb7e41ac65f8556e5")
    version("1.23.12", sha256="e1cce9379a24e895714a412c7ddd157d2614d9edbe83a84449b6e1840b4f1226")
    version("1.23.10", sha256="800a7ae1bff179a227b653a2f644517c800443b8b4abf3273af5e1cb7113de59")
    version("1.23.9", sha256="08f6419547563ed9e7037d12b9c8909677c72f75f62ef85887ed9dbf49b8d2dd")
    version("1.23.8", sha256="0ca1f1e37ea255e3ce283af3f4e628502fb444587da987a5bb96d6c6f15930d4")
    version("1.23.7", sha256="7cfabd46b73eb4c26b19d69515dd043d7183a6559acccd5cfdb25eb6b266a458")
    version("1.23.6", sha256="039c5b04e65279daceee8a6f71e70bd05cf5b801782b6f77c6e19e2ed0511222")
    version("1.23.5", sha256="a6f3f4bbd3e6bdd626f79b668f212fbb5649daf75084fb79b678a0ae4d97423b")
    version("1.23.4", sha256="ad345ac421e90814293a9699cca19dd5238251c3f687980bbcae28495b263531")
    version("1.23.3", sha256="8d6a77332487557c6afa2421131b50f83db4ae3c579c3bc72e670ee1f6968599")
    version("1.23.2", sha256="36930162a93df417d90bd22c6e14daff4705baac2b02418edda671cdfa9cd07f")
    version("1.23.1", sha256="6ee44e298379d146a5e5aa6b1c5b5d5f5d0a3365eabdd70741e6e21340ec3b0d")
    version("1.22.12", sha256="012a7e1f37f362c0918c1dfa3334458ac2da1628c4b9cf4d9ca02db986e17d71")
    version("1.22.8", sha256="df12c23ebf19dea0f4bf46a22cbeda4a3eca6f474f318390ce774974278440b8")
    version("1.22.7", sha256="66432d87d85e0cfac3edffe637d5930fc4ddf5793313fe11e4a0f333023c879f")
    version("1.22.6", sha256="9e48d99d519882579917d8189c17e98c373ce25abaebb98772e2927088992a51")
    version("1.22.4", sha256="fed720678e728a7ca30ba8d1ded1caafe27d16028fab0232b8ba8e22008fb784")

    provides("golang")

    depends_on("bash", type="build")
    depends_on("grep", type="build")
    depends_on("sed", type="build")

    depends_on("go-or-gccgo-bootstrap@1.24:", type="build", when="@1.26:")
    depends_on("go-or-gccgo-bootstrap@1.22:", type="build", when="@1.24:")
    depends_on("go-or-gccgo-bootstrap@1.20:", type="build", when="@1.22:")
    depends_on("go-or-gccgo-bootstrap", type="build")

    phases = ["build", "install"]

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def url_for_version(self, version):
        return f"https://go.dev/dl/go{version}.src.tar.gz"

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("version", output=str, error=str)
        match = re.search(r"go version go(\S+)", output)
        return match.group(1) if match else None

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # We need to set CC/CXX_FOR_TARGET, otherwise cgo will use the
        # internal Spack wrappers and fail.
        env.set("CC_FOR_TARGET", self["c"].cc)
        env.set("CXX_FOR_TARGET", self["cxx"].cxx)
        env.set("GOMAXPROCS", str(make_jobs))

    def build(self, spec, prefix):
        # Build script depend on bash
        bash = which("bash", required=True)

        with working_dir("src"):
            bash(f"{'all' if self.run_tests else 'make'}.bash")

    def install(self, spec, prefix):
        install_tree(".", prefix.go)
        symlink(prefix.go.bin, prefix.bin)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("GO111MODULE", "on")
        env.set("GOTOOLCHAIN", "local")
        env.set("GOMAXPROCS", str(make_jobs))
        env.set("GOPATH", join_path(dependent_spec.package.stage.path, "go"))

    def setup_dependent_package(self, module, dependent_spec):
        """Called before go modules' build(), install() methods.

        go('get', '<package>', env=env)
        install_tree('bin', prefix.bin)
        """
        #  Add a go command/compiler for extensions
        module.go = self.command
