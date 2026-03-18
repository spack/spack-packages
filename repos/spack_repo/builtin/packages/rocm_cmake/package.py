# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RocmCmake(CMakePackage):
    """rocm-cmake provides CMake modules for common build tasks
    in the ROCm software stack"""

    homepage = "https://github.com/ROCm/rocm-cmake"
    git = "https://github.com/ROCm/rocm-cmake.git"
    url = "https://github.com/ROCm/rocm-cmake/archive/rocm-6.4.2.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")

    license("MIT")
    version("7.2.0", sha256="3f3899e84d78a0fecab62a35eed0014bb503c04d2cf76d263b29daf17f178636")
    version("7.1.1", sha256="4ef6bbe518a3d4670272203c83f98b2a7135ad570a13498f871efda2320b698e")
    version("7.1.0", sha256="d17a109b3ade999926f5b25ce25082b378399654e3b2234cad5f83cdd00a2f32")
    version("7.0.2", sha256="79c40408be17f7c73105e281154267fcc6851e1db8b6be01a411ef1d8050bc71")
    version("7.0.0", sha256="16b220cb10c8ebe438c1ba3b9de014abcd782fd0b0bcffb39d3d2d1ff6957f2a")
    version("6.4.3", sha256="a2a29d5d5b6fcf01af8a662c2453c8c1bfc647fbcbfcbe86fc87d6af17287d24")
    version("6.4.2", sha256="61e0217a453e30a68e0a42cba61e7181b07ef0be72d19a1133f8f24cedebddf1")
    version("6.4.1", sha256="d6dfa862009d593f4d334e0c6da9ac52b228e52bb3b38b53405975f28087ca2f")
    version("6.4.0", sha256="be8109c52e9309d1ae9553e067346ecdf1a25f653cc21974ddc542f31ce54615")
    version("6.3.3", sha256="4238cccc22226ba9487185fc2faa66b11c0cb8e7982240332e1b919cec8d909e")
    version("6.3.2", sha256="f5104c2289da99a70d8c4c1befbca4f8efa7c89711eaac7b6b63592cd4bd99a8")
    version("6.3.1", sha256="6994a5bdeea55cd41ec01ab4142785ea02bbdcb83e70f6911095c7cea766ebe8")
    version("6.3.0", sha256="45a1b96f85ae28a7f62895ddc4d6648500b883af250f52f6417bafb31b3cc75d")
    version("6.2.4", sha256="76bfac6fba31a9c4ec196d9b9b2d5ec51b8b68840b3fba8686aa42323d76a425")
    version("6.2.1", sha256="5ea05ad58186ac9bac40ab083c1e769a36ecaed950f82e88863169a25bc6ac8f")
    version("6.2.0", sha256="7b6aaa1bb616669636aa2cd5dbc7fdb7cd05642a8dcc61138e0efb7d0dc7e1a3")
    version("6.1.2", sha256="0757bb90f25d6f1e6bc93bdd1e238f76bbaddf154d66f94f37e40c425dc6d259")
    version("6.1.1", sha256="0eb81245f7573a3cadf9e91a854d9a0a014ce93610e4e7ea4d8309867a470bf6")
    version("6.1.0", sha256="8b37d458e801b486521f12d18ca2103125173dd0f1130d37c8c36e795d34772b")
    version("6.0.2", sha256="7bd3ff971b1a898b8cf06b0ed9fac45891e2523ae651c3194ba36050ab45f869")
    version("6.0.0", sha256="82bd97ba23d1883ef38bb667e92f7367fedc50d6c11c82f54cced4ab04b0412d")
    version("5.7.1", sha256="4a4c6aa09576ccb834f869bdcb49e98cc0f0bac3678b802358065d1179a9d6f1")
    version("5.7.0", sha256="93b98144201a1143eeca32744a9927d063f4685189f132ba52a6f3bba158a86b")

    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.6:", type="build")

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
    ]:
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    test_src_dir = "test"

    @run_after("install")
    def cache_test_sources(self):
        """Copy the tests source files after the package is installed to an
        install test subdirectory for use during `spack test run`."""
        cache_extra_test_sources(self, [self.test_src_dir])

    def test_cmake(self):
        """Test cmake"""
        test_dir = join_path(self.test_suite.current_test_cache_dir, self.test_src_dir)
        with working_dir(test_dir, create=True):
            cc_options = [f"-DCMAKE_PREFIX_PATH={self.prefix}", "."]
            make = self.spec["gmake"].command
            cmake = self.spec["cmake"].command
            cmake(*cc_options)
            make()
            make("clean")
