# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Just(CargoPackage):
    """just is a handy way to save and run project-specific commands"""

    homepage = "https://github.com/casey/just"
    url = "https://github.com/casey/just/archive/refs/tags/1.46.0.tar.gz"
    git = "https://github.com/casey/just.git"

    maintainers("Dando18")

    license("CC0-1.0", checked_by="Dando18")

    version("master", branch="master")
    version("1.52.0", sha256="cd869b45801f1434d26c05df7ca999b7b56c7d1d57fb1211cdfd2526ec28f130")
    version("1.50.0", sha256="cca015e07739a1c26c6fc459f7d46e1e36ce0f7613114eddedd8cd3af55a10b7")
    version("1.49.0", sha256="442406ee14eb9a59414525cf262354fe2e752b22c224ce2a5e42b2c493226e09")
    version("1.46.0", sha256="f60a578502d0b29eaa2a72c5b0d91390b2064dfd8d1a1291c3b2525d587fd395")
    version("1.42.2", sha256="9929acc303b881106d2bf2d3440d44f413372c14b0e44bf47cda8ada8801553a")
    version("1.42.1", sha256="6a6ec94ae02791c2101fd65201032d7c1929fc6294e4deebc92d0e846882fe15")
    version("1.42.0", sha256="6fdbd6199b5469c70762a4991ae03d88fae42b99b48124ad7ad84808b67cdfb8")
    version("1.41.0", sha256="4ab64ebeaf7d6cf90d2824fddb91f7a3a4cfbb5d016e99cc5039ded475c8a244")
    version("1.40.0", sha256="e0d48dcc7a086c5746b7f281a40e615c290cddf9c06134198c703dff2f62c1c4")
    version("1.39.0", sha256="8a900072d7f909bc91030df5896168752bb9108967dbb7149d2cfb11fdeb087a")
    version("1.38.0", sha256="3d47e27755d39f40e1ca34bc0ef535fa514e7ed547b2af62311dcadd8bd6d564")
    version("1.37.0", sha256="13af58413af8f5d41d72c955de0ed9863a53f286df5f848e3d68bcb070b54ef2")
    version("1.36.0", sha256="bc2e2ff0268c2818659c524b21663564864b50ba102afb0a44fe73c08cf35ff0")
    version("1.35.0", sha256="f1ce3fe46c57cba0096227f8c9251d3b476e54e8a620eb39707d0ab3e16b8f55")

    depends_on("c", type="build")

    depends_on("rust@1.85:", type="build", when="@1.49.0:")
    depends_on("rust@1.82:", type="build", when="@1.46.0:")
    depends_on("rust@1.77:", type="build", when="@1.41.0:")
    depends_on("rust@1.74:", type="build", when="@1.35.0:")
