# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.build_systems.python import PythonExtension, PythonPipBuilder

from spack.package import *


class Nvtx(Package, PythonExtension):
    """Python code annotation library"""

    git = "https://github.com/NVIDIA/NVTX.git"
    url = "https://github.com/NVIDIA/NVTX/archive/refs/tags/v3.1.0.tar.gz"

    maintainers("thomas-bouvier")

    license("Apache-2.0")

    version("develop", branch="dev")
    version("3.2.1", sha256="737c3035f0e43a2252e7cd94c3f26e11e169f624236efe31794f044ce44a70af")
    version("3.1.0", sha256="dc4e4a227d04d3da46ad920dfee5f7599ac8d6b2ee1809c9067110fb1cc71ced")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    variant("python", default=True, description="Install Python bindings.")
    extends("python", when="+python")
    depends_on("py-pip", type="build", when="+python")
    depends_on("py-setuptools", type="build", when="+python")
    depends_on("py-wheel", type="build", when="+python")
    depends_on("py-cython", type="build", when="+python")

    build_directory = "python"

    # nvtxExtPayloadTypeInfo.h (included transitively via nvToolsExtPayload.h)
    # uses char8_t, which requires C23 (-std=c23).  GCC gained C23 char8_t
    # support in 13.0, so earlier compilers cannot build the Python extension.
    conflicts("%gcc@:12", when="@3.3.0: +python")

    # Create a nvtx-config.cmake file to make calls to find_package(nvtx) to
    # work as expected
    patch("nvtx-config.patch")

    def patch(self):
        """Patch setup.py to provide include directory."""
        include_dir = prefix.include
        setup = FileFilter("python/setup.py")
        setup.filter("include_dirs=include_dirs", f"include_dirs=['{include_dir}']", string=True)
        # see comment in patch below
        if self.spec.satisfies("@3.3.0:"):
            header = FileFilter(
                "c/include/nvtx3/nvtxDetail/nvtxExtPayloadTypeInfo.h"
            )
            header.filter(
                "#define NVTX_HAVE_CHAR8 1",
                "/* Fallback for systems where glibc < 2.36 does not define char8_t\n"
                " * in uchar.h even when the compiler supports C23 (e.g. RHEL 9). */\n"
                "#ifndef __cpp_char8_t\n"
                "typedef unsigned char char8_t;\n"
                "#endif\n"
                "#define NVTX_HAVE_CHAR8 1",
                string=True,
            )

    def install(self, spec, prefix):
        install_tree("c/include", prefix.include)
        install("c/CMakeLists.txt", prefix)
        install("c/nvtxImportedTargets.cmake", prefix)
        install("./LICENSE.txt", prefix)

        install("./nvtx-config.cmake", prefix)  # added by the patch above

        with working_dir(self.build_directory):
            pip(*PythonPipBuilder.std_args(self), f"--prefix={self.prefix}", ".")

