# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Dcm2niix(CMakePackage):
    """DICOM to NIfTI converter"""

    homepage = "https://github.com/rordenlab/dcm2niix"
    url = "https://github.com/rordenlab/dcm2niix/archive/refs/tags/v1.0.20220720.tar.gz"

    license("BSD-3-Clause AND MIT", checked_by="Markus92")

    version(
        "1.0.20250506", sha256="1b24658678b6c24141e58760dbea9fe2786ffdd736bcc37a36d9cdabc731bafa"
    )
    version(
        "1.0.20240202", sha256="ad8e4a5b97a682c32ef1d88283c15c7cb767c4092cb1754119f8e8b3d940fe91"
    )
    version(
        "1.0.20220720", sha256="a095545d6d70c5ce2efd90dcd58aebe536f135410c12165a9f231532ddab8991"
    )
    version(
        "1.0.20210317", sha256="42fb22458ebfe44036c3d6145dacc6c1dc577ebbb067bedc190ed06f546ee05a"
    )

    # Only compile the console app. The superbuild pulls in lot of dependencies through Git
    # and doesn't propagate some Spack-controlled CMake parameters (most notably RPath)
    # In practice, the app is what we want anyways
    root_cmakelists_dir = "console"

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    variant("jp2k", default=False, description="Enable JPEG2000 support")
    variant("jpegls", default=False, description="Enable JPEG-LS support")

    depends_on("pkgconfig", type="build")

    depends_on("openjpeg", when="+jp2k")
    depends_on("zlib-api")

    def cmake_args(self):
        args = [
            self.define("ZLIB_IMPLEMENTATION", "System"),
            # Not all systems have a libstdc++.a while dynamic is always there
            self.define("USE_STATIC_RUNTIME", "OFF"),
            self.define_from_variant("USE_JPEGLS", "jpegls"),
        ]

        if self.spec.satisfies("+jp2k"):
            args.append(self.define("USE_OPENJPEG", "System"))

        return args
