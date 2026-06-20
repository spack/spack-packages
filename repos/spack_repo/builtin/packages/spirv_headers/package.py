# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SpirvHeaders(CMakePackage):
    """This package contains machine-readable files for the SPIR-V Registry"""

    homepage = "https://github.com/KhronosGroup/SPIRV-Headers"

    maintainers("williampiat3")

    license("CC-BY-4.0", checked_by="dneto0")

    version(
        "1.4.350.1",
        sha256="9e6d5c78878172d2b810e97f3a74ecbbb14b4ad52b07384ce915fbbeb226d610",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.350.1.tar.gz",
    )
    version(
        "1.4.350.0",
        sha256="9905d9341f20388adb852c77dd982f2c4d539fd68e6c1f1bcebf034715f2d1d5",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.350.0.tar.gz",
    )
    version(
        "1.4.341.0",
        sha256="cab0a654c4917e16367483296b44cdb1d614e3120c721beafcd37e3a8580486c",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.341.0.tar.gz",
    )
    version(
        "1.4.335.0",
        sha256="1c47ca6342ebe86f57b46b8dbeb266fa655a1ca8e10d07e45370ff2d9c36312e",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.335.0.tar.gz",
    )
    version(
        "1.4.328.1",
        sha256="602364ab7bf404a7f352df7da5c645f1c4558a9c92616f8ee33422b04d5e35b7",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.328.1.tar.gz",
    )
    version(
        "1.4.328.0",
        sha256="00284a33e1e19014723c8e88ca7a16e8988cd23f839ec2b7da6bb1808fd2a751",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.328.0.tar.gz",
    )
    version(
        "1.4.321.0",
        sha256="5bbea925663d4cd2bab23efad53874f2718248a73dcaf9dd21dff8cb48e602fc",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.321.0.tar.gz",
    )
    version(
        "1.4.313.0",
        sha256="f68be549d74afb61600a1e3a7d1da1e6b7437758c8e77d664909f88f302c5ac1",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.313.0.tar.gz",
    )
    version(
        "1.4.309.0",
        sha256="a96f8b4f2dfb18f7432e5c523e220ab0075372a9509e0c25fbff21c76af0de7c",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.309.0.tar.gz",
    )
    version(
        "1.4.304.1",
        sha256="66e6cec19e7433fc58ace8cdf4040be0d52bb5920e54109967df2dd9598a8d48",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.304.1.tar.gz",
    )
    version(
        "1.4.304.0",
        sha256="162b864ebaf339d66953fc2c4ad974bc4f453e0f04155cd3755a85e33f408eee",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.4.304.0.tar.gz",
    )
    version(
        "1.3.296.0",
        sha256="1423d58a1171611d5aba2bf6f8c69c72ef9c38a0aca12c3493e4fda64c9b2dc6",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.3.296.0.tar.gz",
    )
    version(
        "1.3.290.0",
        sha256="1b9ff8a33e07814671dee61fe246c67ccbcfc9be6581f229e251784499700e24",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.3.290.0.tar.gz",
    )
    version(
        "1.3.283.0",
        sha256="a68a25996268841073c01514df7bab8f64e2db1945944b45087e5c40eed12cb9",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.3.283.0.tar.gz",
    )
    version(
        "1.3.280.0",
        sha256="a00906b6bddaac1e37192eff2704582f82ce2d971f1aacee4d51d9db33b0f772",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.3.280.0.tar.gz",
    )
    version(
        "1.3.275.0",
        sha256="d46b261f1fbc5e85022cb2fada9a6facb5b0c9932b45007a77fe05639a605bd1",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.3.275.0.tar.gz",
    )
    version(
        "1.3.268.0",
        sha256="1022379e5b920ae21ccfb5cb41e07b1c59352a18c3d3fdcbf38d6ae7733384d4",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-1.3.268.0.tar.gz",
    )
    version(
        "1.3.261.1",
        sha256="32b4c6ae6a2fa9b56c2c17233c8056da47e331f76e117729925825ea3e77a739",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.261.1.tar.gz",
    )
    version(
        "1.3.261.0",
        sha256="846d60811fb696b517e1e30073320f4e12572be57f1f4c9572843f87f2d07f81",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.261.0.tar.gz",
    )
    version(
        "1.3.250.1",
        sha256="d5f8c4b7906baf9c51aedbbb2dd942009e8658e3340c6e64699518666a03e043",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.250.1.tar.gz",
    )
    version(
        "1.3.250.0",
        sha256="9d632a4dddd11f89a74a8c6f19cd29e8b0741d2fbb41ecc4dec26b922d28a2f3",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.250.0.tar.gz",
    )
    version(
        "1.3.246.1",
        sha256="71668e18ef7b318b06f8c466f46abad965b2646eaa322594cd015c2ac87133e6",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.246.1.tar.gz",
    )
    version(
        "1.3.246.0",
        sha256="9fcaff6a4b7155973a31d455530af556b0fac81a22e157baf752ebb9483d8856",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.246.0.tar.gz",
    )
    version(
        "1.3.243.0",
        sha256="16927b1868e7891377d059cd549484e4158912439cf77451ae7e01e2a3bcd28b",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.243.0.tar.gz",
    )
    version(
        "1.3.239.0",
        sha256="fdaf6670e311cd1c08ae90bf813e89dd31630205bc60030ffd25fb0af39b51fe",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.239.0.tar.gz",
    )
    version(
        "1.3.236.0",
        sha256="4d74c685fdd74469eba7c224dd671a0cb27df45fc9aa43cdd90e53bd4f2b2b78",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.236.0.tar.gz",
    )
    version(
        "1.3.231.1",
        sha256="fc340700b005e9a2adc98475b5afbbabd1bc931f789a2afd02d54ebc22522af3",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.231.1.tar.gz",
    )
    version(
        "1.3.231.0",
        sha256="dbd579f6d1351d03f49b821fb273a068ab6ca9e4e0beb498d48eb4d5f72d8dee",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.231.0.tar.gz",
    )
    version(
        "1.3.224.1",
        sha256="c85714bfe62f84007286bd3b3c0471af0a7e06ab66bc2ca4623043011b28737f",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.224.1.tar.gz",
    )
    version(
        "1.3.224.0",
        sha256="2fb1039ec6cec8943400e9b4d01d8bfe8c62a0bd1fafb7c39c56469aa247b838",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.224.0.tar.gz",
    )
    version(
        "1.3.216.0",
        sha256="46c49a0e49ea120138102b1dcb3778e5a4f2267c45b9e937810a4cf4fb889e3d",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.216.0.tar.gz",
    )
    version(
        "1.3.211.0",
        sha256="30a78e61bd812c75e09fdc7a319af206b1044536326bc3e85fea818376a12568",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.211.0.tar.gz",
    )
    version(
        "1.3.204.1",
        sha256="262864053968c217d45b24b89044a7736a32361894743dd6cfe788df258c746c",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.204.1.tar.gz",
    )
    version(
        "1.3.204.0",
        sha256="519d09906dcdd4bf27089ff136d4e8c70abe2915bbde17a1d5ac18c5de6aee67",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.204.0.tar.gz",
    )
    version(
        "1.2.198.0",
        sha256="3301a23aca0434336a643e433dcacacdd60000ab3dd35dc0078a297c06124a12",
        url="https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.2.198.0.tar.gz",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
