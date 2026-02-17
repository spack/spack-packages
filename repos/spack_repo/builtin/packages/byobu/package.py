# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Byobu(AutotoolsPackage):
    """Byobu: Text-based window manager and terminal multiplexer."""

    homepage = "https://www.byobu.org/"

    maintainers("ebagrenrut")

    license("GPL-3.0-or-later")

    version("6.13", sha256="9690c629588e8f95d16b2461950d39934faaf8005dd2a283886d4e3bd6c86df6")
    version("5.131", sha256="77ac751ae79d8e3f0377ac64b64bc9738fa68d68466b8d2ff652b63b1d985e52")
    version("5.127", sha256="4bafc7cb69ff5b0ab6998816d58cd1ef7175e5de75abc1dd7ffd6d5288a4f63b")
    version("5.125", sha256="5022c82705a5d57f1d4e8dcb1819fd04628af2d4b4618b7d44fa27ebfcdda9db")
    version("5.123", sha256="2e5a5425368d2f74c0b8649ce88fc653420c248f6c7945b4b718f382adc5a67d")

    variant("python", default=True, description="Python support for byobu-config")

    # byobu 6 source is not pre-autoconfigured
    depends_on("autoconf", when="@6:", type="build")
    depends_on("automake", when="@6:", type="build")
    depends_on("libtool", when="@6:", type="build")

    depends_on("coreutils", type=("build", "run"))
    depends_on("findutils", type=("build", "run"))
    depends_on("gawk", type=("build", "run"))
    depends_on("grep", type=("build", "run"))
    depends_on("sed", type=("build", "run"))

    # The `-h` argument to byobu commands invokes man
    depends_on("man-db", type="run")
    depends_on("screen", type="run")
    depends_on("tmux", type="run")

    # newt and its snack Python module are needed for byobu-config. If the user
    # does not want byobu@6 with a python in its spec, they can disable the
    # python variant, but sacrifice the byobu-config functionality.
    depends_on("newt+python", when="+python", type="run")
    depends_on("python", when="+python", type="run")

    def url_for_version(self, version):
        # byobu 6+ are released on GitHub
        if version < Version("6"):
            return (
                f"https://launchpad.net/byobu/trunk/{version}/+download/"
                f"byobu_{version}.orig.tar.gz"
            )

        else:
            return f"https://github.com/dustinkirkland/byobu/archive/refs/tags/{version}.tar.gz"

    @when("+python")
    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("BYOBU_PYTHON", f"{self.spec['python'].command}")
