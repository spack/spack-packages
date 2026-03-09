# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySounddevice(PythonPackage):
    """This Python module provides bindings for the PortAudio library and a few convenience functions to play and record NumPy arrays containing audio signals."""

    homepage = "https://python-sounddevice.readthedocs.io/"
    url = "https://github.com/spatialaudio/python-sounddevice/archive/refs/tags/0.5.5.tar.gz"

    license("MIT")

    version("0.5.5", sha256="1f13a3990978860db8960768c046e9b83dd344ee90e4891f22056cca3d15c3e7")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-cffi", type=("build", "run"))
    depends_on("portaudio", type=("link", "run"))

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["portaudio"].libs.directories[0])
