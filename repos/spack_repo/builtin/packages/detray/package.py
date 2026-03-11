# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Detray(CMakePackage):
    """Detray is a description library for high energy physics experiments that
    works entirely without polymorphism, making it exceptionally suitable for
    use on GPU platforms."""

    homepage = "https://github.com/acts-project/detray"
    url = "https://github.com/acts-project/detray/archive/refs/tags/v0.67.0.tar.gz"

    tags = ["hep"]

    maintainers("stephenswat")

    license("MPL-2.0", checked_by="stephenswat")

    version("0.110.0", sha256="32e29b010d703fc7c718d3cc687ac2cd95115bdf63c764bde35cc95a5f1a89d0")
    version("0.109.2", sha256="512975a20524b24d3d84aa536b950bacba66aa1fee5213b2d92f35e8dd090ae4")
    version("0.109.1", sha256="bb5f1285f5ca0c465f7ca13609348f849d57628dc7bfa5558b184cabc485f57e")
    version("0.109.0", sha256="84e26928e17cf7c503920fe3502d38ad94684d9481fd11918a730df6eecc29fb")
    version("0.108.0", sha256="e4ac45df0ae0dc9f10eb0d178a699afeb5e1b67834bed6017d57660fe4cd5f8a")
    version("0.107.0", sha256="7764bfc27521965b28c28b65b5f099266b4ae355cd0f4a9944e47fea143dc35c")
    version("0.106.0", sha256="9695430a1537e86c06b1423054dfd3b5ae717c9b84e1b233ae48fc3fd859b27a")
    version("0.105.1", sha256="100f5954560426a14258a5debe1c1f25ae491611eec557d6733fa821889abbb7")
    version("0.105.0", sha256="a2c5758420a1544a745e58cb2aa0eaac02cd4548a9a527b8b58d94759e5d38c7")
    version("0.104.1", sha256="b75b3f2a27d4a03a69e66815b34ef2e7f6973919c8d9b1daff32d1135a28c0c6")
    version("0.104.0", sha256="b11b98e32fbae972ae065d71ab70fcccfee1a83d7f71e611d4cfe2fce4bce6d8")
    version("0.103.0", sha256="7b3d3c94cf42be7450e9fe008b567a2f425e6f1986b61d8a3a66814383599043")
    version("0.102.0", sha256="534848b5d5d25c33dffd35a48cda04b24aea03c7c13d0c1240ad73ef06765368")
    version("0.101.0", sha256="f13db54da9b888258ab73a963d5a4bc08b655cc4aef47935e486b7cbe43e0965")
    version("0.100.1", sha256="5e68986889ae083503b3506015c649a0dcf1eadbeec642bb7749ee91c9fca201")
    version("0.100.0", sha256="a34686403807db822dc71f2bc61b9d72e9837a525b22c0b86c6452bf9ec7b0e4")
    version("0.99.0", sha256="86baa957ec55e8eecb5a9dffe135b88265dd0f88f75bf0068c9068ea304c0fb5")
    version("0.98.0", sha256="d90c70d2d4bdd9dbd09024ff6990d57f610947c9544afccadf611316de76b2d9")
    version("0.97.0", sha256="cddee6074b92da9823afe016949c023843d9bc079caddaa7f52900dbefdf64a7")
    version("0.96.0", sha256="b009fad9780adf2bf8d683469d6167b37b4f682da0dbaf58f9f67166096f9bcc")
    version("0.95.0", sha256="86cc981eb0105143b971acea3544b9a668326e1027f317d77cf76918f766e7c4")
    version("0.94.0", sha256="a04e8193757846df50d0fbec858744dd66629a98be8ffc6faa04c2ab51770492")
    version("0.93.0", sha256="7d56771d213649de836905efbb21b5be59cc966b00417b0b1fa85bfe12ac92da")
    version("0.92.0", sha256="512669c1ea51936b0fe871fb5a33450b54161e811e48cc51445dc83fe3338c42")
    version("0.91.0", sha256="6aa822f8bdc7339286d2255079a00ecc3204c0e194c5cf9d0fc5b9262c3cfb39")
    version("0.90.0", sha256="f965429c33622a48c5a7b007086e22125ddd384860c4de3e010d72e05b5cca70")
    version("0.89.0", sha256="b893b7f5434c1c9951433876ef43d1db1b08d36749f062e261b4e6d48e77d5db")
    version("0.88.1", sha256="89134c86c6857cb3a821181e3bb0565ebb726dd8b1245678db1681483d792cf9")
    version("0.88.0", sha256="bda15501c9c96af961e24ce243982f62051c535b9fe458fb28336a19b54eb47d")
    version("0.87.0", sha256="2d4a76432dd6ddbfc00b88b5d482072e471fefc264b60748bb1f9a123963576e")
    version("0.86.0", sha256="98350c94e8a2395b8712b7102fd449536857e8158b38a96cc913c79b70301170")
    version("0.85.0", sha256="a0121a27fd08243d4a6aab060e8ab379ad5129e96775b45f6a683835767fa8e7")
    version("0.84.0", sha256="b1d133a97dc90b1513f8c1ef235ceaa542d80243028a41f59a79300c7d71eb25")
    version("0.83.0", sha256="c870a0459d1f9284750f6afbb97c759392e636b56d107f32b9bc891df717a0fe")
    version("0.82.0", sha256="48794d37496dd5013b755d5d401da7b9d1023fadff86b2a454e5c21e2aaf8c60")
    version("0.81.0", sha256="821313a7e3ea90fcf5c92153d28bba1f85844e03d7c6b6b98d0b3407adb86357")
    version("0.80.0", sha256="a12f3e333778ddd20a568b5c8df5b2375f9a4d74caf921822c1864b07b3f8ab7")
    version("0.79.0", sha256="3b9f18cb003e59795a0e4b1414069ac8558b975714626449293a71bc4398a380")
    version("0.78.0", sha256="ca3a348f4e12ed690c3106197e107b9c393b6902224b2543b00382050864bcf3")
    version("0.77.0", sha256="c2c72f65a7ff2426335b850c0b3cfbbbf666208612b2458c97a534ecf8029cb8")
    version("0.76.1", sha256="54d9abee395e9faf0f56b5d9c137a9990f23712fbcc88fd90af20643bcae635e")
    version("0.76.0", sha256="affa0e28ca96d168e377ba33642e0b626aacdc79f9436233f5561006018f9b9e")
    version("0.75.3", sha256="1249d7398d1e534bd36b6f5a7d06a5e67adf6adeb8bca188d7e35490a675de7a")
    version("0.75.2", sha256="249066c138eac4114032e8d558f3a05885140a809332a347c7667978dbff54ee")

    variant("csv", default=True, description="Enable the CSV IO plugin")
    _cxxstd_values = (
        conditional("17", when="@:0.72.1"),
        conditional("20", when="@0.67.0:"),
        conditional("23", when="@0.67.0:"),
    )
    _cxxstd_common = {
        "values": _cxxstd_values,
        "multi": False,
        "description": "C++ standard used.",
    }
    variant("cxxstd", default="17", when="@:0.72.1", **_cxxstd_common)
    variant("cxxstd", default="20", when="@0.73.0:", **_cxxstd_common)
    variant("json", default=True, description="Enable the JSON IO plugin")
    variant(
        "scalar",
        default="float",
        values=("float", "double"),
        multi=False,
        description="Scalar type to use by default",
    )
    variant("eigen", default=True, description="Enable the Eigen math plugin")
    variant("smatrix", default=False, description="Enable the SMatrix math plugin")
    variant("vc", default=True, description="Enable the Vc math plugin")

    depends_on("cmake@3.11:", type="build")
    depends_on("cmake@3.21:", type="build", when="@0.95:")
    depends_on("vecmem@1.6.0:")
    depends_on("vecmem@1.8.0:", when="@0.76:")
    depends_on("vecmem@1.18.0:", when="@0.102:")
    depends_on("covfie@0.10.0:")
    depends_on("covfie@0.15.3:", when="@0.102:")
    depends_on("nlohmann-json@3.11.0:", when="+json")
    depends_on("dfelibs@20211029:", when="@:0.88")
    depends_on("acts-algebra-plugins@0.18.0: +vecmem")
    depends_on("acts-algebra-plugins +vc", when="+vc")
    depends_on("acts-algebra-plugins +eigen", when="+eigen")
    depends_on("acts-algebra-plugins +smatrix", when="+smatrix")
    # The version number of algebra plugins was not correct before v0.28.0.
    depends_on("acts-algebra-plugins@0.28.0:", when="@0.87:")
    depends_on("acts-algebra-plugins@0.28.0: +vecmem", when="@0.95:")
    depends_on("acts-algebra-plugins@0.30.0: +vecmem", when="@0.103:")

    # Detray imposes requirements on the C++ standard values used by Algebra
    # Plugins.
    with when("+smatrix"):
        for _cxxstd in _cxxstd_values:
            for _v in _cxxstd:
                depends_on(
                    f"acts-algebra-plugins cxxstd={_v.value}", when=f"cxxstd={_v.value} {_v.when}"
                )

    depends_on("actsvg +meta")
    depends_on("actsvg @0.4.57:", when="@0.100:")

    def cmake_args(self):
        args = [
            self.define("DETRAY_USE_SYSTEM_LIBS", True),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("CMAKE_CUDA_STANDARD", "cxxstd"),
            self.define_from_variant("CMAKE_SYCL_STANDARD", "cxxstd"),
            self.define_from_variant("DETRAY_CUSTOM_SCALARTYPE", "scalar"),
            self.define_from_variant("DETRAY_EIGEN_PLUGIN", "eigen"),
            self.define_from_variant("DETRAY_SMATRIX_PLUGIN", "smatrix"),
            self.define_from_variant("DETRAY_IO_CSV", "csv"),
            self.define_from_variant("DETRAY_IO_JSON", "json"),
            self.define_from_variant("DETRAY_VC_PLUGIN", "vc"),
            self.define_from_variant("DETRAY_VC_AOS_PLUGIN", "vc"),
            self.define_from_variant("DETRAY_VC_SOA_PLUGIN", "vc"),
            self.define("DETRAY_SVG_DISPLAY", True),
            self.define("DETRAY_SETUP_ACTSVG", True),
            self.define("DETRAY_BUILD_TESTING", False),
            self.define("DETRAY_SETUP_GOOGLETEST", False),
            self.define("DETRAY_SETUP_BENCHMARK", False),
            self.define("DETRAY_BUILD_TUTORIALS", False),
            self.define("DETRAY_BUILD_TEST_UTILS", True),
        ]

        return args
