# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Typos(CargoPackage):
    """Source code spell checker."""

    homepage = "https://github.com/crate-ci/typos"
    url = "https://github.com/crate-ci/typos/archive/refs/tags/v1.28.4.tar.gz"

    maintainers("alecbcs")

    license("Apache-2.0 OR MIT", checked_by="alecbcs")

    version("1.40.0", sha256="f8317b77e124f0201a47289a1d3e7a196e93cdbec3df9a0fc82d10c934c0ca85")
    version("1.38.1", sha256="f7e83dfecba57d778c916bd3d554129fd6d79e0fa781f605e83c7dd89e30711d")
    version("1.36.2", sha256="23229bf78a136bce3c456019d71e25b57858275c8fd947426b8a5b32d639abe3")
    version("1.35.1", sha256="41e981cc763393b1374d2891f64c0ec62eb9b99320f4af6e1e3f4aa85fe1db36")
    version("1.32.0", sha256="11c1ac4f9427cd572ce728c20814ebd8b8769ed909b7d1309d805d9a37b81084")
    version("1.30.2", sha256="20a5c2354894215fb87126f1805a171808fec93c427720f873a025466114e44c")
    version("1.28.4", sha256="acfbaf16d61fb35532ddb91a32e720181450487f60fe60757f72c3879496955d")

    depends_on("rust@1.87:", type="build", when="@1.39.1:")
    depends_on("rust@1.80:", type="build")

    build_directory = "crates/typos-cli"
