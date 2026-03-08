# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAwkwardCpp(PythonPackage):
    """py-awkward-cpp provides precompiled routines for the py-awkward package.
    It is not useful on its own, only as a dependency for py-awkward."""

    git = "https://github.com/scikit-hep/awkward.git"
    pypi = "awkward-cpp/awkward_cpp-36.tar.gz"
    homepage = "https://awkward-array.org"

    maintainers("vvolkl", "wdconinc")

    license("BSD-3-Clause")

    version("52", sha256="ef141eb20544df261b973c986cfae57be329022061be86817506add676597275")
    version("51", sha256="8c74e8f9fb2501766d1b0f9f2eb8777e384411d33534a8fa667d56599223a04b")
    version("50", sha256="264b6fb4e82acc1057b5b2ff0d33fabc361032528e233815cd2224c6dbc96d8e")
    version("49", sha256="cb84e0f484453a580682731ae3058e6f3aac066558ddf015e67fd9515717e1de")
    version("48", sha256="368a9f7d317e7da42d291f51b814e9580825db7d3eb7026b0d47427bfad23e2f")
    version("47", sha256="676cf4976810edab32187edf5a8a716af95047b9038c96d27d3be44f1331950f")
    version("44", sha256="8dc499288d6d16b2ea20b51a27d5047e51a247b6aacfcbcb3b302cad6d3c87d8")
    version("40", sha256="ca5658a3db04cc80e9c5d0eb9f7db41290d882c123a068bef724a879c9084367")
    version("35", sha256="1f8b112a597bd2438794e1a721a63aa61869fa9598a17ac6bd811ad6f6400d06")
    version("12", sha256="429f7fcc37a671afa67fe9680f2edc3a123d1c74d399e5889c654f9529f9f8f2")
    version("11", sha256="02d719a4da7487564b29b8e8b78925a32ac818b6f5572c2f55912b4e0e59c7a4")
    version("10", sha256="d1c856cb6ef5cf3d4f67506a7efc59239f595635865cc9f4ab18440b8bfb11c6")
    version("9", sha256="db1c91c21f88b89a39b46176edc67a08b37f7283c16a2ed5159e3c874613c61a")
    version("8", sha256="a51b554490b3197fc5433822becb2e8208bf78fca82ffa314d839b72b3cc4169")
    version("7", sha256="dde733575b2a5ae5b946fe8667b4ae842d937d3b36ebb383d53dc53ea86ea65d")
    version("6", sha256="58e32afa8aa44c365e764f4b5d07637c79a79be2da7cfbaa3469d8bd26b0bfa2")
    version("5", sha256="e5d6a90d98a14dab36598015e69243b9f83b8851556104cbe778ca9c79923656")
    version("4", sha256="fbc4b5e552873e00ffb6286941efc7b629e4fbc4752e28afb9b54854128937f7")
    version("3", sha256="6070557762bd95d3642ad9c585609db51f899a1e79ce4f41568835efd7d6e066")
    version("2", sha256="5e63f43e3135f76db81e0924a74ecf4870f585c11a9f432568b377c04028868c")

    depends_on("cxx", type="build")  # generated

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"), when="@19:")
    depends_on("py-scikit-build-core@0.9:", when="@36:", type="build")
    depends_on("py-scikit-build-core@0.10:", when="@38:", type="build")
    depends_on("py-pybind11", type=("build", "link"))
    depends_on("py-numpy@1.17.0:", when="@12:", type=("build", "run"))
    depends_on("py-numpy@1.18.0:", when="@19:", type=("build", "run"))

    # older versions
    depends_on("py-numpy@1.14.5:", when="@:11", type=("build", "run"))
    depends_on("py-scikit-build-core@0.1.3:+pyproject", when="@:9", type="build")
    depends_on("py-scikit-build-core@0.2.0:+pyproject", when="@10:35", type="build")

    # https://github.com/scikit-hep/awkward/issues/3132#issuecomment-2136042870
    conflicts("%gcc@14:", when="@:33")

    def url_for_version(self, version):
        if version <= Version("35"):
            return super().url_for_version(version).replace("_", "-")
        else:
            return super().url_for_version(version)
