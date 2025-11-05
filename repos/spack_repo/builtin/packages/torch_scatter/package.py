from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class TorchScatter(CMakePackage):
    """Torch Extension Library of Optimized Scatter Operations.

    This version of the package is consumable by downstream users via CMake
    """

    homepage = "https://github.com/rusty1s/pytorch_scatter"
    git = "https://github.com/rusty1s/pytorch_scatter"
    url = "https://github.com/rusty1s/pytorch_scatter/archive/refs/tags/2.1.2.tar.gz"

    license("MIT")

    version("master", branch="master")
    version("2.1.2", sha256="6f375dbc9cfe03f330aa29ea553e9c7432e9b040d039b041f08bf05df1a8bf37")
    version("2.1.1", sha256="ea4f4ac4210a983d878df29e82190f60a7e6e9a791adbe0c0d635040e6256c4d")
    version("2.1.0", sha256="c587ddf7ffaf8e4ddc31d8016d7f445d5896ce491209574800166a9f85c29377")
    version("2.0.9", sha256="f7f87395e3a87c1db5a48d675138a15f7e4f5d7fd1c5e5067ade9a01890d7f8e")
    version("2.0.8", sha256="3f4fd8787006e55bfc38d716b484b27ba7d37291d80b69d94930676f6f990b51")
    version("2.0.7", sha256="0d5568f907a3f948b3359cf741838bd34cd840cf31efd686b0c44f6671fc325e")
    version("2.0.6", sha256="d95e552f69d1304b060fb72770d2ea543c3e6c2d41e69baba792117831379f8c")
    version("2.0.5", sha256="e29b364beaa9c84a99e0e236be89ed19d4452d89010ff736184ddcce488b47f6")
    version("2.0.4", sha256="4fdadd6587f16ef3ff63c52f313f0c9dd97d13ae6496867fe566c309a4ea4036")
    version("2.0.3", sha256="ff2ca1468cb4e49b65bea8f889971f196f209231fbee0cc8bd1615ecb367400b")

    variant("cuda", default=False, description="Build with CUDA support")

    depends_on("cxx", type="build")
    depends_on("c", type="build")

    depends_on("py-torch")
    depends_on("py-torch +cuda", when="+cuda")

    conflicts("py-torch@2.1:", when="@:2.1.2")

    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_CUDA", "cuda"),
            self.define("CMAKE_CXX_STANDARD", "20"),
            self.define("WITH_PYTHON", True),
        ]
        return args
