# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class AlsaPlugins(AutotoolsPackage):
    """The ALSA Plugins package contains plugins for various audio libraries and sound servers."""

    homepage = "https://github.com/alsa-project/alsa-plugins"
    url = "https://github.com/alsa-project/alsa-plugins"
    git = "https://github.com/alsa-project/alsa-plugins"

    # notify when the package is updated.
    maintainers("biddisco")

    license("LGPL-2.1-or-later", checked_by="biddisco")

    version("1.2.12", tag="v1.2.12", commit="52574cb5ccbb8b546df2759e4b341a20332269b6")

    depends_on("c", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    depends_on("alsa-lib")
    depends_on("pulseaudio +alsa", when="+pulseaudio")

    variant("pulseaudio", default=False, description="Enable pulseaudio support")

    conflicts("platform=darwin", msg="ALSA (+plugins) only works for Linux")

    def configure_args(self):
        args = []
        args += self.enable_or_disable("pulseaudio")
        return args

    # to get plugins to load without the user manually entering env vars for paths
    def setup_run_environment(self, env):
        # 1. ALSA plugin directory in ALSA_PLUGIN_DIR
        alsa_plugin_dir = os.path.join(self.prefix.lib, "alsa-lib")
        if os.path.exists(alsa_plugin_dir):
            env.prepend_path("ALSA_PLUGIN_DIR", alsa_plugin_dir)

        # 2. ALSA lib directory in LD_LIBRARY_PATH
        alsa_lib_libdir = self.spec["alsa-lib"].prefix.lib
        if os.path.exists(alsa_lib_libdir):
            env.prepend_path("LD_LIBRARY_PATH", alsa_lib_libdir)

        # 2. Pulseaudio lib directory in LD_LIBRARY_PATH
        pulseaudio_libdir = os.path.join(self.spec["pulseaudio"].prefix.lib, "pulseaudio")
        if os.path.exists(pulseaudio_libdir):
            env.prepend_path("LD_LIBRARY_PATH", pulseaudio_libdir)
