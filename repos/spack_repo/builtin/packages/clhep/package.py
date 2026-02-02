# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Clhep(CMakePackage):
    """CLHEP is a C++ Class Library for High Energy Physics."""

    homepage = "https://gitlab.cern.ch/CLHEP/CLHEP"
    git = "https://gitlab.cern.ch/CLHEP/CLHEP.git"

    tags = ["hep"]

    maintainers("drbenmorgan")

    version("2.4.7.2", sha256="c40c239fa2c5810b60f4e9ddd6a8cc2ce81b962aa170994748cd2a2b5ac87f84")
    version("2.4.7.1", sha256="6c39dfecfb8369c4ba9d353471fa7cc818116f9c4dfef35bb5a086a9b2ccd40b")
    version("2.4.7.0", sha256="6705da2fa08db9b8ad16cff6687932f3135d402c28ee48f23ee7e7297f9fab91")
    version("2.4.6.4", sha256="df94daccadc422dda70162c71103c963581f258c7d160f4e20fce26fc1949f4a")
    version("2.4.6.3", sha256="6c24d015e8dfaf81112c79ce7ebcf1ce1273e014c980917a9225b9664d27ff28")
    version("2.4.6.2", sha256="97bf944d672e10fdd1824a2b27cf99f26f4868593e31b14af510fd36230955a3")
    version("2.4.6.0", sha256="f2dffc46d4221276b396fbb1ab5b2dff1e62215a231426b5396c5ba5daca0cb3")
    version("2.4.5.4", sha256="d00cb79f3902a12ec573219e6590725afc0e77176e4e5096c4de4c51a20ba47d")
    version("2.4.5.3", sha256="3d5df7e4dce698ff401c2744c5dcdf24796d25894443339e2426ae7eb62b8feb")
    version("2.4.5.1", sha256="8729e1c0fe545f2c1b631b3a0bfaa6edb3880c4d401ec638db98a8f63b136bc4")
    version("2.4.4.0", sha256="b9d9364fe0f3fbc03e0f0cf53b81e8190dae38f81cc854b6b712e1b85d472752")
    version("2.4.1.3", sha256="aa2725db049c455d8e3c78678889c013deef83bcba0146bdf04e859c38054d52")
    version("2.4.1.2", sha256="bb6e36dc1ab055d0b47bb24377b570b100b37ace402cbc0d858e49be0a1b72c6")
    version("2.4.1.0", sha256="21b6823c8f859f2e042c71032cc23ddcca22a98186a374f0bde4ed54683a649b")
    version("2.4.0.4", sha256="058cf042fedc5ac21c59a4acb2b5af2c56bf4a310456ada4ecf590dd8ac7b444")
    version("2.4.0.2", sha256="d459681835ecfa272dfe48d42667f25fb2cb480981c0df381b4c051f26504b80")
    version("2.4.0.1", sha256="1370a036ca8530df97d0c20722f26ace7c34b34070a5d3bf892feeb9d4f83756")
    version("2.4.0.0", sha256="e205c51b7b8e5109d30a55d72570c65440ebf670d43063b729264a4dc69c9645")
    version("2.3.4.6", sha256="ef12c4e0e0452d07f4a5e6370c747589b8bc1ed5001507ccd17685aab4728752")
    version("2.3.4.5", sha256="4ed1b18a0c146a915cbc44b8f6b2b8289c99bf9e9a538bf4db9f7b3bbe3d762e")
    version("2.3.4.4", sha256="f7228b83396ee34e6ab12538c470a3f6bd4d657158dd362bee443a29f1d4abe6")
    version("2.3.4.3", sha256="91eaaaad6c60f58a9bb71ea525259f81829d0f47384a61ca07f8d3920ebb3540")
    version("2.3.4.2", sha256="deaa9396b23779f185eead508fa156637d4c85abfdb3dfb8a673436fa05ad562")
    version("2.3.3.2", sha256="3dd41587ac99b27c6aa4ca3dd6204ba96b774627f3f28079cf0f01663340a811")
    version("2.3.3.1", sha256="fc837873e4172497f97b8d3e77c7508d6c554320465da73cf6b0bea8a2aae993")
    version("2.3.3.0", sha256="aacf0fdbdd6f38f485533e1b92d383a1eb6252dab8e5644694580cc7121ffe06")
    version("2.3.2.2", sha256="9a9b6ac3e6c6c9dcd29e528a3ac3371a67223c75fb8898770d36d0ae4a222ace")
    version("2.3.1.1", sha256="6300568a5fbdf0bd3c051349bee11aca8d95993921ecf01147ce298db58a30b4")
    version("2.3.1.0", sha256="68863cfa89d15c7ca026524b67f5ab663c9a737ed3b9927dfbc732379a1937d0")
    version("2.3.0.0", sha256="b3d1d81bacc0997ca9bcf730e0d6046b3759d9573ade0d89d24afeca15a51836")
    version("2.2.0.8", sha256="ad3fcd9a5c650b8eb7b5a78ae2016d64066ca451adda774afef46da497a116ea")
    version("2.2.0.5", sha256="97d6e08c1e6b6cfc89cc6b98c2b49f35cdfe338e71cd6a85f0ae2aa1d5995b7e")
    version("2.2.0.4", sha256="2d98542c26e077eb54909c625b448c9adb2726e27b23f5e027f43da5e9789ecd")
    version("2.1.2.3", sha256="a3fb65bb4ded5271db889e07a42cd988ae928216f0758a27a52772d243efa07f")

    variant(
        "cxxstd",
        default="11",
        values=(
            "11",
            "14",
            conditional("17", when="@2.3.4.3:"),
            conditional("20", when="@2.4.6.4:"),
        ),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@2.8.12.2:", when="@2.2.0.4:2.3.0.0", type="build")
    depends_on("cmake@3.2:", when="@2.3.0.1:", type="build")

    variant("cms", default=False, description="Apply CMS-specific changes")

    patch("clhep-cms.patch", when="+cms", level=0)

    def patch(self):
        # Patched line removed since 2.3.2.2
        # https://gitlab.cern.ch/CLHEP/CLHEP/-/commit/5da6830d69c71dc178632f7f5121a3a00e379f94
        if self.spec.satisfies("@2.3.2.2:"):
            return

        filter_file(
            "SET CMP0042 OLD",
            "SET CMP0042 NEW",
            "%s/CLHEP/CMakeLists.txt" % self.stage.source_path,
        )

    def cmake_args(self):
        cmake_args = [
            "-DCLHEP_BUILD_CXXSTD=-std=c++{0}".format(self.spec.variants["cxxstd"].value)
        ]
        return cmake_args

    def url_for_version(self, version):
        url = "https://gitlab.cern.ch/CLHEP/CLHEP/-/archive/CLHEP_{0}/CLHEP-CLHEP_{0}.tar.gz"
        return url.format(version.underscored)
