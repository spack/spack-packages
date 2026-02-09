# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Jasper(CMakePackage):
    """Library for manipulating JPEG-2000 images"""

    homepage = "https://www.ece.uvic.ca/~frodo/jasper/"
    url = "https://github.com/jasper-software/jasper/archive/version-2.0.32.tar.gz"

    version("4.2.8", sha256="987e8c8b4afcff87553833b6f0fa255b5556a0ecc617b45ee1882e10c1b5ec14")
    version("4.2.7", sha256="93d3472ae50b2cc6547d3d8ea53de7e820588a0e5be6557a7fe0b1d94eb1e5ca")
    version("4.2.6", sha256="0f92ddc4cf3c2c8f6e06dc1a909c671c579926d3be066f5101037ca2f83975b2")
    version("4.2.5", sha256="3f4b1df7cab7a3cc67b9f6e28c730372f030b54b0faa8548a9ee04ae83fffd44")
    version("4.2.4", sha256="23a3d58cdeacf3abdf9fa1d81dcefee58da6ab330940790c0f27019703bfd2cd")
    version("4.2.3", sha256="1263d70c663f1b5a4ed2a428371486091d282af96b7270e8b1cbfcbf44ad95ff")
    version("4.2.2", sha256="0fb8ad07ea6c06d43567fa5d2592f60c53a2e868fff8b9da1bc2bb950d7dbfe5")
    version("4.2.1", sha256="970002b774b91edd9d2dedf76d0b8d5a88af28e0c6d603cc51988311a99a869f")
    version("4.2.0", sha256="c9a3e35c95447f530b006fab6634a2dadec70276cc3e42c343b9e5ce5a1f2b6b")
    version("4.1.2", sha256="64937eee9377f59d6222e443ed643857729c5378e627f54cdb1995776405be18")
    version("4.1.1", sha256="57299e40db869cee4ea410c021f18ced793796db8c053dd987afc7b876afda96")
    version("4.1.0", sha256="32879db502f59c1fde58e65b80d9b7db759f0173b7933c003517caf8f3892230")
    version("4.0.1", sha256="a251eae29c90ccae4757a051a795c456ff1218da0a180e3eb2ab8427c5f1d31d")
    version("4.0.0", sha256="977c4c2e4210f4e37313cd2232d99e73d57ab561917b3c060bcdd5e83a0a13f1")
    version("3.0.6", sha256="c79961bc00158f5b5dc5f5fcfa792fde9bebb024432689d0f9e3f95a097d0ec3")
    version("3.0.3", sha256="1b324f7746681f6d24d06fcf163cf3b8ae7ac320adc776c3d611b2b62c31b65f")
    version("2.0.32", sha256="a3583a06698a6d6106f2fc413aa42d65d86bedf9a988d60e5cfa38bf72bc64b9")
    version("2.0.31", sha256="d419baa2f8a6ffda18472487f6314f0f08b673204723bf11c3a1f5b3f1b8e768")
    version("2.0.16", sha256="f1d8b90f231184d99968f361884e2054a1714fdbbd9944ba1ae4ebdcc9bbfdb1")
    version("2.0.14", sha256="85266eea728f8b14365db9eaf1edc7be4c348704e562bb05095b9a077cf1a97b")

    variant("jpeg", default=True, description="Enable the use of the JPEG library")
    variant("opengl", default=False, description="Enable the use of the OpenGL and GLUT libraries")
    variant("shared", default=True, description="Enable the building of shared libraries")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@2.8.11:", type="build")
    depends_on("cmake@3.12:", type="build", when="@3:")

    depends_on("jpeg", when="+jpeg")
    depends_on("gl", when="+opengl")

    # invalid compilers flags
    conflicts("@2", when="%nvhpc")

    def cmake_args(self):
        return [
            self.define("JAS_ENABLE_DOC", False),
            self.define("JAS_ENABLE_LATEX", False),
            self.define_from_variant("JAS_ENABLE_LIBJPEG", "jpeg"),
            self.define_from_variant("JAS_ENABLE_OPENGL", "opengl"),
            self.define_from_variant("JAS_ENABLE_SHARED", "shared"),
        ]
