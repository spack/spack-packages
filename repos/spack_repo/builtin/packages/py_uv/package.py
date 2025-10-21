# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUv(PythonPackage):
    """An extremely fast Python package and project manager, written in Rust."""

    homepage = "https://github.com/astral-sh/uv"
    pypi = "uv/uv-0.4.15.tar.gz"

    license("APACHE 2.0 or MIT")

    version("0.8.9", sha256="54d76faf5338d1e5643a32b048c600de0cdaa7084e5909106103df04f3306615")
    version("0.8.8", sha256="6880e96cd994e53445d364206ddb4b2fff89fd2fbc74a74bef4a6f86384b07d9")
    version("0.8.7", sha256="6e638d6a92639c398e00148178e2e56f7f8f79cf15b1f477f4652b9fff0ae7eb")
    version("0.8.6", sha256="4d4e042f6bd9f143094051a05de758684028f451e563846cbc0c6f505b530cca")
    version("0.8.5", sha256="078cf2935062d5b61816505f9d6f30b0221943a1433b4a1de8f31a1dfe55736b")
    version("0.8.4", sha256="2ab21c32a28dbe434c9074f899ed8084955f7b09ac5e7ffac548d3454f77516f")
    version("0.8.3", sha256="2ccaae4c749126c99f6404d67a0ae1eae29cbafb05603d09094a775061fdf4e5")
    version("0.8.2", sha256="1a2c6d332a4c38f7489f08829aea19cd1e276df7f2c6e51ae64ed92f8574cd68")
    version("0.8.1", sha256="ddae2dfd298adcc960759784b207ed6b90db940d7b05d040a34b58634bb74a69")
    version("0.8.0", sha256="5d4b05056cc923e579007aede5ad1c3cf2c22628a89585f503b724521036748c")
    version("0.7.22", sha256="f5cf159907d594e33433f14737d1ee843dc8799edfcf57b5b8c0f282d1117051")
    version("0.7.21", sha256="9da06b797370c32f9ac9766257602258960d686e3847e102d9c293a77f8449e7")
    version("0.7.20", sha256="6adf2ad333e8da133eecbdd2bdb4e8dfb6d4b2db2c3b4739b6705aa347c997ee")
    version("0.7.19", sha256="c99b4ee986d2ca3a597dfe91baeb86ce5ccc7cd4292a9f5eb108d1ae45ec2705")
    version("0.7.18", sha256="1e57e02890ffbf82c2bbb3ddb865c63367829c213ebaecaa4d8c5ac7b6b942e6")
    version("0.7.17", sha256="afa3bc3d9ef414a40d49ae1e97b388d86b453d5018af9a30a9742f0e0389b30a")
    version("0.7.16", sha256="5a9e703e07f1263d801e90179d15c13ad3da9d6dcea69e93215930409303fa85")
    version("0.7.15", sha256="c608cd2d89db7482ab40fc6e7de27afc87b20595e145ed81a2a8702e9a0d7e2d")
    version("0.7.14", sha256="0bdc5b64bd93bac674e1ff1f2cbda340eb12568d6092397cc33b01952c5fe943")
    version("0.7.13", sha256="05f3c03c4ea55d294f3da725b6c2c2ff544754c18552da7594def4ec3889dcfb")
    version("0.7.12", sha256="4aa152e6a70d5662ca66a918f697bf8fb710f391068aa7d04e032af2edebb095")
    version("0.7.11", sha256="33daeb9f1e5f49f1f192815c580beb996fd3be131821af2e887af4ec575c2a4f")
    version("0.7.10", sha256="b37b8afd1429268f82690063652173ad65b541dcacf49c11e27ec823da4a55db")
    version("0.7.9", sha256="baac54e49f3b0d05ee83f534fdcb27b91d2923c585bf349a1532ca25d62c216f")
    version("0.7.8", sha256="a59d6749587946d63d371170d8f69d168ca8f4eade5cf880ad3be2793ea29c77")
    version("0.7.7", sha256="e93b2a33d103d4c5a3e8119ca8e62412e72f6816fee74bd671c2060447f98d93")
    version("0.7.6", sha256="bd188ac9d9902f1652130837ede39768d7c8f72b0a68fd484ba884d88e963b66")
    version("0.7.5", sha256="ae2192283eb645ccab189b1dfd8b13d3264eae631469a903c0e0f2dffce65e3b")
    version("0.7.4", sha256="0cc0eee98197f3cd77a4cbf3fd22cebdcea9e77d3f21e74698548ed008ef54a1")
    version("0.7.3", sha256="863ceb63aefc7c2db9918313a1cb3c8bf3fc3d59b656b617db9e4abad90373f3")
    version("0.7.2", sha256="45e619bb076916b79df8c5ecc28d1be04d1ccd0b63b080c44ae973b8deb33b25")
    version("0.7.1", sha256="40a15f1fc73df852d7655530e5768e29dc7227ab25d9baeb711a8dde9e7f8234")
    version("0.7.0", sha256="d117a5f90606badb6c7169b05b9c4cd7c256f1462879d2da5a3328b160ad2510")
    version("0.6.8", sha256="45ecd70cfe42132ff84083ecb37fe7a8d2feac3eacd7a5872e7a002fb260940f")
    version("0.4.27", sha256="c13eea45257362ecfa2a2b31de9b62fbd0542e211a573562d98ab7c8fc50d8fc")
    version("0.4.17", sha256="01564bd760eff885ad61f44173647a569732934d1a4a558839c8088fbf75e53f")
    version("0.4.16", sha256="2144995a87b161d063bd4ef8294b1e948677bd90d01f8394d0e3fca037bb847f")
    version("0.4.15", sha256="8e36b8e07595fc6216d01e729c81a0b4ff029a93cc2ef987a73d3b650d6d559c")

    # from Cargo.toml
    depends_on("rust@1.86:", type=("build", "run"), when="@0.7.16:")
    depends_on("rust@1.85:", type=("build", "run"), when="@0.7.6:")
    depends_on("rust@1.84:", type=("build", "run"), when="@0.6.13:")
    depends_on("rust@1.83:", type=("build", "run"), when="@0.5.9:")
    depends_on("rust@1.81:", type=("build", "run"))

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-maturin@1", type="build")

    depends_on("gmake", type="build")

    # Historical dependencies
    depends_on("cmake", type="build", when="@:0.6.3")

    @when("@:0.6.3")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CMAKE", self.spec["cmake"].prefix.bin.cmake)

    executables = ["^uv$"]
