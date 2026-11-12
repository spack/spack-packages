# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Polyclipper(CMakePackage):
    """Library for polyhedral clipping planes."""

    homepage = "https://github.com/llnl/PolyClipper"
    url = "https://github.com/llnl/PolyClipper/archive/refs/tags/v1.2.6.tar.gz"
    git = "https://github.com/llnl/PolyClipper.git"

    maintainers("jmikeowen", "ldowen")
    license("BSD-3-Clause")

    version("master", branch="master", submodules=True)
    version("1.2.6", sha256="ffce2fe36fb888b7aaf93d4b3591b0875909573537ca39c0730b7d85bbc5558c")
    version("1.2.5", sha256="914b3f4bcc89f3c63f66b80cf3a45daa772dc71f3bdbc2ee4d312d7c5bbe60f3")
    version("1.2.4", sha256="02066fbf34b8bdbd22414514583c481c573cbb003e6dace398bc78678d967d38")
    version("1.2.3", sha256="5c2ed2202db3b4172703a9d6d219ba5dc9d4e9276791d4e45cc201c1974c3572")
    version("1.2.2", sha256="fd7ca794c1189bde1563b9704b371c65d7ba94b3582351fa2c3e0dd487b431da")

    variant("python", default=True, description="Enable python bindings.")
    depends_on("python@3.10:", when="+python")

    with default_args(type="build"):
        depends_on("blt")
        depends_on("cmake@3.20:")
        depends_on("cxx")
        depends_on("c")

    def url_for_version(self, version):
        if version >= Version("1.2.6") or version <= Version("1.2.3"):
            url = "https://github.com/llnl/PolyClipper/archive/refs/tags/v{0}.tar.gz"
        else:
            url = "https://github.com/llnl/PolyClipper/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    def cmake_args(self):
        args = []
        args.append(self.define("BLT_SOURCE_DIR", self.spec["blt"].prefix))
        args.append(self.define("POLYCLIPPER_BLT_DIR", self.spec["blt"].prefix))
        if self.spec.satisfies("+python"):
            args.append(self.define("POLYCLIPPER_ENABLE_PYTHON", "ON"))
        else:
            args.append(self.define("ENABLE_CXXONLY", "ON"))
            args.append(self.define("POLYCLIPPER_ENABLE_PYTHON", "OFF"))
        args.append(self.define("POLYCLIPPER_ENABLE_TESTS", "OFF"))
        return args
