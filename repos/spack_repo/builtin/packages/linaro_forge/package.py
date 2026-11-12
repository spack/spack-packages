# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import platform
import subprocess

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class LinaroForge(Package):
    """Build reliable and optimized code for the right results on multiple
    Server and HPC architectures, from the latest compilers and C++ standards
    to Intel, 64-bit Arm, AMD, OpenPOWER and Nvidia GPU hardware. Linaro Forge
    combines Linaro DDT, the leading debugger for time-saving high performance
    application debugging, Linaro MAP, the trusted performance profiler for
    invaluable optimization advice across native and Python HPC codes, and
    Linaro Performance Reports for advanced reporting capabilities."""

    homepage = "https://www.linaroforge.com"
    maintainers("kenche-linaro")

    if platform.machine() == "aarch64":
        version("26.1", sha256="330ffee09d30105562291cbc9e415c621d0c0e839d32a673c7f13e186bee8902")
        version(
            "26.0.3", sha256="b76137ec53b265ae597c8b764237fcb5f2598bf1179b598179f40be2f074f47d"
        )
        version(
            "26.0.2", sha256="11d9a445230d0293a81c57494eed96babd6951f22ce8c719c00e4e4ed1c7b32e"
        )
        version(
            "26.0.1", sha256="407117379bf5fe3a3a41ec9d8059195a951e27bb9e45c333f8696319f38fe77b"
        )
        version("26.0", sha256="e1510c0377bbc49821ba9758c8ed5563fe3e08dc072860319ea0ac5cb088c7c8")
        version(
            "25.1.3", sha256="befc2d9689d9eead6b3e6f383d417ca5873c71055013735e8ac3a79545d4cbb7"
        )
        version(
            "25.1.2", sha256="4bd7928dae0d9e3f01c6cecc671ad31b957731a1f137c81993b7b20373c5623d"
        )
        version(
            "25.1.1", sha256="41595c4e4e0f560d59cd1c70517471d6fe64ee2c1224d1a531cc2d2a2867ad27"
        )
        version("25.1", sha256="62d215e4ffd20e69863b1ffb7f043968aa7a3bf21280f5dcf2e64a2db7deb675")
        version(
            "25.0.4", sha256="6d9a7ffcc18c6b89175167e100d80c46e2206b7a3655d6449dc63881f834b031"
        )
        version(
            "25.0.3", sha256="0cb6cc547bf53f63bb196da13b32f33ae5b9551d53535ed4e96b3606ade8a5f8"
        )
        version(
            "25.0.2", sha256="5cbce0612e76eafd47931154ad0b3183683112cfb5f2a38ae14769c56041f447"
        )
        version(
            "25.0.1", sha256="da16574f34c97142712cd4a56f1c99914abb069936a29b682a4d08cc39dc2e8d"
        )
        version("25.0", sha256="11c85015c069f3f37fd8d45f9b701d88ae2f729bdfd3fc7f8ceeb5ca0be32a90")
        version(
            "24.1.3", sha256="e79975611ae17b17481ec6626e9932bd0901cffcc6919bed523e3dc58dddefcd"
        )
        version(
            "24.1.2", sha256="c3821b2e792d07b1b09f1ca81d1a27590b1bef62d5c48d6f7271debef62b6398"
        )
        version(
            "24.1.1", sha256="ad02a8912650bdca6f50de12c2b6fb471730a5f38f3c58fe91d48429337d3a10"
        )
        version("24.1", sha256="e297d0c19c95d4db842187eb38882db094094ec667d854aaf396e11a81bffe0b")
        version(
            "24.0.6",
            sha256="a7f9f71e4352be3680854611fe433a9974fcb8a327ac65ca3bc950c956eac6e4",
            deprecated=True,
        )
        version(
            "24.0.5",
            sha256="fc0c80ce9f66c6966faaca77de0f13e26da564c853e5bfc1e8acd17b65bc2ba0",
            deprecated=True,
        )
        version(
            "24.0.4",
            sha256="d126e4690f7c9bf21e541721dac51dcee1f336a882211426bf98a15d80671e3d",
            deprecated=True,
        )
        version(
            "24.0.3",
            sha256="5030c5c23824963f82e94ed606e47cce802393fa4cb7757966818baa7012aa21",
            deprecated=True,
        )
        version(
            "24.0.2",
            sha256="8346eb0375910498a83baff6833256c8221c2c06737670687bcf9f1497d9ede9",
            deprecated=True,
        )
        version(
            "24.0.1",
            sha256="d9d8e8fd56894032ea98a5ff7885c16c0522a192d9cbf4e131581c65e34efb82",
            deprecated=True,
        )
        version(
            "24.0",
            sha256="ee631177f5289127f0d3d99b600d437b4bd40c34c1c15388288b72543dc420ad",
            deprecated=True,
        )
        version(
            "23.1.2",
            sha256="8c01f4768a8f784f0bfa78c82dbd39e5077bbc6880b6f3c3704019eecfca5b3a",
            deprecated=True,
        )
        version(
            "23.1.1",
            sha256="6e95a9c9f894caad073e58590733c4ce4489aec0d8db6553050e71a59e41e6f8",
            deprecated=True,
        )
        version(
            "23.1",
            sha256="c9889b95729f97bcffaf0f15b930efbd27081b7cf2ebc958eede3a186cc4d93a",
            deprecated=True,
        )
    elif platform.machine() == "ppc64le":
        # N.B. support for ppc64le was dropped in 24.0
        version(
            "23.1.2",
            sha256="5c588a6b7391d75cced4016936d0c5a00023431269339432738ff33b860487b3",
            deprecated=True,
        )
        version(
            "23.1.1",
            sha256="9d4dfa440ef1cc9c6a7cb4f7eeec49fc77f0b6b75864fbe018a41783ac5fc5df",
            deprecated=True,
        )
        version(
            "23.1",
            sha256="39a522c1d9a29f0a35bba5201f3e23c56d87543410505df30c85128816dd455b",
            deprecated=True,
        )
    elif platform.machine() == "x86_64":
        version("26.1", sha256="b86acae14344ccc991ad17972f5457475a46664bdd85a73e4b3b249e3f3cc0a8")
        version(
            "26.0.3", sha256="a141a0acf89c6bd5ada44f9045933eaeb874d9526f2873111459636cb36aa0a3"
        )
        version(
            "26.0.2", sha256="ac552111f1256b6a4790b5f12bf74d8849c69adfd38fd1363cba8d95d4b8492a"
        )
        version(
            "26.0.1", sha256="a44ed2bc1f73bc657f47e3a71b728148eed8c93014439ca7d3f2884b0f5e547f"
        )
        version("26.0", sha256="060b44e014b13632f1d56386acd3bbbbd7d07b5033dbb2af264bd91c5ac23e1e")
        version(
            "25.1.3", sha256="eb23bbe09450ea2d7e5c4054f2e9d07567bf5e5af4a2dfce47f21d329a986b80"
        )
        version(
            "25.1.2", sha256="277f810b6cb52428a10c3317d07d0887140b8dbe5269485ba6715e23be3b55bb"
        )
        version(
            "25.1.1", sha256="a256fdbf57450511969d1c8121c1c45ec55b1212e2608fae2779b15a103819a1"
        )
        version("25.1", sha256="153b0264939762431cb5242cd67774832c9ac9c2a2658a6918110064c322eaa1")
        version(
            "25.0.4", sha256="ee93a414f6183165cd8addf926a4a586668ce29930f34edd43d33c750646f0be"
        )
        version(
            "25.0.4", sha256="ee93a414f6183165cd8addf926a4a586668ce29930f34edd43d33c750646f0be"
        )
        version(
            "25.0.3", sha256="4d6abe4f46356339e0df789229f19b92c1ba13b794ce426a2e73e5aed319a6f6"
        )
        version(
            "25.0.2", sha256="9be88c3b2471af7f408f129f6941f11dc7838661d8f3cd172f82405b67e8f8c4"
        )
        version(
            "25.0.1", sha256="88313be739e64615bc8de68eea784de79adf4ff5821c6808ab47bd03e3df1143"
        )
        version("25.0", sha256="903079063965c12b4f8bb934ffae32a679a78bb69b8b9c5fbf7d859897b2655a")
        version(
            "24.1.3", sha256="94ac68bbde8b56897d507c1ed27ff113bc8bf5167a2c513510a7ac7aed139d50"
        )
        version(
            "24.1.2", sha256="794fed7cb60dd96fd68f0f414f6a8d15920cd2bd5a8795978150ca27c55a547d"
        )
        version(
            "24.1.1", sha256="b58b59f0b4ccf50eb48753d740172f71941b1fbe132dea96d35c6dad58cd9b96"
        )
        version("24.1", sha256="0b96878ab73c20b39c4730ed15f24ca86dc5985637ff5d8e68f55e1e802e5fe3")
        version(
            "24.0.6",
            sha256="eab198b964862b4664359ccbec1edb27c2dd3b9fa82bcb4e14fc616a2b0341da",
            deprecated=True,
        )
        version(
            "24.0.5",
            sha256="da0d4d6fa9120b5e7c4a248795b7f5da32c4987588ecb7406213c8c9846af2bc",
            deprecated=True,
        )
        version(
            "24.0.4",
            sha256="001e7b7cd796d8e807971b99a9ca233c24f8fcd6eee4e9b4bbb0ec8560d44f08",
            deprecated=True,
        )
        version(
            "24.0.3",
            sha256="1796559fb86220d5e17777215d3820f4b04aba271782276b81601d5065284526",
            deprecated=True,
        )
        version(
            "24.0.2",
            sha256="e2ad12273d568560e948a9bcdd49b830a2309f247b146bf36579053f99ec59a3",
            deprecated=True,
        )
        version(
            "24.0.1",
            sha256="70aa6b610d181c12be10e57d2fd3439261e2c6cb23d9f1f33303b85f04cb7bf2",
            deprecated=True,
        )
        version(
            "24.0",
            sha256="5976067e3de14d0838e1069021a4a4a96d048824454668779473ff0776d66a01",
            deprecated=True,
        )
        version(
            "23.1.2",
            sha256="675d2d8e4510afefa0405eecb46ac8bf440ff35a5a40d5507dc12d29678a22bf",
            deprecated=True,
        )
        version(
            "23.1.1",
            sha256="6dcd39fc582088eb4b13233ae1e9b38e12bfa07babf77d89b869473a3c2b66e6",
            deprecated=True,
        )
        version(
            "23.1",
            sha256="31185d5f9855fd03701089907cdf7b38eb72c484ee730f8341decbbd8f9b5930",
            deprecated=True,
        )

    variant(
        "probe",
        default=False,
        description='Detect available PMU counters via "forge-probe" during install',
    )

    variant("accept-eula", default=False, description="Accept the EULA")

    # forge-probe executes with "/usr/bin/env python"
    depends_on("python@2.7:", type="build", when="+probe")

    # Licensing
    license_required = True
    license_comment = "#"
    license_files = ["licences/Licence"]
    license_vars = [
        "ALLINEA_LICENSE_DIR",
        "ALLINEA_LICENCE_DIR",
        "ALLINEA_LICENSE_FILE",
        "ALLINEA_LICENCE_FILE",
    ]
    license_url = "https://docs.linaroforge.com/latest/html/licenceserver/index.html"

    def url_for_version(self, version):
        return f"https://downloads.linaroforge.com/{version}/linaro-forge-{version}-linux-{platform.machine()}.tar"

    @run_before("install")
    def abort_without_eula_acceptance(self):
        install_example = "spack install linaro-forge +accept-eula"
        license_terms_path = os.path.join(self.stage.source_path, "license_terms")
        if not self.spec.variants["accept-eula"].value:
            raise InstallError(
                "\n\n\nNOTE:\nUse +accept-eula "
                + "during installation "
                + "to accept the license terms in:\n"
                + "  {0}\n".format(os.path.join(license_terms_path, "license_agreement.txt"))
                + "  {0}\n\n".format(os.path.join(license_terms_path, "supplementary_terms.txt"))
                + "Example: '{0}'\n".format(install_example)
            )

    def install(self, spec, prefix):
        subprocess.call(["./textinstall.sh", "--accept-license", prefix])
        if spec.satisfies("+probe"):
            probe = join_path(prefix, "bin", "forge-probe")
            subprocess.call([probe, "--install", "global"])

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Only PATH is needed for Forge.
        # Adding lib to LD_LIBRARY_PATH can cause conflicts with Forge's internal libs.
        env.clear()
        env.prepend_path("PATH", join_path(self.prefix, "bin"))
