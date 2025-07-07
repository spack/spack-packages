# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install manifold
#
# You can edit this file again by typing:
#
#     spack edit manifold
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Manifold(CMakePackage):
    """Geometry library for creating and operating on manifold triangle meshes"""

    homepage = "https://github.com/elalish/manifold"
    url = "https://github.com/elalish/manifold/archive/refs/tags/v3.1.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    license("Apache-2.0", checked_by="moloney")

    version("3.1.1", sha256="1e47f69a96fe228a953e6bfce99657b6d278ed98a822e950322f722adf2e74ed")
    version("3.1.0", sha256="bdfc2cced7e41bad74aef01f765eb01e5d93b8ff4ef7434be6f825efe7908f93")
    version("3.0.1", sha256="5e84fdaab7933a00fb4279a9bbe2885e94db3adfc45a2ef56ae35abfe5e6ea43")
    version("3.0.0", sha256="3ffafd7b7c22497df54d5a95b811f2f3cb04ec1b857301d489b0cbc11a10aeaf")
    version("2.5.1", sha256="80e91b62cc84ca0acf0209cecfed1b02517f390bf072cee6604119652435ab59")
    version("2.5.0", sha256="9d22e409c341fd30a2d0d2762d6238446176a7622f5aa31515e98c0107ff29be")
    version("2.4.5", sha256="29d4cd01ffc77eae4d0ce08b191d41b4b0e5099e4a918cae0123b49087b17140")
    version("2.4.0", sha256="d06823fa0ca2d9035a470533f5cf1c82c458e11d9e01573ec008fadee647fb08")
    version("2.3.1a", sha256="13bc2dd6145b779aadbae6454395dbd443cf5c70ecd241fbcb4f315ee66c1526")
    version("2.3.0", sha256="61db92a857966882be9cfa69d370608d9cc6f86e896f8d61a64eeec28449a91f")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Add variants / deps
    variant("tbb", default=True, description="Use TBB for parallelization")
    depends_on("tbb", when="+tbb")
    # TODO: For now allow manifold to build clipper2 internally as not in spack
    #variant("clipper2", default=True, description="")
    #depends_on("clipper2", when="+clipper2")
    variant("python", default=True, description="Build python bindings")
    depends_on("py-nanobind", when="+python")
    extends("python", when="+python")

    def cmake_args(self):
        args = [
            self.define("MANIFOLD_JSBIND", "OFF"),
            self.define_from_variant("MANIFOLD_PAR", "tbb"),
            self.define_from_variant("MANIFOLD_PYBIND", "python"),
        ]
        return args
