# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary, ROCmPackage

from spack.package import *


class Libhipcxx(ROCmLibrary,CMakePackage):
    """libhipcxx is the AMD HIP C++ Standard Library. It provides a
heterogeneous implementation of the C++ Standard Library that can be used in
HIP and non-HIP code"""

    homepage = "https://github.com/ROCm/libhipcxx"

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")

    rocm_url_map = [
        (None, "https://github.com/ROCm/libhipcxx/archive/refs/tags/therock-{1}.{2}.tar.gz"),    
    ]


    version("10.1.0", sha256="d6268c6d99c60bfc88771d7d92b440cb34c3e32f343e6d685b5b138d7a4363e7")
    version("10.0.0", sha256="95a6c2eea96b99baddd0029a0dc4f64905fe7fe7b342f9dd7b1cd7795628fdeb")

    depends_on("cxx", type="build")
    depends_on("cmake@3.31:", type="build")

    for ver in ["10.0.0", "10.1.0"]:
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")
        depends_on(f"hip@{ver}", when=f"@{ver}")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", "OFF"),
            self.define("libhipcxx_ENABLE_CMAKE_TESTS", "OFF"),
            self.define("LIBCUDACXX_ENABLE_LIBCUDACXX_TESTS", "OFF"),
        ]
        return args
