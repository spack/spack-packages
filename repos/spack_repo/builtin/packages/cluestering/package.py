# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cluestering(CMakePackage):
    """Header-only density-based weighted clustering library based on alpaka."""

    homepage = "https://github.com/cms-patatrack/CLUEstering"
    url = "https://github.com/cms-patatrack/CLUEstering/archive/refs/tags/2.14.0.tar.gz"
    git = "https://github.com/cms-patatrack/CLUEstering.git"

    maintainers("sbaldu")

    license("MPL-2.0")

    version("main", branch="main")
    version("2.14.2", sha256="ff95fac879eac511170f07f289b96bbfea447f5592ad9f0f418e709022f535ae")
    version("2.14.0", sha256="21e7b8b44a4c8e151573a7783497754f72e1a1b6f39b223b6060be4adbd60f30")
    version("2.13.0", sha256="8d8b4b9c6e9fbd77464571ee3268f7fad66d3dbe6557ba342e64bd2fc3646b1b")
    version("2.12.0", sha256="16b1e44c4e5389c95e1b638a32b10105842fee568692cc1e3c3895d016b01299")
    version("2.11.0", sha256="92212857bfbedb2673896862bcd3d312495c89df20690ca2774a55418320817f")
    version("2.10.0", sha256="98217630d40c71cd78074c9afc0fdefc017783804039e2f3815587fb472047a8")
    version("2.9.0", sha256="00e0c228f75f9d140896fcc91a0741f958985769dd09618e7effef339f2e2f6a")

    depends_on("cxx", type="build")
    depends_on("cmake@3.16:", type="build")

    depends_on("alpaka")
    depends_on("alpaka@2.2:2", when="@2.13:")
    depends_on("alpaka@2.1:2", when="@:2.12")
