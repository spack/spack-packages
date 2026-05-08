# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Sfml(CMakePackage):
    """SFML is a simple, fast, cross-platform and object-oriented
    multimedia API. It provides access to windowing, graphics,
    audio and network. It is written in C++ and has bindings for
    various languages such as C, .NET, Ruby, Python."""

    homepage = "https://www.sfml-dev.org/"
    url = "https://github.com/SFML/SFML/archive/refs/tags/3.1.0.tar.gz"
    git = "https://github.com/SFML/SFML.git"

    maintainers("wdconinc")

    license("Zlib", checked_by="wdconinc")

    version("3.1.0", sha256="91209a112c2bd0bc6f4ce0d5f3e413cfb48b57c0de59f5507dc81f71b1ad7a5c")
    version("2.6.2", sha256="15ff4d608a018f287c6a885db0a2da86ea389e516d2323629e4d4407a7ce047f")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.7.2:", type="build")
    depends_on("cmake@3.24:", type="build", when="@3.0.0:")
    depends_on("cmake@3.28:", type="build", when="@3.1.0:")

    variant("window", default=True, description="Build the window module", when="~graphics")
    variant("graphics", default=True, description="Build the graphics module")
    variant("audio", default=True, description="Build the audio module")
    variant("network", default=True, description="Build the network module")

    conflicts("+window", msg="The window module requires UDev, which is not in spack")
    conflicts("+graphics", msg="The graphics module requires UDev, which is not in spack")
    conflicts(
        "+audio", msg="The audio module requires OpenAL, Vorbis, FLAC, which are not in spack"
    )

    def cmake_args(self):
        args = [
            self.define("SFML_USE_SYSTEM_DEPS", True),
            self.define_from_variant("SFML_BUILD_WINDOW", "window"),
            self.define_from_variant("SFML_BUILD_GRAPHICS", "graphics"),
            self.define_from_variant("SFML_BUILD_AUDIO", "audio"),
            self.define_from_variant("SFML_BUILD_NETWORK", "network"),
        ]
        return args
