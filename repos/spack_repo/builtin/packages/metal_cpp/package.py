# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class MetalCpp(Package):
    """Metal-cpp is a low-overhead C++ interface for Metal that helps you add Metal
    functionality to graphics apps, games, and game engines that are written in C++."""

    homepage = "https://developer.apple.com/metal/cpp/"
    git = "https://github.com/apple/metal-cpp.git"

    license("Apache-2.0")

    maintainers("rbberger")

    version(
        "27",
        tag="release/metal-cpp_macOS27_iOS27",
        commit="27c4382b7151d55a51692cdcb27aaa98752240de",
    )
    version(
        "26.4",
        tag="release/metal-cpp_macOS26.4_iOS26.4",
        commit="c595afef4a5dc388f4047cd0c69f9e7f9468d9ed",
    )
    version(
        "26",
        tag="release/metal-cpp_macOS26_iOS26",
        commit="f567ed836e4cbb85788c42115a2682bbe68097ee",
    )

    requires("platform=darwin", msg="Metal is only available on macOS")

    def install(self, spec, prefix):
        install_tree("Foundation", prefix.include.Foundation)
        install_tree("Metal", prefix.include.Metal)
        install_tree("MetalFX", prefix.include.MetalFX)
        install_tree("QuartzCore", prefix.include.QuartzCore)
