# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ecbuild(CMakePackage):
    """ecBuild is the ECMWF build system. It is built on top of CMake and
    consists of a set of macros as well as a wrapper around CMake"""

    homepage = "https://github.com/ecmwf/ecbuild"
    url = "https://github.com/ecmwf/ecbuild/archive/refs/tags/3.6.1.tar.gz"
    list_url = "https://github.com/ecmwf/ecbuild/tags"

    maintainers("climbfuji", "victoria-cherkas")

    license("Apache-2.0")

    version("3.13.1", sha256="9759815aef22c9154589ea025056db086c575af9dac635614b561ab825f9477e")
    version("3.13.0", sha256="7be83510e7209c61273121bcf817780597c3afa41a5129bfccc281f0df1ffda1")
    version("3.12.0", sha256="70c7fc9b17f736a3312167c2c36d13b3b5833a255fe2b168b2886ad7c743ffdf")
    version("3.11.0", sha256="38a96bdeb38feb65446b6f95b35492232abd188c41b8a28fd128f9f88e00b05d")
    version("3.10.0", sha256="7065e1725584b507517cbfc456299ff588e20adf37bc6210ce89fb65a1ad08d0")
    version("3.9.1", sha256="48c2dbd342865049cc39afd7fe886fce9ce162105ca72b8aef9a09c21d9655ba")
    version("3.9.0", sha256="8ad20169a7d917d6ac81a7ca0d1b11616e2aeb82c7782f6ae5b768603a3e000a")
    version("3.8.5", sha256="aa0c44cab0fffec4c0b3542e91ebcc736b3d41b68a068d30c023ec0df5f93425")
    version("3.7.2", sha256="7a2d192cef1e53dc5431a688b2e316251b017d25808190faed485903594a3fb9")
    version("3.6.5", sha256="98bff3d3c269f973f4bfbe29b4de834cd1d43f15b1c8d1941ee2bfe15e3d4f7f")
    version("3.6.1", sha256="796ccceeb7af01938c2f74eab0724b228e9bf1978e32484aa3e227510f69ac59")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.11:", type=("build", "run"))
    depends_on("cmake@3.18:", type=("build", "run"), when="@3.11:")

    # See https://github.com/ecmwf/ecbuild/issues/35
    depends_on("cmake@:3.19", type=("build", "run"), when="@:3.6.1")

    # Some of the installed scripts require running Perl:
    depends_on("perl", type=("build", "run"))

    variant("fismahigh", default=False, description="Apply patching for FISMA-high compliance")

    @when("+fismahigh")
    def patch(self):
        filter_file('ssh://[^"]+', "", "cmake/compat/ecmwf_git.cmake")
        filter_file('https?://[^"]+', "", "cmake/compat/ecmwf_git.cmake")
        filter_file(
            "https?://.*test-data", "DISABLED_BY_DEFAULT", "cmake/ecbuild_check_urls.cmake"
        )
        filter_file(
            "https?://.*test-data", "DISABLED_BY_DEFAULT", "cmake/ecbuild_get_test_data.cmake"
        )
