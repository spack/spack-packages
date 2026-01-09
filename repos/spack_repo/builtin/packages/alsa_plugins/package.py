# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install alsa-plugins
#
# You can edit this file again by typing:
#
#     spack edit alsa-plugins
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *
import os

class AlsaPlugins(AutotoolsPackage):
    """The ALSA Plugins package contains plugins for various audio libraries and sound servers."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/alsa-project/alsa-plugins"
    url = "https://github.com/alsa-project/alsa-plugins"
    git = "https://github.com/alsa-project/alsa-plugins"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.2.12", tag="v1.2.12", commit="52574cb5ccbb8b546df2759e4b341a20332269b6")

    depends_on("c",        type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool",  type="build")

    depends_on("alsa-lib")
    depends_on("pulseaudio +alsa", when="+pulseaudio")

    variant('pulseaudio', default=True, description="Enable pulseaudio support")

    conflicts("platform=darwin", msg="ALSA (+plugins) only works for Linux")
   
    def configure_args(self):
        args = []
        if '+pulseaudio' in self.spec:
            args.append("--enable-pulseaudio")
        return args

    def setup_build_environment(self, env):
        alsa_prefix = self.spec["alsa-lib"].prefix
        env.prepend_path("PKG_CONFIG_PATH", self.spec["alsa-lib"].prefix.lib64.pkgconfig)

    def setup_run_environment(self, env):
        # 1. ALSA plugin directory
        alsa_plugin_dir = os.path.join(self.prefix.lib, "alsa-lib")
        if os.path.exists(alsa_plugin_dir):
            env.prepend_path("ALSA_PLUGIN_DIR", alsa_plugin_dir)

        # 2. PulseAudio libraries (needed for dlopen dependencies)
        if "pulseaudio" in self.spec:
            pulseaudio_libdir = os.path.join(self.spec["pulseaudio"].prefix.lib64, "pulseaudio")
            if os.path.exists(pulseaudio_libdir):
                env.prepend_path("LD_LIBRARY_PATH", pulseaudio_libdir)

