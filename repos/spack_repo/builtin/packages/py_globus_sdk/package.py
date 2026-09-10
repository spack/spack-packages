# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGlobusSdk(PythonPackage):
    """
    Globus SDK for Python
    """

    homepage = "https://github.com/globus/globus-sdk-python"
    pypi = "globus_sdk/globus_sdk-3.0.2.tar.gz"

    maintainers("hategan", "climbfuji")

    license("Apache-2.0", checked_by="wdconinc")

    version("4.3.1", sha256="f892bf26bb0b48fb96d4a79bd820c103733abbc5068bb96db812e585ffdfe14a")
    version("4.3.0", sha256="bc815d7ee9b3e789b9c5f85cb6bafc9b01db777b638147af3c2f035226087b89")
    version("4.2.0", sha256="d72715f6feae6dd947e167df803d5c1424b69513bb01f5fb6d184936a74705b2")
    version("4.1.0", sha256="2848eeebf9310fa2a580258798a9995020516867116919043bb20ca657b56a9b")
    version("4.0.0", sha256="0754e7adc0b193df2a12a847cbe3207392e463bd29a41168283398a7eb86185b")
    version("3.65.0", sha256="a4b350b980809e86d768c8e327de9ddee4405b60cfb83429cdf831ac0c63d763")
    version("3.64.0", sha256="88e5263af8421d5117845485785f0eda8359927b56c56528a5d489809107000d")
    version("3.63.0", sha256="9a3c4668197f710e2748c015eb06f3b5eb34e929028bc4bf37558b8e0022ab45")
    version("3.62.0", sha256="5eabe95ee8c8f891b6b3367924037627bcd388b3433f2994062c5efc67915890")
    version("3.61.0", sha256="6b9c9f05a095ec7c26b94cbf22ed9dcecd8b4309a8ac17bf823cb349f54c4a01")
    version("3.60.0", sha256="9047af9980dd40c878d9d88a8954f6f59dc75ed55a93722c101b0e7f9359740d")
    version("3.59.0", sha256="16fd4410e3b61d86a8c88b68910569ca5e31d945a5022cb67b58603987752f74")
    version("3.58.0", sha256="21cc8ad62cde662999ff18daf45eccfb374dfc2d2533714d4e51e89f655e0a7a")
    version("3.57.0", sha256="15ac2cd1313777be9ce026a51437c90db7c25311e8a4b3950a76ab744d0fb425")
    version("3.56.1", sha256="07674b12b0e6667fa7be6fc91e419647bb00c1630a72ee862cec034e011aab2f")
    version("3.56.0", sha256="3a794106136f3d43505bb2fede3e81a63735d608a812d11338135126a857e7ca")
    version("3.55.0", sha256="3b905c9cc7ec638b9e652130500a2a4bb8fd368a93fec0f07aeda76f66ca66f6")
    version("3.54.0", sha256="55297ec204e69f9da2c161b1e7b66906867c9ab32b6e0e3a10aa81066133cda0")
    version("3.53.0", sha256="502cf6f2fac3d8f2ee1f0270db07307adb0b928f367dad522c3ec5ac90b5acec")
    version("3.52.0", sha256="4ad17d6442608be851c881c746411ed785a66f9532758ff30735ed1061af5d96")
    version("3.51.0", sha256="e7b59cd4a4c64cb23d92009b0488ad7e975f8a9701b786b49b7043c6240a59a5")
    version("3.50.0", sha256="758e638cd28f13c310d97ee5b30605496b3ca5d83f048d2bc1bbcbe4527c29c5")
    version("3.49.0", sha256="6268a1a9ea04cce0eb06cd1a02eeaa8a04dad8682e16a6c65520b743446d0479")
    version("3.48.0", sha256="54eab5bbed54924d7d1ad15f7059b6efdb7ef1a1d7c49e06a662b4f3f85428de")
    version("3.47.0", sha256="1c860c5115100a2cce1ef9cf1e053bea51393bcfd899f7f33050a29da9ec6198")
    version("3.46.0", sha256="eb5e1a3e724b6afe89277f2e3aed6d4959d7d3c4b05ed51f084eaa60ee6a4d25")
    version("3.45.0", sha256="80da09d3ca254a63e1aa6d2f7cf86bc3252cf62f4321378a09199283b9df87fb")
    version("3.44.0", sha256="645ebeeb7140a5095126696b37323010452a7d8216549c2df5931489a1827983")
    version("3.43.0", sha256="753a21baa8c1e26480451cd2075e044e362bbca91b723cc06c4731d4f35097fd")
    version("3.42.0", sha256="7f239acf26cd98c72568b07cc69d7e8d84511004881435c83129bf37c9495f43")
    version("3.41.0", sha256="a097829e7516735675c1535bd17a8d9137636678bdbf50e95b3e7af8b32638ef")
    version("3.40.0", sha256="6394f01c35b2b3275622f4f7c194eaf6750cb6c1e82cb2448dac2eb4ec394d75")
    version("3.39.0", sha256="10af5291ba261e817665d5951948206232ecebccdc2aa8adc0528f0031ab80c3")
    version("3.38.0", sha256="b83faacc103e3d3d3ac2ae33fd73a20a09d4d566cfa0cb03716b3fd8f51adcff")
    version("3.37.0", sha256="87cd4cc191bca5912138c1f992589c735e13436208db10f2de5831efbebc83a7")
    version("3.36.0", sha256="7693954a9ee3d69d09a0914c934ebcf4b4f47f016baa5c33612a03e367ee65a3")
    version("3.35.0", sha256="9da40d5f251f98d89297c2a92abd9f24bfa3c041dfd0e957579884ef0c882cf2")
    version("3.34.0", sha256="4db2ff439de9bd650bc2ba2d7c00614bd3dee34bd9b79da708951b8148236a36")
    version("3.33.0", sha256="38b048590cf7bbd01c5ac82346401c3f42c3f105c81421d61bcb771aa788f481")
    version("3.32.0", sha256="fe9df4ca2f2d16bbf40098df482e1713070946c70e2d6ec6a687c7086c1b559c")
    version("3.31.0", sha256="5f077a8e532828a137a54f2858e63695af16d02577de058278da4ec873556cc1")
    version("3.30.0", sha256="29d25f83d3b250d28a3a4bca8d046601a4bbb725330f409e6401295fa6bfb0ce")
    version("3.29.0", sha256="a5f3c2da86ac6e7165841c9364ae80893f2ae667add5af5cd2237fc3fa14a1be")
    version("3.28.0", sha256="249423dda76f162bb0d5515509135b68d6a779ad0cf2cd02a8204b2c7903e365")
    version("3.27.0", sha256="1e9afac3bcce7dd69199c6e85372b0d6cadcc0906b27129d88db7e41dc32f195")
    version("3.26.0", sha256="5a2bca267635c62e0f7c60fce10c47c7fd0fa8923c3363d44871c4abca8a68d1")
    version("3.25.0", sha256="d9be275d4ec18054db04732f75649c4227800c79b31fbcfb3f4f31eccfa5f4f7")
    version("3.10.1", sha256="c20fec55fc7e099f4d0c8224a36e194604577539445c5985cb465b23779baee8")
    version("3.10.0", sha256="7a7e7cd5cfbc40c6dc75bdb92b050c4191f992b5f7081cd08895bf119fd97bbf")
    version("3.9.0", sha256="456f707b25a8c502607134f1d699b5970ef1aa9d17877474db73fc6d87c711e9")
    version("3.8.0", sha256="492611636c190806409198cdadc9960227fa712281dce95ef3ec0d7e8f9823a9")
    version("3.7.0", sha256="81dbcb7bb7072bf9a5f730becc65e4a0f15f0fa0e2022faf2d943a99b5ce1fb5")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"), when="@3.17:")
    depends_on("python@3.8:", type=("build", "run"), when="@3.42:")
    depends_on("python@3.9:", type=("build", "run"), when="@4.0.0:")
    depends_on("py-setuptools", type="build")
    depends_on("py-requests@2.19.1:2", type=("build", "run"))
    depends_on("py-pyjwt@2.0.0:2+crypto", type=("build", "run"))
    depends_on("py-cryptography@3.3.1:3.3,3.4.1:", type=("build", "run"))
    depends_on("py-typing-extensions@4:", when="@3.46: ^python@:3.10", type=("build", "run"))
    depends_on("py-typing-extensions@4:", when="@3.25:3.45 ^python@:3.9", type=("build", "run"))
    depends_on("py-importlib-resources@5.12.0:", when="@3.41: ^python@:3.8", type=("build", "run"))

    def url_for_version(self, version):
        if version <= Version("3.39"):
            return super().url_for_version(version).replace("_", "-")
        else:
            return super().url_for_version(version)
