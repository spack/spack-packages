# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrimesh(PythonPackage):
    """Import, export, process, analyze and view triangular meshes"""

    homepage = "https://github.com/mikedh/trimesh"
    pypi = "trimesh/trimesh-2.38.10.tar.gz"

    license("MIT")

    version("3.17.1", sha256="025bb2fa3a2e87bdd6873f11db45a7ca19216f2f8b6aed29140fca57e32c298e")
    version("2.38.10", sha256="866e73ea35641ff2af73867c891d7f9b90c75ccb8a3c1e8e06e16ff9af1f8c64")

    variant(
        "easy",
        default=False,
        description="Install all 'easy' soft dependencies",
    )
    variant(
        "recommended",
        default=False,
        description="Install most 'recommended' (and all easy) soft dependencies",
        when="+easy",
    )

    depends_on("py-setuptools@40.8:", type="build")
    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        with when("+easy"):
            depends_on("py-chardet")
            depends_on("py-colorlog")
            depends_on("py-jsonschema")
            depends_on("py-lxml")
            depends_on("py-mapbox-earcut")
            depends_on("py-msgpack")
            depends_on("py-networkx")
            depends_on("pil")
            depends_on("py-pycollada")
            depends_on("py-requests")
            depends_on("py-rtree")
            depends_on("py-scipy")
            depends_on("py-setuptools")
            depends_on("py-shapely")
            depends_on("py-svgpath")
            depends_on("py-xxhash")

        with when("+recommended"):
            depends_on("py-sympy")
            depends_on("py-pyglet@:1")
            depends_on("py-glooey")
            depends_on("py-meshio")
            depends_on("py-scikit-image")
            depends_on("py-psutil")
            depends_on("py-vhacdx")
            depends_on("manifold +python")

