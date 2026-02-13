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
    version("4.2.4", sha256="23a3d58cdeacf3abdf9fa1d81dcefee58da6ab330940790c0f27019703bfd2cd")
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
